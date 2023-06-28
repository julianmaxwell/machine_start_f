"""
first pin ------>next  parts ------>last  machine
pin is the real objct    parts creat objct    machin like facade make object
"""

from abc import ABC,abstractmethod,ABCMeta
# from PyMata import pymata
import seting
import inspect
import asyncio
# from multiprocessing import Manager
from functools import partial
import time
from multiprocessing import Pipe, Process
import engine
last_direct_stop = 0
forward = 1
backward = 2
encode_push_pull_stop_percent = 0.65
# waiting_read_event = asyncio.Event

load_data2 = seting.parameter_load_data



class ABSpin(ABC):
    __class__ = ABCMeta

    def __init__(self, pin_parameter, board_obj_name=None, pin_number=None, pin_AD_type="DIGITAL", pin_IO_type = 'INPUT'):
        self.low_equepment_objs = []
        self.last_W_data = None
        self.pin_value = None
        self.write_value = None
        self.pin_id_map_equepment_objs = []
        if pin_parameter != None:
            self.pin_parameter = pin_parameter
            self.pin_number = pin_parameter[1]
            self.pin_AD_type = pin_parameter[2]
            self.pin_IO = pin_parameter[3]
            self.board_obj = pin_parameter[0]
            self.something_wrong = None
            self.storage = []
            self.flag = False
        if pin_parameter == None:
            self.pin_parameter = (board_obj_name, pin_number, pin_AD_type, pin_IO_type)
            self.pin_number = pin_number
            self.pin_AD_type = pin_AD_type
            self.pin_IO = pin_IO_type
            self.board_obj = board_obj_name
        if self.pin_IO == "OUTPUT":
            self.write_value = None

    def set_(self):
        turn_back = None
        if self.pin_IO == 'OUTPUT':

            # if self.pin_number == 50:
            #     print(self.pin_number, "55 pin trace.............set2")
            if hasattr(self, "read_single"):
                delattr(self, "read_single")

            def write_single(self, value):
                self.write_value = value
            self.write_single = partial(write_single, self)
            turn_back = self.write_single
        if self.pin_IO == 'INPUT':
            if hasattr(self, "write_single"):
                delattr(self, "write_single")

            def read_single(self, machine_read_data):
                time_, com_dict = list(machine_read_data.items())[0]
                self.pin_value = com_dict[self.pin_parameter]
                for equepment in self.pin_id_map_equepment_objs:
                    equepment.read_status(time_, self.pin_value, self.pin_parameter)
            self.read_single_ = partial(read_single, self)
            # setattr(self, "read_single_", read_single_)
            turn_back = self.read_single_
        return turn_back

    def register_equeepment(self, low_equepment_obj):
        self.low_equepment_objs.append(low_equepment_obj)
        self.pin_id_map_equepment_objs.append(low_equepment_obj)


class DIGITAL(ABSpin):
    def __init__(self, pin_parameter, board_obj=None, pin_number=None, pin_AD_type="DIGITAL", pin_IO_type = 'INPUT'):
        super().__init__(pin_parameter, board_obj_name=board_obj, pin_number=pin_number,
                         pin_AD_type=pin_AD_type, pin_IO_type=pin_IO_type)


class ANALOG(ABSpin):
    def __init__(self, pin_parameter, board_obj=None, pin_number=None, pin_AD_type="ANALOG", pin_IO_type='INPUT'):
        super().__init__(pin_parameter, board_obj_name=board_obj, pin_number=pin_number, pin_AD_type=pin_AD_type,
                         pin_IO_type=pin_IO_type)


class pwm_pin(ABSpin):
    def __init__(self, pin_parameter, board_obj=None, pin_number=None, pin_AD_type="DIGITAL", pin_IO_type='INPUT'):
        super().__init__(pin_parameter, board_obj_name=None, pin_number=None, pin_AD_type="DIGITAL",
                         pin_IO_type='INPUT')


class servo_pin(ABSpin):
    def __init__(self, pin_parameter, board_obj=None, pin_number=None, pin_AD_type="DIGITAL", pin_IO_type='INPUT'):
        super().__init__(pin_parameter, board_obj_name=None, pin_number=None, pin_AD_type="DIGITAL",
                         pin_IO_type='INPUT')
class modbus_rtu_485_child_machine__(ABSpin):
    def __init__(self, pin_parameter, read_code, write_code, set_code=None):
        super(modbus_rtu_485_child_machine__, self).__init__(pin_parameter, board_obj_name=None, pin_number=None, pin_AD_type="DIGITAL", pin_IO_type = 'INPUT')
        self.pin_parameter = pin_parameter
        self.write_code = write_code
        self.read_code = read_code
        self.set_code = set_code



class Equepment(metaclass=ABCMeta):
    """ def equepmet_read_begin()    def operation_equepmet(self)  is the interface function
    """
    def __init__(self, equepment_obj_name, observation, all_equepment_updated):       ##   ABCMeta
        self.observation = observation
        self.equepment_obj_name = equepment_obj_name
        self.equepment_pinname_map_pinobj = {}
        self.pin_input_count = seting.setting_class.getEquepment_obj_readpin_number(self.equepment_obj_name)
        self.recev_times = 0
        self.recev_everypins_data = {}
        self.get_equepment_pin_obj_and_other_parameter()
        self.simulation = False
        self.order = "Auto"    ## has # Auto Manual
        self.all_equepment_updated = all_equepment_updated

        self.coordinate_delta = 5
        if self.equepment_obj_name == "Equepment_main_beam_obj":
            print(f"im creat Equepment_main_beam_obj  {__class__}   {inspect.currentframe().f_code.co_name}   {inspect.currentframe().f_lineno}")
    def read_status(self, time_, pin_value, pin_id):

# get every pin send itself data  every times .and exclude
# other pin data in function parameter (self,time_, pin_value,pin_id)
        self.recev_times = self.recev_times + 1
        self.recev_everypins_data[pin_id] = (time_, pin_value)
        self.pin_value = pin_value
        self.time_ = time_
        if self.recev_times == self.pin_input_count:
            self.recev_times = 0
            self.equepmet_read_begin_befor(self.recev_everypins_data)
        return time_, pin_value

    def equepmet_read_begin_befor(self,recev_everypins_data):

        self.equepmet_read_begin()
        self.all_equepment_updated.statistics_updated_number()   ## statistics runs equepment number
        # importent  here  all is begin

    def  equepmet_read_begin(self):
        raise NotImplemented

    def operation_equepment(self, operation_pin_in_equepment, value):
        raise NotImplemented
         #     self.equepment_pin_obj  this dict  be used to operation  {key= pin_id_name    value = pin_obj}
        # pin_id_name  is pin_name in equepment like "A_pin"     "Backward_pin"

    def regester_equepment_pin_obj(self):
        for equepmennt_obj_name, pin_obj in self.equepment_pinname_map_pinobj[self.equepment_obj_name].items():
            pin_obj.register_equeepment(self)
            pin_obj.set_()
        if self.equepment_obj_name == "Equepment_main_beam_obj":
            print(f"im creat Equepment_main_beam_obj  {__class__}   {inspect.currentframe().f_code.co_name}   {inspect.currentframe().f_lineno}")
    def get_equepment_pin_obj_and_other_parameter(self):
# creat self all parameter   and get equepment_pinname_map_pinobj
        every_equepment_pinname_map_pinpatameter = seting.setting_class.get_everyequepment_pinname_map_pingparameter_dict()
        every_equepment_pinname_map_pinobj = {}
        for equepment_obj_name,equepment_obj_pin_parameter in every_equepment_pinname_map_pinpatameter.items():
              every_equepment_pinname_map_pinobj[equepment_obj_name] = {}
              for pinname_,pinobj_parameter in equepment_obj_pin_parameter.items():
                try:
                  every_equepment_pinname_map_pinobj[equepment_obj_name][pinname_] = self.observation.pin_obj[pinobj_parameter]
                except Exception:
                    print(equepment_obj_name)

        self.equepment_pinname_map_pinobj = every_equepment_pinname_map_pinobj

        for attr_, value_ in self.equepment_pinname_map_pinobj[self.equepment_obj_name].items():
            setattr(self, attr_, value_)
        equepmentj_other_parameter_without_class_and_pin  = seting.setting_class.equepmentj_other_parameter_without_class_and_pin()[self.equepment_obj_name]

        if equepmentj_other_parameter_without_class_and_pin:

            for attr1_, value1_ in equepmentj_other_parameter_without_class_and_pin.items():
                # print(self.equepment_obj_name)
                setattr(self, attr1_, value1_)      #   #

    def reset(self):
        raise NotImplemented



class push_pull_rocker_arm(Equepment):
    def __init__(self, equepment_obj_name, observation, all_equepment_updated):
        super().__init__(equepment_obj_name, observation, all_equepment_updated)
        self.flag = 0  ###changge this to 1,  if it still = 0  it means  data is not process
        self.direction = None
        self.delta_push_pull_ = 5
        self.coordinate = 0
        self.last_temporary_coordiate = None
        self.Backward_pin_last = True
        self.Forward_pin_last = True
        self.PUSH_LEVEL = {}
        self.PULL_LEVEL = {}
        self.operation__ = None
        old_parameter_load_data = seting.parameter_load_data
        self.parse_pull_push_level()
        new_equepment_obj_name = equepment_obj_name + "_coordinate"
        self.coordinate_start = old_parameter_load_data[new_equepment_obj_name][0]
        self.coordinate_stop = old_parameter_load_data[new_equepment_obj_name][1]
        self.coordinate_end = old_parameter_load_data[new_equepment_obj_name][2]
        self.stop_gera_delta_coordinate = old_parameter_load_data[new_equepment_obj_name][3]


    def parse_pull_push_level(self):

        every_step = (self.coordinate_stop - self.coordinate_start) / 6
        self.PUSH_LEVEL[6] = self.coordinate_start
        self.PUSH_LEVEL[5] = every_step + self.coordinate_start
        self.PUSH_LEVEL[4] = every_step * 2 + self.coordinate_start
        self.PUSH_LEVEL[3] = every_step * 3 + self.coordinate_start
        self.PUSH_LEVEL[2] = every_step * 4 + self.coordinate_start
        self.PUSH_LEVEL[1] = every_step * 5 + self.coordinate_start
        self.PUSH_LEVEL[0] = every_step * 6 + self.coordinate_start

        every_step_pull = (self.coordinate_end - self.coordinate_stop) / 6
        self.PULL_LEVEL[1] = every_step_pull + self.coordinate_stop
        self.PULL_LEVEL[2] = every_step_pull * 2 + self.coordinate_stop
        self.PULL_LEVEL[3] = every_step_pull * 3 + self.coordinate_stop
        self.PULL_LEVEL[4] = every_step_pull * 4 + self.coordinate_stop
        self.PULL_LEVEL[5] = every_step_pull * 5 + self.coordinate_stop
        self.PULL_LEVEL[6] = every_step_pull * 6 + self.coordinate_stop

        self.gear_list = [
            self.PUSH_LEVEL[6],
            self.PUSH_LEVEL[5],
            self.PUSH_LEVEL[4],
            self.PUSH_LEVEL[3],
            self.PUSH_LEVEL[2],
            self.PUSH_LEVEL[1],
            self.PUSH_LEVEL[0],
            self.PULL_LEVEL[1],
            self.PULL_LEVEL[2],
            self.PULL_LEVEL[3],
            self.PULL_LEVEL[4],
            self.PULL_LEVEL[5],
            self.PULL_LEVEL[6],
        ]

    @property
    def get_current_gear(self):
        new_list = [*map(lambda x: abs(x - self.coordinate), self.gear_list)]
        gear_number = new_list.index(min(new_list))
        if gear_number == 0:
            delta_ds = self.coordinate - self.PUSH_LEVEL[0]
            if abs(delta_ds) > self.stop_gera_delta_coordinate:
                if delta_ds > 0:
                    gear_number = 5
                else:
                    gear_number = 7
            else:
                gear_number = 6
        # data range is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12], 6 is the stop gear
        return gear_number

    def operation_target_coordinate(self, gear_coordinate):                    #### other class operation action is here

        if self.coordinate - gear_coordinate > self.delta_push_pull_:
            self.operation__ = self.forward_operation
        elif self.coordinate - gear_coordinate < - self.delta_push_pull_:
            self.operation__ = self.back_operation
        else:
            self.stop_action()
            return True
        if  self.operation__ != None:
            self.operation__()


    def forward_operation(self):   ## only forward
        if self.Backward_pin_last is not True or self.Forward_pin_last is not False:
            self.Forward_pin.write_single(False)
            self.Backward_pin.write_single(True)
            self.Backward_pin_last = True
            self.Forward_pin_last = False

    def back_operation(self):
        if self.Backward_pin_last is not False or self.Forward_pin_last is not True:
            try:
                self.Forward_pin.write_single(True)
            except Exception:
                print(self.equepment_obj_name)
            self.Backward_pin.write_single(False)
            self.Backward_pin_last = False
            self.Forward_pin_last = True

    def stop_action(self):
        print("i do stop", type(self.Forward_pin), self.Forward_pin.pin_number, self.Forward_pin.pin_IO)
        if self.Backward_pin_last is not True or self.Forward_pin_last is not True:
            self.Forward_pin.write_single(True)
            self.Backward_pin.write_single(True)
            self.Backward_pin_last = True
            self.Forward_pin_last = True

    def equepmet_read_begin(self):
        if self.simulation is False:
            self.coordinate = self.modbus_rtu_485_xiAnZz12_0_pin.pin_value
            self.flag = True



class EncodeEquepment(Equepment):
    direction = {
        (0, 1): forward,   #"clock_wise"
        (1, 0): backward   # "anti_cloc wise"
    }

    def __init__(self, equepment_obj_name, observation,all_equepment_updated):
        super().__init__(equepment_obj_name, observation,all_equepment_updated)
        self.flag = 0      ###changge this to 1,  if it still = 0  it means  data is not process
        self.direction = None
        self.cycle_number = 0
        self.__Alast = 0
        self.count = 0
        self.__last_b  = None
        self.__currentb = None
        self.coordinate = 0

    def reset(self):
        self.flag = 0
        self.direction = None
        self.cycle_number = 0
        self.__Alast = 0
        self.count = 0
        self.__last_b = None
        self.__currentb = None
        self.coordinate = 0

    def equepmet_read_begin(self):
        print("im in subclass")
        pass

    def encode_decode(self, A, B):  ###this function an usede by distance and direct
        distance = 0

        if self.__Alast == 1 and A == 0:
            self.__last_b = B
            self.__Alast = A
            self.flag = True
        elif self.__Alast == 0 and A == 1:
            self.__currentb = B
            self.__Alast = A
        else:
            pass
        if self.__currentb != None or self.__last_b != None:
              self.direction = EncodeEquepment.direction[self.__last_b,self.__currentb]
        if self.flag == True and self.direction == forward :
            self.count = self.count + 1
            self.flag = 0
            if self.count == self.puls:
                self.cycle_number = self.cycle_number +1
                self.count = 0
        elif self.flag == True and self.direction == backward :
            self.count = self.count - 1
            self.flag = 0
            if self.count == 0:
                self.cycle_number = self.cycle_number - 1
                self.count = self.puls-1
        self.coordinate = (self.cycle_number + self.count/self.puls)*self.circumference_of_cycle  ###this is define in other
    def equepmet_read_begin(self):
        if self.simulation is False:
            self.encode_decode(self.A_pin.pin_value, self.B_pin.pin_value)

class drill_hole_orbit():
    def __init__(self,ardiuno_board,hole_code,hole_type=73):
        self.hole_code = hole_code
        self.hole_type = hole_type
        self.forward_hole = None
        self.forward_total_count = 0
        self.back_hole = None
        self.back_total_count = 0
        self.push_pull_pressure =0
        self.torque_pressure = 0
        self.distance = 0
        self.angle_left_right = 0
        self.angle_up_down = 0
        self.deep = 0
        self.GPS = []
        self.flag = False
        self.storage_hole =[]

    def equepmet_read_begin(self, recev_everypins_data):
        pass


class line_distance(Equepment):
    # all the rule is normal is small  and move forward of the pole  the digital is became greater.
    def __init__(self, equepment_obj_name, observation, all_equepment_updated):
        super().__init__(equepment_obj_name, observation, all_equepment_updated)
        self.zero_begin_set_flag = 0
        self.lin_end_set_flag = 1023
        self.time__ = 0
        self.coordinate = None
        self.cycle_number_coordinate = None

    def coordinate_(self):        #this is the out class interface function
        # print("i caclude coodinate",self.equepment_obj_name)
        if self.equepment_obj_name in ("Equepment_main_beam_obj", "Equepment_line_distance_measure_4m_beam"):
            self.coordinate = self.modbus485__2_MainBeam_4mRopeEncode_pin.pin_value
            if hasattr(self, "modbus_rtu_485MainBeam4mAbsEncode_pin"):
                self.cycle_number_coordinate = self.modbus_rtu_485MainBeam4mAbsEncode_pin.pin_value
        elif self.equepment_obj_name == "Equepment_line_distance_measure_1m_drill_box":
            self.coordinate = self.modbus485__2_BoxHand1mRopeEncode_pin.pin_value
        else:
            self.coordinate = self.recve_pin.pin_value


    def equepmet_read_begin(self):
        if self.simulation is False:
            self.coordinate_()


class pressure_measure(Equepment):
    def __init__(self, equepment_obj_name, observation,all_equepment_updated):
        super().__init__(equepment_obj_name, observation,all_equepment_updated)
        self.zero_begin_set_flag = 0
        self.pressure_zero = 0
        self.pressure = None
    def reset(self):
        if self.zero_begin_set_flag == True:
            self.pressure_zero = self.recve_pin.pin_value
    def calculat(self):
        if self.recve_pin.pin_value == None:
            self.recve_pin.pin_value = 0
        self.pressure =  (self.recve_pin.pin_value - self.pressure_zero)/(1024-self.pressure_zero)*self.measure_range
    def equepmet_read_begin(self):
        self.calculat()

class water_deep(Equepment):
    def __init__(self, equepment_obj_name, observation,all_equepment_updated):
        super().__init__(equepment_obj_name, observation,all_equepment_updated)
        self.water_deep_number = None
        self.warter_deep_safe = 0

    def equepmet_read_begin(self):
        self.calculat()

    def calculat(self):
        if self.warter_deep_pin.pin_value != None:
            data = (self.warter_deep_pin.pin_value - 205)/(1024-205)*3000
        else:
            data = 0
        self.water_deep_number = data


class angle_torque(Equepment):
    def __init__(self, equepment_obj_name, observation,all_equepment_updated):
        super().__init__(equepment_obj_name, observation,all_equepment_updated)
        self.zero_angle_set_flag = False
        self.zero_angle = 0
        self.angle = None
    def reset(self):
        if self.zero_angle_set_flag == True:
                self.zero_angle = self.recve_pin.pin_value

    def calculat(self):
        if self.recve_pin.pin_value is None:
            self.recve_pin.pin_value = 0
        if self.recve_pin.pin_value >= self.zero_angle:
            angle = self.recve_pin.pin_value - self.zero_angle
        else:
            angle = self.recve_pin.pin_value + (1024-self.zero_angle)
        self.angle = angle/1024*360

    def equepmet_read_begin(self):
        self.calculat()

class main_beam_position(Equepment):
    print(f"im in {__file__},   my lines is {inspect.currentframe().f_lineno}, name is {inspect.currentframe().f_code.co_name}")
    def equepmet_read_begin(self):
        pass

class drill_box(Equepment):
    def __init__(self, equepment_obj_name, observation,all_equepment_updated):
        super().__init__(equepment_obj_name, observation,all_equepment_updated)
        self.zero_begin_set_flag = 0
        self.order = None
        self.lastpole_box_arm_backward_pin = False
        self.lastpole_box_arm_forward_pin = False
        self.last_updown_up = False
        self.last_updown_down = False
        self.last_hand_grap_time = 0
        self.lastlast_hand_relax_time = 0
        self.lastpole_box_hand_grip_pin = False
        self.lastpole_box_hand_relax_pin = False
        self.delta_time_grap_faile_time = load_data2["delta_time_grap_faile_time"]

        self.point_beam_grap_coordinate = load_data2["point_beam_grap_coordinate"]
        self.point_beam_grap_cycle_number = load_data2["point_beam_grap_cycle_number"]

        self.point_unstop_beam_coordinate = load_data2["point_unstop_beam_coordinate"]
        self.point_unstop_beam_cycle_number = load_data2["point_unstop_beam_cycle_number"]

        self.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate = load_data2["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate"]
        self.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number = load_data2["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number"]

        self.box_updown_column_up = load_data2["box_updown_column_up"]
        self.box_updown_bottom = load_data2["box_updown_bottom"]

        self.box_updown_column_can_grap = load_data2["box_updown_column_can_grap"]

        self.pole_point_delta = load_data2["pole_point_delta"]
        self.begin_grap_time = None


        self.box_grap_hand_tight_strong = load_data2["box_grap_hand_tight_strong"]
        self._drill_box_grap_hand_tight_slight = load_data2["_drill_box_grap_hand_tight_slight"]
        self.drill_box_grap_hand_tight_greater_strong = load_data2["drill_box_grap_hand_tight_greater_strong"]
        self.drill_box_grap_hand_relax_full = load_data2["drill_box_grap_hand_relax_full"]
        self.drill_box_grap_hand_relax_half = load_data2["drill_box_grap_hand_relax_half"]
        self.drill_box_grap_hand_relax_greater_part = load_data2["drill_box_grap_hand_relax_greater_part"]
        self.point1_coordinate = load_data2["point1_coordinate"]
        self.point2_coordinate = load_data2["point2_coordinate"]
        self.point3_coordinate = load_data2["point3_coordinate"]

        self.point1_cycle_number = load_data2["point1_cycle_number"]
        self.point2_cycle_number = load_data2["point2_cycle_number"]
        self.point3_cycle_number = load_data2["point3_cycle_number"]


    def equepmet_read_begin(self):
        pass

    def operate_box_hand(self, order_obj):
        if self.order == "forward":
            if (self.beam_taile_hand_pin is True and self.beam_forward_hand_pin is True) or (
                    self.beam_taile_hand_pin is False and self.beam_forward_hand_pin is False ):
                order_obj()
            else:
                self.grap_hand_stop()
        if self.order == "backward":
            if self.order == "forward":
                if (self.beam_taile_hand_pin == True and self.beam_forward_hand_pin == True) or (
                        self.beam_taile_hand_pin == False and self.beam_forward_hand_pin == False):
                    order_obj()
                else:
                    self.grap_hand_stop()

    def grap_hand_stop(self):
        if self.lastpole_box_arm_backward_pin != False or self.lastpole_box_arm_forward_pin != False:
            self.lastpole_box_arm_backward_pin = False
            self.lastpole_box_arm_forward_pin = False
            self.pole_box_arm_forward_pin.write_single(False)
            self.pole_box_arm_backward_pin.write_single(False)
        if self.lastpole_box_arm_backward_pin is False and self.lastpole_box_arm_forward_pin is False:
            if self.begin_grap_time == None:
                self.begin_grap_time = time.time()
            d_time_ = time.time() - self.begin_grap_time
            if d_time_ >= self.box_grap_hand_tight_strong:
                self.begin_grap_time = None
                return True


    def handforward(self):
        if self.lastpole_box_arm_backward_pin != False or self.lastpole_box_arm_forward_pin != True:
            self.pole_box_arm_backward_pin.write_single(False)
            self.pole_box_arm_forward_pin.write_single(True)
            self.lastpole_box_arm_backward_pin = False
            self.lastpole_box_arm_forward_pin = True

    def handbackward(self):
        if self.lastpole_box_arm_backward_pin != True or self.lastpole_box_arm_forward_pin != False:
            self.pole_box_arm_forward_pin.write_single(False)
            self.pole_box_arm_backward_pin.write_single(True)
            self.lastpole_box_arm_forward_pin = False
            self.lastpole_box_arm_backward_pin = True

    def updown_up(self):
        if self.last_updown_up != True or self .last_updown_down != False:
            self.last_updown_down = False
            self.last_updown_up = True
            self.pole_box_down_pin.write_single(False)
            self.pole_box_up_pin.write_single(True)

    def updown_down(self):
        if self.last_updown_up != False or self .last_updown_down != True:
            self.last_updown_down = True
            self.last_updown_up = False
            self.pole_box_up_pin.write_single(False)
            self.pole_box_down_pin.write_single(True)

    def updown_stop(self):
        self.last_updown_down = False
        self.last_updown_up = False
        self.pole_box_up_pin.write_single(False)
        self.pole_box_down_pin.write_single(False)

    def hand_grap_time(self,hand_time):
        if self.lastpole_box_hand_grip_pin != True or self.lastpole_box_hand_relax_pin != False:
            self.pole_box_hand_relax_pin.write_single(False)
            self.pole_box_hand_grip_pin.write_single(True)
            self.lastpole_box_hand_grip_pin = True
            self.lastpole_box_hand_relax_pin = False
            if self.lastlast_hand_grap_time == 0:
                self.lastlast_hand_grap_time = time.time()
            delta_time = time.time() - self.lastlast_hand_grap_time
            if delta_time > hand_time:
                self.pole_box_hand_grip_pin.write_single(False)
                self.lastpole_box_hand_grip_pin = False
            if delta_time - hand_time > self.delta_time_grap_faile_time:
                self.lastlast_hand_grap_time = 0
                return False
            else:
                if delta_time < hand_time:
                    self.lastlast_hand_grap_time = 0
                    return True



    def hand_grap_relax(self):
        if self.lastpole_box_hand_grip_pin != False or self.lastpole_box_hand_relax_pin != True:
            self.pole_box_hand_relax_pin.write_single(True)
            self.pole_box_hand_grip_pin.write_single(False)
            self.lastpole_box_hand_grip_pin = False
            self.lastpole_box_hand_relax_pin = True
            if self.lastlast_hand_relax_time == 0:
                self.lastlast_hand_relax_time = time.time()
            delta_time = time.time() - self.lastlast_hand_relax_time
            if delta_time > self.drill_box_grap_hand_relax_full:
                self.pole_box_hand_relax_pin.write_single(False)
                self.lastpole_box_hand_grip_pin = False
                return True
    def hand_grap_relax_half_time(self):
        if self.lastpole_box_hand_grip_pin != False or self.lastpole_box_hand_relax_pin != True:
            self.pole_box_hand_relax_pin.write_single(True)
            self.pole_box_hand_grip_pin.write_single(False)
            self.lastpole_box_hand_grip_pin = False
            self.lastpole_box_hand_relax_pin = True
            if self.lastlast_hand_relax_time == 0:
                self.lastlast_hand_relax_time = time.time()
            delta_time = time.time() - self.lastlast_hand_relax_time
            if delta_time > self.drill_box_grap_hand_relax_half:
                self.pole_box_hand_relax_pin.write_single(False)
                self.lastpole_box_hand_grip_pin = False
                return True
    def hand_grap_relax_greater_part_time(self):
        if self.lastpole_box_hand_grip_pin != False or self.lastpole_box_hand_relax_pin != True:
            self.pole_box_hand_relax_pin.write_single(True)
            self.pole_box_hand_grip_pin.write_single(False)
            self.lastpole_box_hand_grip_pin = False
            self.lastpole_box_hand_relax_pin = True
            if self.lastlast_hand_relax_time == 0:
                self.lastlast_hand_relax_time = time.time()
            delta_time = time.time() - self.lastlast_hand_relax_time
            if delta_time > self.drill_box_grap_hand_relax_greater_part:
                self.pole_box_hand_relax_pin.write_single(False)
                self.lastpole_box_hand_grip_pin = False
                self.lastlast_hand_relax_time = 0
                return True
    def beam_first_point_hand_grap_relax_greater_part_time(self):
        if self.lastpole_box_hand_grip_pin != False or self.lastpole_box_hand_relax_pin != True:
            self.pole_box_hand_relax_pin.write_single(True)
            self.pole_box_hand_grip_pin.write_single(False)
            self.lastpole_box_hand_grip_pin = False
            self.lastpole_box_hand_relax_pin = True
            if self.lastlast_hand_relax_time == 0:
                self.lastlast_hand_relax_time = time.time()
            delta_time = time.time() - self.lastlast_hand_relax_time
            if delta_time > self.drill_box_grap_hand_relax_greater_part:
                self.pole_box_hand_relax_pin.write_single(False)
                self.lastpole_box_hand_grip_pin = False
                self.lastlast_hand_relax_time = 0
                return True


class   lamp_(Equepment):
    pass


class warning_lamp(Equepment):
    pass


class all_equepment_updated():
    def __init__(self):
        self.updated_equepmet_number = 0
        self.all_equepment_numbers = len(seting.setting_class.getEquepment_obj_getEquepment_class())
        self.order = []

    def statistics_updated_number(self):
        self.updated_equepmet_number = self.updated_equepmet_number + 1
        if self.updated_equepmet_number == self.all_equepment_numbers:
            self.updated_equepmet_number = 0
            self.begin()

    def begin(self):
        for order in self.order:
            order.run()
    def regester_order(self,order_obj):
        self.order.append(order_obj)


class observation:

    def __init__(self):

        self.pipeGetFromMachineBoard, self.pipeSendToMachineBoard = self.run_borads()
        self.getisetin_data()
        self.pin_obj = {}
        self.register_pin_obj()
        self.write_collect_data = {}
        self.read_data_from_board = None
        self.send_statue_event_flag = False


    def run_borads(self):
        pipeGetFromObservation, pipeSendToMachineBoard = Pipe()
        pipeGetFromMachineBoard, pipeSendtoObservation = Pipe()
        print(f"im class is {inspect.currentframe().f_code.co_name}, im lines {inspect.currentframe().f_lineno}")
        board_engine = engine.board_basic_data_operation(pipeGetFromObservation, pipeSendtoObservation)
        print(f"im class is {inspect.currentframe().f_code.co_name}, im lines {inspect.currentframe().f_lineno}")
        board_process = Process(target=board_engine.runing)
        board_process.start()
        return pipeGetFromMachineBoard, pipeSendToMachineBoard

    def register_pin_obj(self):
        for pin_ in self.port_all_need_read_pin:

            try:
                self.pin_obj[pin_] = eval(pin_[2])(pin_)
            except Exception as e:
                self.port_all_need_read_pin.remove(pin_)

    def collect_write_data(self):
        for pin_w_obj in self.pin_obj.values():
                if pin_w_obj.pin_number in (49, 50):
                    if pin_w_obj.write_value != None:

                         print("im in collect ,pin_number is {}, pin_value is {}, pin_Io is {} ".format(
                             pin_w_obj.pin_number, pin_w_obj.write_value,  pin_w_obj.pin_IO))
                if pin_w_obj.pin_IO == 'OUTPUT':
                    if pin_w_obj.write_value != None:
                        self.write_collect_data[pin_w_obj.pin_parameter] = pin_w_obj.write_value
                        print("current operation  pin number is {} and data is {}".format(pin_w_obj.pin_parameter, pin_w_obj.write_value))
                        pin_w_obj.write_value = None

        time_ = time.time()
        if len(self.write_collect_data) != 0:
            write_machine = {time_: self.write_collect_data}
            return write_machine
        else:
            return None

    def distribute_read_data(self, getdata):
        for key_time, value in getdata.items():
            for pin, pin_value in value.items():
                # print(pin, pin_value)
                self.pin_obj[pin].pin_value = pin_value
                if hasattr(self.pin_obj[pin], "read_single_"):
                    self.pin_obj[pin].read_single_(getdata)

    def running(self, every_call_back_function,):
        self.mashine_statue_obervision_time = 0.1
        distribute_read_data = self.distribute_read_data
        delta_last = None
        write_collect_data_ = self.write_collect_data
        collect_write_data = self.collect_write_data
        pipeGetFromMachineBoard = self.pipeGetFromMachineBoard
        pipeSendToMachineBoard = self.pipeSendToMachineBoard
        while True:
            if not delta_last:
                delta_last = time.time()
            getdata = None
            try:
                 getdata = pipeGetFromMachineBoard.recv()
                 self.read_data_from_board = getdata
            except Exception as e:
                print(inspect.currentframe().f_lineno, __class__, __file__)
                print(e)
            if getdata:
                # self.read_data_from_board = getdata
                distribute_read_data(getdata)
                collect_write_data = collect_write_data()
                if collect_write_data is not None:
                    pipeSendToMachineBoard.send(collect_write_data)
                    write_collect_data_.clear()
                if self.send_statue_event_flag:
                    current_time = time.time()
                    delta_current = current_time - delta_last
                    if delta_current > self.mashine_statue_obervision_time:
                        every_call_back_function()
                        delta_last = current_time

    def getisetin_data(self):
        self.port_all_need_read_pin = seting.setting_class.getsetin_data2()


    def Give_pinobj_equepment(self,pin_list):
        for pin_ in pin_list.keys():
            pin_list[pin_] = self.pin_obj[pin_]
        return pin_list


class sensor_wrong(Exception):
    def __init__(self, single):
        self.single = single
        
    def __str__(self):
        return self.single
###  here  get pre_hole and next hole      change them value


