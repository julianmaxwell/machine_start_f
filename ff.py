from  order import *
from  machine_high_lever_equepment import angle_speed_calclude,max_pressure
import time
from abc import ABC,abstractmethod,ABCMeta
from functools import partial
import contextlib

back_pole_thread = 8
outhead_pole_thread = 8
tiger_tooth_loose_pole_thread_angle = 20
beam_come_last = 4600     #pole_in_middle_tiger_tooth_to_taile_tofaward   copy to here

pole_in_middle_tiger_tooth = 800
beam_taile_5cm = 50
man_give_pole_place = 2300
pole_thread_full_out = 1
pole_thread_full_out2 = 20
pole_pull_back_can_out_box_hand_to_grap = 1800
pole_in_middle_tiger_tooth_to_taile_tofaward = 4650
beam_can_out_all_thread_pole = 900

box_to_beam_can_grap = 90

the_new_point_man_can_let_pole_out_beam = 50   ##this is the new data  not find in program

class auto_forward():

    def __init__(self,box_pole_obj,machin_obj,box_prepare_obj,ui_widget_main):
        self.ui_widget_main = ui_widget_main
        self.box_pole_obj = box_pole_obj
        self.machin_obj = machin_obj
        self.box_prepare_obj = box_prepare_obj
        self.order = None  #"go", "back"
        self.stop = None

        self.tooth_in_relaxt_out_tight_slight_forward = True
        self.flag_check_box_hand_unstop_beam = False
        self.flag_open_OUT_IN_tiger_tooth = False
        self.flag_forward_go = False
        self.forward_stop = False
        self.flag_bite_OUT_tiger_tooth = False
        self.clockwise_rotate_same_place_away_thread = False
        self.orde_change_flag = False
        self.forward_stop_place_to_get_pole_auto = False
        self.counter_back_and_let_pole_in_middle_tooth_auto = False
        self.forward_stop_place_to_get_pole_manual = False
        self.back_pole_and_box_hand_can_out_manual = False
        self.counter_back_and_let_pole_in_middle_tooth_manua_ = False
        self.step=(self.tooth_in_relaxt_out_tight_slight_forward,
        self.flag_check_box_hand_unstop_beam,
        self.flag_open_OUT_IN_tiger_tooth,
        self.flag_forward_go,
        self.forward_stop,
        self.flag_bite_OUT_tiger_tooth,
        self.clockwise_rotate_same_place_away_thread,
        self.orde_change_flag,
        self.forward_stop_place_to_get_pole_auto,
        self.counter_back_and_let_pole_in_middle_tooth_auto,
        self.forward_stop_place_to_get_pole_manual,
        self.back_pole_and_box_hand_can_out_manual,
        self.counter_back_and_let_pole_in_middle_tooth_manua_,)
        self.detect_tiger_pole_tight_angle = angle_speed_calclude()
        self.detect_tiger_pole_tight_max_pressure = max_pressure()


        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()

        self.detect_tiger_pole_tight_angle3 = angle_speed_calclude()

        self.pole_out_order = "auto"    #"auto"  or  "manual"           ################################## interface


        self.pole_drill_to_next_pole_pressure = max_pressure()

        self.pole_out_manual_order =None    #if value = "back" begin go back   ################################## interface

        self.max_totle_use_pole = 0                     ################################## interface
        self.totle_use_pole = 0                            ################################## interface
        self.totle_use_pole_can_statistics = None  #"statistics"       ################################## interface

        self.counter_back_and_let_pole_in_middle_tooth_manual_flag = False
        self.flag_open_OUT_IN_tiger_tooth_flgN = False

        self.fflag = False
        self.fflag1 = False
        self.fflag2 = False
        self.fflag3 = False

        self.flag_open_OUT_IN_tiger_tooth_flgN1 = False

        self.relaxauto1 = False
        self.rotate_slight = False
        self.rotate_slight2 = False
    def set_value(self):
        self.auto__plan = (  self.tooth_in_relaxt_out_tight,
                             self.flag_check_box_hand_unstop_beam,
                             self.flag_open_OUT_IN_tiger_tooth,
                             self.flag_forward_go,
                             self.forward_stop,
                             self.flag_bite_OUT_tiger_tooth,
                             self.clockwise_rotate_same_place_away_thread,
                             self.orde_change_flag,
                             self.forward_stop_place_to_get_pole_auto,
                             self.counter_back_and_let_pole_in_middle_tooth_auto,
                             self.forward_stop_place_to_get_pole_manual,
                             self.back_pole_and_box_hand_can_out_manual,
                             self.counter_back_and_let_pole_in_middle_tooth_manua_,)
    def auto_go(self):
        self.set_value()

        if self.auto__plan ==   (False, False, False, False, False, False, False, False, False, False, False, False, False):   # step1
                self.step__1 = step_1(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
                if self.step__1.run() == True:
                    self.tooth_in_relaxt_out_tight_slight_forward = True
                    self.set_value()
        elif self.auto__plan == (True, False, False, False, False, False, False, False, False, False, False, False, False):     # step2
            self.step__2 = step_2(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__2.run() == True:
                self.flag_check_box_hand_unstop_beam = True
                self.set_value()
        elif self.auto__plan == (True, True, False, False, False, False, False, False, False, False, False, False, False):      # step3
            self.step__3 = step_3(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__3.run() == True:
                                self.flag_open_OUT_IN_tiger_tooth = True
                                self.set_value()
        elif self.auto__plan == (True, True, True, False, False, False, False, False, False, False, False,False, False):    # step4
            self.step__4 = step_4(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__4.run() == True:
                self.flag_forward_go = True
                self.set_value()
        elif self.auto__plan == (True, True, True, True, False, False, False, False, False, False, False, False, False):        # step 5
            self.step__5 = step_5(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__5.run() == True:
                self.forward_stop = True
                self.set_value()
        elif self.auto__plan == (True, True, True, True, True, False, False, False, False, False, False, False, False):     # step6
            self.step__6 = step_6(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__6.run() == True:
                self.flag_bite_OUT_tiger_tooth = True
                self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, False, False, False, False, False, False, False):      # step7
            self.step__7 = step_7(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__7.run() == True:
                        self.clockwise_rotate_same_place_away_thread = True
                        self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, False, False, False, False, False, False):       # step8
            if self.pole_out_order == "auto" and self.box_pole_obj.box_no_pole == False:
                self.forward_stop_place_to_get_pole_auto = False


                self.forward_stop_place_to_get_pole_manual = True
                self.back_pole_and_box_hand_can_out = True
                self.counter_back_and_let_pole_in_middle_tooth = True
                self.orde_change_flag = True
            else:
                self.pole_out_order = "manual"

            if self.pole_out_order == "manual":
                self.forward_stop_place_to_get_pole_auto = True

                self.forward_stop_place_to_get_pole_manual = False
                self.back_pole_and_box_hand_can_out = False
                self.counter_back_and_let_pole_in_middle_tooth = False
                self.orde_change_flag = True
            if self.orde_change_flag == True:
                self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, False, False, False, False, False):        # step 9
            self.step__9 = step_9(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__9.run() == True:
                self.forward_stop_place_to_get_pole_auto = True
                self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, False, False, False, False):     ####################################### must repair    # step 10
            self.step__10 = step_10(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__10.run() == True:

                                self.counter_back_and_let_pole_in_middle_tooth_auto = True

                                self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, False, False, False):          # step 11
            self.step__11 = step_11(self.box_pole_obj,self.machin_obj,self.box_prepare_obj)
            if self.step__11.run() == True:
                self.forward_stop_place_to_get_pole_manual = True
                self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, False, False):         # step 12
            self.step__12 = step_12(self.box_pole_obj, self.machin_obj, self.box_prepare_obj)
            if self.step__12.run() == True:
                            self.back_pole_and_box_hand_can_out = True
                            self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, False):          # step 13

                    if self.pole_out_manual_order == "go":
                        if  self.counter_back_and_let_pole_in_middle_tooth_manual_flag == False:
                                if self.machin_obj.main_beam.move_and_clockwise() == True:
                                    self.counter_back_and_let_pole_in_middle_tooth_manual_flag = True
                        if self.pole_drill_to_next_pole_pressure.max_pressure__ > 4:
                                        if self.machin_obj.main_beam.move_stop() == True:
                                            self.counter_back_and_let_pole_in_middle_tooth_manual_flag = False
                                            self.counter_back_and_let_pole_in_middle_tooth_manual = True
                                            self.set_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True):           # step 14
            self.auto__plan = (False, False, False, False, False, False, False, False, False, False)
            self.box_prepare_pole_out = True
            self.box_pole_obj.other_out_pole()
            self.totle_use_pole = len(self.box_pole_obj.empty)+self.box_pole_obj.other_out-self.box_pole_obj.other_in
            if self.max_totle_use_pole < len(self.box_pole_obj.empty)+self.box_pole_obj.other_out-self.box_pole_obj.other_in:
                self.max_totle_use_pole = len(self.box_pole_obj.empty)+self.box_pole_obj.other_out
            self.tooth_in_relaxt_out_tight = True
            self.flag_check_box_hand_unstop_beam = False
            self.flag_open_OUT_IN_tiger_tooth = False
            self.flag_forward_go = False
            self.forward_stop = False
            self.flag_bite_OUT_tiger_tooth = False
            self.clockwise_rotate_same_place_away_tread = False
            self.orde_change_flag = False
            self.forward_stop_place_to_get_pole_auto = False
            self.forward_stop_place_to_get_pole_manual = False
            self.back_pole_and_box_hand_can_out = False
            self.counter_back_and_let_pole_in_middle_tooth = False
            self.counter_back_and_let_pole_in_middle_tooth_manual = False
            self.set_value()

class auto_back_ward():
    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):
        self.box_pole_obj = box_pole_obj
        self.machin_obj = machin_obj
        self.box_prepare_obj = box_prepare_obj
        self.stop = None
        self.manual_order = "auto"

        self.flag_check_box_hand_unstop_beam = False
        self.flag_open_OUT_IN_tiger_tooth = False
        self.flag_pullward_go = False
        self.pullward_stop = False
        self.flag_bite_OUT_tiger_tooth = False
        self.clockwise_rotate_same_place = False
        self.flag__bite_IN_tiger_tooth = False
        self.counter_clock_wise = False
        self.flag__open_IN_tiger_tooth2 = False
        self.loose_back = False
        self.back_pole_thread = False
        self.move___ = False
        self.flag__bite_IN_tiger_3 = False
        self.changge_auto_manual = False
        self.counter_clock_wise_manual_20 = False
        self.beam_come_to_taile_mauale = False
        self.tiger_out_innertooth_relax_manual = False
        self.box_prepair_other_in_pole = False
        self.counter_clock_wise2_auto = False
        self.tiger_out_innertooth_bite_tight_last_auto = False
        self.counter_clock_wise3_auto = False
        self.beam_come_to_taile_auto = False
        self.box_prepair_in_pole_auto = False
        self.next_ready = False

        self.step_back = (self.flag_check_box_hand_unstop_beam,
                          self.flag_open_OUT_IN_tiger_tooth,
                          self.flag_pullward_go,
                          self.pullward_stop,
                          self.flag_bite_OUT_tiger_tooth,
                          self.clockwise_rotate_same_place,
                          self.flag__bite_IN_tiger_tooth,
                          self.counter_clock_wise,
                          self.flag__open_IN_tiger_tooth2,
                          self.loose_back,
                          self.back_pole_thread,
                          self.move___,
                          self.flag__bite_IN_tiger_3,
                          self.counter_clock_wise2,
                          self.tiger_out_innertooth_bite_tight_last,
                          self.counter_clock_wise3,
                          self.beam_come_to_taile,
                          self.box_prepair_in_pole,
                          self.next_ready,)
        self.detect_tiger_pole_tight_angle = angle_speed_calclude()
        self.detect_tiger_pole_tight_max_pressure = max_pressure()

        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()

        self.detect_tiger_pole_tight_angle3 = angle_speed_calclude()

        self.reach = None
        self.reach2 = False

        self.manual_order_can_go_to_in_hole_to_next = None    #  "go"

        self.flag_open_OUT_IN_tiger_tooth_flag = None

        self.next_ready_flag1 = False
        self.next_ready_flag2 = False

        self.counter_clock_wise3_flag = False
        self.counter_clock_wise_manual_20_flag = False
    def set_back_value(self):
        self.auto__plan = (self.flag_check_box_hand_unstop_beam,
        self.flag_open_OUT_IN_tiger_tooth,
        self.flag_pullward_go ,
        self.pullward_stop,
        self.flag_bite_OUT_tiger_tooth,
        self.clockwise_rotate_same_place,
        self.flag__bite_IN_tiger_tooth,
        self.counter_clock_wise,
        self.flag__open_IN_tiger_tooth2 ,
        self.loose_back ,
        self.back_pole_thread ,
        self.move___ ,
        self.flag__bite_IN_tiger_3 ,
        self.changge_auto_manual ,
        self.counter_clock_wise_manual_20 ,
        self.beam_come_to_taile_mauale ,
        self.tiger_out_innertooth_relax_manual ,
        self.box_prepair_other_in_pole ,
        self.counter_clock_wise2_auto,
        self.tiger_out_innertooth_bite_tight_last_auto ,
        self.counter_clock_wise3_auto ,
        self.beam_come_to_taile_auto ,
        self.box_prepair_in_pole_auto ,
        self.next_ready , )
    def auto_go(self):

        if self.auto__plan == (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            self.backstep__1 = back_step1(self.box_pole_obj, self.machin_obj, self.box_prepare_obj)
            if self.backstep__1.run() == True:
                self.flag_check_box_hand_unstop_beam = True
                self.set_back_value()
        elif self.auto__plan == (True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):

            if self.flag_open_OUT_IN_tiger_tooth_flag == False:
                if self.machin_obj.main_beam.tiger_out_innertooth_relax() == True:
                    self.flag_open_OUT_IN_tiger_tooth_flag = True
            if self.flag_open_OUT_IN_tiger_tooth_flag == True:
                if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True :
                    self.flag_open_OUT_IN_tiger_tooth_flag = False
                    self.flag_open_OUT_IN_tiger_tooth = True
                    self.set_back_value()
        elif self.auto__plan == (True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.machin_obj.main_beam.auto_rotate_pull() == True:
                self.flag_pullward_go = True
                self.set_back_value()
        elif self.auto__plan == (True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.machin_obj.main_beam.main_beam_move_stop(beam_come_last) == True:  ### target_coordinate paramete must add
                self.pullward_stop = True
                self.set_back_value()
        elif self.auto__plan == (True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.machin_obj.main_beam.tiger_out_innertooth_bite_tight() == True:
                self.flag_bite_OUT_tiger_tooth = True
                self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.detect_tiger_pole_tight_angle.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle.beam_first_angle == None or \
                    self.detect_tiger_pole_tight_angle.beam_first_angle_time_ == None:
                self.detect_tiger_pole_tight_angle.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            if self.detect_tiger_pole_tight_max_pressure.pre_pressure == 0:
                self.detect_tiger_pole_tight_max_pressure.pre_pressure = self.machin_obj.main_beam.Equepment_pressure_torque.pressure
            self.detect_tiger_pole_tight_max_pressure.current_pressure = self.machin_obj.main_beam.Equepment_pressure_torque.pressure
            self.detect_tiger_pole_tight_angle.beam_angle_speed_calclude_and_rotate_number()
            self.detect_tiger_pole_tight_max_pressure.max_pressure_()
            self.detect_tiger_pole_tight_angle.rotate_number = 0
            if self.machin_obj.main_beam.clockwise_rotate_same_place() == True:
                if self.detect_tiger_pole_tight_max_pressure.max_pressure__ > 5 and self.detect_tiger_pole_tight_angle.beam_last_angle_speed < 20:
                    self.detect_tiger_pole_tight_angle.beam_first_angle_not_update = None
                    self.detect_tiger_pole_tight_angle.beam_first_angle = None
                    self.detect_tiger_pole_tight_angle.beam_first_angle_time_ = None
                    self.detect_tiger_pole_tight_max_pressure.max_pressure__ = 0
                    self.clockwise_rotate_same_place = True
                    self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.machin_obj.main_beam.tiger_out_innertooth_bite_tight(tiger_name="inner") == True:
                self.flag__bite_IN_tiger_tooth = True
                self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection = "counter_clocwise")
            if self.machin_obj.main_beam.tiger_loose_pole() == True:
                if self.detect_tiger_pole_tight_angle2.rotate_number*360  > tiger_tooth_loose_pole_thread_angle:
                    self.counter_clock_wise = True
                    self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number()
            if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
                self.flag__open_IN_tiger_tooth2 = True
                self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number()
            if self.machin_obj.main_beam.tiger_loose_pole(order_="tight_or_back") == True:   ##tiger init  to the relax position
                self.loose_back = True
                self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False):
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number()
            if self.machin_obj.main_beam.counterclockwise(pulllevel=2) == True:
                self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
                self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
                if self.detect_tiger_pole_tight_angle2.rotate_number  > pole_thread_full_out2 :
                    self.detect_tiger_pole_tight_angle2.rotate_number = 0
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                    self.detect_tiger_pole_tight_angle2.beam_first_angle = None
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None
                    self.back_pole_thread = True
                    self.set_back_value()

        # next is 9 class  run 1
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.machin_obj.main_beam.move_() == True:
                self.move___ = True
                self.set_back_value()
        # next is 9 class  run_2
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False):
            if self.machin_obj.main_beam.tiger_out_innertooth_bite_tight(tiger_name="inner") == True:
                self.flag__bite_IN_tiger_3 = True
                self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False):
            if self.manual_order == "auto" and len(self.box_pole_obj.empty) != 0:
                self.counter_clock_wise_manual_20 = True
                self.beam_come_to_taile_mauale = True
                self.tiger_out_innertooth_relax_manual = True
                self.box_prepair_other_in_pole = True

                self.counter_clock_wise2 = False
                self.tiger_out_innertooth_bite_tight_last = False
                self.counter_clock_wise3 = False
                self.beam_come_to_taile = False
                self.box_prepair_in_pole = False
                self.changge_auto_manual = True



            if self.manual_order == "manual" or len(self.box_pole_obj.empty) == 0:
                self.counter_clock_wise_manual_20 = False
                self.beam_come_to_taile_mauale = False
                self.tiger_out_innertooth_relax_manual = False
                self.box_prepair_other_in_pole = False

                self.counter_clock_wise2 = True
                self.tiger_out_innertooth_bite_tight_last = True
                self.counter_clock_wise3 = True
                self.beam_come_to_taile = True
                self.box_prepair_in_pole = True


                self.manual_order = "manual"
                self.changge_auto_manual = True
            if self.changge_auto_manual == True:
                self.set_back_value()

# next is 10 class
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False,  False, False, False, False, False, False):
            if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
            if self.counter_clock_wise_manual_20_flag == False:
                        if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=True) == True:
                            self.counter_clock_wise_manual_20_flag = True
            if self.counter_clock_wise_manual_20_flag == True:
                if self.detect_tiger_pole_tight_angle2.rotate_number > pole_thread_full_out2:
                    if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=False) == True:
                        self.detect_tiger_pole_tight_angle2.rotate_number = 0
                        self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                        self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                        self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None
                        self.counter_clock_wise_manual_20_flag = False
                        self.counter_clock_wise_manual_20 = True
                        self.set_back_value()

                        # next is 10 class
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False,  False, False, False, False, False, False):
            if self.machin_obj.main_beam.main_beam_move_stop(beam_taile_5cm) == True:
                self.beam_come_to_taile_mauale = True
                self.set_back_value()
                # next is 10 class
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False,  False, False, False, False, False, False):
            if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
                self.tiger_out_innertooth_relax_manual = True
                self.set_back_value()
                # next is class 11
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False,  False, False, False, False, False, False):

            if self.manual_order_can_go_to_in_hole_to_next =="go"  :
                    if (self.reach,self.reach2) == (False,False):
                       if self.machin_obj.main_beam.main_beam_move_stop(beam_come_last-200,pull_level=5) == True:
                           self.reach = True
                    if (self.reach, self.reach2) == (True, False):
                        self.machin_obj.main_beam.move_and_clockwise_slight(on=True)
                        self.reach2 = True
                    if (self.reach, self.reach2) == (True, True):
                        if self.machin_obj.main_beam.Equepment_pressure_torque.pressure > 2:
                            if self.machin_obj.main_beam.move_and_clockwise_slight(on=False) == True:
                                self.reach = False
                                self.reach2 = False
                                self.box_prepair_other_in_pole = True
                                self.set_back_value()
        # next is in class 12
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False):
            if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")

            if self.machin_obj.main_beam.counterclockwise(pulllevel=4, delt_time_=0.2) == True:
                if self.detect_tiger_pole_tight_angle2.rotate_number> pole_thread_full_out :
                    self.detect_tiger_pole_tight_angle2.rotate_number = 0
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None
                    self.counter_clock_wise2_auto = True
                    self.set_back_value()


                    # next is in class 12
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False):
            if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
                self.tiger_out_innertooth_bite_tight_last_auto = True
                self.set_back_value()

            # next is in class 13
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False):
           if self.machin_obj.main_beam.main_beam_move_stop(pole_pull_back_can_out_box_hand_to_grap) == True:  # here need a paramete of stop coordinate
                if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                        self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                        self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                    self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
                self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
                self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
                if self.counter_clock_wise3_flag == False:
                    if self.machin_obj.main_beam.counterclockwise(pulllevel=2 ,on= True) == True:
                        self.counter_clock_wise3_flag = True
                if self.counter_clock_wise3_flag == True:
                        if self.detect_tiger_pole_tight_angle2.rotate_number > pole_thread_full_out2:
                            if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=False) == True:
                                self.detect_tiger_pole_tight_angle2.rotate_number = 0
                                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None
                                self.counter_clock_wise3_flag = False
                                self.counter_clock_wise3_auto = True
                                self.set_back_value()
                        # next is in class 13
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False):
                if self.machin_obj.main_beam.main_beam_move_stop(beam_taile_5cm) == True:
                    self.beam_come_to_taile_auto = True
                    self.set_back_value()
                    # next is in class 14   UNDO  TOMAORROW DO IT
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False):
            if self.box_pole_obj.pole_in() == True:
                self.box_prepair_in_pole_auto = True
                self.set_back_value()
                # next is in class 14
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False):


            if (self.next_ready_flag1,self.next_ready_flag2) == (False,False):
                if self.machin_obj.main_beam.main_beam_move_stop(beam_come_last-80) == True:
                        self.next_ready_flag1 = True
            if (self.next_ready_flag1, self.next_ready_flag2) == (True, False):
                if self.machin_obj.main_beam.move_and_clockwise_slight(on=True) == True:
                    self.next_ready_flag2 = True
            if (self.next_ready_flag1, self.next_ready_flag2) == (True, True):
                if self.machin_obj.main_beam.Equepment_pressure_torque.pressure >3 and self.machin_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate> beam_come_last:
                        self.next_ready_flag1 = False
                        self.next_ready_flag2 = False
                        self.next_ready = True
                        self.set_back_value()
        elif self.auto__plan == (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True):

            self.box_pole_obj.other_in_pole()
            self.totle_use_pole = len(self.box_pole_obj.empty)+(self.box_pole_obj.other_out-self.box_pole_obj.other_in_pole)
            self.max_totle_use_pole = len(self.box_pole_obj.empty)+self.box_pole_obj.other_in_pole
            self.flag_check_box_hand_unstop_beam = False
            self.flag_open_OUT_IN_tiger_tooth = False
            self.flag_pullward_go = False
            self.pullward_stop = False
            self.flag_bite_OUT_tiger_tooth = False
            self.clockwise_rotate_same_place = False
            self.flag__bite_IN_tiger_tooth = False
            self.counter_clock_wise = False
            self.flag__open_IN_tiger_tooth2 = False
            self.loose_back = False
            self.back_pole_thread = False
            self.move___ = False
            self.flag__bite_IN_tiger_3 = False
            self.changge_auto_manual = False
            self.counter_clock_wise_manual_20 = False
            self.beam_come_to_taile_mauale = False
            self.tiger_out_innertooth_relax_manual = False
            self.box_prepair_other_in_pole = False
            self.counter_clock_wise2 = False
            self.tiger_out_innertooth_bite_tight_last = False
            self.counter_clock_wise3 = False
            self.beam_come_to_taile = False
            self.box_prepair_in_pole = False
            self.next_ready = False

            self.auto__plan =(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)


class auto_forward_backward_stop_changge():
    def __init__(self,auto_forward_obj,auto_back_ward_obj):
        self.auto_forward_obj = auto_forward_obj
        self.auto_back_ward_obj = auto_back_ward_obj

        self.operation = {}
        self.order = None    # order {forward,backward,stop,manual}
        self.action = None

        self.forward_plan = None
        self.backward_plan = None
        self.forward_turn_back_ward = {
            # (False, False, False, False, False, False, False, False, False, False, False, False, False): [( False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function1],
            # (True, False, False, False, False, False, False, False, False, False, False, False, False): [(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function2],
            # (True, True, False, False, False, False, False, False, False, False, False, False, False): [(True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function3],
            # (True, True, True, False, False, False, False, False, False, False, False, False, False): [(True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function4],
            (True, True, True, True, False, False, False, False, False, False, False, False, False): [(True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function2],
            (True, True, True, True, True, False, False, False, False, False, False, False, False): [(True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function6],
            (True, True, True, True, True, True, False, False, False, False, False, False, False): [(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function2],
            (True, True, True, True, True, True, True, False, False, False, False, False, False): [(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),self.forward_turn_back_ward_stop_function2],
            (True, True, True, True, True, True, True, True, False, False, False, False, False): [(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),self.forward_turn_back_ward_stop_function2],
            (True, True, True, True, True, True, True, True, True, False, False, False, False): [(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),self.forward_turn_back_ward_stop_function2],
            (True, True, True, True, True, True, True, True, True, True, False, False, False): [(True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function2],
            (True, True, True, True, True, True, True, True, True, True, True, False, False): [(True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),self.forward_turn_back_ward_stop_function2],
            (True, True, True, True, True, True, True, True, True, True, True, True, False): [(True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function2], # besure here run must run in back function
            (True, True, True, True, True, True, True, True, True, True, True, True, True): [(True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False),self.forward_turn_back_ward_stop_function2], # besure here run must run in back function
        }
        self.backward_turn_forward = {
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(False, False, False, False, False, False, False, False, False, False, False, False),1],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[(True, False, False, False, False, False, False, False, False, False, False, False),2],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[],
            (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False):[],

        }

    def action(self):
        self.order_has = None
        if self.order == "forward" and self.backward_plan == None and  self.forward_plan == None:
            if self.order_has != True:
                self.auto_forward_obj.auto__plan = ( False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
                self.action_obj = self.auto_forward_obj
                self.order_has = True
                self.order_has = True
        if self.order == "backward" and  self.backward_plan == None and  self.forward_plan == None :
            if self.order_has != True:
                self.auto_back_ward_obj.auto__plan = ( False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
                self.action_obj = self.auto_back_ward_obj

        if self.order == "forward" and  isinstance(self.action_obj,auto_back_ward):
            if self.order_has != True:
                self.backward_turn_forward[self.action_obj.auto__plan][1]()
                self.auto_forward_obj.auto__plan =  self.backward_turn_forward[self.action_obj.auto__plan][0]
                self.action_obj = self.auto_forward_obj
                self.order_has = True

        if self.order == "backward" and  isinstance(self.action_obj,auto_forward):
            if self.order_has != True :
                try:
                    self.forward_turn_back_ward[self.action_obj.auto__plan][1]()
                    self.auto_back_ward_obj.auto__plan =  self.backward_turn_forward[self.action_obj.auto__plan][0]
                    self.action_obj = self.auto_back_ward_obj
                    self.order_has = True
                except:
                    pass
        self.action_obj.auto_go()

    def forward_turn_back_ward_stop_function1(self):
        pass



    def auto_forward_stop_and_back1(self):
        pass


class manual_operation():
    pass


class warning():
    pass



class step():

    def __init__(self,box_pole_obj,machin_obj,box_prepare_obj):
        self.box_pole_obj = box_pole_obj
        self.machin_obj = machin_obj
        self.box_prepare_obj = box_prepare_obj

        self.pause = False

        self.step = [
                    [self.run_0, False, "wait_run"]
                    [self.run_1, False, "wait_run"],
                    [self.run_2, False, "wait_run"],
                    [self.run_3, False, "wait_run"],
                    [self.run_4, False, "wait_run"],
                    [self.run_5, False, "wait_run"],
                    [self.run_6, False, "wait_run"],
                    [self.run_7, False, "wait_run"]

        ]
        self.current_step = []

    def run_set(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],


    @contextlib.contextmanager
    def in_run(self,N):
        self.step[N][2] = "begin"
        self.current_step = step[N]
        yield self.step[N][0]()
        self.step[N][2] = "complete"

    def run(self):
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False,False, False, False, False, False, False):
            with self.in_run(0) as T0:
                 if T0 == True:
                    self.step[0][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,False, False, False, False, False, False):
            with self.in_run(1) as T:
                 if T == True:
                    self.step[1][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, False, False, False, False, False):
            with self.in_run(2) as T:
                if T == True:
                    self.step[2][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, False, False, False, False):
            with self.in_run(3) as T:
                if T == True:
                    self.step[3][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, True, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, True, True, False):
            with self.in_run(6) as T:
                if T == True:
                    self.step[6][1] = True
        if (self.step[0][1],self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True,True, True, True, True, True, True):
            with self.in_run(7) as T:
                if T == True:
                    self.step[7][1] = True
                    return  True

    def run_pause_stop(self,current_step,current_function):
        if self.step.index(self.current_step) == 0:
            pass
        if self.step.index(self.current_step) == 1:
            pass
        if self.step.index(self.current_step) == 2:
            pass

    def run_backward(self):
        if self.step.index(self.current_step) == 0:
            pass
        if self.step.index(self.current_step) == 1:
            pass
        if self.step.index(self.current_step) == 2:
            pass


    def run_1(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1,False,"wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_2(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_3(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_4(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_5(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_6(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_7(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],

    def run_0(self):
        self.step[0] = [self.run_0, False, "wait_run"],
        self.step[1] = [self.run_1, False, "wait_run"],
        self.step[2] = [self.run_2, False, "wait_run"],
        self.step[3] = [self.run_3, False, "wait_run"],
        self.step[4] = [self.run_4, False, "wait_run"],
        self.step[5] = [self.run_5, False, "wait_run"],
        self.step[6] = [self.run_6, False, "wait_run"],
        self.step[7] = [self.run_7, False, "wait_run"],


class step_1(step):     # let pole turn tight
    only = None
    def __new__(cls, *args, **kwargs):
        if step_1.only == None:
            step_1.only = super(step_1,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_1.only
    def run(self):
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(0) as T0:
                if T0 == True:
                    self.step[0][1] = True
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (True, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (True, True, False, False, False, False, False):
            with self.in_run(2) as T:
                if T == True:
                    self.step[2][1] = True
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(3) as T:
                if T == True:
                    self.step[3][1] = True
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (True, True, True, True, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
                    self.run_set()
                    return True

    def run_0(self):
        self.current_step[2] = "running"
        if self.machin_obj.main_beam.tiger_out_innertooth_bite_tight() == True:

            return True

    def run_1(self):
        self.current_step[2] = "running"
        if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:

            return True

    def run_2(self):
        self.current_step[2] = "running"
        if self.machin_obj.main_beam.move_and_clockwise() == True:
            return True

    def run_3(self):
        self.current_step[2] = "running"
        if self.machin_obj.main_beam.Equepment_pressure_torque.pressure > 3 :
            return True

    def run_4(self):
        self.current_step[2] = "running"
        if self.machin_obj.main_beam.move_stop(warterclose=False) == True:
            return True

class step_2(step):   ## dirll box hand back to unstop beam forward
    only = None
    def __new__(cls, *args, **kwargs):
        if step_2.only == None:
            step_2.only = super(step_2,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_2.only

    def run(self):
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(0) as T0:
                if T0 == True:
                    self.step[0][1] = True

    def run_0(self):
        self.current_step[2] = "running"
        if self.box_pole_obj.prepare_let_beam_forward() == True:
            return True

class step_3(step):     ## relax the outer and inner tooth
    only = None
    def __new__(cls, *args, **kwargs):
        if step_3.only == None:
            step_3.only = super(step_3,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_3.only

    def run(self):
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(0) as T0:
                if T0 == True:
                    self.step[0][1] = True
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (True, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True
                    return True

    def run_0(self):

        if self.machin_obj.main_beam.tiger_out_innertooth_relax() == True:
            return True

    def run_1(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
            return True

class step_4(step):    # pole forward to guide or  let the reamer forward
    only = None
    def __new__(cls, *args, **kwargs):
        if step_4.only == None:
            step_4.only = super(step_4,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_4.only

    def run(self):
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(0) as T0:
                if T0 == True:
                    self.step[0][1] = True
                    return True
    def run_1(self):
        if self.machin_obj.main_beam.beam_move_forward() == True:
            return True

class step_5(step):
    only = None
    def __new__(cls, *args, **kwargs):
        if step_5.only == None:
            step_5.only = super(step_5,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_5.only

    def run(self):
        if (self.step[0][1], self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1],
            self.step[6][1], self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(0) as T0:
                if T0 == True:
                    self.step[0][1] = True
                    return True
    def run_0(self):
        if self.machin_obj.main_beam.main_beam_move_stop(beam_come_last) == True:
            return True

class step_6(step):
    only = None
    def __new__(cls, *args, **kwargs):
        if step_6.only == None:
            step_6.only = super(step_6,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_6.only

    def run(self):
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True
            return True
    def run_1(self):
        if self.machin_obj.main_beam.main_beam_move_stop(beam_come_last) == True:
            return True


############################# to here




class step_7(step):
    def __init__(self,box_pole_obj,machin_obj,box_prepare_obj):
        super().__init__(self,box_pole_obj,machin_obj,box_prepare_obj)
        self.detect_tiger_pole_tight_angle = angle_speed_calclude()
        self.flag = False
    only = None
    def __new__(cls, *args, **kwargs):
        if step_7.only == None:
            step_7.only = super(step_7,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_7.only

    def run(self):
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                 if T == True:
                    self.step[1][1] = True
                    return True
    def run_1(self):
        if self.detect_tiger_pole_tight_angle.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle.beam_first_angle_time_ == None:
            self.detect_tiger_pole_tight_angle.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.flag == False:
            if self.machin_obj.main_beam.counterclockwise(pulllevel=4) == True:
                self.flag = True
        if self.flag == True:
            if self.detect_tiger_pole_tight_angle.rotate_number > 20:
                return True

class step_9(step):
    def __init__(self,box_pole_obj,machin_obj,box_prepare_obj):
        super().__init__(self,box_pole_obj,machin_obj,box_prepare_obj)
        self.detect_tiger_pole_tight_angle = angle_speed_calclude()
        self.flag = False
    only = None
    def __new__(cls, *args, **kwargs):
        if step_9.only == None:
            step_9.only = super(step_9,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_9.only

    def run(self):
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                 if T == True:
                    self.step[1][1] = True
                    return True
    def run_1(self):
        if self.machin_obj.main_beam.main_beam_move_stop(beam_taile_5cm) == True:
            return True

class   step_10(step):


    def __init__(self,box_pole_obj,machin_obj,box_prepare_obj):
        super().__init__(self,box_pole_obj,machin_obj,box_prepare_obj)
        self.pole_drill_to_next_pole_pressure = max_pressure()

    only = None
    def __new__(cls, *args, **kwargs):
        if step_10.only == None:
            step_10.only = super(step_10,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_10.only

    @contextlib.contextmanager
    def in_run(self, N):
        self.step[N][2] = "begin"
        self.current_step = step[N]
        yield self.step[N][0]()
        self.step[N][2] = "complete"
    def run(self):
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                 if T == True:
                    self.step[1][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, False, False, False, False, False, False):
            with self.in_run(2) as T:
                if T == True:
                    self.step[2][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, False, False, False, False, False):
            with self.in_run(3) as T:
                if T == True:
                    self.step[3][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, True, True, False, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, True, True, True, False, False):
            with self.in_run(6) as T:
                if T == True:
                    self.step[6][1] = True
                    self.run_set()
                    return True
    def run_1(self):
        if self.box_prepare_obj.prepare_pole_out() == True:
            return True
    def run_2(self):
        if self.box_prepare_obj.prepare_to_reach_beam_with_pole() == True:
            self.pole_drill_to_next_pole_pressure.current_pressure = self.machin_obj.main_beam.Equepment_pressure_torque.pressure
            self.pole_drill_to_next_pole_pressure.max_pressure_()
            return True
    def run_3(self):
        self.pole_drill_to_next_pole_pressure.current_pressure = self.machin_obj.main_beam.Equepment_pressure_torque.pressure
        self.pole_drill_to_next_pole_pressure.max_pressure_()
        if self.machin_obj.main_beam.move_and_clockwise() == True:
            return True
    def run_4(self):
        self.pole_drill_to_next_pole_pressure.current_pressure = self.machin_obj.main_beam.Equepment_pressure_torque.pressure
        self.pole_drill_to_next_pole_pressure.max_pressure_()
        if self.pole_drill_to_next_pole_pressure.max_pressure__ > 4:
            self.pole_drill_to_next_pole_pressure.max_pressure__ = 0
            return True
    def run_5(self):
        if self.machin_obj.main_beam.move_stop(warterclose=False) == True:
            return True
    def run_6(self):
        if self.box_pole_obj.box_in_pole() == True:
            return True

class step_11(step):
    only = None
    def __new__(cls, *args, **kwargs):
        if step_11.only == None:
            step_11.only = super(step_11,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_11.only

    def run(self):
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True
            return True
    def run_1(self):
        if self.machin_obj.main_beam.main_beam_move_stop(man_give_pole_place) == True:
            return True


class step_12(step):
    only = None
    def __new__(cls, *args, **kwargs):
        if step_12.only == None:
            step_12.only = super(step_12,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_12.only

    def run(self, order):
        if order == "go":
            return True
        else:
            if order== "back":
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

                if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
                self.step[7][1]) == (True, True, True, False, False, False, False):
                    with self.in_run(4) as T:
                        if T == True:
                            self.step[4][1] = True
                            return True

    def run_1(self,order):
        if self.pole_out_manual_order == "back":
            return True
    def run_2(self):
        if self.machin_obj.main_beam.move_and_clockwise(derection="back") == True:
            return True
    def run_3(self):
        if abs(self.machin_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - (
                pole_in_middle_tiger_tooth - 20)) < 15:
            return True
    def run_4(self):
        if self.machin_obj.main_beam.move_stop() == True:
            return True



class step_13(step):
    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):

        super().__init__(self, box_pole_obj, machin_obj, box_prepare_obj)
        self.pole_drill_to_next_pole_pressure = max_pressure()
    only = None
    def __new__(cls, *args, **kwargs):
        if step_13.only == None:
            step_13.only = super(step_13,cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return step_13.only

    def run(self,order):
        if order == "back":
            return True
        else:
            if order == "go":
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
        if self.order == "go":
            return True
    def run_2(self):
        if self.machin_obj.main_beam.move_and_clockwise() == True:
            return True
    def run_3(self):
        if self.pole_drill_to_next_pole_pressure.pre_pressure == 0:
            self.pole_drill_to_next_pole_pressure.pre_pressure = self.machin_obj.main_beam.Equepment_pressure_torque.pressure
        self.pole_drill_to_next_pole_pressure.current_pressure = self.machin_obj.main_beam.Equepment_pressure_torque.pressure
        self.detect_tiger_pole_tight_max_pressure.max_pressure_()
        if self.pole_drill_to_next_pole_pressure.max_pressure__ > 4:
            self.pole_drill_to_next_pole_pressure.max_pressure__ = 0
            return True



class back_step1(step):
    only = None

    def __new__(cls, *args, **kwargs):
        if back_step1.only == None:
            back_step1.only = super(back_step1, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step1.only

    def run(self):
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True

                    return True

    def run_1(self):
        if self.box_pole_obj.prepare_let_beam_forward() == True:
            return True

    def run_2(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_relax() == True:
            return True

    def run_3(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
            return True

    def run_4(self):
        if self.machin_obj.main_beam.auto_rotate_pull() == True:
            return True
    def run_5(self):  # this used to protect the beam spring
        if self.machin_obj.main_beam.main_beam_move_stop(pole_in_middle_tiger_tooth_to_taile_tofaward) == True:
            return True

class back_step5(step):
    only = None
    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):
        super().__init__(self, box_pole_obj, machin_obj, box_prepare_obj)
        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()
        self.step = [
            [self.run_1, True, "wait_run"],
            [self.run_2, False, "wait_run"],
            [self.run_3, False, "wait_run"],
            [self.run_4, False, "wait_run"],
            [self.run_5, False, "wait_run"],
            [self.run_6, False, "wait_run"],
            [self.run_7, False, "wait_run"]
        ]
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False


    def __new__(cls, *args, **kwargs):
        if back_step5.only == None:
            back_step5.only = super(back_step5, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step5.only

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
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, False, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, True, False, False):
            with self.in_run(6) as T:
                if T == True:
                    self.step[6][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, True, True, False):
            with self.in_run(7) as T:
                if T == True:
                    self.step[7][1] = True
                    return True



    def run_1(self):
        if (self.flag1,self.flag2,self.flag3,self.flag4) == (False,False,False,False):
            if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
                self.flag1 = True
        if (self.flag1, self.flag2, self.flag3, self.flag4) == (True, False, False, False):
            if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
                self.flag2 = True
        if (self.flag1, self.flag2, self.flag3, self.flag4) == (True, True, False, False):
            if self.machin_obj.main_beam.main_beam_move_stop(pole_in_middle_tiger_tooth_to_taile_tofaward) == True:
                self.flag3 = True
        if self.machin_obj.main_beam.tiger_loose_pole(order_="tight_or_back") == True:
                self.flag1 = False
                self.flag2 = False
                self.flag3 = False
                self.flag4 = False
                return  True

    def run_2(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_bite_tight() == True:
            return True

    def run_3(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_bite_tight(tiger_name="inner") == True:
            return True

    def run_4(self):
        if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        return True
    def run_5(self):
        self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.machin_obj.main_beam.tiger_loose_pole() == True:
                if  self.detect_tiger_pole_tight_angle2.rotate_number * 360 > tiger_tooth_loose_pole_thread_angle:
                    return True
                else:
                    self.step[0][1] = False
                    self.step[1][1] = False
                    self.step[2][1] = False
                    self.step[3][1] = False
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
                    self.detect_tiger_pole_tight_angle2.beam_first_angle = None
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None

    def run_6(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
            return True

    def run_7(self):
        def run_1(self):
            if self.machin_obj.main_beam.tiger_loose_pole(order_="tight_or_back") == True:
                return True





##  class 8 9 10,11  merged together


class back_step8(step):
    only = None

    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):
        super().__init__(self, box_pole_obj, machin_obj, box_prepare_obj)
        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()

    def __new__(cls, *args, **kwargs):
        if back_step8.only == None:
            back_step8.only = super(back_step8, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step8.only

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
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, False, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
                    return  True

    def run_1(self):
        if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        return True


    def run_2(self):
            self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
            if self.machin_obj.main_beam.counterclockwise(pulllevel=2) == True:
                return True

    def run_3(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.detect_tiger_pole_tight_angle2.rotate_number > pole_thread_full_out2:
            self.detect_tiger_pole_tight_angle2.rotate_number = 0
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
            self.detect_tiger_pole_tight_angle2.beam_first_angle = None
            self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None
            return True

    def run_4(self):
        if self.machin_obj.main_beam.move_() == True:
            return True
    def run_5(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_bite_tight(tiger_name="inner") == True:
            return True





class back_step10auto1(step):
    only = None

    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):
        super().__init__(self, box_pole_obj, machin_obj, box_prepare_obj)
        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()
        self.detect_tiger_pole_tight_max_pressure = max_pressure()
        self.run_5_begin = 0
        self.run_5_delta_time = 0

        self.run_8_flag1 = False
        self.run_8_flag2 = False
        self.run_8_flag3 = False

        self.run_6_flag = False

    def __new__(cls, *args, **kwargs):
        if back_step10.only == None:
            back_step10.only = super(back_step10, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step10.only

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
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, False, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
                    return True

    def run_1(self):
        if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        return True

    def run_2(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=True) == True:
            return True

    def run_3(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.detect_tiger_pole_tight_angle2.rotate_number > 0.5:
            return True

    def run_4(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=False) == True:

            return True

    def run_5(self):
        if self.run_5_begin == 0:
            self.run_5_begin = time.time()
        self.run_5_delta_time = time.time() - self.run_5_begin
        if self.box_prepare_obj.prepare_to_reach_beam_without_pole() == True:
            return True
        if self.run_5_delta_time > 3 :
            if abs(self.machin_obj.Equepment_line_distance_measure_1m_drill_box.coordinate - box_to_beam_can_grap) < 15:
                self.run_pause_stop()

    def run_6(self):

        if self.run_6_flag == False:
            if self.box_prepare_obj.prepare_in_grap_slight() == True:
                self.run_6_flag = True
        if self.run_6_flag == True:
            if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:
                self.run_6_flag = False
                return True
    def run_7(self):
        if self.machin_obj.main_beam.main_beam_move_stop(beam_can_out_all_thread_pole) == True:
            return True

    def run_8(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if (self.run_8_flag1,self.run_8_flag2,self.run_8_flag3) == (False,False,False):
            if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=True) == True:
                self.run_8_flag1 = True
        if (self.run_8_flag1, self.run_8_flag2, self.run_8_flag3) == (True, False, False):
            if self.box_prepare_obj.prepare_in_grap_hold_tight() == True:
                    self.run_8_flag2 = True
        if (self.run_8_flag1, self.run_8_flag2, self.run_8_flag3) == (True, True, False):
            if self.detect_tiger_pole_tight_angle2.rotate_number > 20:
                self.run_8_flag3 = True
        if (self.run_8_flag1, self.run_8_flag2, self.run_8_flag3) == (True, True, False):
            if self.machin_obj.main_beam.main_beam_move_stop(beam_taile_5cm) == True:
                self.run_8_flag1 = False
                self.run_8_flag2 = False
                self.run_8_flag3 = False
                return True
                # self.box_pole_obj.other_in_pole()
                # return True
    def run_pause_stop(self):
        if self.pause == False:
            self.pause = True
        if self.step.index(self.current_step) == 4:
            self.box_prepare_obj.reach_start_prepare()
            if self.pause == False:
                return True
        if self.step.index(self.current_step) == 5:
            self.box_prepare_obj.reach_start_prepare()
            if self.pause == False:
                return True
        if self.step.index(self.current_step) == 2:
            pass


class back_step10auto2(step):
    only = None

    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):
        super().__init__(self, box_pole_obj, machin_obj, box_prepare_obj)

    def __new__(cls, *args, **kwargs):
        if back_step10auto2.only == None:
            back_step10auto2.only = super(back_step10auto2, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step10auto2.only
    def run(self):
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True

    def run_1(self):
        self.box_prepare_obj.pole_in()



class back_step11(step):
    only = None

    def __new__(cls, *args, **kwargs):
        if back_step11.only == None:
            back_step11.only = super(back_step11, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step11.only

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
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, False, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
                    return True

    def run_1(self):
        if self.manual_order_can_go_to_in_hole_to_next == "go":
            return True

    def run_2(self):
        if self.machin_obj.main_beam.main_beam_move_stop(beam_come_last - 200, pull_level=5) == True:
            return True

    def run_3(self):
        if self.machin_obj.main_beam.move_and_clockwise_slight(on=True) == True:
            return True

    def run_4(self):
        if self.machin_obj.main_beam.Equepment_pressure_torque.pressure > 2:
            return True

    def run_5(self):
        if self.machin_obj.main_beam.move_and_clockwise_slight(on=False) == True:
            return True


class back_step12(step):
    only = None

    def __init__(self, box_pole_obj, machin_obj, box_prepare_obj):
        super().__init__(self, box_pole_obj, machin_obj, box_prepare_obj)
        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()
        self.detect_tiger_pole_tight_max_pressure = max_pressure()

    def __new__(cls, *args, **kwargs):
        if back_step12.only == None:
            back_step12.only = super(back_step12, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step12.only

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
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, False, False, False):
            with self.in_run(5) as T:
                if T == True:
                    self.step[5][1] = True
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (True, True, True, True, True, False, False):
            with self.in_run(6) as T:
                if T == True:
                    self.step[6][1] = True
                    return True

    def run_1(self):
        if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        return True

    def run_2(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=True) == True:
            return True

    def run_3(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(derection="counter_clocwise")
        if self.detect_tiger_pole_tight_angle2.rotate_number*360 > tiger_tooth_loose_pole_thread_angle*2:
            return True
    def run_4(self):
        if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=False) == True:
            self.detect_tiger_pole_tight_angle2.rotate_number = 0
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
            self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None
            return True
    def run_5(self):
        if self.machin_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") == True:

            return True

    def run_6(self):
        if self.machin_obj.main_beam.main_beam_move_stop(beam_taile_5cm) == True:
            return True

class back_step13(step):
    only = None
    def __init__(self,box_pole_obj,machin_obj,box_prepare_obj):
        super().__init__(self,box_pole_obj,machin_obj,box_prepare_obj)
        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()
        self.detect_tiger_pole_tight_max_pressure = max_pressure()

    def __new__(cls, *args, **kwargs):
        if back_step13.only == None:
            back_step13.only = super(back_step13, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step13.only

    def run(self):
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                 if T == True:
                    self.step[1][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, False, False, False, False, False, False):
            with self.in_run(2) as T:
                if T == True:
                    self.step[2][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, False, False, False, False, False):
            with self.in_run(3) as T:
                if T == True:
                    self.step[3][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
                    return True

    def run_1(self):
        if self.machin_obj.main_beam.main_beam_move_stop(
                pole_pull_back_can_out_box_hand_to_grap) == True:  # here need a paramete of stop coordinate
            if self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update == None or \
                    self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ == None:
                self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
                self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
            self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(
                derection="counter_clocwise")
            return True
    def run_2(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(
            derection="counter_clocwise")
        if self.machin_obj.main_beam.counterclockwise(pulllevel=2, on=True) == True:
            return True
    def run_3(self):
        self.detect_tiger_pole_tight_angle2.current_angle = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.detect_tiger_pole_tight_angle2.current_time = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.time_
        self.detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(
            derection="counter_clocwise")
        if self.detect_tiger_pole_tight_angle2.rotate_number > pole_thread_full_out2:
            return True

    def run_4(self):
        if self.machin_obj.main_beam.counterclockwise(pulllevel=4, on=False) == True:
            self.detect_tiger_pole_tight_angle2.rotate_number = 0
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
            self.detect_tiger_pole_tight_angle2.beam_first_angle_not_update = None
            self.detect_tiger_pole_tight_angle2.beam_first_angle_time_ = None
            return True


class back_step14(step):
    only = None
    def __init__(self,box_pole_obj,machin_obj,box_prepare_obj):
        super().__init__(self,box_pole_obj,machin_obj,box_prepare_obj)
        self.detect_tiger_pole_tight_angle2 = angle_speed_calclude()
        self.detect_tiger_pole_tight_max_pressure = max_pressure()

    def __new__(cls, *args, **kwargs):
        if back_step14.only == None:
            back_step14.only = super(back_step14, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step14.only

    def run(self):
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                 if T == True:
                    self.step[1][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, False, False, False, False, False, False):
            with self.in_run(2) as T:
                if T == True:
                    self.step[2][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, False, False, False, False, False):
            with self.in_run(3) as T:
                if T == True:
                    self.step[3][1] = True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, True, False, False, False, False):
            with self.in_run(4) as T:
                if T == True:
                    self.step[4][1] = True
                    return True

    def run_1(self):
        if self.box_pole_obj.pole_in() == True:
            return True

    def run_2(self):
        if self.machin_obj.main_beam.main_beam_move_stop(beam_come_last - 80) == True:
            return True

    def run_3(self):
        if self.machin_obj.main_beam.move_and_clockwise_slight(on=True) == True:
            return True

    def run_4(self):
        if self.machin_obj.main_beam.Equepment_pressure_torque.pressure > 3 and self.machin_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate > beam_come_last:
            return True


class back_step15(step):
    only = None

    def __new__(cls, *args, **kwargs):
        if back_step15.only == None:
            back_step15.only = super(back_step15, cls).__new__(cls, *args, **kwargs)
        else:
            pass
        return back_step15.only

    def run(self):
        if (self.step[1][1], self.step[2][1], self.step[3][1], self.step[4][1], self.step[5][1], self.step[6][1],
            self.step[7][1]) == (False, False, False, False, False, False, False):
            with self.in_run(1) as T:
                if T == True:
                    self.step[1][1] = True
                    return True

    def run_1(self):
        if self.machin_obj.main_beam.auto_rotate_pull() == True:
            return True