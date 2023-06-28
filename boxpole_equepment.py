__author__ = "boss"
__date__ = '2022/11/29 16:42'
import time
import pickle
from abs_task_step import step_
import seting
relax_time = 0.7
box_hand_arm_run_stop_time = 0.4
grap_time_long = 0.7
grap_time_middle = 0.4
grap_time_slight = 0.2
box_power_distance = {
    (1, 1): 150, (1, 2): 150, (1, 3): 150, (1, 4): 150, (1,5): 150,(1,6):150,(1,7):150,(1,8):150,(1,9):150,(1,10):150,
    (2, 1): 150, (2, 2): 150, (2, 3): 150, (2, 4): 150, (2,5): 150,(2,6):150,(2,7):150,(2,8):150,(2,9):150,(2,10):150,
    (3, 1): 150, (3, 2): 150, (3, 3): 150, (3, 4): 150, (3,5): 150,(3,6):150,(3,7):150,(3,8):150,(3,9):150,(3,10):150,
}
max_forward_pressure = 12
max_back_ward_pressure = 33
try:
    with open("parameter_backup_data.tex", "rb") as parameter4:
        load_data2 = pickle.load(parameter4)
except:
    load_data2 = None


try:
    box_hand_grap_arm_start_coordinnate = load_data2["point_unstop_beam"]
    box_updown_column_up = load_data2["box_updown_column_up"]
    box_updown_column_can_grap = load_data2["box_updown_column_can_grap"]
    box_hand_low_grap_time = 0.3  # this data  must test  and get a new data
    box_updown_bottom = load_data2["box_updown_bottom"]
except:
    box_hand_grap_arm_start_coordinnate = 700
    box_updown_column_up =  190
    box_updown_column_can_grap =  900
    box_hand_low_grap_time = 0.3  # this data  must test  and get a new data
    box_updown_bottom = 0
class delta_time():
    def __init__(self, delay_tim=0.0):
        self.first_time = time.time()
        self.delay_tim = delay_tim

    @property
    def delay_time(self):
        if (time.time() - self.first_time) > self.delay_tim:
            return True


class prepare_to_reach_beam_without_pole_step(step_):
    only = None


    def __init__(self, machin_obj, box_pole_obj):
        super().__init__()
        self.machin_obj = machin_obj
        self.box_pole_obj = box_pole_obj
        self.point_beam_grap = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.can_hold_beam_pole_coordinate

    def __new__(cls, *args, **kwargs):
        if prepare_to_reach_beam_without_pole_step.only == None:
            prepare_to_reach_beam_without_pole_step.only = super(prepare_to_reach_beam_without_pole_step, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return prepare_to_reach_beam_without_pole_step.only

    def run(self):
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, False, False, False, False, False, False):
            with self.in_run(2) as T:
                if T == True:
                    self.step[2][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, False, False, False, False, False):
            with self.in_run(3) as T:
                if T == True:
                    self.step[3][1] = True
                    return True

    def run_1(self):
        if self.box_prepare_obj.drill_box.hand_run(box_hand_grap_arm_start_coordinnate) == True:
            return True

    def run_2(self):
       if self.box_prepare_obj.drill_box.Equepment_drill_box_digit_piont.hand_grap_relax(relax_time=relax_time) == True:
           return True

    def run_3(self):
        if  self.box_prepare_obj.drill_box.hand_run(self.point_beam_grap) == True:
            return True
import machine_high_lever_equepment
class box_prepare():

    def __init__(self, machine_obj):
        self.box_pole_obj = box_pole(machine_obj)
        self.machine_obj = machine_high_lever_equepment.machine()
        self.last_hand_grap = False
        self.box_power_distance = box_power_distance
        self.point3 = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point3_coordinate
        self.point2 = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point2_coordinate
        self.point1 = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point1_coordinate

        self.point3_cycle_number = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point3_cycle_number
        self.point2_cycle_number = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point2_cycle_number
        self.point1_cycle_number = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point1_cycle_number

        self.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate
        self.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number

        self.point_beam_grap =  self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point_beam_grap_coordinate
        self.point_beam_grap_cycle_number = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point_beam_grap_cycle_number

        self.point_unstop_beam_coordinate =  self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point_unstop_beam_coordinate
        self.point_unstop_beam_cycle_number = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.point_unstop_beam_cycle_number

        self.point_unstop_beam = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate

        self.stop_point_rech = False
        self.updown_up = False
        self.reach_column_coordinate = False
        self.updown_dow_can_grap_pole_and_keep_down = False
        self.reach_cannt_stop_beam_coordinate = False
        self.prepare_count = 0

        self.prepare_in_reach_beam = False
        self.prepare_in_grap = False
        self.prepare_in_goback = False
        self.prepare_in_updow_up = False
        self.prepare_in_over = False
        self.result1 = False
        self.result2 = False
        self.result3 = False

        self.reach_start_prepare_flag = False

        self.prepare_in_goback__delay = delta_time(delay_tim=0.5)

    def prepare_let_beam_forward(self):
            if (self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_taile_hand_pin.pin_value is True and
                self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_forward_hand_pin.pin_value is True) or (
                   self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_taile_hand_pin.pin_value is False and
                   self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_forward_hand_pin.pin_value is False):
                self.machine_obj.drill_box.hand_run(self.machine_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate)
                if self.machine_obj.main_beam.self.Equepment_line_distance_measure_4m_beam.coordinate == \
                        self.machine_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate:
                    return True


    def prepare_pole_out(self):
        self.plan = (self.stop_point_rech, self.updown_up, self.reach_column_coordinate,
                     self.updown_dow_can_grap_pole_and_keep_down, self.reach_cannt_stop_beam_coordinate)
        if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_taile_hand_pin.pin_value is True and \
                self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_forward_hand_pin.pin_value is True:
            if self.machine_obj.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate == \
                        self.machine_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate:
                    return True
            else:
                if self.plan == (0, 0, 0, 0, 0):
                    self.reach_start_prepare()
                if self.plan == (1, 0, 0, 0, 0):
                    self.updown_dow_up()
                if self.plan == (1, 1, 0, 0, 0):
                    self.reach_column_coordinate_state()
                if self.plan == (1, 1, 1, 0, 0):
                    self.updown_dow_can_grap_pole()
                if self.plan == (1, 1, 1, 1, 0):
                    flag = self.reach_cant_stop_beam()
                    if flag is True:
                        self.stop_point_rech = False
                        self.updown_up = False
                        self.reach_column_coordinate = False
                        self.updown_dow_can_grap_pole_and_keep_down = False
                        self.reach_cannt_stop_beam_coordinate = False
                        return True

    def reach_cant_stop_beam(self):
        coordinate = self.machine_obj.drill_box.Equepment_drill_box_digit_piontdrill_box_unstoppable_coordinate
        result = self.machine_obj.drill_box.hand_run(coordinate)
        if self.machine_obj.drill_box.Equepment_line_distance_measure_dirll_box_updown.coordinate != 0:
            result_botom = self.machine_obj.drill_box.updown_run(0)
            if result is True and result_botom is True:
                self.stop_point_rech = True
                self.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop()
                return True

    def  updown_dow_can_grap_pole(self):      # here if doing not sucess  can
        result = self.machine_obj.drill_box.updown_run(box_updown_column_can_grap)
        if result is True:
            self.updown_dow_can_grap_pole_and_keep_down = True
            self.machine_obj.drill_box.Equepment_drill_box_digit_piont.updown_stop()
            grap_statu = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.hand_grap_time(box_hand_low_grap_time)
            if grap_statu is True:
                if self.updown_dow_bottom() is True:
                    if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.pole_box_arm_forward_pin.pin_value ==True and \
                            self.machine_obj.drill_box.Equepment_drill_box_digit_piont.pole_box_arm_backward_pin.pin_value == True:
                        self.updown_dow_can_grap_pole_and_keep_down = True
                        if self.prepare_count != 0:
                            self.prepare_count = 0
                        return True
                    else:
                        self.updown_dow_up()
                        self.stop_point_rech = False
                        self.updown_up = False
                        self.reach_column_coordinate = False
                        self.updown_dow_can_grap_pole_and_keep_down = False
                        self.reach_cannt_stop_beam_coordinate = False
                        self.prepare_count = self.prepare_count + 1



    def reach_column_coordinate_state(self):
         coordinate = self.box_pole_obj.calclude_get_column_coordinate_out_box()
         if coordinate is None:
             print("pole is nothing")
         else:
             result = self.machine_obj.drill_box.hand_run(coordinate)
             if result == True:
                 self.reach_column_coordinate = True
                 return True


    def reach_start_prepare(self):

                 if self.reach_start_prepare_flag == False:

                        if self.machine_obj.drill_box.hand_run(box_hand_grap_arm_start_coordinnate) == True:
                            self.reach_start_prepare_flag = True
                 if self.reach_start_prepare_flag == True:
                     if  self.machine_obj.drill_box.Equepment_drill_box_digit_piont.hand_grap_relax() == True:
                         self.reach_start_prepare_flag = False
                         return True

    def updown_dow_up(self):
        result = self.machine_obj.drill_box.updown_run(box_updown_column_up )
        if result == True:
            self.updown_up = True
            self.machine_obj.drill_box.Equepment_drill_box_digit_piont.updown_stop()
            return True


    def updown_dow_bottom(self):
        result = self.machine_obj.drill_box.updown_run(box_updown_bottom )
        if result == True:
            self.machine_obj.drill_box.Equepment_drill_box_digit_piont.updown_stop()
            return True



    def calclude_get_column_coordinate(self,point3,point2,point1):
        # coordinate = 0
        if point3 == True:
            coordinate = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_point3_pin_new
        elif (point3, point2) == (False, True):
            coordinate = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_point2_pin_new
        elif (point3, point2, point1) == (False,False,True):
            coordinate = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_point1_pin_new
        else:
            return "pole is None"
        return coordinate

    def pole_in(self):
        self.plan2 = (self.prepare_in_goback, self.prepare_in_updow_up, self.prepare_in_over)
        if self.plan2 == (False, False, False):
            self.prepare_in_goback_()
        if self.plan2 == (True, False, False):
            self.prepare_in_updow_up_()
        if self.plan2 == (True, True, False):
            over = self.prepare_in_over_()
            if over == True:
                self.prepare_in_goback = False
                self.prepare_in_updow_up = False
                self.prepare_in_over = False
                return True


    def prepare_in_goback_(self):
        pole = self.box_pole_obj.calclude_get_column_coordinate_in_box()
        if pole[0] == 1:
            coordinate = self.point1
        elif pole[0] == 2:
            coordinate = self.point2
        elif pole[0] == 3:
            coordinate = self.point3
        keep_distance_coordinat = coordinate + self.box_power_distance[pole]
        goback = pole_in_the_prepare_in_goback_step(self.box_pole_obj, self.machine_obj)
        if goback.run(coordinate,keep_distance_coordinat) == True:
            return True



    def prepare_in_updow_up_(self):
        result = self.machine_obj.drill_box.updown_run(box_updown_column_up)
        if result  is True:
            self.prepare_in_updow_up = True

    def prepare_in_over_(self):
        result3 = self.machine_obj.drill_box.hand_run(self.point_unstop_beam)
        if result3 is True:
            self.prepare_in_over = True
            return True

    def prepare_to_reach_beam_without_pole(self):
        prepare_to_reach_beam_without_pole_step_ = prepare_to_reach_beam_without_pole_step(self.machine_obj,self.box_pole_obj)
        if  prepare_to_reach_beam_without_pole_step_.run() == True:
                return True




    def prepare_in_grap_slight(self):
        grap_statu = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.hand_grap_time(grap_time_slight)
        if grap_statu == True:
            return True

    def prepare_in_grap_hold_tight(self):
        grap_statu = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.hand_grap_time(grap_time_long)
        if grap_statu == True:
            return True

    def prepare_to_reach_beam_with_pole(self):
        result1 = self.machine_obj.drill_box.hand_run(self.point_beam_grap)
        if result1 == True:
            return True


class box_pole():
    box_keys = list(box_power_distance.keys())  # box_pole.box_keys
    box_keys.sort()
    def __init__(self,machine_obj):
        self.box_power_distance = box_power_distance
        self.parameter = seting.setting_class.getEquepmentobj_other_parameter_without_class_and_pinparameter()[
            "Equepment_drill_box_digit_piont"]
        self.point3 = self.parameter['point3_coordinate']  # box_pole.point3
        self.point2 = self.parameter['point2_coordinate']  # box_pole.point2
        self.point1 = self.parameter['point1_coordinate']  # box_pole.point1
        box_keys = list(box_power_distance.keys())  # box_pole.box_keys
        self.boxkeys = box_pole.box_keys
        self.last_out_pole = {}  #####
        self.empty = set()
        self.machine_obj = machine_obj
        self.max_number = 0
        self.max_number_coordinate = 0
        self.in_hole_pole = 0
        self.other_in = 0
        self.other_out = 0
        self.box_no_pole = None
    def calclude_get_column_coordinate_out_box(self):
        self.point3 = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_point3_pin_new
        self.point2 = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_point2_pin_new
        self.point1 = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.box_point1_pin_new

        if (self.point3, self.point2, self.point1) == (False, False, False):
            self.box_no_pole = True
            return
        if self.point1 == True:
            self.last_out_pole = self.box_keys[0]

        else:
            for every_point in self.box_keys:
                if every_point < (2, 1):
                    self.box_keys.remove(every_point)
                    self.last_out_pole = (1, 10)
        if (self.point1, self.point2) == (0, 1):
            self.last_out_pole = self.box_keys[0]
        elif (self.point1, self.point2) == (0, 0):
            for every_point in self.box_keys:
                if every_point < (3, 1):
                    self.box_keys.remove(every_point)
                    self.last_out_pole = (2, 10)
        if (self.point1, self.point2, self.point3) == (0, 0, 1):
            self.last_out_pole = self.box_keys[0]


        return self.last_out_pole

    def calclude_get_column_coordinate_in_box(self):
        l_empty = list(self.empty)
        point = min(l_empty)
        coordinate = point[0]
        return coordinate

    def box_in_pole(self):
         box_sequence = list(self.empty)
         box_sequence.sort()

         self.empty.remove(self.last_out_pole)
         self.box_keys.append(self.last_out_pole)
         self.last_out_pole = box_sequence.pop(-1)
         self.box_keys.sort()

    def box_out_pole(self):
        if len(self.empty) < 30:
            self.box_keys.remove(self.last_out_pole)
            self.empty.add(self.last_out_pole)
        else:
            self.other_out_pole()


    def other_in_pole(self):
        self.other_in = self.other_in + 1


    def other_out_pole(self):
        self.other_out = self.other_out + 1


class pole_in_the_prepare_in_goback_step(step_):
    only = None

    def __init__(self, box_pole_obj, machin_obj):
        super().__init__(machin_obj, box_pole_obj )
        self.time_first = 0

    def __new__(cls, *args, **kwargs):
        if pole_in_the_prepare_in_goback_step.only == None:
            pole_in_the_prepare_in_goback_step.only = super(pole_in_the_prepare_in_goback_step, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return pole_in_the_prepare_in_goback_step.only

    def run(self, coordinate, keep_distance_coordinat):
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1, coordinate, keep_distance_coordinat) as T:
                if T is True:
                    self.step[1][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, False, False, False, False, False, False):
            with self.in_run(2, coordinate, keep_distance_coordinat) as T:
                if T is True:
                    self.step[2][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, False, False, False, False, False):
            with self.in_run(3, coordinate, keep_distance_coordinat) as T:
                if T is True:
                    self.step[3][1] = True
                    self.run_set()
                    return True

    def run_1(self, keep_distance_coordinat):
        if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.pole_box_arm_forward_pin.pin_value == True and \
                self.machine_obj.drill_box.Equepment_drill_box_digit_piont.pole_box_arm_backward_pin.pin_value == True:
                        if self.machine_obj.drill_box.hand_run(keep_distance_coordinat) == True:
                            if self.time_first == 0:
                                self.time_first = time.time()
                            if time.time() - self.time_first > 0.5:
                                return True
        else:
            self.run_pause_stop()

    def run_2(self, keep_distance_coordinat):
        if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.pole_box_arm_forward_pin.pin_value == True and \
                self.machine_obj.drill_box.Equepment_drill_box_digit_piont.pole_box_arm_backward_pin.pin_value == True:
            if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop(box_hand_arm_run_stop_time) == True:
                            return True
        else:
            self.run_pause_stop()
    def run_3(self, coordinate):

        if self.machine_obj.drill_box.hand_run(coordinate) == True:
            return True

    def run_pause_stop(self):
        if self.pause == False:
            self.pause = True
        if self.step.index(self.current_step) == 0:
            if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop() == True:
                if self.pause == False:
                    self.step[1][1] = False
                    return True
        if self.step.index(self.current_step) == 1:

                if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop() == True:
                    if self.pause == True:
                        self.step[1][1] = True
                        return True
        if self.step.index(self.current_step) == 2:
                if self.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop() == True:
                    if self.pause == True:
                        self.step[1][1] = False
                        self.step[2][1] = False
                        return True

