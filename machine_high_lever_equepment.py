import inspect
import sys
from abc import abstractmethod,ABCMeta
import time
import seting
import queue
import sensor
import uuid

load_data2 = seting.parameter_load_data
clockwise_que = queue.Queue(5)

push_pull_strenth_powerful = "powerful"

pole_in_middle_tiger_tooth = load_data2["pole_in_middle_tiger_tooth"]
# pole_in_middle_tiger_tooth_tiggerback = load_data2["pole_in_middle_tiger_tooth_tiggerback"]  # back 20 thread
# pole_in_middle_tiger_tooth_to_taile = load_data2["pole_in_middle_tiger_tooth_to_taile"]   ## can turn out pole taile the mother silk

try:
    pole_in_middle_tiger_tooth_to_taile_tofaward =  load_data2["pole_in_middle_tiger_tooth_to_taile_tofaward"]     #push pole, and push end  pole head in the middle tooth    not finished
except:
    pole_in_middle_tiger_tooth_to_taile_tofaward = 0    ## self.pole_in_middle_tiger_tooth_to_taile_tofaward has changged
# pole_pull_back_can_out_box_hand_to_grap = load_data2["pole_pull_back_can_out_box_hand_to_grap"]
# try:
#     pole_can_box_back = load_data2["pole_can_box_back"]
# except:
#     pole_can_box_back = 0
# beam_taile_5cm = load_data2["beam_taile_5cm"]
# main_beam_last_pole_up_down_expangd_hole = load_data2["main_beam_last_pole_up_down_expangd_hole"]
# beam_come_last = 4600
# beam_come_last_forward = 4650
# beam_come_last_backward = 4550




# delta_water_deepcheck_time  = 120
# MINI_ANGLE_SPEED = 70

# DRILL_BOX_UNSTOPPALE_COORDINATE = load_data2["point_unstop_beam"]
sys.path.append("D:\comunication_ui_")
import communication_setting
machine_id = communication_setting.bmachine_id

function_code6001 = communication_setting.function_code6001
function_code8001 = communication_setting.function_code8001
winip = communication_setting.window_ip
tiger_tooth_bite_wait_time = 7

def sendData_towin(target_ip, function_name, arges):
    """
    sendData format is uuid, machine_id, function_code, target_obj_code, target_ip, function_name, arges

    """

    function_code = function_code6001
    target_obj_code = function_code8001
    send_data = (
        str(uuid.uuid1()), machine_id, function_code, target_obj_code, target_ip, function_name, arges)
    return send_data

class ABC_high_level_equepment():
    __class__ = ABCMeta
    def __init__(self,obj_name, observasion, all_equepment_updated):
        self.obj_name = obj_name
        self.observasion = observasion


    @abstractmethod
    def register_low_equepment(self, low_equepment_obj):
# here use facade mode  creat equepment_obj
        pass

    @abstractmethod
    def equepment_statius(self):
        ## here rutur every low equepement statius class
        pass

    @abstractmethod
    def recev_order(self):
        # this is the interface of operator
        pass


class main_beam(ABC_high_level_equepment):

   def __init__(self, obj_name, observasion, all_equepment_updated, drill_box):
        super().__init__(obj_name, observasion, all_equepment_updated)
        # parameter_load_data = pandas.
        self.drill_box = drill_box

        self.current_pole_number_in_hole = load_data2["current_pole_number_in_hole"]
        self.current_pole_distance_not_in_hole = load_data2["current_pole_distance_not_in_hole"]

        self.beam_begin = load_data2["beam_head_coordinate"]
        self.beam_end = load_data2["beam_tail_coordinate"]
        self.MAX_PUSH_QUICK_PRESSURE = load_data2["MAX_PUSH_QUICK_PRESSURE"]
        self.MAX_PUSH_SLOW_PRESSURE = load_data2["MAX_PUSH_SLOW_PRESSURE"]
        self.MAX_DRILL_QUICK_PRESSURE = load_data2["MAX_DRILL_QUICK_PRESSURE"]
        self.MAX_DRILL_SLOW_PRESSURE = load_data2["MAX_DRILL_SLOW_PRESSURE"]
        self.MINI_ANGLE_SPEED = load_data2["MINI_ANGLE_SPEED"]
        self.beam_water_open = False
        self.beam_water_order = None
        self.beam_water_order = None
        self.pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate = load_data2["pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate"]   ##      20 father thread point
        self.pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number = load_data2["pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number"]   ##      20 father thread point

        self.pole_in_middle_tiger_tooth = load_data2["pole_in_middle_tiger_tooth"]

        self.pole_in_middle_tiger_tooth_coordinate = load_data2["pole_in_middle_tiger_tooth_coordinate"]               ## the pole begin to the tiggertooth.        changged ok
        self.pole_in_middle_tiger_tooth_cycle_number = load_data2["pole_in_middle_tiger_tooth_cycle_number"]               ## the pole begin to the tiggertooth.        changged ok    0209

        self.pole_in_middle_tiger_tooth_to_taile_tofaward = load_data2["pole_in_middle_tiger_tooth_to_taile_tofaward"]

        self.pole_in_middle_tiger_tooth_tiggerback = load_data2["pole_in_middle_tiger_tooth_tiggerback_coordinate"]   ###the pole all out the tigger tooth     # changed ok
        self.pole_in_middle_tiger_tooth_tiggerback_cycle_number = load_data2["pole_in_middle_tiger_tooth_tiggerback_cycle_number"]   ###the pole all out the tigger tooth     # changed ok



        self.pole_in_middle_tiger_tooth_to_taile = load_data2["pole_in_middle_tiger_tooth_to_taile"]   # can out mather thread     # changed ok

        self.fouoint_coordinate_map_tiger_rurth_pler_range = load_data2["fouoint_coordinate_map_tiger_rurth_pler_range"]
        self.pole_mather_thread_on_beam_can_counter_drill_out = load_data2["pole_mather_thread_on_beam_can_counter_drill_out"]   # attention this isn't finished in handhold

        self.beam_taile_5cm_coordinate = load_data2["beam_taile_5cm_coordinate"]     # changed ok
        self.beam_taile_5cm_cycle_number = load_data2["beam_taile_5cm_cycle_number"]        # changed ok


        self.pole_pull_back_can_out_box_hand_to_grap = load_data2["pole_pull_back_can_out_box_hand_to_grap"]            # changed ok
        self.main_beam_last_pole_up_down_expangd_hole = load_data2["main_beam_last_pole_up_down_expangd_hole"]             # changed ok
        self.man_can_get_out_pole_coordinate = load_data2["man_can_get_out_pole_coordinate"]

        self.man_give_pole_place = load_data2["man_give_pole_place"]
        self.man_give_pole_place_cycle_number = load_data2["man_give_pole_place_cycle_number"]


        # changed ok
        self.man_give_pole_place_back_last_point = load_data2["man_give_pole_place_back_last_point_coordinate"]
        self.man_give_pole_place_back_last_point_cycle_number = load_data2["man_give_pole_place_back_last_point_cycle_number"]
        # changed ok
        self.the_new_point_man_can_let_pole_out_beam_coordinate = load_data2["the_new_point_man_can_let_pole_out_beam_coordinate"]
        self.the_new_point_man_can_let_pole_out_beam_cycle_number = load_data2["the_new_point_man_can_let_pole_out_beam_cycle_number"]


        # changed ok
        self.main_beam_of_the_tigger_point_delta = load_data2["main_beam_of_the_tigger_point_delta"]     ###  must
        self.angle_0_corected_value = 0

        self.thread_tight_tight_level = load_data2["thread_tight_tight_level"]
        self.polethread_out_circle_number_intiger = load_data2["polethread_out_circle_number_intiger"]
        self.pole_taile_mother_thread_out_circle_numeber = load_data2["pole_taile_mother_thread_out_circle_numeber"]
        self.pole_taile_mother_thread_out_pressure = load_data2["pole_taile_mother_thread_out_pressure"]


        self.first_successtaile = load_data2["first_successtaile"]
        self.first_success_both = load_data2["first_success_both"]

        self.pole_recircle_times_into_hole_break_time = load_data2["pole_recircle_times_into_hole_break_time"]

        self.tiger_dirll_pole_pole_tight_max_pressure = load_data2["tiger_dirll_pole_pole_tight_max_pressure"]
        self.tiger_dirll_pole_pole_tight_max_pressure_level = load_data2["tiger_dirll_pole_pole_tight_max_pressure_level"]
        self.tiger_dirll_pole_pole_tight_push_max_pressure = load_data2["tiger_dirll_pole_pole_tight_push_max_pressure"]
        self.tiger_dirll_pole_pole_tight_push_max_pressure_level = load_data2["tiger_dirll_pole_pole_tight_push_max_pressure_level"]

        self.tigger_inner_drill_relax = False

        self.tiger_outer_rule_grap = load_data2["tiger_outer_rule_grap"]
        self.tiger_outer_rule_relax = load_data2["tiger_outer_rule_relax"]

        self.tiger_inner_rule_grap = load_data2["tiger_inner_rule_grap"]
        self.tiger_inner_rule_relax = load_data2["tiger_inner_rule_relax"]

        self.tiger_forward_move_max_coordinate = load_data2["tiger_forward_move_max_coordinate"]
        self.tiger_backward_move_max_coordinate = load_data2["tiger_backward_move_max_coordinate"]

        self.tiger_coordinate_beam_not_reach_beamself_slot = load_data2["tiger_coordinate_beam_not_reach_beamself_slot"]
        self.tiger_coordinate_beam_reached_beamself_slot = load_data2["tiger_coordinate_beam_reached_beamself_slot"]
        self.tiger_self_middle_zero_coordinate_ = load_data2["tiger_self_middle_zero_coordinate_"]
        self.tiger_self_ruler_coordinate_delta = load_data2["tiger_self_ruler_coordinate_delta"]

        self.no_load_move_parameter_contrl_distance = load_data2["no_load_move_parameter_contrl_distance"]
        self.no_load_move_start_level = load_data2["no_load_move_start_level"]
        self.no_load_move_end_level = load_data2["no_load_move_end_level"]
        self.no_load_move_to_coordinnate_point_max_pressure = load_data2["no_load_move_to_coordinnate_point_max_pressure"]
        self.dangger_no_load_move_to_coordinnate_point = False

        self.dangger_move_and_clockwise_slight = False

        self.tiger_touch_delta = load_data2["tiger_touch_delta"]

        self.beam_push_pull_in_tiger_step_distance = load_data2["beam_push_pull_in_tiger_step_distance"]



        self.Equepment_line_distance_measure_beam_taile_point_beam_solt_top = load_data2["Equepment_line_distance_measure_beam_taile_point_beam_solt_top"]

        self.first_point_characteristic_success_value = load_data2["first_point_characteristic_success_value"]


        self.pole_loose_need_mini_angle = load_data2["pole_loose_need_mini_angle"]

        self.tiger_dirll_pole_pole_loose_max_pressure = load_data2["tiger_dirll_pole_pole_loose_max_pressure"]
        self.pole_loose_need_mini_circle_drill_level = load_data2["pole_loose_need_mini_circle_drill_level"]


        self.delta_water_deepcheck_time = load_data2["delta_water_deepcheck_time"]
        self.beam_movement_speed_delta_time = load_data2["beam_movement_speed_delta_time"]
        self.beam_angle_speed_delta_time = load_data2["beam_angle_speed_delta_time"]
        self._pressure_torque_sameping_delta_time = load_data2["_pressure_torque_sameping_delta_time"]
        self.pressure_push_pull_sameping_delta_time = load_data2["pressure_push_pull_sameping_delta_time"]

        self.tiger_loose_time_ = load_data2["tiger_loose_time_"]
        self.tiger_tight_time_ = load_data2["tiger_tight_time_"]
        self.tiger_dirll_pole_and_poletight_max_pressure = load_data2["tiger_dirll_pole_and_poletight_max_pressure"]


        self.speed_contrl_function_distance = load_data2["speed_contrl_function_distance"]                                              # self.speed_contrl() function distance 25cm
        self.speed_contrl_function_speed_contral_rangge = load_data2["speed_contrl_function_speed_contral_rangge"]
        self.speed_contrl_function_delt_mini_speed = load_data2["speed_contrl_function_delt_mini_speed"]

        # self.speed_contrl() function distance 25cm
        # in this distance must lower speed

        self.beam_jog_move_move_start = False
        self.beam_jog_move_move_start_level = load_data2["beam_jog_move_move_start_level"]

        self.beam_jog_drill_start = False
        self.beam_jog_drill_start_level = load_data2["beam_jog_drill_start_level"]

        self.begin_drill = False

        self.first_point_coordinate = load_data2["first_point_coordinate"]
        self.first_point_coordinate_delta = load_data2["first_point_coordinate_delta"]
        self.first_point_coordinate_map_tiger_ruler_range = load_data2["first_point_coordinate_map_tiger_ruler_range"]
        self.first_point_characteristic_value = load_data2["first_point_characteristic_value"]


        self.second_point_coordinate = load_data2["second_point_coordinate"]     # pole male thread half in next pole in tiger
        self.second_point_coordinate_delta = load_data2["second_point_coordinate_delta"]   # pole male thread half in next pole in tiger
        self.second_point_coordinate_map_tiger_ruler_range = load_data2["second_point_coordinate_map_tiger_ruler_range"]     # pole male thread half in next pole in tiger

        self.taile_thread_is_ok_point_coordinate = load_data2["taile_thread_is_ok_point_coordinate"]
        self.taile_thread_is_ok_point_coordinate_delat = load_data2["taile_thread_is_ok_point_coordinate_delat"]
        self.taile_thread_is_ok_point_coordinate_map_tiger_ruler_range = load_data2["taile_thread_is_ok_point_coordinate_map_tiger_ruler_range"]





        self.third_point_coordinate = load_data2["third_point_coordinate"]
        self.third_point_coordinate_delta = load_data2["third_point_coordinate_delta"]
        self.third_point_coordinate_map_tiger_ruler_range = load_data2["third_point_coordinate_map_tiger_ruler_range"]

        self.fourth_point_coordinate = load_data2["fourth_point_coordinate"]
        self.fourth_point_coordinate_delta = load_data2["fourth_point_coordinate_delta"]
        self.fourth_point_coordinate_map_tiger_ruler_range = load_data2["fourth_point_coordinate_map_tiger_ruler_range"]

        self.delta_contrast_beam_ruler_tiger_ruler = load_data2["delta_contrast_beam_ruler_tiger_ruler"]





        self.Equepment_tigger_tooch_f = sensor.push_pull_rocker_arm("Equepment_tigger_tooch_f", observasion, all_equepment_updated)
        self.Equepment_tigger_tooch_f.regester_equepment_pin_obj()
        self.Equepment_tigger_tooch_b = sensor.push_pull_rocker_arm("Equepment_tigger_tooch_b", observasion, all_equepment_updated)
        self.Equepment_tigger_tooch_b.regester_equepment_pin_obj()
        self.Equepment_tigger_drill = sensor.push_pull_rocker_arm("Equepment_tigger_drill", observasion, all_equepment_updated)
        self.Equepment_tigger_drill.regester_equepment_pin_obj()
        self.Equepment_pole_push_pull = sensor.push_pull_rocker_arm("Equepment_pole_push_pull", observasion, all_equepment_updated)
        self.Equepment_pole_push_pull.regester_equepment_pin_obj()
        self.Equepment_pole_dirll = sensor.push_pull_rocker_arm("Equepment_pole_dirll", observasion, all_equepment_updated)
        self.Equepment_pole_dirll.regester_equepment_pin_obj()
        self.Equepment_warter_deep_measure = sensor.water_deep("Equepment_warter_deep_measure", observasion, all_equepment_updated)
        self.Equepment_warter_deep_measure.regester_equepment_pin_obj()
        self.Equepment_line_distance_measure_4m_beam = sensor.line_distance("Equepment_line_distance_measure_4m_beam", observasion, all_equepment_updated)
        self.Equepment_line_distance_measure_4m_beam.regester_equepment_pin_obj()
        self.Equepment_line_distance_measure_beam_taile = sensor.line_distance("Equepment_line_distance_measure_beam_taile", observasion, all_equepment_updated)
        self.Equepment_line_distance_measure_beam_taile.regester_equepment_pin_obj()
        self.Equepment_line_distance_measure_beam_head = sensor.line_distance("Equepment_line_distance_measure_beam_head", observasion, all_equepment_updated)
        self.Equepment_line_distance_measure_beam_head.regester_equepment_pin_obj()
        self.Equepment_line_distance_measure_dirll_box_updown = sensor.line_distance("Equepment_line_distance_measure_dirll_box_updown", observasion, all_equepment_updated)
        self.Equepment_line_distance_measure_dirll_box_updown.regester_equepment_pin_obj()
        self.Equepment_pressure_warter = sensor.pressure_measure("Equepment_pressure_warter", observasion, all_equepment_updated)
        self.Equepment_pressure_warter.regester_equepment_pin_obj()
        self.Equepment_pressure_push_pull = sensor.pressure_measure("Equepment_pressure_push_pull", observasion, all_equepment_updated)
        self.Equepment_pressure_push_pull.regester_equepment_pin_obj()
        self.Equepment_pressure_torque = sensor.pressure_measure("Equepment_pressure_torque", observasion, all_equepment_updated)
        self.Equepment_pressure_torque.regester_equepment_pin_obj()
        self.Equepment_angle_torque_to_pole = sensor.angle_torque("Equepment_angle_torque_to_pole", observasion, all_equepment_updated)
        self.Equepment_angle_torque_to_pole.regester_equepment_pin_obj()
        self.Equepment_main_beam_obj = sensor.main_beam_position("Equepment_main_beam_obj", observasion, all_equepment_updated)
        self.Equepment_main_beam_obj.regester_equepment_pin_obj()



        self.check_pressure_torque_and_pullpush = False
        self.move_last_coordinate = 0
        self.order_begin_coordinate = 0
        self.order_target_coordinate = 0

        self.beam_speed_first_coordinate = None
        self.beam_speed_first_coordinate_time_ = None
        self.beam_last_speed = None

        self.beam_first_angle = None
        self.beam_first_angle_time_ = None
        self.beam_last_angle_speed = None

        self.beam_last_torque = None
        self.beam_last_torque_time_ = None
        self.beam_last_pull_push_pressure = None
        self.beam_last_pull_push_pressure_time_ = None

        self.beam_move_forward_begin_coordinate =  None



        self.dangger_head_coordinate = 16    #middle is 10  10+6
        self.dangger_taile_coordinate = 10

        self.beam_move_forward_step2_tiger_keeptime = None

        self.lastbeam_headcoordinate = None

        self.lastbegin_forward_test = None


        self.flaaggg = False
        self.flaaggg2 = False

        self.beam_move_forward_step2_flag1_ = False
        self.beam_move_forward_step2_flag2_ = False


        self.beam_move_forward_length_begin = None

        self.water_deep_number  = None
        self.water_deep_number_first_time =   None

        self.last_push_level = None
        self.current_push_level = None
        self.last_rotate_level = None
        self.current_rotate_level = None

        self.push_level0_flag = False
        self.push_level1_flag = False
        self.push_level2_flag = False

        self.clockwise_distance_begin = None

        self.direction_forward_begin = None


        self.out_tooth_bite_statue = False
        self.inner_tooth_bite_statue = False
        self.out_tooth_bite_statue_time = None
        self.outtiger_tooth_push_flag = False
        self.outtiger_tooth_push_back = False
        self.biting_tight = None
        self.still_bite_tight = None

        self.tiger_out_innertooth_relax_flag1 = False
        self.tiger_out_innertooth_relax_flag2 = False
        self.out_tooth_bite_statue_time_relax = None
        self.biting = None
        self.still_bite = None




        self.tiger_loose_pole_statues = "loose"    # or "tight"
        self.tiger_loose_pole_flag1 = False


        self.counterclockwise_time = None
        self.counter_clock_check_first_head = None
        self.counter_clock_check_first_taile = None

        self.bengin_time_rotate = None

        self.move_begin_time = None

        self.flag_auto_rotate1 = False
        self.flag_auto_rotate2 = False

        self.flag_auto_rotate_pull1 = False
        self.flag_auto_rotate_pull2 = False
        self.current_pull_level = None

        self.pull_max_level = 6

        self.begin_drill = True    # in auto_push function

        self.move_and_clockwise_flag = False
        self.clockwise_rotate_same_place_flag = False
        self.counter_clockwise_rotate_same_place_flag = False

        self.move_flag = False



        self.clockwise_get_flag = False
        self.clockwise_get_flag2 = False

        self.rotate_speed_control_push_level = 1

        self.remenber_coordinate = None
        self.remenber_coordinate_pull = None

        self.auto_rotate_pull_flag = False
        self.auto_rotate_pull_flag2 = False

        self.last_speed_control_function_speed = None

        self.move_stop_flag1 = False
        self.move_stop_flag2 = False

   def beam_angle_speed_calclude(self):
       if self.beam_first_angle == None or self.beam_first_angle_time_ == None:
           current_angle = self.Equepment_angle_torque_to_pole.angle
           current_angle_time_ = self.Equepment_angle_torque_to_pole.time_
           self.beam_first_angle = current_angle
           self.beam_first_angle_time_ = current_angle_time_
       current_angle_time_ = self.Equepment_angle_torque_to_pole.time_
       delta_time = current_angle_time_ - self.beam_first_angle_time_
       if delta_time > self.beam_angle_speed_delta_time:
           current_angle = self.Equepment_angle_torque_to_pole.angle
           delta_angle = self.calclude_angle_delt(self.beam_first_angle,current_angle)
           if self.beam_last_angle_speed == None:
               self.beam_last_angle_speed = 0
           else:
               current_angle_speed = delta_angle/delta_time
               self.beam_first_angle = current_angle
               self.beam_first_angle_time_ = current_angle_time_
       return  current_angle_speed

   def beam_speed_calclude(self):

       if self.beam_speed_first_coordinate == None or self.beam_speed_first_coordinate_time_ == None:
           current_coordinate = self.Equepment_line_distance_measure_4m_beam.coordinate
           current_coordinate_time_ = self.Equepment_line_distance_measure_4m_beam.time_
           self.beam_speed_first_coordinate = current_coordinate
           self.beam_speed_first_coordinate_time_ = current_coordinate_time_
           return 0
       current_coordinate_time_ = self.Equepment_line_distance_measure_4m_beam.time_
       self.delta_time = current_coordinate_time_ - self.beam_speed_first_coordinate_time_
       if self.delta_time > self.beam_movement_speed_delta_time:
           current_coordinate = self.Equepment_line_distance_measure_4m_beam.coordinate
           delta_s = current_coordinate - self.beam_speed_first_coordinate
           speed = delta_s/self.delta_time
           self.beam_speed_first_coordinate_time_ = current_coordinate_time_
           self.beam_speed_first_coordinate = current_coordinate
           self.delta_time = 0

       return speed

   def beam_calclude_pressure_torque(self):

       if self.beam_last_torque == None or self.beam_last_torque_time_ == None:
           current_torque = self.Equepment_pressure_torque.pressure
           current_torque_time_ = self.Equepment_pressure_torque.time_
           self.beam_last_torque = current_torque
           self.beam_last_torque_time_ = current_torque_time_
       else:
           current_torque_time_ = self.Equepment_pressure_torque.time_
           delta_time = current_torque_time_ - self.beam_last_torque_time_
           if delta_time > self._pressure_torque_sameping_delta_time:
               current_torque = self.Equepment_pressure_torque.pressure
               self.beam_last_torque_time_ = current_torque_time_
       return current_torque

   def  beam_calclude_pull_push_pressure_pressure(self):      # pressure sampling

       if self.beam_last_pull_push_pressure == None or self.beam_last_pull_push_pressure_time_ == None:
           current_pull_push_pressure = self.Equepment_pressure_push_pull.pressure
           current_pull_push_pressure_time_ = self.Equepment_pressure_push_pull.time_
           self.beam_last_pull_push_pressure = current_pull_push_pressure
           self.beam_last_pull_push_pressure_time_ = current_pull_push_pressure_time_
       else:
           current_pull_push_pressure_time_ = self.Equepment_pressure_push_pull.time_
           delta_time = current_pull_push_pressure_time_ - self.beam_last_pull_push_pressure_time_
           if delta_time > self.pressure_push_pull_sameping_delta_time:
               current_pull_push_pressure = self.Equepment_pressure_push_pull.pressure

       return   current_pull_push_pressure

   def calclude_soil_quality_value(self,torque,angle_sped,pull_push,speed):
       if (torque == 0) or (pull_push == 0):
           return None
       quality = (torque*pull_push/(0.1+abs(speed)*abs(angle_sped)))
       return quality

   def beam_move_forward(self,distangce=None,beam_coordinate=None,rotate_deriction=None,operation="auto",push_max_level=6,rotate ="auto"):
        self.rotate = rotate
        self.push_max_level = push_max_level
        self.operation = operation
        self.rotate_deriction = rotate_deriction

        # beam_current_speed = self.beam_speed_calclude(0.1)
        # beam_current_angle_speed_ = self.beam_angle_speed_calclude(0.1)
        # beam_current_pullpush_pressure = self.beam_calclude_pull_push_pressure_pressure(0.1)
        # beam_current_torque = self.beam_calclude_pressure_torque(0.1)

        self.beam_move_forward_step1 = False  # check BOX and besuue is untstop
        self.beam_move_forward_step2 = False # statistatics the temporary_long. in_hole = number*3 + temporary_long
        # and step 2 must check the tiger tooth isnt open  useing the beam head ruler test .give_water,temple_stop
        self.beam_move_forward_step3 = False  # forward_contronl and statistatics the pole the same pressure distance
        # if more 50cm send warning and stop and sennd the digit
        self.beam_move_forward_step4 = False  # forward over
        if (self.beam_move_forward_step1, self.beam_move_forward_step2, self.beam_move_forward_step3) == ( False,False,False):
               self.beam_move_forward_step1_()
        if (self.beam_move_forward_step2, self.beam_move_forward_step2, self.beam_move_forward_step3) == ( True,False, False):
               self.beam_move_forward_step2_()
        if (self.beam_move_forward_step1, self.beam_move_forward_step2, self.beam_move_forward_step3) == ( True,True, False):
               self.beam_move_forward_step3_()
        self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(True)
        self.beam_water_open = True
        return True

   def  beam_move_forward_step1_(self):
       if abs(self.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate -self.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate ) < self.drill_box.Equepment_drill_box_digit_piont.pole_point_delta:
           self.beam_move_forward_step1 = True
       else:
           self.drill_box.hand_run(self.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate)
           if abs(self.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate -self.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate ) < self.drill_box.Equepment_drill_box_digit_piont.pole_point_delta:
               self.beam_move_forward_step1 = True

   def  beam_move_forward_step2_(self):     ##check water_deep changge in the step3

       if self.beam_move_forward_step2_flag1() == True:
           self.beam_move_forward_step2 = True



   def beam_move_forward_step2_flag1(self): # (self.beam_move_forward_step2_flag1,   self.beam_move_forward_step2_flag2)  = (0,0)
      if self.Equepment_warter_deep_measure.water_deep_number < self.Equepment_warter_deep_measure.warter_deep_safe :
          self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(False)
          self.beam_water_open = False
          self.move_stop()
      if  self.Equepment_warter_deep_measure.water_deep_number > self.Equepment_warter_deep_measure.warter_deep_safe :
          if self.beam_water_order == None:
              if self.beam_water_open == False:
                    self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(True)
                    self.beam_water_open = True  # water is the first condiction
          else:
              if self.beam_water_order == True:
                  self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(True)
                  self.beam_water_open = True
              if self.beam_water_order == False:
                  self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(False)
                  self.beam_water_open = False

          self.Equepment_pole_push_pull.parse_pull_push_level()
          self.begin_forward_test = self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[self.thread_tight_tight_level])
          if self.begin_forward_test == True:
                return True
      else:
          print("warning,here next expangd other function,no water is need ,other stop machine and will be punish  if"
                "water not b ")


   def  beam_move_forward_step3_(self):
        if self.Equepment_line_distance_measure_4m_beam.coordinate ==  self.pole_in_middle_tiger_tooth_to_taile_tofaward:
            self.beam_move_forward_step3 = True
            self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(False)
            self.beam_water_open = False  #
            return True
        if self.beam_move_forward_length_begin == None:
            self.beam_move_forward_length_begin =  self.Equepment_line_distance_measure_4m_beam.coordinate
        self.tamprory_length = abs(self.Equepment_line_distance_measure_4m_beam.coordinate - self.beam_move_forward_length_begin)

        if self.water_deep_number == None:
            self.water_deep_number = self.Equepment_warter_deep_measure.water_deep_number
            self.water_deep_number_first_time = self.Equepment_warter_deep_measure.time_
        curreent_water_deep_number_time = self.Equepment_warter_deep_measure.time_
        if curreent_water_deep_number_time - self.water_deep_number_first_time > self.delta_water_deepcheck_time:
            curreent_deep = self.Equepment_warter_deep_measure.water_deep_number
            if curreent_deep < self.water_deep_number:
                print("ok,water is normal out")
            if curreent_deep <  self.Equepment_warter_deep_measure.warter_deep_safe:    #### lable
                self.move_stop()
                print("danger,you must prepare water")
        if self.beam_last_speed == None:
            self.beam_last_speed = self.beam_speed_calclude()
        beam_current_speed = self.beam_speed_calclude()
        if self.beam_last_angle_speed == None:
            self.beam_last_angle_speed = self.beam_angle_speed_calclude()
        beam_current_angle_speed_ = self.beam_angle_speed_calclude()
        if self.beam_last_pull_push_pressure == None:
            self.beam_last_pull_push_pressure = self.beam_calclude_pull_push_pressure_pressure()
        beam_current_pullpush_pressure = self.beam_calclude_pull_push_pressure_pressure()
        if self.beam_last_torque == None:
            self.beam_last_torque = self.beam_calclude_pressure_torque()
        beam_current_torque = self.beam_calclude_pressure_torque()
        if self.rotate == "auto" and self.rotate_deriction != None:
                self.auto_rotate_push(beam_current_torque,beam_current_pullpush_pressure,beam_current_speed)
        if self.rotate_deriction != None and self.rotate == "auto":
            self. clockwise_get(clock=None,push_level = 3 )
            self.direction_forward(ditance = 300)


   def auto_rotate_push(self,beam_current_rotate_speek,beam_current_pullpush_pressure,beam_current_speed,target,derection = "forward"):
       #  this function is used to pushed with a clock derection
            self.Equepment_pole_dirll.parse_pull_push_level()
            self.Equepment_pole_push_pull.parse_pull_push_level()
                  # self.flag_auto_rotate = (self.flag_auto_rotate1,self.flag_auto_rotate2,self.flag_auto_rotate3,self.flag_auto_rotate4)

            if abs(self.Equepment_line_distance_measure_4m_beam.coordinate - self.pole_in_middle_tiger_tooth_to_taile_tofaward) < self.main_beam_of_the_tigger_point_delta:
               if self.move_stop(warterclose=True) == True:
                   return True
            else:
               if self.beam_water_open == False:
                   self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(True)
                   self.beam_water_open = True
               if self.begin_drill != True:
                    self.Equepment_pole_dirll.operation_target_coordinate(self.Equepment_pole_dirll.PUSH_LEVEL[6])
                    self.begin_drill = True
            if abs(self.Equepment_line_distance_measure_4m_beam.coordinate -
                  self.pole_in_middle_tiger_tooth_to_taile_tofaward) < 250:
                self.speed_contrl(self.pole_in_middle_tiger_tooth_to_taile_tofaward, contrl_distance=250)

            if abs(self.Equepment_line_distance_measure_4m_beam.coordinate - self.pole_in_middle_tiger_tooth_to_taile_tofaward ) > 250:
                if self.current_push_level == None:
                    self.current_push_level = 2
                self.begin_this_pole = self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[self.current_push_level])
                if  self.begin_this_pole == True:
                    if beam_current_speed - self.beam_last_speed > 5 and beam_current_rotate_speek - self.MINI_ANGLE_SPEED > 100:
                               self.beam_last_speed = self.current_push_level
                               if beam_current_pullpush_pressure - self.MAX_PUSH_QUICK_PRESSURE < -3:
                                    self.current_push_level = self.current_push_level + 1
                               elif 1 > (beam_current_pullpush_pressure - self.MAX_PUSH_QUICK_PRESSURE) - 1:
                                   self.current_push_level = self.current_push_level
                               else:
                                   self.current_push_level = self.current_push_level - 1
                               if self.current_push_level > self.push_max_level:
                                   self.current_push_level = self.push_max_level
                    if beam_current_rotate_speek < self.MINI_ANGLE_SPEED:
                           if self. remenber_coordinate == None:
                                self.remenber_coordinate = self.Equepment_line_distance_measure_4m_beam.coordinate
                           stop = self.main_beam_move_stop( self.remenber_coordinate-100,pull_level=2)           ## idiot for this code
                           if stop == True:
                               self.speed_contrl(self.pole_in_middle_tiger_tooth_to_taile_tofaward)

   def auto_rotate_pull(self):
    # this function has used in operation_interface
            if abs(self.Equepment_line_distance_measure_4m_beam.coordinate -
                    self.pole_in_middle_tiger_tooth_to_taile_tofaward) < -self.main_beam_of_the_tigger_point_delta:
                if self.move_stop(warterclose=True) is True:
                    self.Equepment_pole_dirll.operation(
                        "keep", self.Equepment_pole_push_pull.gear_list[12])
                    return True
            else:
                if self.beam_water_open is False:
                    self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(True)
                    self.beam_water_open = True
            if self.speed_contrl(self.pole_in_middle_tiger_tooth_to_taile_tofaward, contrl_distance=250) is True:
                    self.flag_auto_rotate_pull1 = True
            self.Equepment_pole_dirll.operation(
                "forward", self.Equepment_pole_push_pull.gear_list[12])

   def clockwise_get(self, clock=1, push_level=3):
       self.Equepment_pole_dirll.parse_pull_push_level()
       if (self.clockwise_get_flag,self.clockwise_get_flag2) == (False,False):
               if self.calclude_angle_delt(self.Equepment_angle_torque_to_pole.angle,clock*30) >15 or self.calclude_angle_delt(self.Equepment_angle_torque_to_pole.angle,clock*30,derection="counter_clockwise") > 15:
                   self.begin_this_pole = self.Equepment_pole_dirll.operation("forward", self.Equepment_pole_dirll.PUSH_LEVEL[push_level])
                   self.clockwise_get_flag = True
       if (self.clockwise_get_flag,self.clockwise_get_flag2) == (True,False):
           if self.calclude_angle_delt(self.Equepment_angle_torque_to_pole.angle,clock*30) < 15 or self.calclude_angle_delt(self.Equepment_angle_torque_to_pole.angle,clock*30,derection="counter_clockwise") < 15 :
               self.Equepment_pole_dirll.operation("keep", self.Equepment_pole_dirll.PUSH_LEVEL[push_level])
               self.clockwise_get_flag2 = True
       if (self.clockwise_get_flag, self.clockwise_get_flag2) == (True, True):
           if self.calclude_angle_delt(self.Equepment_angle_torque_to_pole.angle, clock * 30) < 15 or self.calclude_angle_delt(self.Equepment_angle_torque_to_pole.angle, clock * 30, derection="counter_clockwise") < 15:
               self.clockwise_get_flag = False
               self.clockwise_get_flag2 = False
               return True
           else:
               self.clockwise_get_flag = False
               self.clockwise_get_flag2 = False
   def rotate_speed_control(self,angle_speed,on=False):
       self.Equepment_pole_dirll.parse_pull_push_level()
       if on ==True:
           current_speed = self.beam_angle_speed_calclude()
           if current_speed - angle_speed >30:
               self.rotate_speed_control_push_level = self.rotate_speed_control_push_level + 1
           if  current_speed - angle_speed <30 :
               self.rotate_speed_control_push_level = self.rotate_speed_control_push_level + 1
           self.Equepment_pole_dirll.operation("forward", self.Equepment_pole_dirll.PUSH_LEVEL[self.rotate_speed_control_push_level])
       elif on == False:
           if self.Equepment_pole_dirll.operation("keep", self.Equepment_pole_dirll.PUSH_LEVEL[self.rotate_speed_control_push_level]) == True:
               return True

   def calclude_angle_delt(self,anglea_begin,angleb_end,derection="clockwise"):
       if derection == "clockwise":
           if angleb_end >= anglea_begin:
               delt = angleb_end -anglea_begin
           if angleb_end < anglea_begin:
               delt = 360 - anglea_begin + angleb_end
       if derection == "counter_clockwise":
           if anglea_begin > angleb_end:
               delt = angleb_end - anglea_begin
           if   anglea_begin < angleb_end:
               delt = 360 - angleb_end + anglea_begin
           return delt
   def get_current_angle(self):   # correcting _zero
       angle = self.calclude_angle_delt(self.angle_0_corected_value, self.Equepment_angle_torque_to_pole.angle)//360
       return angle


   def clockwise_rotate_same_place(self,level =3 ,time_delta = 0.3):
       self.Equepment_pole_dirll.parse_pull_push_level()

       if self.clockwise_rotate_same_place_flag == False:
            if self.Equepment_pole_dirll.operation("forward", self.Equepment_pole_dirll.PUSH_LEVEL[level]) == True:
                self.clockwise_rotate_same_place_flag = True
       if self.clockwise_rotate_same_place_flag == True:
           if self.bengin_time_rotate == None:
               self.bengin_time_rotate = time.time()
           if time.time() - self.bengin_time_rotate > time_delta:
               if self.Equepment_pole_dirll.operation("forward", self.Equepment_pole_dirll.PUSH_LEVEL[level]) == True:
                    self.clockwise_rotate_same_place_flag = False
                    self.bengin_time_rotate = None
                    return True

   def counter_clockwise_rotate_same_place(self, level=3, time_delta=0.3):
       self.Equepment_pole_dirll.parse_pull_push_level()

       if self.counter_clockwise_rotate_same_place_flag == False:
           if self.Equepment_pole_dirll.operation("backward", self.Equepment_pole_dirll.PULL_LEVEL[level]) == True:
               self.clockwise_rotate_same_place_flag = True
       if self.counter_clockwise_rotate_same_place_flag == True:
           if self.bengin_time_rotate == None:
               self.bengin_time_rotate = time.time()
           if time.time() - self.bengin_time_rotate > time_delta:
               if self.Equepment_pole_dirll.operation("backward", self.Equepment_pole_dirll.PULL_LEVEL[level]) == True:
                   self.counter_clockwise_rotate_same_place_flag = False
                   self.bengin_time_rotate = None
                   return True

   def  direction_forward(self,ditance = 300):
       # this is the very important function . whenever used it to instead other .

        self.Equepment_pole_push_pull.parse_pull_push_level()
        if abs(self.Equepment_line_distance_measure_4m_beam.coordinate - self.pole_in_middle_tiger_tooth_to_taile_tofaward) < 15:
           self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(False)
           self.beam_water_open = False
           return False

        if self.direction_forward_begin is None:
            self.direction_forward_begin = self.Equepment_line_distance_measure_4m_beam.coordinate
        if abs(self.Equepment_line_distance_measure_4m_beam.coordinate - self.direction_forward_begin - ditance)  < 15:
           if self.Equepment_pole_push_pull.operation("keep", self.Equepment_pole_push_pull.PUSH_LEVEL[self.current_push_level]) == True:
                self.direction_forward_begin = None
                return True

        self.begin_this_pole = self.Equepment_pole_push_pull.operation("forward", self.Equepment_pole_push_pull.PUSH_LEVEL[self.current_push_level])
        if self.begin_this_pole is True:
            if self.Equepment_pressure_push_pull.pressure < self.MAX_PUSH_QUICK_PRESSURE:
                self.beam_last_speed = self.current_push_level
                self.current_push_level = self.current_push_level + 1
                if self.current_push_level > self.push_max_level:
                       self.current_push_level = self.push_max_level
            else:
               self.beam_last_speed = self.current_push_level
               self.current_push_level = self.current_push_level - 1

   def speed_contrl(self, target_coordinate, contrl_distance=250, current_push_level=2, mini_speed=35):
        # target_will reach  speed must control in a low range
        # this function usual in the pole load pull back wo push out.
        if self.Equepment_line_distance_measure_4m_beam.coordinate > target_coordinate:
            direction = "backward"
        else:
            direction = "forward"

        if self.current_push_level == None:
            if direction == "forward":
                self.current_push_level = 6 - current_push_level
            if direction == "backward":
                self.current_push_level = current_push_level - 6
        delt = self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate
        if delt < self.main_beam_of_the_tigger_point_delta:
            self.move_stop(warterclose=True)
            self.current_push_level = None
            return True
        current_speed = self.beam_speed_calclude()
        if direction == "forward":
            if self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate < -contrl_distance:
                    if self.Equepment_pressure_push_pull.pressure > self.MAX_PUSH_QUICK_PRESSURE:
                        gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull.coordinate)
                        if gear < self.current_push_level:
                            self.current_push_level = self.current_push_level
                        elif gear >= self.current_push_level:
                            self.current_push_level = gear + 1
                    ## follower is keep the mini speed
                    else:
                        if current_speed - mini_speed > self.speed_contrl_function_speed_contral_rangge:
                            # mini is a positive number
                                gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                                if gear < self.current_push_level:
                                    self.current_push_level = self.current_push_level
                                elif gear >= self.current_push_level:
                                    self.current_push_level = gear + 1
                        else:
                            gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                            if gear < self.current_push_level:
                                self.current_push_level = gear - 1
                            elif gear > self.current_push_level:
                                self.current_push_level = self.current_push_level
                            elif gear == self.current_push_level:
                                self.current_push_level = self.current_push_level - 1
           # follower is keep max speed
            else:
                if self.Equepment_pressure_push_pull.pressure > self.MAX_PUSH_QUICK_PRESSURE:
                    gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                    if gear < self.current_push_level:
                        self.current_push_level = self.current_push_level
                    elif gear >= self.current_push_level:
                        self.current_push_level = gear + 1
                else:
                    if self.last_speed_control_function_speed == None:
                        self.last_speed_control_function_speed = current_speed
                    if current_speed >= self.last_speed_control_function_speed:
                        gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                        if gear < self.current_push_level:
                            self.current_push_level = gear - 1
                        elif gear > self.current_push_level:
                            self.current_push_level = self.current_push_level
                        elif gear == self.current_push_level:
                            self.current_push_level = self.current_push_level - 1
                    else:
                        gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                        if gear < self.current_push_level:
                            self.current_push_level = self.current_push_level
                        elif gear >= self.current_push_level:
                            self.current_push_level = gear + 1
            self.Equepment_pole_push_pull.operation_target_coordinate(
                self.Equepment_pole_push_pull.gear_list[self.current_push_level])
        if (direction == "backward") or (
                self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate > contrl_distance):
            if self.last_speed_control_function_speed is None:
                self.last_speed_control_function_speed = current_speed
            if current_speed >= self.last_speed_control_function_speed:
                # it's means  speed is lower  must turn gear_list large
                gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                if gear < self.current_push_level:
                    self.current_push_level = self.current_push_level
                elif gear >= self.current_push_level:
                    self.current_push_level = gear + 1
            # follower is means the speed is too large turn it lower
            else:
                gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                if gear < self.current_push_level:
                    self.current_push_level = gear - 1
                elif gear > self.current_push_level:
                    self.current_push_level = self.current_push_level
                elif gear == self.current_push_level:
                    self.current_push_level = self.current_push_level - 1
        else:
            if abs(current_speed + mini_speed) < abs(self.speed_contrl_function_delt_mini_speed) :       # master set it
                self.current_push_level = self.current_push_level
            elif current_speed < -abs(mini_speed -self.speed_contrl_function_delt_mini_speed):
                gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                if gear < self.current_push_level:
                    self.current_push_level = gear - 1
                elif gear > self.current_push_level:
                    self.current_push_level = self.current_push_level
                elif gear == self.current_push_level:
                    self.current_push_level = self.current_push_level - 1
            elif current_speed > -abs(mini_speed -self.speed_contrl_function_delt_mini_speed):
                gear = self.current_gear_of_push_pull_rocker(self.Equepment_pole_push_pull)
                if gear < self.current_push_level:
                    self.current_push_level = self.current_push_level
                elif gear >= self.current_push_level:
                    self.current_push_level = gear + 1

        self.Equepment_pole_push_pull.operation_target_coordinate(
                      self.Equepment_pole_push_pull.gear_list[self.current_push_level])

   def current_gear_of_push_pull_rocker(self, messure_equepment_obj):
        gear_value = messure_equepment_obj.coordinate
        gear_list = [
                     messure_equepment_obj.PUSH_LEVEL[6],
                     messure_equepment_obj.PUSH_LEVEL[5],
                     messure_equepment_obj.PUSH_LEVEL[4],
                     messure_equepment_obj.PUSH_LEVEL[3],
                     messure_equepment_obj.PUSH_LEVEL[2],
                     messure_equepment_obj.PUSH_LEVEL[1],
                     messure_equepment_obj.PUSH_LEVEL[0],
                     messure_equepment_obj.PULL_LEVEL[1],
                     messure_equepment_obj.PULL_LEVEL[2],
                     messure_equepment_obj.PULL_LEVEL[3],
                     messure_equepment_obj.PULL_LEVEL[4],
                     messure_equepment_obj.PULL_LEVEL[5],
                     messure_equepment_obj.PULL_LEVEL[6],
                     ]
        new_list = [*map(lambda x:abs(x-gear_value), gear_list)]
        gear_number = new_list.index(min(new_list))
        return gear_number

   def main_beam_move_stop(self, target_coordinate):
       delt = self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate
       if delt <self.main_beam_of_the_tigger_point_delta:
           self.move_stop(warterclose=False)
           return True
       if delt > 1500 :
           if delt > 0:
               self.speed_contrl(target_coordinate, contrl_distance=0, mini_speed=120)
           else:
               self.speed_contrl(target_coordinate, contrl_distance=0,  mini_speed=120)
       if 1500 > delt>800 :
           if delt > 0:
               self.speed_contrl(target_coordinate, contrl_distance=0,  mini_speed=80)
           else:
               self.speed_contrl(target_coordinate, contrl_distance=0,  mini_speed=80)
       if 800 > delt> 200 :
           if delt > 0:
               self.speed_contrl(target_coordinate, contrl_distance=0,  mini_speed=50)
           else:
               self.speed_contrl(target_coordinate, contrl_distance=0,  mini_speed=50)
       if  200 > delt> 15 :
           if delt > 0:
               self.speed_contrl(target_coordinate, contrl_distance=0)
           else:
               self.speed_contrl(target_coordinate, contrl_distance=0)

   def counterclockwise(self, delt_time_=None, on=None, pulllevel=4):
       if  delt_time_!=None:
           if  self.counterclockwise_time == None:
                    self.counterclockwise_time = time.time()

           if time.time() - self.counterclockwise_time < delt_time_:
              self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PULL_LEVEL[pulllevel])

           else:
               keep_e = self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PUSH_LEVEL[0])
               if keep_e == True:
                   self.counterclockwise_time = None
                   return True
       else:
           if on is True:
                keep_o = self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PULL_LEVEL[pulllevel])
                if keep_o == True:
                    self.counterclockwise_time = None
                    return True
           if on is False:
               keep_f = self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PUSH_LEVEL[0])
               if keep_f == True:
                   self.counterclockwise_time = None
                   return True


   def counter_clock_check(self):

        current_headcoordinate = self.Equepment_line_distance_measure_beam_head.coordinate
        current_tailcoordinate = self.Equepment_line_distance_measure_beam_taile.coordinate
        if abs(current_headcoordinate - self.counter_clock_check_first_head) + abs(current_tailcoordinate - self.counter_clock_check_first_taile) > 2:
            self.counter_clock_check_first_head = None
            self.counter_clock_check_first_taile = None
            return True
        else:
                self.counter_clock_check_first_head = None
                self.counter_clock_check_first_taile = None
                return False

   def move_(self, direction="forward", time_delta=0.3, pull_level=2):
        if direction == "forward":

            if self.move_flag is False:
                if self.Equepment_pole_push_pull.operation_target_coordinate(
                        self.Equepment_pole_push_pull.PUSH_LEVEL[pull_level]) is True:
                    self.move_flag = True
            if self.move_flag is True:
                if self.Equepment_pole_push_pull.operation_target_coordinate(
                        self.Equepment_pole_push_pull.PUSH_LEVEL[0]) is True:
                    self.move_flag = False
                    return True
        else:
            if self.move_flag is False:
                if self.Equepment_pole_push_pull.operation_target_coordinate(
                        self.Equepment_pole_push_pull.PULL_LEVEL[pull_level]) is True:
                    self.move_flag = True
            if self.move_flag is True:
                    if time.time() - self.move_begin_time > time_delta:
                        if self.Equepment_pole_push_pull.operation_target_coordinate(
                                self.Equepment_pole_push_pull.PUSH_LEVEL[0]) is True:
                            self.move_begin_time = None
                            self.move_flag = False
                            return True
   def beam_jog_move(self):
       if  self.beam_jog_move_move_start == True:
          self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[self.beam_jog_move_move_start_level])
       else:
           self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0])

   def no_load_move_to_coordinnate_point(self, target_coordinate):
        # check plessure   must zero   only farward or back no drill
        # check

        if self.Equepment_pressure_push_pull.pressure > self.no_load_move_to_coordinnate_point_max_pressure:
            self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0])
            self.dangger_no_load_move_to_coordinnate_point = True
        else:
            if abs(self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate) < self.main_beam_of_the_tigger_point_delta:
                self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0])
                return True
            if self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate > 0:
                if self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate > self.no_load_move_parameter_contrl_distance:    # calclude direction is back
                    self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PULL_LEVEL[self.no_load_move_start_level])
                else:
                    self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PULL_LEVEL[self.no_load_move_end_level])
            else:
                if self.Equepment_line_distance_measure_4m_beam.coordinate - target_coordinate < -self.no_load_move_parameter_contrl_distance:   # calclude direction is farward
                    self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[self.no_load_move_start_level])
                else:
                   self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[ self.no_load_move_end_level])


   def beam_jog_drill(self, on=True):
        if on is True:
            self.Equepment_pole_dirll.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[self.beam_jog_drill_start_level])

        else:
            self.Equepment_pole_dirll.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0])

   def move_and_clockwise_slight(self):
       # nomal used to connexc pole male  mother thread
            self.Equepment_pole_dirll.parse_pull_push_level()
            if self.Equepment_pressure_push_pull.pressure > self.no_load_move_to_coordinnate_point_max_pressure or\
                    self.Equepment_pressure_torque.pressure > self.no_load_move_to_coordinnate_point_max_pressure or\
                    self.Equepment_line_distance_measure_beam_head.coordinate > self.tiger_forward_move_max_coordinate:
                self.move_stop(warterclose=False)
                self.dangger_move_and_clockwise_slight = True
            else:
                if self. move_and_clockwise_flag is False:
                    if self.Equepment_pole_dirll.operation_target_coordinate(self.Equepment_pole_dirll.PUSH_LEVEL[
                                                         self.tiger_dirll_pole_pole_tight_max_pressure_level]) is True:
                        self.move_and_clockwise_flag = True
                if self.move_and_clockwise_flag is True:
                    if self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_dirll.PULL_LEVEL[
                                                    self.tiger_dirll_pole_pole_tight_push_max_pressure_level]) is True:
                        self.move_and_clockwise_flag = False
                        return True

   def only_clockwise_rotate_pole_into_hole(self):

       if self.Equepment_pole_dirll.operation_target_coordinate( self.Equepment_pole_dirll.PUSH_LEVEL[
                                                          self.tiger_dirll_pole_pole_tight_max_pressure_level]) is True:
           return True

   def move_stop(self, warterclose=True):
        if self.move_stop_flag1 is False:
            if self.Equepment_pole_dirll.operation_target_coordinate(self.Equepment_pole_dirll.PUSH_LEVEL[0]) is True:
                self.move_stop_flag1 = True
        if self.move_stop_flag2 is False:
            if self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0]) is True:
                self.move_stop_flag2 = False
        if self.beam_water_open is True:
            if warterclose is True:
                self.beam_water_open = False
                self.Equepment_main_beam_obj.pole_water_open_close_pin.write_single(False)
        if (self.move_stop_flag1, self.move_stop_flag2, self.beam_water_open) == (True, True, False):
            self.move_stop_flag1 = False
            self.move_stop_flag2 = False
            return True

   def only_stop_push_pull(self):
       self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0])

   def tiger_out_innertooth_bite_tight(self, tiger_name="outer"):
        if (self.outtiger_tooth_push_flag, self.outtiger_tooth_push_back) == (0, 0):
                    if tiger_name == "outer":
                        self.biting_tight = self.Equepment_tigger_tooch_f.operation_target_coordinate(
                            self.Equepment_tigger_tooch_f.PUSH_LEVEL[5])
                    elif tiger_name == "inner":
                        self.biting_tight = self.Equepment_tigger_tooch_b.operation_target_coordinate(
                           self.Equepment_tigger_tooch_b.PUSH_LEVEL[5])
                    if self.biting_tight is True:
                        if self.out_tooth_bite_statue_time is None:
                            self.out_tooth_bite_statue_time = time.time()
                            self.outtiger_tooth_push_flag = True

        if (self.outtiger_tooth_push_flag, self.outtiger_tooth_push_back) == (1, 0):
                if time.time() - self.out_tooth_bite_statue_time > self.tiger_loose_time_:
                    if tiger_name == "outer":
                        self.still_bite_tight = self.Equepment_tigger_tooch_f.operation_target_coordinate(
                            self.Equepment_tigger_tooch_f.PUSH_LEVEL[0])
                    elif tiger_name == "inner":
                        self.still_bite_tight = self.Equepment_tigger_tooch_b.operation_target_coordinate(
                            self.Equepment_tigger_tooch_b.PUSH_LEVEL[0])
                    if self.still_bite_tight is True:
                        if tiger_name == "outer":
                            self.out_tooth_bite_statue = True
                        if tiger_name == "inner":
                            self.inner_tooth_bite_statue = True
                        self.biting_tight = None
                        self.still_bite_tight = None
                        self.out_tooth_bite_statue_time = None
                        return True

   def tiger_out_innertooth_relax(self, tiger_name="outer"):
        self.Equepment_tigger_tooch_f.parse_pull_push_level()
        self.Equepment_tigger_tooch_b.parse_pull_push_level()
        if (self.tiger_out_innertooth_relax_flag1, self.tiger_out_innertooth_relax_flag2) == (0, 0):
            if tiger_name == "outer":
                self.biting = self.Equepment_tigger_tooch_f.operation_target_coordinate(
                    self.Equepment_tigger_tooch_f.PULL_LEVEL[5])
            elif tiger_name == "inner":
                self.biting = self.Equepment_tigger_tooch_b.operation_target_coordinate(
                    self.Equepment_tigger_tooch_b.PULL_LEVEL[5])
            if self.biting is True:
                if self.out_tooth_bite_statue_time_relax is None:
                    self.out_tooth_bite_statue_time = time.time()
                    self.tiger_out_innertooth_relax_flag1 = True
        if (self.tiger_out_innertooth_relax_flag1, self.tiger_out_innertooth_relax_flag2) == (1, 0):
            if time.time() - self.out_tooth_bite_statue_time_relax > self.tiger_tight_time_:
                if tiger_name == "outer":
                    self.biting = self.Equepment_tigger_tooch_f.operation_target_coordinate(
                       self.Equepment_tigger_tooch_f.PUSH_LEVEL[0])
                elif tiger_name == "inner":
                    self.still_bite = self.Equepment_tigger_tooch_b.operation_target_coordinate(
                        self.Equepment_tigger_tooch_b.PUSH_LEVEL[0])
                if self.biting is True:
                    if tiger_name == "outer":
                        self.out_tooth_bite_statue = True
                    if tiger_name == "inner":
                        self.inner_tooth_bite_statue = True
                    self.out_tooth_bite_statue_time_relax = None
                    self.biting = None
                    self.tiger_out_innertooth_relax_flag1 = None
                    self.tiger_out_innertooth_relax_flag2 = None
                    self.still_bite = None
                    return True

   def tiger_loose_pole(self, loose_time=5, order_="loose"):
        self.Equepment_tigger_drill.parse_pull_push_level()
        if order_ == "loose":
            if self.tiger_loose_pole_flag1 is False:
                    loosin = self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PUSH_LEVEL[5])
                    if loosin == True:
                        if self.tiger_loose_time_ == None:
                            self.tiger_loose_time_ = time.time()
                            self.tiger_out_innertooth_relax_flag1 = True
            else:
                if time.time() - self.tiger_loose_time_ > loose_time:
                    loosin_keep = self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PUSH_LEVEL[0])
                    if loosin_keep is True:
                        self.tiger_loose_pole_statues = True
                        self.tiger_out_innertooth_relax_flag1 = False
                        self.tiger_loose_time_ = None
                        return True
        if order_ == "tight_or_back":
            if self.tiger_loose_pole_flag1 == False:
                    loosin = self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PULL_LEVEL[5])
                    if loosin == True:
                        if self.tiger_tight_time_ == None:
                            self.tiger_tight_time_ = time.time()
                            self.tiger_out_innertooth_relax_flag1 = True
            else:
                if time.time() - self.tiger_tight_time_ > loose_time:
                    loosin_keep = self.Equepment_tigger_drill.operation_target_coordinate(self.Equepment_tigger_drill.PUSH_LEVEL[0])
                    if loosin_keep is True:
                        self.tiger_loose_pole_statues = False
                        self.tiger_loose_time_ = None
                        self.tiger_tight_time_ = None
                        return True

   def move_back_tiger_ruler_number_equal_zero(self):
        if self.Equepment_line_distance_measure_beam_head.coordinate - self.tiger_self_middle_zero_coordinate_ < \
                -self.Equepment_line_distance_measure_beam_head.coordinate_delta:
            self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PULL_LEVEL[
                                                                  self.tiger_dirll_pole_pole_tight_push_max_pressure])

        else:
            self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0])
            return True


   def move_back_tiger_ruler_to_tuch_point(self):
        if abs(
                self.Equepment_line_distance_measure_beam_head.coordinate - self.tiger_self_middle_zero_coordinate_) > \
                self.Equepment_line_distance_measure_beam_head.coordinate_delta:
            self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PULL_LEVEL[
                                                                  self.tiger_dirll_pole_pole_tight_push_max_pressure])
        else:
            self.Equepment_pole_push_pull.operation_target_coordinate(self.Equepment_pole_push_pull.PUSH_LEVEL[0])
            return True




class drill_box_(ABC_high_level_equepment):
    def __init__(self, obj_name, observasion, all_equepment_updated):
        super().__init__(obj_name, observasion, all_equepment_updated)
        self.Equepment_line_distance_measure_1m_drill_box = sensor.line_distance(
            "Equepment_line_distance_measure_1m_drill_box",observasion, all_equepment_updated)
        self.Equepment_line_distance_measure_1m_drill_box.regester_equepment_pin_obj()
        self.Equepment_line_distance_measure_dirll_box_updown = sensor.line_distance(
            "Equepment_line_distance_measure_dirll_box_updown",observasion, all_equepment_updated)
        self.Equepment_line_distance_measure_dirll_box_updown.regester_equepment_pin_obj()
        self.Equepment_drill_box_digit_piont = sensor.drill_box(
            "Equepment_drill_box_digit_piont", observasion, all_equepment_updated)
        self.Equepment_drill_box_digit_piont.regester_equepment_pin_obj()

        self.box_grap_hand_tight_strong = load_data2["box_grap_hand_tight_strong"]
        self._drill_box_grap_hand_tight_slight = load_data2["_drill_box_grap_hand_tight_slight"]
        self.drill_box_grap_hand_tight_greater_strong = load_data2["drill_box_grap_hand_tight_greater_strong"]
        self.drill_box_grap_hand_relax_full = load_data2["drill_box_grap_hand_relax_full"]
        self.drill_box_grap_hand_relax_half = load_data2["drill_box_grap_hand_relax_half"]
        self.drill_box_grap_hand_relax_greater_part = load_data2["drill_box_grap_hand_relax_greater_part"]

        self.delta_drill_box_hand_run_coordinate = load_data2["delta_drill_box_hand_run_coordinate"]
        self.Equepment_line_distance_measure_dirll_box_updown_coordinate_delta = load_data2["Equepment_line_distance_measure_dirll_box_updown_coordinate_delta"]

        self.box_updown_column_can_grap = load_data2["box_updown_column_can_grap"]
        self.box_updown_column_up = load_data2["box_updown_column_up"]
        self.box_updown_bottom = load_data2["box_updown_bottom"]


    def hand_run(self,coordinate):
        if (self.Equepment_drill_box_digit_piont.beam_taile_hand_pin == True and self.Equepment_drill_box_digit_piont.beam_forward_hand_pin == True) or (
                self.Equepment_drill_box_digit_piont.beam_taile_hand_pin == False and self.Equepment_drill_box_digit_piont.beam_forward_hand_pin == False):
            if  self.Equepment_line_distance_measure_1m_drill_box.coordinate - coordinate > - self.Equepment_drill_box_digit_piont.pole_point_delta:
                self.Equepment_drill_box_digit_piont.handforward()
            elif  self.Equepment_line_distance_measure_1m_drill_box.coordinate - coordinate < self.Equepment_drill_box_digit_piont.pole_point_delta:
                self.Equepment_drill_box_digit_piont.handbackward()
            else:
                self.Equepment_drill_box_digit_piont.grap_hand_stop()
                return True
        else:
            self.Equepment_drill_box_digit_piont.grap_hand_stop()

    def updown_run(self, coordinate):
        if (self.beam_taile_hand_pin == True and self.beam_forward_hand_pin == True) or (
                self.beam_taile_hand_pin == False and self.beam_forward_hand_pin == False):
            if  self.Equepment_line_distance_measure_dirll_box_updown.coordinate - coordinate > - self.Equepment_line_distance_measure_dirll_box_updown.coordinate_delta:
                self.Equepment_drill_box_digit_piont.updown_down()      # updown_up    updown_down
            elif  self.Equepment_line_distance_measure_dirll_box_updown.coordinate - coordinate < self.Equepment_line_distance_measure_dirll_box_updown.coordinate_delta:
                self.Equepment_drill_box_digit_piont.updown_up()
            else:
                return True

        else:
            self.Equepment_drill_box_digit_piont.updown_stop()


class angle_speed_calclude:
    def __init__(self):
       self.beam_first_angle_not_update = None
       self.beam_first_angle = None
       self.beam_first_angle_time_ = None
       self.current_angle = None
       self.current_time = None
       self.delta_angle = None
       self.beam_last_angle_speed = None
       self.rotate_number = 0

    def beam_angle_speed_calclude_and_rotate_number(self, delt_time=0.1,  direction="clock_wise"):
        # direction = "clock_wise" or "counter_clockwise"
        if self.beam_first_angle_time_ is None:
             self.beam_first_angle_time_ = time.time()
        if self.beam_first_angle is None:
            self.beam_first_angle = self.current_angle
        if self.beam_first_angle_not_update is None:
            self.beam_first_angle_not_update = self.current_angle

        if direction == "clock_wise":
            delta_time = time.time() - self.beam_first_angle_time_
            if delta_time > delt_time:
                self.delta_angle = self.current_angle - self.beam_first_angle
                if self.delta_angle < 0:
                         self.rotate_number = self.rotate_number + 1 + (self.current_angle - self.beam_first_angle_not_update)/360
                         self.delta_angle = self.current_angle + (360 - self.current_angle)
                current_angle_speed = self.delta_angle/delta_time
                self.beam_first_angle = self.current_angle
                self.beam_first_angle_time_ = self.current_time
                self.beam_last_angle_speed = current_angle_speed
                return current_angle_speed
        elif direction == "counter_clockwise":
            delta_time = self.current_time - self.beam_first_angle_time_
            if delta_time > delt_time:
                self.delta_angle = self.current_angle - self.beam_first_angle
                if self.delta_angle > 0:
                    self.rotate_number = self.rotate_number + 1 + (self.beam_first_angle_not_update - self.current_angle) / 360
                    self.delta_angle = (360 - self.current_angle + self.beam_first_angle)
                self.rotate_number = self.rotate_number + self.delta_angle/360
                current_angle_speed = self.delta_angle/delta_time
                self.beam_first_angle = self.current_angle
                self.beam_first_angle_time_ = self.current_time
                self.beam_last_angle_speed = current_angle_speed
                return current_angle_speed

    def calculation_over_re_init(self):
        self.beam_first_angle_not_update = None
        self.beam_first_angle = None
        self.beam_first_angle_time_ = None
        self.current_angle = None
        self.current_time = None
        self.delta_angle = None
        self.beam_last_angle_speed = None
        self.rotate_number = 0

class  speed_calclude ():
    def __init__(self):
        self.beam_speed_first_coordinate = None
        self.beam_speed_first_coordinate_time_ = None
        self.current_coordinate = None
        self.current_coordinate_time_ = None
        self.last_speed = None

    def beam_speed_calclude(self,delt_time):
       self.delta_time = self.current_coordinate_time_ - self.beam_speed_first_coordinate_time_
       if self.delta_time > delt_time:
           delta_s = self.current_coordinate - self.beam_speed_first_coordinate
           speed = delta_s/self.delta_time
           self.beam_speed_first_coordinate_time_ = self.current_coordinate_time_
           self.beam_speed_first_coordinate = self.current_coordinate
           self.last_speed = speed
           return speed


class max_pressure():
    def __init__(self):
        self.pre_pressure = 0
        self.current_pressure = 0
        self.max_pressure__ = 0

    def max_pressure_(self):
        if self.current_pressure > self.max_pressure__ :
            self.max_pressure__ = self.current_pressure



class lamp(ABC_high_level_equepment):
    def __init__(self,obj_name, observasion, all_equepment_updated):
       super().__init__(obj_name, observasion, all_equepment_updated)
       self.Equepment_lamp_light = sensor.lamp_("Equepment_lamp_light", observasion,
                                                               all_equepment_updated)
       self.Equepment_lamp_light.regester_equepment_pin_obj()


class warning_lamp_all(ABC_high_level_equepment):
    def __init__(self,obj_name, observasion, all_equepment_updated):
        super().__init__(obj_name, observasion, all_equepment_updated)
        self.Equepment_warning_light = sensor.warning_lamp("Equepment_warning_light", observasion, all_equepment_updated)
        self.Equepment_warning_light.regester_equepment_pin_obj()


class machine():  ###facade method

    def __init__(self):
        all_equepment_updated = sensor.all_equepment_updated()
        oberservation = sensor.observation()
        self.authticate = None
        self.ProcessSendOrderToWindowPipe = None
        self.drill_box = drill_box_("drill_box_", oberservation, all_equepment_updated)
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee1", __file__, __name__,  inspect.currentframe().f_lineno)
        self.main_beam = main_beam("main_beam_", oberservation, all_equepment_updated, self.drill_box)
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee2", __file__, __name__,  inspect.currentframe().f_lineno)
        self.lamp = lamp("lamp_", oberservation, all_equepment_updated)
        self.warning_lamp_all = warning_lamp_all("warning_lamp_all_", oberservation, all_equepment_updated)
        self.pins_equepmeent_name = seting.setting_class.get_pin_equepment_name()
        self.oberservation = oberservation
        self.wrong_data = [
            [False, False, False, False, False],
            # process result, trouble name, trouble start time, trouble end time,assessment time
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

    def init_parameter(self, s_end):
        self.processSendToCommunicationPipe = s_end
        self.ProcessSendOrderToWindowPipe = s_end




    def run(self):
        from threading import Thread
        oberservation_thread = Thread(target=self.oberservation.running, args=(self.colect_data_to_que,))
        oberservation_thread.start()

    def begin_distribute_order(self):
        pass

    def send_data(self, machine_read_data=None, Eauepment_data=None):
        if machine_read_data is not None:
            try:

                self.ProcessSendOrderToWindowPipe.send(machine_read_data)
            except:
                pass
        if Eauepment_data is not None:
            try:
                self.ProcessSendOrderToWindowPipe.send(Eauepment_data)
            except:
                pass

    def colect_data_to_que(self, delta=0.1):
        pin_data = [0, 0, 0, 0]
        sleep_ = time.sleep
        oberservationread_data_from_board = self.oberservation
        pins_equepmeent_name = self.pins_equepmeent_name
        main_beamEquepment_line_distance_measure_4m_beam = self.main_beam.Equepment_line_distance_measure_4m_beam
        main_beamEquepment_line_distance_measure_beam_taile = self.main_beam.Equepment_line_distance_measure_beam_taile
        main_beam = self.main_beam
        ProcessSendOrderToWindowPipe = self.ProcessSendOrderToWindowPipe
        drill_boxEquepment_line_distance_measure_1m_drill_box = self.drill_box.Equepment_line_distance_measure_1m_drill_box

        sleep_(delta)
        try:
            first_point_coordinate = (main_beamEquepment_line_distance_measure_4m_beam.coordinate -
                              abs(main_beamEquepment_line_distance_measure_beam_taile.coordinate -
                                  main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top))
        except Exception:
            first_point_coordinate = None
        try:
            second_point_coordinate = (main_beamEquepment_line_distance_measure_4m_beam.coordinate -
                           abs(
                               main_beamEquepment_line_distance_measure_beam_taile.coordinate -
                               main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top))
        except Exception:
            second_point_coordinate = None

        try:
            fourth_point_coordinate = (main_beamEquepment_line_distance_measure_4m_beam.coordinate -
                         abs(
                             main_beamEquepment_line_distance_measure_beam_taile.coordinate -
                             main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top))
        except Exception:
            fourth_point_coordinate = None
        try:
            third_point_coordinate = (main_beamEquepment_line_distance_measure_4m_beam.coordinate -
            main_beamEquepment_line_distance_measure_beam_taile.coordinate -
            main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top)-(
main_beam.Equepment_line_distance_measure_beam_head.coordinate - main_beam.tiger_self_middle_zero_coordinate_)
        except Exception:
            third_point_coordinate = None
        try:
            taile_thread_is_ok_point_coordinate = (
                main_beamEquepment_line_distance_measure_4m_beam.coordinate -
                main_beamEquepment_line_distance_measure_beam_taile.coordinate -
                main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top) - (
                main_beam.Equepment_line_distance_measure_beam_head.coordinate -
                main_beam.tiger_self_middle_zero_coordinate_)
        except Exception:
            taile_thread_is_ok_point_coordinate = None

        equepment_data = {
            "main_beam_coordinate_single1": main_beamEquepment_line_distance_measure_4m_beam.coordinate,
            "main_beam_cycle_number_coordinate_single1": main_beamEquepment_line_distance_measure_4m_beam.cycle_number_coordinate,
            "hand_grap_coordinate_single2": drill_boxEquepment_line_distance_measure_1m_drill_box.coordinate,
            "main_beam_taile_20cm_single3": main_beamEquepment_line_distance_measure_beam_taile.coordinate,
            "main_beam_head_20cm_single4": main_beam.Equepment_line_distance_measure_beam_head.coordinate,
            "main_beam_pulpush_rocer_arm_coordinate_single5": main_beam.Equepment_pole_push_pull.coordinate,
            "drill_rocker_arm_coordinate_single6": main_beam.Equepment_pole_dirll.coordinate,
            "pole_angle_single7": main_beam.Equepment_angle_torque_to_pole.angle,
            "warter_deep_coordinate_single8": main_beam.Equepment_warter_deep_measure.water_deep_number,
            "outer_tiger_rocker_arm_coordinate_single9": main_beam.Equepment_tigger_tooch_f.coordinate,
            "inner_tiger_rocker_arm_coordinate_single10": main_beam.Equepment_tigger_tooch_b.coordinate,
            "loose_tiger_rocker_arm_coordinate_single11": main_beam.Equepment_tigger_drill.coordinate,
            "water_pressure_single12": main_beam.Equepment_pressure_warter.pressure,
            "push_pull_pressure_single13": main_beam.Equepment_pressure_push_pull.pressure,
            "drill_pressure_single14": main_beam.Equepment_pressure_torque.pressure,
            "dirll_box_up_dow_point_single15": main_beam.Equepment_line_distance_measure_dirll_box_updown.coordinate,
            "angle_0_corectting": main_beam.Equepment_angle_torque_to_pole.angle,

            "first_point_coordinate": first_point_coordinate,

            "second_point_coordinate": second_point_coordinate,

            "fourth_point_coordinate": fourth_point_coordinate,

            "third_point_coordinate": third_point_coordinate,

            "taile_thread_is_ok_point_coordinate": taile_thread_is_ok_point_coordinate
        }
        datas = sendData_towin(winip, "machine_equepment_instantaneous_read_data", equepment_data)
        ProcessSendOrderToWindowPipe.send(datas)



