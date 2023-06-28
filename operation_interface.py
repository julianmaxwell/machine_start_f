import inspect
import time
from abc import ABC,abstractmethod,ABCMeta
from functools import partial
import contextlib
import order
from machine_high_lever_equepment import angle_speed_calclude, max_pressure


from 主表 import *





class step_(ABC):

    def __init__(self, order_name_, operator_all_name_obj_dict, obj=None, parent=None, child_index=0, leader=None,
                 ProcessSendOrderToWindowPipe=None):
        self.ProcessSendOrderToWindowPipe = ProcessSendOrderToWindowPipe
        self.obj = obj
        self.obj_result = False
        self.order = None
        self.parent = parent
        self.order_name_ = order_name_
        self.childs_step = []
        self.childs_step_dict = {}
        self.init_for_loop_clect =set()
        self.leader_name_obj_dict = {}
        self.operator_all_name_obj_dict = operator_all_name_obj_dict
        self.regist_step(operator_all_name_obj_dict, parent=parent, leader=leader)
        self.child_index = child_index
        self.over = None
        self.loop = False
        self.loop_times = 0
        self.loop_max_times = None
        self.will_run_step_obj = None
        self.run_time_delta = None
        self.run_begin_time = None

        if len(self.childs_step) == 0:
            self.will_run_step_obj = self
        else:
            if self.obj == None:
                self.will_run_step_obj = self.childs_step[self.child_index]
            else:
                self.will_run_step_obj = self


    def regist_step(self,operator_all_name_obj_dict,parent,leader=None):
            self.parent = parent
            self.operator_all_name_obj_dict[self.order_name_] = self
            if self.parent != None:

                self.parent.childs_step.append(self)
            if leader != None:
                self.leader_name_obj_dict[self.order_name_] = self
            if leader != None:
                if len(self.childs_step) > 0:
                    leader.init_for_loop_clect.union(self.childs_step)



    def run(self,*args):
        """"
                follow gray remarks is used to change the self.over . check the next step judge are right.it should be delete
        but for check late  i reserved it .
        if self.order_name_ in ["drill_box_unstop_beam_move",
                              "beam_male_thread_into_the_pole_mather_thread_back_taile_5cm",
                              "drill_box_send_pole",
                              "beam_move_and_clockwise_slight",
                              "beam_move_and_clockwise_slight_intohole",
                              ]:
            self.over = True

        """
        time.sleep(2)
        if self.over != True:
            if len(self.childs_step) > 0:
                # print("opera_run正在运行任务名称_ 有子任务： ",
                #       len(self.operator_all_name_obj_dict[self.order_name_].childs_step), "个")
                # print(self.operator_all_name_obj_dict[self.order_name_].childs_step)
                # print(self.childs_step[self.child_index].order_name_, ":  is the next will run function")
                print("opera_run : 正在运行任务名称{name},有子任务：{count}个，详细名称{detaile_name} ".format(
                    name=self.order_name_, count=len(self.operator_all_name_obj_dict[self.order_name_].childs_step),
                    detaile_name=list(map(lambda x: x.order_name_, self.operator_all_name_obj_dict[self.order_name_].childs_step))
                ))

            else:
                print("opera_run : 正在运行任务名称_无子任务： ", self.operator_all_name_obj_dict[self.order_name_].order_name_,
                      self.operator_all_name_obj_dict[self.order_name_])
            time.sleep(5)

            if self.run_begin_time == None:
                self.run_begin_time = time.time()

            if self.obj != None:
                try:
                    # print("opera_run运行的具体动作return value is : ", self.obj_result, "  ", self.obj)
                    print("opera_run : 本次will run obj 运行的 obj 返回结果是 {result},obj instance is {instance} ".format(
                        result=self.obj_result, instance=self.obj
                    ))
                    self.obj_result = self.obj()

                    # time.sleep(10)

                except :
                    self.obj_result = None
                finally:
                    if self.obj_result is True:
                        if len(self.childs_step) > 0:
                            self.will_run_step_obj = self.set_next_step()
                            print(self.will_run_step_obj, "11111111111111111111111111111")
                        else:
                            self.over = True
                    elif  self.obj_result == False:
                        self.over = False
                        self.will_run_step_obj = self
                    elif  self.obj_result == None:
                        print("return the current step, because the self.obj return None , self step name is :",
                              self.order_name_)

                        self.will_run_step_obj = self

            else:

                print("opera_run :im {order_name_},i current received parameter from order_run(parameter) is {parameter} "
                      ". now current order is over. my childes step number is {number}".format(
                      order_name_=self.will_run_step_obj.order_name_, parameter=args, number=len(self.childs_step)
                      ))
                self.will_run_step_obj = self.set_next_step()
            self.run_time_delta = time.time() - self.run_begin_time
            print("opera_run : 下一个任务名称是{name}，本次任务已经运行时间是{time_1}秒".format(name=self.will_run_step_obj.order_name_,
                                                                                  time_1=self.run_time_delta))
            return self.will_run_step_obj

        else:
            xx = self.will_run_step_obj.set_next_step()
            print("opera_run :  self.over == True and the next will run setp is : ", xx.order_name_)

            return xx


    def set_next_step(self,next_step = None):
        # here not analysis the self.over , for test the funtion work order . untill the real work begin ,
        # must add the funtion  if self.over == True       if self.over == False   next self.will_run_obj = .......

                len_childs = len(self.will_run_step_obj.childs_step)
                if len_childs > 0:
                    print("opera_run : I'm in the will_run,i'm running ,now i begin return my next step from {child} ".format(
                        child=list(map(lambda x: x.order_name_, self.will_run_step_obj.childs_step))
                    ))
                else:
                    print("opera_run : {order_name_} has no child ,later will run it's younger brother".format(
                        order_name_=self.will_run_step_obj.order_name_
                    ))
                if self.over is None or self.over is True:


                    if len(self.will_run_step_obj.childs_step) > 0:
                        self.will_run_step_obj = self.childs_step[self.child_index]
                    else:
                        if self.parent != None:
                            try:
                                self.will_run_step_obj = self.parent.childs_step[self.parent.childs_step.index(self) + 1]

                            except IndexError:

                                if self.parent.loop != True:
                                    self.parent.over = True
                                    self.will_run_step_obj = self.will_run_step_obj.parent.set_next_step()
                                else:
                                    self.init_for_loop()
                                    self.will_run_step_obj = self.parent.childs_step[0]
                    print("opera_run :  in current loop, i return will run obj is {order_name_} ".format(
                        order_name_=self.will_run_step_obj.order_name_))
                    return self.will_run_step_obj

                elif self.over == False:
                    pass

    def init_for_loop(self):

        for every in self.init_for_loop_clect:
            every.over = False
            every.obj_result = False
            every.will_run_step_obj = None

import boxpole_equepment
import abs_task_step
import machine_high_lever_equepment

class operator():
    # every manual action's  man operation flag parameter  is in the function for the action . so you check easy

    def __init__(self):

        self.machine_obj = machine_high_lever_equepment.machine()
        self.box_prepare_obj = boxpole_equepment.box_prepare(self.machine_obj)
        self.processSendToCommunicationPipe = None
        self.ProcessSendOrderToWindowPipe = None

        self.action_ = None
        self.order = None
        self.step_begin_time = None
        self.all_name_obj_dict = {}
        self.will_run_obj = None
        self.operator_man_order = False
        self.set_step()

        self.run_flag = False

        self.loose_pole_and_check_True_flag1 = False
        self.loose_pole_and_check_True_flag2 = False
        self.loose_pole_and_check_True_flag3 = False
        self.loose_pole_and_check_True_flag4 = False
        self.loose_pole_and_check_True_man_help = False
        self.loose_pole_and_check_True_move_stop_flag = False
        self.receve_order_name = None



    def init_parameter(self,  r_cve, s_end):
        self.processSendToCommunicationPipe = s_end
        self.ProcessSendOrderToWindowPipe = s_end


    def set_step(self):
        self.tools_ddetect_tiger_pole_tight_angle = angle_speed_calclude()
        self.tools_detect_tiger_pole_tight_angle2 = angle_speed_calclude()
        self.tools_detect_tiger_pole_tight_angle3 = angle_speed_calclude()
        self.toolsdetect_tiger_pole_tight_max_pressure = max_pressure()
        self.tools_speed_calclude = order.speed_calclude()
        self.tools_speed_calclude1 = order.speed_calclude()
        self.tools_speed_calclude2 = order.speed_calclude()

        self.auto_rotate_forward()

        self.manual_rotate_forward()

        self.auto_rotate_backward()

        self.manual_rotate_back_ward()

        self.operator_top_pause_stop = step_("operator_top_pause_stop", self.all_name_obj_dict, None)


# followed code is the    "operator_top_forward_auto" order  begin


    def manual_rotate_back_ward(self):

        # machine statues   there is no pole on beam . and the tiger tooth has a pole
        self.manual_back_operator_backward_manual_over_flag = True


        tiger_inner_tooth_bitte_tight = partial(self.machine_obj.main_beam.tiger_out_innertooth_bite_tight,
                                                tiger_name="inner")

        # every attribute name add string "manual_back_" include it new name  and deleted the word "auto"
        self.manual_back_operator_top_backward_ = step_(
            "manual_back_operator_top_backward_",
            self.all_name_obj_dict,
            None)
        # manual_back_operator_top_backward_ step3 .1
        run_to_the_point_pole_in_middle_tiger_tooth_tiger_back = \
            partial(self.machine_obj.main_beam.speed_contrl,
                    self.machine_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback)
        self.manual_back_come_to_the_point_pole_in_middle_tiger_tooth_tiger_back = step_(
            "manual_back_come_to_the_point_pole_in_middle_tiger_tooth_tiger_back",
            self.all_name_obj_dict,
            obj=run_to_the_point_pole_in_middle_tiger_tooth_tiger_back,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .2

        self.manual_back_BeamMaleThreadIntoPoleAtTigerMatherThread = step_(
            "manual_back_BeamMaleThreadIntoPoleAtTigerMatherThread",
            self.all_name_obj_dict,
            obj=self.drill_box_move_unstop,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .3

        self.manual_back_operator_top_backward_relax_outter_tiger_tooth = step_(
            "manual_back_operator_top_backward_relax_outter_tiger_tooth",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.tiger_out_innertooth_relax,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .4

        self.manual_back_manual_back_operator_top_backward__pull_back_pole = step_(
            "manual_back_manual_back_operator_top_backward__pull_back_pole",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.auto_rotate_pull,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .5

        self.manual_back_tiger_outer_bitte_tight = step_(
            "manual_back_tiger_outer_bitte_tight",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .6

        tiger_inner_tooth_bitte_tight = partial(self.machine_obj.main_beam.tiger_out_innertooth_bite_tight,
                                                tiger_name="inner")
        self.manual_back_tiger_inner_bitte_tight = step_(
            "manual_back_tiger_inner_bitte_tight",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .7

        self.manual_back_loose_pole_and_checke_True = step_(
            "manual_back_loose_pole_and_checke_True",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.tiger_loose_pole,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .8

        tiger_loose_back = partial(self.machine_obj.main_beam.tiger_loose_pole, order_="tight_or_back")
        self.manual_back_tiger_loose_back_init = step_(
           "manual_back_tiger_loose_back_init",
           self.all_name_obj_dict,
           obj=tiger_loose_back,
           parent=self.manual_back_operator_top_backward_,
           leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .9

        self.manual_back_drill_out_male_thread_in_tiger = step_(
            "manual_back_drill_out_male_thread_in_tiger",
            self.all_name_obj_dict,
            obj=self.drill_out_male_thread_in_tiger,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .10

        self.manual_back_bite_tight_inner_tooth = step_(
            "manual_back_bite_tight_inner_tooth",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .11
        self.manual_back_drill_loose_pole_taile_mother_thread = step_(
            "manual_back_drill_loose_pole_taile_mother_thread",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .12
        relax_inner_tiger_tooth = partial(self.machine_obj.main_beam.tiger_out_innertooth_relax, tiger_name="inner")
        self.manual_back_operator_top_backward_relax_inner_tiger_tooth = step_(
            "manual_back_operator_top_backward_relax_inner_tiger_tooth",
            self.all_name_obj_dict,
            obj=relax_inner_tiger_tooth,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .13
        self.manual_back_operator_top_backward_hand_grap_reach_can_relax_hand_and_relax = step_(
            "manual_back_operator_top_backward_hand_grap_reach_can_relax_hand_and_relax",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.reach_start_prepare,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .14
        self.manual_back_operator_top_backward_hand_grap_reach_beam = step_(
            "manual_back_operator_top_backward_hand_grap_reach_beam",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.prepare_to_reach_beam_with_pole,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .15
        self.manual_back_operator_top_backward_hand_grap_tight = step_(
            "manual_back_operator_top_backward_hand_grap_tight",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.prepare_in_grap_hold_tight,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .16
        move_can_drill_out_the_pole_mather_thread = partial(self.machine_obj.main_beam.speed_contrl,
                                                            self.machine_obj.main_beam.pole_mather_thread_on_beam_can_counter_drill_out)
        self.manual_back_operator_backward_beam_move_to_loose_out_the_mother_thread_point = step_(
            "manual_back_operator_backward_beam_move_to_loose_out_the_mother_thread_point",
            self.all_name_obj_dict,
            obj=move_can_drill_out_the_pole_mather_thread,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .17
        self.manual_back_operator_backward_loose_out_the_mother_thread_point = step_(
            "manual_back_operator_backward_loose_out_the_mother_thread_point",
            self.all_name_obj_dict,
            obj=self.operator_backward_auto__loose_out_the_mother_thread_point_,
            parent=self.manual_back_operator_top_backward_,
            leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .18

        self.manual_back_operator_backward_come_back_the_beam_taile_5cm = \
            step_("manual_forward_forward_end_come_back_the_beam_taile_5cm",
                  self.all_name_obj_dict,
                  obj=self.move_no_load,
                  parent=self.manual_back_operator_top_backward_,
                  leader=self.manual_back_operator_top_backward_)

        # manual_back_operator_top_backward_ step3 .19
        # the beam separated with pole  and the pole now is on the drill box relax hand .
        self.manual_back_operator_backward_manual_over = \
            step_("manual_back_operator_backward_manual_over",
                  self.all_name_obj_dict,
                  obj=self.manual_back_operator_backward_manual_over_,
                  parent=self.manual_back_operator_top_backward_,
                  leader=self.manual_back_operator_top_backward_)
        # manual_back_operator_top_backward_ step3 .19
        # it's all over in this loop


    def manual_back_operator_backward_manual_over_(self):
        if self.manual_back_operator_backward_manual_over_flag == True:
            return True

    def manual_rotate_forward(self):
        self.manual_rotate_forward_man_prepared_over = False
        self.move_forward_30cm_rotate_clockwise_sucess = False
        self.mannual_rotate_forward_back_pole_in_tiger_prepared_over_order = False
        # up is parameter  control period need .in follow instance.2.0


        self.manual_rotate_forward_manual = step_("operator_top_forward_manual", self.all_name_obj_dict, None)


        self.manual_rotate_forward_drill_box_move_unstop = partial(self.machine_obj.drill_box.hand_run,
                            self.machine_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate)
        self.manual_rotate_forward_drill_box_unstop_beam_move = step_(
            "manual_rotate_forward_drill_box_unstop_beam_move",
            self.all_name_obj_dict,
            obj=self.drill_box_move_unstop,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2.1 .

        self.manual_rotate_forward_move_man_can_get_pole = partial(
            self.machine_obj.main_beam.no_load_move_to_coordinnate_point, self.machine_obj.main_beam.man_give_pole_place)

        self.manual_rotate_forward_move_manual_rotate_forward_move_man_can_get_pole = step_(
            "manual_rotate_forward_move_manual_rotate_forward_move_man_can_get_pole",
            self.all_name_obj_dict,
            obj=self.manual_rotate_forward_move_man_can_get_pole,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2.2

        self.move_forward_30cm_rotate_clockwise_ = step_(
            "move_forward_30cm_rotate_clockwise_",
            self.all_name_obj_dict,
            obj=self.move_forward_30cm_rotate_clockwise,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .3
        self.move_backward_let_pole_in_tiger = partial(
            self.machine_obj.main_beam.speed_contrl, self.machine_obj.main_beam.man_give_pole_place_back_last_point
        )
        self.move_back_ward_let_the_male_thread_in_tiger_ = step_(
            "move_forward_let_the_male_thread_in_tiger_",
            self.all_name_obj_dict,
            obj=self.move_backward_let_pole_in_tiger,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .4
        self.pole_is_in_place_forward_please = step_(
            "pole_is_in_place_forward_please",
            self.all_name_obj_dict,
            obj=self.mannual_rotate_forward_back_pole_in_tiger_prepared_over,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .5

        # next every add string "manual_forward_"  in place of "auto_rotate_backward" action

        self.manual_forward_beam_move_and_clockwise_slight_intohole = beam_move_and_clockwise_slight_intohole_(
            "manual_forward_beam_move_and_clockwise_slight_intohole",
            self.all_name_obj_dict,
            self.machine_obj,
            obj=self.machine_obj.main_beam.move_and_clockwise_slight,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual,
            ProcessSendOrderToWindowPipe=self.ProcessSendOrderToWindowPipe)
        # manual_rotate_forward_manual step2 .6
        self.manual_forward_first_point_coordinate = first_point_coordinate_(
            "manual_forward_first_point_coordinate", self.all_name_obj_dict, self.machine_obj, obj=None,
            parent=self.beam_move_and_clockwise_slight_intohole, leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.1  beam hydrauly driver power header normal reach point 1
        # both taile and head thread of the pole is wrong .

        self.manual_forward_box_hand_lose_pole = box_hand_lose_pole_(
            "manual_forward_box_hand_lose_pole", self.all_name_obj_dict, self.machine_obj,
            obj=self.machine_obj.main_beam.move_and_clockwise_slight,
            parent=self.beam_move_and_clockwise_slight_intohole, leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.2  box hand grap lose pole in beam hydrauly driver power header reach point 1
        #     , order_name_, machine_obj, obj = None, parent = None, child_index = 0, leader = None
        self.manual_forward_first_point_coordinate_functon1 = step_(
            "manual_forward_first_point_coordinate_functon1",
            self.all_name_obj_dict,
            obj=self.move_back_tiger_ruler_tuch_motion_point,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.3  beam hydrauly driver power header normal reach point 1
        self.manual_forward_first_point_coordinate_functon2 = step_(
            "manual_forward_first_point_coordinate_functon2",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.only_clockwise_rotate_pole_into_hole,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.4  beam hydrauly driver power header normal reach point 2
        self.manual_forward_first_point_coordinate_functon3 = relax_strong_or_slight_(
            "manual_forward_first_point_coordinate_functon3",
            self.all_name_obj_dict, self.machine_obj,
            obj=self.machine_obj.drill_box.Equepment_drill_box_digit_piont.hand_grap_relax_half_time,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.5  beam hydrauly driver power header normal reach point 3
        self.manual_forward_first_point_coordinate_funtion4 = step_(
            "first_point_coordinate_funtion4",
            self.all_name_obj_dict,
            obj=self.only_move_step,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.6 beam hydrauly driver power header normal reach point 4
        self.manual_forward_first_point_coordinate_funtion5 = step_(
            "manual_forward_first_point_coordinate_funtion5",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.only_stop_push_pull,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.7 beam hydrauly driver power header normal reach point 5
        self.manual_forward_first_point_coordinate_funtion6 = step_(
            "manual_forward_first_point_coordinate_funtion6",
            self.all_name_obj_dict,
            obj=self.grap_hand_grap_strong,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.8  beam hydrauly driver power header normal reach point 6
        self.manual_forward_first_point_coordinate_funtion7 = step_(
            "manual_forward_first_point_coordinate_funtion7",
            self.all_name_obj_dict,
            obj=self.wait_delta_time,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .6.9  beam hydrauly driver power header normal reach point 7
        self.manual_forward_first_point_coordinate_analysis = first_point_coordinate_analysis_(
            "manual_forward_first_point_coordinate_analysis",
            self.all_name_obj_dict,
            self.machine_obj, obj=None,
            parent=self.first_point_coordinate,
            leader=self.manual_rotate_forward_manual,

            ProcessSendOrderToWindowPipe=self.ProcessSendOrderToWindowPipe)
        # manual_rotate_forward_manual step2 .6.10  beam hydrauly driver power header normal reach point 8

        self.manual_forward_after_pole_prepared_relax_tiger = step_(
            "manual_forward_after_pole_prepared_relax_tiger",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.tiger_out_innertooth_relax,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .7  manual_forward_
        self.manual_forward_rotate_forward_begin = step_(
            "manual_forward_rotate_forward_begin",
            self.all_name_obj_dict,
            obj=self.rotate_forward_begin_,
            parent=self.manual_rotate_forward_manual,
            leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .8

        self.manual_forward_forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over = \
            step_("manual_forward_forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over",
                  self.all_name_obj_dict,
                  obj=self.machine_obj.main_beam.tiger_out_innertooth_bite_tight,
                  parent=self.manual_rotate_forward_manual,
                  leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .9

        self.manual_forward_forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over = \
            step_("manual_forward_forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over",
                  self.all_name_obj_dict,
                  obj=self.machine_obj.main_beam.tiger_out_innertooth_bite_tight,
                  parent=self.manual_rotate_forward_manual,
                  leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .10

        self.manual_forward_counter_wise_clock_out_pole_mather_thread_from_hydraulic_power_head = \
            step_("manual_forward_counter_wise_clock_out_pole_mather_thread_from_hydraulic_power_head",
                  self.all_name_obj_dict,
                  obj=self.rotate_forward_begin_,
                  parent=self.manual_rotate_forward_manual,
                  leader=self.manual_rotate_forward_manual)
        # manual_rotate_forward_manual step2 .11

        self.manual_forward_forward_end_come_back_the_beam_taile_5cm = \
            step_("manual_forward_forward_end_come_back_the_beam_taile_5cm",
                  self.all_name_obj_dict,
                  obj=self.move_no_load,
                  parent=self.manual_rotate_forward_manual,
                  leader=self.manual_rotate_forward_manual)
    # manual_rotate_forward_manual step2 .12
    # upped code is the    "manual_rotate_forward" order  end

    def auto_rotate_backward(self):
        tiger_inner_tooth_bitte_tight = partial(self.machine_obj.main_beam.tiger_out_innertooth_bite_tight,
                                                tiger_name="inner")
        self.operator_top_backward_auto = step_(
            "operator_top_backward_auto",
            self.all_name_obj_dict,
            )

        # operator_top_backward_auto step3 .1
        run_to_the_point_pole_in_middle_tiger_tooth_tiger_back = \
            partial(self.machine_obj.main_beam.speed_contrl,
                    self.machine_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback)
        self.come_to_the_point_pole_in_middle_tiger_tooth_tiger_back = step_(
            "come_to_the_point_pole_in_middle_tiger_tooth_tiger_back",
            self.all_name_obj_dict,
            obj=run_to_the_point_pole_in_middle_tiger_tooth_tiger_back,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)


        self.BeamMaleThreadIntoPoleAtTigerMatherThread = step_(
            "operator_top_backward_auto",
            self.all_name_obj_dict,
            obj=self.drill_box_move_unstop,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)

        # operator_top_backward_auto step3 .4
        self.operator_top_backward_auto_relax_outter_tiger_tooth = step_(
            "operator_top_backward_auto",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.tiger_out_innertooth_relax,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)

        # operator_top_backward_auto step3 .5
        self.operator_top_backward_auto_pull_back_pole = step_(
            "operator_top_backward_auto_pull_back_pole",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.auto_rotate_pull,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .6
        self.tiger_outer_bitte_tight = step_(
            "tiger_outer_bitte_tight",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .7
        # tiger_inner_tooth_bitte_tight = partial(self.machine_obj.main_beam.tiger_out_innertooth_bite_tight,
        #                                         tiger_name="inner")
        self.tiger_inner_bitte_tight = step_(
            "tiger_inner_tooth_bitte_tight",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .8
        self.loose_pole_and_checke_True = step_(
            "loose_pole_and_checke_True",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.tiger_loose_pole,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .9
        tiger_loose_back = partial(self.machine_obj.main_beam.tiger_loose_pole, order_="tight_or_back")
        self.tiger_loose_back_init = step_(
           "tiger_loose_back_init",
           self.all_name_obj_dict,
           obj=tiger_loose_back,
           parent=self.operator_top_backward_auto,
           leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .10

        self.drill_out_male_thread_in_tiger = step_(
            "drill_out_male_thread_in_tiger",
            self.all_name_obj_dict,
            obj=self.drill_out_male_thread_in_tiger,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .11

        self.bite_tight_inner_tooth = step_(
            "bite_tight_inner_tooth",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .12
        self.drill_loose_pole_taile_mother_thread = step_(
            "drill_loose_pole_taile_mother_thread",
            self.all_name_obj_dict,
            obj=tiger_inner_tooth_bitte_tight,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .13
        relax_inner_tiger_tooth = partial(self.machine_obj.main_beam.tiger_out_innertooth_relax, tiger_name="inner")
        self.operator_top_backward_auto_relax_inner_tiger_tooth = step_(
            "operator_top_backward_auto_relax_inner_tiger_tooth",
            self.all_name_obj_dict,
            obj=relax_inner_tiger_tooth,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .14
        self.operator_top_backward_auto_hand_grap_reach_can_relax_hand_and_relax = step_(
            "operator_top_backward_auto_hand_grap_reach_can_relax_hand_and_relax",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.reach_start_prepare,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .15
        self.operator_top_backward_auto_hand_grap_reach_beam = step_(
            "operator_top_backward_auto_hand_grap_reach_beam",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.prepare_to_reach_beam_with_pole,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .16
        self.operator_top_backward_auto_hand_grap_tight = step_(
            "operator_top_backward_auto_hand_grap_reach_beam",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.prepare_in_grap_hold_tight,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .17
        move_can_drill_out_the_pole_mather_thread = partial(self.machine_obj.main_beam.speed_contrl,
                                                            self.machine_obj.main_beam.pole_mather_thread_on_beam_can_counter_drill_out)
        self.operator_backward_auto_beam_move_to_loose_out_the_mother_thread_point = step_(
            "operator_backward_auto_beam_move_to_loose_out_the_mother_thread_point",
            self.all_name_obj_dict,
            obj=move_can_drill_out_the_pole_mather_thread,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .18
        self.operator_backward_auto__loose_out_the_mother_thread_point = step_(
            "operator_backward_auto__loose_out_the_mother_thread_point",
            self.all_name_obj_dict,
            obj=self.operator_backward_auto__loose_out_the_mother_thread_point_,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .19

        self.operator_top_backward_auto_back_taile_5cm = step_(
            "operator_top_backward_auto_back_taile_5cm",
            self.all_name_obj_dict,
            obj=self.move_no_load,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        self.drill_box_get_pole = step_(
            "operator_backward_auto__loose_out_the_mother_thread_point",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.pole_in,
            parent=self.operator_top_backward_auto,
            leader=self.operator_top_backward_auto)
        # operator_top_backward_auto step3 .21

    def auto_rotate_forward(self):
        self.operator_top_forward_auto = step_("operator_top_forward", self.all_name_obj_dict, None)

        self.beam_male_thread_into_the_pole_mather_thread_ = step_(
            "beam_male_thread_into_the_pole_mather_thread",
            self.all_name_obj_dict,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1
        self.drill_box_move_unstop = partial(self.machine_obj.drill_box.hand_run,
                                             self.machine_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate)
        self.drill_box_unstop_beam_move = step_(
            "drill_box_unstop_beam_move",
            self.all_name_obj_dict,
            obj=self.drill_box_move_unstop,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .2

        self.move_no_load = partial(self.machine_obj.main_beam.no_load_move_to_coordinnate_point,
                                    self.machine_obj.main_beam.beam_taile_5cm_coordinate)

        self.beam_male_thread_into_the_pole_mather_thread_back_taile_5cm = step_(
            "beam_male_thread_into_the_pole_mather_thread_back_taile_5cm",
            self.all_name_obj_dict,
            obj=self.move_no_load,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .3

        self.drill_box_send_pole = step_(
            "drill_box_send_pole",
            self.all_name_obj_dict,
            obj=self.box_prepare_obj.prepare_pole_out,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .4

        self.beam_move_and_clockwise_slight = step_(
            "beam_move_and_clockwise_slight", self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.move_and_clockwise_slight,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .5

        self.beam_move_and_clockwise_slight_intohole = beam_move_and_clockwise_slight_intohole_(
            "beam_move_and_clockwise_slight_intohole",
            self.all_name_obj_dict,
            self.machine_obj,
            obj=self.machine_obj.main_beam.move_and_clockwise_slight,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto,
            ProcessSendOrderToWindowPipe=self.ProcessSendOrderToWindowPipe)
        # operator_top_forward_auto step1 .6
        self.first_point_coordinate = first_point_coordinate_(
            "first_point_coordinate1",
            self.all_name_obj_dict,
            self.machine_obj,
            obj=None,
            parent=self.beam_move_and_clockwise_slight_intohole,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.1  beam hydrauly driver power header normal reach point 1
        # both taile and head thread of the pole is wrong .
        # operator_top_forward_auto step1 .6.3  beam hydrauly driver power header normal reach point 4
        self.box_hand_lose_pole = box_hand_lose_pole_(
            "box_hand_lose_pole4",
            self.all_name_obj_dict,
            self.machine_obj,
            obj=self.machine_obj.main_beam.move_and_clockwise_slight,
            parent=self.beam_move_and_clockwise_slight_intohole,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.4  box hand grap lose pole in beam hydrauly driver power header reach point 1
        #     , order_name_, machine_obj, obj = None, parent = None, child_index = 0, leader = None
        self.first_point_coordinate_functon1 = step_(
            "first_point_coordinate_functon1",
            self.all_name_obj_dict,
            obj=self.move_back_tiger_ruler_tuch_motion_point,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.5  beam hydrauly driver power header normal reach point 1
        self.first_point_coordinate_functon2 = step_(
            "first_point_coordinate_functon2",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.only_clockwise_rotate_pole_into_hole,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.6  beam hydrauly driver power header normal reach point 2
        self.first_point_coordinate_functon3 = relax_strong_or_slight_(
            "first_point_coordinate_functon3",
            self.all_name_obj_dict,
            self.machine_obj,
            obj=self.machine_obj.drill_box.Equepment_drill_box_digit_piont.hand_grap_relax_half_time,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.7  beam hydrauly driver power header normal reach point 3
        self.first_point_coordinate_funtion4 = step_(
            "first_point_coordinate_funtion4",
            self.all_name_obj_dict,
            obj=self.only_move_step,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.8  beam hydrauly driver power header normal reach point 4
        self.first_point_coordinate_funtion5 = step_(
            "first_point_coordinate_funtion5",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.only_stop_push_pull,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.9  beam hydrauly driver power header normal reach point 5
        self.first_point_coordinate_funtion6 = step_(
            "first_point_coordinate_funtion6",
            self.all_name_obj_dict,
            obj=self.grap_hand_grap_strong,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.10  beam hydrauly driver power header normal reach point 6
        self.first_point_coordinate_funtion7 = step_(
            "first_point_coordinate_funtion7",
            self.all_name_obj_dict,
            obj=self.wait_delta_time,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .6.11  beam hydrauly driver power header normal reach point 7
        self.first_point_coordinate_analysis = first_point_coordinate_analysis_(
            "first_point_coordinate_analysis",
            self.all_name_obj_dict,
            self.machine_obj, obj=None,
            parent=self.first_point_coordinate,
            leader=self.operator_top_forward_auto,
            ProcessSendOrderToWindowPipe=self.ProcessSendOrderToWindowPipe)
        # operator_top_forward_auto step1 .6.12  beam hydrauly driver power header normal reach point 8

        self.after_pole_prepared_relax_tiger = step_(
            "after_pole_prepared_relax_tiger",
            self.all_name_obj_dict,
            obj=self.machine_obj.main_beam.tiger_out_innertooth_relax,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .7
        self.rotate_forward_begin = step_(
            "rotate_forward_begin",
            self.all_name_obj_dict,
            obj=self.rotate_forward_begin_,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .8

        self.forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over = \
            step_("forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over",
                  self.all_name_obj_dict, obj=self.machine_obj.main_beam.tiger_out_innertooth_bite_tight,
                  parent=self.operator_top_forward_auto, leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .9

        # self.forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over = \
        #     step_("forward_end_bite_tight_outter_tiger_tooth_untill_out_thread_over",
        #           self.all_name_obj_dict, obj=self.machine_obj.Equepment_main_beam_obj.tiger_out_innertooth_bite_tight,
        #           parent=self.operator_top_forward_auto, leader=self.operator_top_forward_auto)
        # # operator_top_forward_auto step1 .10

        self.counter_wise_clock_out_pole_mather_thread_from_hydraulic_power_head = step_(
            "counter_wise_clock_out_pole_mather_thread_from_hydraulic_power_head",
            self.all_name_obj_dict,
            obj=self.rotate_forward_begin_,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        #   operator_top_forward_auto step1 .11

        self.forward_end_come_back_the_beam_taile_5cm = step_(
            "forward_end_come_back_the_beam_taile_5cm",
            self.all_name_obj_dict,
            obj=self.move_no_load,
            parent=self.operator_top_forward_auto,
            leader=self.operator_top_forward_auto)
        # operator_top_forward_auto step1 .12

        # upped code is the    "operator_top_forward_auto" order  end
        # ----------------------------------------------------------------------

    def mannual_rotate_forward_back_pole_in_tiger_prepared_over(self):
        if self.mannual_rotate_forward_back_pole_in_tiger_prepared_over_order == True:
            self.mannual_rotate_forward_back_pole_in_tiger_prepared_over_order = False
            return True

    def move_forward_30cm_rotate_clockwise(self):

        # if self.manual_rotate_forward_man_prepared_over is True:
        if self.manual_rotate_forward_man_prepared_over is True:
            self.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
                "forward", self.machine_obj.main_beam.Equepment_pole_dirll.PUSH_LEVEL[2])
            self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                "forward", self.machine_obj.main_beam.Equepment_pole_push_pull.PUSH_LEVEL[2])
            if self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - \
                    self.machine_obj.main_beam.man_give_pole_place > 300:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                   self.machine_obj.main_beam.Equepment_pole_push_pull.PUSH_LEVEL[0])
                self.manual_rotate_forward_move_man_can_get_pole_flag = True
                self.manual_rotate_forward_man_prepared_over = False

        if self.move_forward_30cm_rotate_clockwise_sucess is True:
            self.manual_rotate_forward_man_prepared_over = False
            self.move_forward_30cm_rotate_clockwise_sucess = False
            self.ProcessSendOrderToWindowPipe.send(("pushButton_188.set_False", False))
            self.ProcessSendOrderToWindowPipe.send(("pushButton_189.set_False", False))
            return True

    def operator_backward_auto__loose_out_the_mother_thread_point_(self):
        self.tools_detect_tiger_pole_tight_angle3.current_angle = \
            self.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.tools_detect_tiger_pole_tight_angle3.beam_angle_speed_calclude_and_rotate_number(
            direction="counter_clockwise")
        self.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
           self.machine_obj.main_bea.Equepment_pole_dirll.PULL_LEVEL[3])
        if self.tools_detect_tiger_pole_tight_angle3.rotate_number > 20:
            self.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
               self.machine_obj.main_beam.Equepment_pole_dirll.PUSH_LEVEL[0])
            self.tools_detect_tiger_pole_tight_angle3.calculation_over_re_init()
            return True

    def drill_loose_pole_taile_mother_thread(self):
        self.tools_detect_tiger_pole_tight_angle2.current_angle = \
            self.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.tools_detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(
            direction="counter_clockwise")
        self.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
            self.machine_obj.main_beam.Equepment_pole_dirll.PULL_LEVEL[3])
        if self.tools_detect_tiger_pole_tight_angle2.rotate_number > 1:
            self.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
                self.machine_obj.main_beam.Equepment_pole_dirll.PUSH_LEVEL[0])
            self.tools_detect_tiger_pole_tight_angle2.calculation_over_re_init()
            return True

    def drill_out_male_thread_in_tiger(self):
        self.tools_detect_tiger_pole_tight_angle2.current_angle = \
            self.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.tools_detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number(
            direction="counter_clockwise")


        if self.tools_ddetect_tiger_pole_tight_angle.rotate_number < 20:
            self.machine_obj.main_beam.counterclockwise()
            if abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate) > \
                    self.machine_obj.main_beam.tiger_self_ruler_coordinate_delta:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                   self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[2])
            else:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                   self.machine_obj.main_beam.Equepment_pole_push_pull.PUSH_LEVEL[0])
        else:
            if self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate < \
                    -self.machine_obj.main_beam.tiger_self_ruler_coordinate_delta:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                  self.machine_obj.main_beam.Equepment_pole_push_pull.PUSH_LEVEL[2])
            else:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                   self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[2])
            if self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate < 2200:
                self.tools_detect_tiger_pole_tight_angle2.calculation_over_re_init()
                return True

    def loose_pole_and_checke_True(self):
        # if first times do it failed ,try again . next man intervene.
        self.tools_detect_tiger_pole_tight_angle2.current_angle = \
            self.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.tools_detect_tiger_pole_tight_angle2.beam_angle_speed_calclude_and_rotate_number()
        if (self.loose_pole_and_check_True_flag1, self.loose_pole_and_check_True_flag2,
            self.loose_pole_and_check_True_flag3, self.loose_pole_and_check_True_flag4) == (False, False, False, False):
            if self.machine_obj.main_beam.tiger_loose_pole() is True:

                if self.tools_detect_tiger_pole_tight_angle2.current_angle > \
                        self.machine_obj.main_beam.self.pole_loose_need_mini_angle:
                    self.tools_detect_tiger_pole_tight_angle2.calculation_over_re_init()
                    self.loose_pole_and_check_True_man_help = False
                    self.loose_pole_and_check_True_move_stop_flag = False
                    self.loose_pole_and_check_True_flag1 = False
                    self.loose_pole_and_check_True_flag2 = False
                    self.loose_pole_and_check_True_flag3 = False
                    self.loose_pole_and_check_True_flag4 = False
                    self.loose_pole_and_check_True_man_help = False
                    return True
                else:
                    self.loose_pole_and_checke_True_flag1 = True
        if (self.loose_pole_and_check_True_flag1, self.loose_pole_and_check_True_flag2,
            self.loose_pole_and_check_True_flag3, self.loose_pole_and_check_True_flag4) == (True, False, False, False):
            if self.machine_obj.main_beam.tiger_out_innertooth_relax(tiger_name="inner") is True:
                self.loose_pole_and_check_True_flag2 = True
        if (self.loose_pole_and_check_True_flag1, self.loose_pole_and_check_True_flag2,
            self.loose_pole_and_check_True_flag3, self.loose_pole_and_check_True_flag4) == (True, True, False, False):
            if self.machine_obj.main_beam.tiger_loose_pole(order_="tight_or_back"):
                self.loose_pole_and_check_True_flag3 = True
        if (self.loose_pole_and_check_True_flag1, self.loose_pole_and_check_True_flag2,
            self.loose_pole_and_check_True_flag3, self.loose_pole_and_check_True_flag4) == (True, True, True, False):
            if self.machine_obj.main_beam.tiger_loose_pole() is True:

                if self.tools_detect_tiger_pole_tight_angle2.current_angle > \
                        self.machine_obj.main_beam.self.pole_loose_need_mini_angle:
                    self.tools_detect_tiger_pole_tight_angle2.calculation_over_re_init()
                    self.loose_pole_and_check_True_man_help = False
                    self.loose_pole_and_check_True_move_stop_flag = False
                    self.loose_pole_and_check_True_flag1 = False
                    self.loose_pole_and_check_True_flag2 = False
                    self.loose_pole_and_check_True_flag3 = False
                    self.loose_pole_and_check_True_flag4 = False
                    self.loose_pole_and_check_True_man_help = False
                    return True
                else:
                    self.loose_pole_and_check_True_flag4 = True
        if (self.loose_pole_and_check_True_flag1, self.loose_pole_and_check_True_flag2,
            self.loose_pole_and_check_True_flag3, self.loose_pole_and_check_True_flag4) == (True, True, True, False):
                    if self.loose_pole_and_check_True_move_stop_flag is False:
                        self.machine_obj.main_beam.move_stop()
                        self.loose_pole_and_check_True_move_stop_flag = True
                    if self.loose_pole_and_check_True_man_help == True:
                        self.loose_pole_and_check_True_man_help = False
                        self.loose_pole_and_check_True_move_stop_flag = False
                        self.loose_pole_and_check_True_flag1 = False
                        self.loose_pole_and_check_True_flag2 = False
                        self.loose_pole_and_check_True_flag3 = False
                        self.loose_pole_and_check_True_flag4 = False
                        self.loose_pole_and_check_True_man_help = False
                        return True

    def beam_male_protect_thread_into_the_pole_mather_thread_(self):
        self.machine_obj.main_beam.move_and_clockwise_slight()
        self.machine_obj.main_beam.counterclockwise()
        delta_coordinate_tiger = self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - \
                                 self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_
        delta_coordinate_beam_taile_ruler = \
            self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate - \
            self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top
        top_hydraulic_drive_head_coordinate = \
            self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - \
            delta_coordinate_beam_taile_ruler - delta_coordinate_tiger
        if self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate > \
                self.machine_obj.main_beam.tiger_self_ruler_coordinate_delta:
            self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[2])
        else:
            self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[2])
        if top_hydraulic_drive_head_coordinate == \
            self.machine_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback and \
            self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate < \
                self.machine_obj.main_beam.tiger_self_ruler_coordinate_delta:
            self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[0])
            return True

    def counter_wise_clock_out_pole_mather_thread_from_hydraulic_power_head(self):
        """
         pole on beam drill anle and circles numbers statistics   measure the distance of tiger ruler.
         calculation the out thread work isn't ok. first let the circle greater than the threshold 20
         next calculation the distance by the tiger ruler .if the pole counter wise clock drill .the
         distance changed in a range .and pole back run . the tiger doesn't run together .

         attention :
         1 threshold distance judge
            if the 20 thread is over ,and the tiger lower the threshold ,it means the tiger tooth is not
         bite tight .
         2 back will not a value .
            if the hydraulic power head is back . the tiger ruler should not back together .if it's back
            and it'wrong.
        """
        self.tools_ddetect_tiger_pole_tight_angle.currrent_angle = \
            self.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle
        self.tools_ddetect_tiger_pole_tight_angle.beam_angle_speed_calclude_and_rotate_number()
        if self.tools_ddetect_tiger_pole_tight_angle.rotate_number < 20:
            self.machine_obj.main_beam.counterclockwise()
            if abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate) > \
                    self.machine_obj.main_beam.tiger_self_ruler_coordinate_delta:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                    self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[2])
            else:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                    self.machine_obj.main_beam.Equepment_pole_push_pull.PUSH_LEVEL[0])
        else:
            if self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate < \
                    -self.machine_obj.main_beam.tiger_self_ruler_coordinate_delta:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                   self.machine_obj.main_beam.Equepment_pole_push_pull.PUSH_LEVEL[2])
            else:
                self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                    self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[2])
            if self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate < 4500:
                self.tools_ddetect_tiger_pole_tight_angle.calculation_over_re_init()
                return True

    def re_init_to_zero_angle(self):
        pass

    def rotate_forward_begin_(self,):
        # this function is the forward main program.
        self.machine_obj.main_beam.pole_water_open_close_pin.write_single(True)
        self.machine_obj.main_beam.clockwise_rotate_same_place(level=6)
        self.machine_obj.main_beam.speed_contrl(
            self.machine_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback,
            contrl_distance=250, current_push_level=2, mini_speed=35)

    def wait_delta_time(self):
        if time.time() > self.machine_obj.main_beam.pole_recircle_times_into_hole_break_time:
            return True

    def delta_run_time_check(self,delta_time=3):
        if self.step_begin_time == None:
            self.step_begin_time = time.time()
        current_delta_time = time.time() - self.step_begin_time
        delta_coordinate_tiger = self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_
        delta_coordinate_beam_taile_ruler = self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate - self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top
        top_hydraulic_drive_head_coordinate = self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - delta_coordinate_beam_taile_ruler - delta_coordinate_tiger
        if current_delta_time > delta_time:
            if top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.first_point_coordinate < self.machine_obj.main_beam.first_point_coordinate_delta:
                return False
        if top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.second_point_coordinate < self.machine_obj.main_beam.second_point_coordinate_delta:
            return False
        if top_hydraulic_drive_head_coordinate - 1 == 1:
            pass

    def first_point_relax_and_move(self):
        result_grap = self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_first_point_hand_grap_relax_greater_part_time()
        result_push = self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(self.machine_obj.main_beam.Equepment_pole_dirll.PUSH_LEVEL[self.machine_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure_level])

    def only_move_step(self):
        delta_coordinate_tiger = abs(
            self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_)
        self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                                                                      self.machine_obj.main_beam.Equepment_pole_dirll.PUSH_LEVEL[
                                                                          self.machine_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure_level])
        if delta_coordinate_tiger > self.machine_obj.main_beam.beam_push_pull_in_tiger_step_distance:
            self.machine_obj.main_beam.only_stop_push_pull()

    def turn_next_by_judge_point1(self):
        coordinate_beam4 = abs(self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate -\
                          self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top))
        delta_coordinate_tiger = abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_)
        if delta_coordinate_tiger > self.machine_obj.main_beam.tiger_touch_delta:
            beam_delta_untouch_to_touch_distance = coordinate_beam4 - self.machine_obj.main_beam.first_point_coordinate
            delta_flag = beam_delta_untouch_to_touch_distance - delta_coordinate_tiger
            if self.machine_obj.main_beam.first_success_both > delta_flag >= self.machine_obj.main_beam.first_successtaile:
                pass
            elif delta_flag >= self.machine_obj.main_beam.first_success_both:
                pass
            else:
                pass

    def move_back_tiger_ruler_tuch_motion_point(self):
        top_hydraulic_drive_head_coordinate = \
            self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate -\
            self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate - abs(
                self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top)
        ruler_coordinate = abs(
            self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_)
        self.machine_obj.main_beam.move_back_tiger_ruler_to_tuch_point()
        if abs(ruler_coordinate - self.machine_obj.main_beam.tiger_touch_delta) < self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate_delta:
            self.machine_obj.main_beam.move_stop()
            return True
        if top_hydraulic_drive_head_coordinate < self.machine_obj.main_beam.first_point_coordinate:
            self.machine_obj.main_beam.move_stop()
            return True

    def first_point_coordinate_functon_move_back(self):
        coordinate =  self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate  - abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate -\
                          self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top)
        self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(self.machine_obj.main_beam.Equepment_pole_push_pull.PULL_LEVEL[
            self.machine_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure])
        if coordinate < self.machine_obj.main_beam.first_point_coordinate:
            self.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate("keep", self.machine_obj.main_beam.Equepment_pole_push_pull.PUSH_LEVEL[0])
        if abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_) < \
                self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate_delta:
            pass

    def first_point_coordinate_functon_same_place_drill1(self):
        keep_p =  self.machine_obj.main_beam.Equepment_tigger_drill.operation_target_coordinate(self.machine_obj.main_beam.Equepment_tigger_drill.PULL_LEVEL[self.machine_obj.main_beam.tiger_dirll_pole_pole_tight_max_pressure_level])
        if self.machine_obj.main_beam.Equepment_pressure_torque.pressure > self.machine_obj.main_beam.no_load_move_to_coordinnate_point_max_pressure and \
            abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_) < self.machine_obj.main_beam.first_point_characteristic_value :
            pass

    def first_point_coordinate_functon_move_stop2(self):
        if abs(self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_) > \
                self.machine_obj.main_beam.first_point_coordinate_map_tiger_ruler_range:
            self.machine_obj.main_beam.move_stop()

    def grap_hand_grap_strong(self):
        self.machine_obj.drill_box.hand_grap_relax_half_time(self.machine_obj.drill_box.box_grap_hand_tight_strong)

    def run(self, *args):
        if self.operator_man_order == True:
            self.will_run_obj.over = True
# up is the code test use  test over  should delete it

        if self.run_flag is False:
            print(args)
            print(self.all_name_obj_dict)
            name = args[0][0].order_name_
            self.will_run_obj = self.all_name_obj_dict[name]
            print(self.will_run_obj.order_name_)
            self.run_flag = True
        else:
            result = self.will_run_obj.run(args)
            if result is None:
                result = self.will_run_obj

            len_result = len(result.childs_step)
            if len_result == 0:
                print("attention {name} has no child step".format(name=result.order_name_))
            else:
                print("{name} has {number} child step, the step detailed is :{son}".format(
                    name=result.order_name_, son=list(map(lambda x: x.order_name_, result.childs_step)), number=len_result))
            if result is True:
                self.run_flag = False
                return True
            elif result is False:
                self.receve_order_name = None
                self.run_flag = False
                return False
            else:
                self.will_run_obj = result
        print("im in operation_interface operator class obj'run function ,i will get back to order.py :",
              self.will_run_obj.order_name_)


class beam_move_and_clockwise_slight_intohole_(step_):
    def __init__(self, order_name_, all_name_obj_dict, machine_obj, obj=None, parent=None, child_index=0, leader=None,
                 ProcessSendOrderToWindowPipe=None):
        super().__init__(order_name_, all_name_obj_dict, obj=obj, parent=parent, child_index=child_index, leader=leader,
                         ProcessSendOrderToWindowPipe=None)
        self.top_hydraulic_drive_head_coordinate = 0
        self.machine_obj = machine_obj
        self.point1 = False
        self.point2 = False
        self.point3 = False



    def regist_step(self,operator_all_name_obj_dict, parent, leader=None):
        super().regist_step(operator_all_name_obj_dict, parent, leader=leader)
        if  self.parent != None:
            self.parent.childs_step_dict[self.order_name_] = self
        operator_all_name_obj_dict[self.order_name_] = self
    def run(self, *args):



        print(self.childs_step, "im in operation interface.py   this sentence will be show  at",self.order_name_,
                                " the operation order run")


        time.sleep(2)

        xx = args[0][1]  #########   finished it  after sleep
        bb = xx.interface_operator_obj.all_name_obj_dict
        if self.point1 is True:
            self.point1 = False
            self.will_run_step_obj = bb["box_hand_lose_pole4"]
            print("im in box_hand lose_pole4")
            return self.will_run_step_obj
        if self.point2 is True:
            self.point2 = False
            self.will_run_step_obj = bb["first_point_coordinate_functon1"]
            print("im in the first point, the important order ")
            return self.will_run_step_obj

        if self.point3 is True:
            self.point3 = False
            self.will_run_step_obj = bb["first_point_coordinate_functon3"]
            return self.will_run_step_obj


        delta_coordinate_tiger = self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_
        delta_coordinate_beam_taile_ruler = self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate - self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top
        self.top_hydraulic_drive_head_coordinate = self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - delta_coordinate_beam_taile_ruler - delta_coordinate_tiger
        self.will_run_step_obj.obj()
        if self.top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.first_point_coordinate < self.machine_obj.main_beam.first_point_coordinate_delta:
            if (self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_forward_hand_pin != True or\
                    self.machine_obj.drill_box.Equepment_drill_box_digit_piont.beam_taile_hand_pin != True):
                print(self.will_run_step_obj.parent.childs_step_dict, args[0][1])

                print(bb, "use "*20)
                self.will_run_step_obj = bb["box_hand_lose_pole4"]

        if self.top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.first_point_coordinate < self.machine_obj.main_beam.first_point_coordinate_delta:
                if abs(delta_coordinate_tiger - self.machine_obj.main_beam.beam_push_pull_in_tiger_step_distance) < self.machine_obj.main_beam.delta_contrast_beam_ruler_tiger_ruler:
                        print(self.will_run_step_obj.parent.childs_step_dict)
                        self.will_run_step_obj = bb["first_point_coordinate"]


        if self.top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.second_point_coordinate < self.machine_obj.main_beam.first_point_coordinate_delta:
            # pole male thread half in next pole in tiger  for this point    ""second_point_coordinate""
                if abs(delta_coordinate_tiger - self.machine_obj.main_beam.beam_push_pull_in_tiger_step_distance) < self.machine_obj.main_beam.delta_contrast_beam_ruler_tiger_ruler:
                    self.will_run_step_obj = bb["second_point_coordinate"]


        if self.top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.first_point_coordinate  < self.machine_obj.main_beam.first_point_coordinate_delta:
            if abs(delta_coordinate_tiger - self.machine_obj.main_beam.beam_push_pull_in_tiger_step_distance) < self.machine_obj.main_beam.delta_contrast_beam_ruler_tiger_ruler:
                self.will_run_step_obj = bb["taile_thread_is_ok_point_coordinate"]

        if (self.top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.third_point_coordinate) <self.machine_obj.main_beam.third_point_coordinate_delta:
            if self.machine_obj.main_beam.Equepment_pressure_torque.pressure > self.machine_obj.main_beam.no_load_move_to_coordinnate_point_max_pressure and \
                                                                                 self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate <self.machine_obj.main_beam.third_point_coordinate_map_tiger_ruler_range:
                self.will_run_step_obj = bb["third_point_coordinate"]
                self.over = True
                if self.leader_name_obj_dict["first_point_coordinate_analysis"].into_truble_time != None:
                    self.leader_name_obj_dict["first_point_coordinate_analysis"].end_truble_time = time.time()
                    self.ProcessSendOrderToWindowPipe.send(self.leader_name_obj_dict["first_point_coordinate_analysis"])
                    self.leader_name_obj_dict["first_point_coordinate_analysis"].order_statue = [
                        None, "first_point_coordinate_analysis", None, None, None]
                self.set_next_step()

        # if (self.top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.fourth_point_coordinate) < self.machine_obj.main_beam.fourth_point_coordinate_delta and\
        #         self.machine_obj.main_beam.Equepment_pressure_torque.pressure == 0 and\
        #         self.machine_obj.main_beam.Equepment_pressure_push_pull.pressure == 0:
        #     self.will_run_step_obj = bb["fourth_point_coordinate"]

        if self.machine_obj.main_beam.Equepment_pressure_push_pull.pressure > self.machine_obj.main_beam.no_load_move_to_coordinnate_point_max_pressure and \
                (self.top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.third_point_coordinate) >self.machine_obj.main_beam.third_point_coordinate_delta:
            self.will_run_step_obj = bb["danger_process"]

        if self.will_run_step_obj.over == True:
            self.will_run_step_obj.set_next_step()


class first_point_coordinate_(step_):
    def __init__(self, order_name_, all_name_obj_dict, machine_obj, obj=None, parent=None, child_index=0, leader=None, ProcessSendOrderToWindowPipe=None):
        super().__init__(order_name_, all_name_obj_dict, obj=obj, parent=parent, child_index=child_index, leader=leader, ProcessSendOrderToWindowPipe=ProcessSendOrderToWindowPipe)
        self.machine_obj = machine_obj
    def run(self,args):

        try:
            self.obj_result = self.obj()
        except AttributeError:
            self.obj_result = None
        finally:
            if self.obj_result == True:
                if len(self.childs_step) > 0:
                    self.will_run_step_obj = self.set_next_step()
                else:
                    self.over = True
                    self.will_run_step_obj = self.parent

            elif self.obj_result == False :
                self.over = False
                self.will_run_step_obj = self
            elif self.obj_result == None:
                if len(self.childs_step) > 0:
                    self.will_run_step_obj = self.set_next_step()
                else:
                    self.will_run_step_obj = self.parent
        return self.will_run_step_obj

class first_point_coordinate_analysis_(first_point_coordinate_):
    def __init__(self, order_name_, all_name_obj_dict, machine_obj, obj=None, parent=None, child_index=0, leader=None, order_dict=None, ProcessSendOrderToWindowPipe=None):
        super().__init__(order_name_, all_name_obj_dict, machine_obj, obj=obj, parent=parent, child_index=child_index, leader=leader, ProcessSendOrderToWindowPipe=ProcessSendOrderToWindowPipe)

        self.order_dict = order_dict
        self.out_window_message_data = []
        self.man_intervene_ = False
        self.man_intervene_stop = False # it used for don't let stop order frequently stop machine, manual can't operate
        self.into_truble_time = None
        self.end_truble_time = None
        self.assessment_time = 300
        self.order_statue = None

        self.point1 = False
        self.point2 = False
        self.point3 = False
        self.hand_grap_relax_half_time_over_flag = False

    def run(self, args):
        if self.point1 is True:
            self.point1 = False
            return self.parent
        if self.point2 is True:
            self.point2 = False
            print(self.parent.parent.order_name_, "   attention i will run this instance soon.")
            time.sleep(20)
            return self.parent.parent
        if self.point3 is True:
            self.point3 = False
            self.loop_times = 6
        if self.run_begin_time is None:
            self.run_begin_time = time.time()

        delta_coordinate_tiger = self.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate - self.machine_obj.main_beam.tiger_self_middle_zero_coordinate_
        delta_coordinate_beam_taile_ruler = self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate - self.machine_obj.main_beam.Equepment_line_distance_measure_beam_taile_point_beam_solt_top
        top_hydraulic_drive_head_coordinate = self.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - delta_coordinate_beam_taile_ruler - delta_coordinate_tiger

        if abs(
                top_hydraulic_drive_head_coordinate - self.machine_obj.main_beam.third_point_coordinate) < self.machine_obj.main_beam.third_point_coordinate_delta:
            self.loop_times = 0
            self.parent.parent.over = True
            self.end_truble_time = time.time()
            self.order_statue = ["first_point_coordinate_analysis_manual_process_ok", (
                True, "first_point_coordinate_analysis_manual_process_ok",
                self.into_truble_time, self.end_truble_time, self.assessment_time)]
            self.ProcessSendOrderToWindowPipe.send(self.order_statue)
            self.ProcessSendOrderToWindowPipe.send(("pushButton_184.setVisible(False))", False))
            self.hand_grap_relax_half_time_over_flag = False

            return self.parent.parent


        if self.loop_times <= 5:

            if self.into_truble_time == None:
                self.into_truble_time = time.time()
                return self.parent
        else:
            if self.hand_grap_relax_half_time_over_flag is False:
                if self.machine_obj.drill_box.hand_grap_relax_half_time() == True:
                    self.hand_grap_relax_half_time_over_flag = True
            if self.hand_grap_relax_half_time_over_flag is True:

                self.machine_obj.wrong_data.insert(0, [True, self.order_name_, self.into_truble_time, True, 300])
                # process result, trouble name, trouble start time, trouble end time,assessment time
                self.ProcessSendOrderToWindowPipe.send(("machine_obj.wrong_data", self.machine_obj.wrong_data))
                self.ProcessSendOrderToWindowPipe.send(("pushButton_184.setVisible(False))", True))
                # data = [None,self.order_name_,time.time(),None,None] self.write_all_message_box_every_data
                # (self.ui_widget_main.message_lable_menu, self.machine_obj.wrong_data,data)
                self.order_statue = ["first_point_coordinate_analysis_manual_process_ok", (
                         False, "first_point_coordinate_analysis_manual_process_ok",
                         self.into_truble_time, self.end_truble_time, self.assessment_time)]
                # result = True False or Concel
                self.ProcessSendOrderToWindowPipe.send(self.order_statue)
                if self.man_intervene_ is True:
                    self.man_intervene_stop = False
                    self.man_intervene_ = False
                    self.hand_grap_relax_half_time_over_flag = False
                    self.loop_times = self.loop_times + 1
                    return self.parent
                else:
                    if self.man_intervene_stop is False:
                        self.machine_obj.main_beam.move_stop(warterclose=True)
                        self.man_intervene_stop = True
                        self.into_truble_time = None





class box_hand_lose_pole_(first_point_coordinate_):
    def __init__(self, order_name_,all_name_obj_dict, machine_obj, obj=None, parent=None, child_index=0, leader=None, order_dict=None):
        super().__init__(order_name_, all_name_obj_dict, machine_obj, obj=obj, parent=parent, child_index=child_index, leader=leader)
        self.order_dict = order_dict
        self.out_window_message_data = []
        self.man_intervene_ = False
        self.man_intervene_stop = False # it used for don't let stop order frequently stop machine, manual can't operate
        self.into_truble_time = None
        self.end_truble_time = None
        self.assessment_time = 300
        self.order_statue = None

    def run(self):

        if self.into_truble_time is None:
            self.ProcessSendOrderToWindowPipe.send(("pushButton_184.setVisible(False))", False))
            self.into_truble_time = time.time()
        if self.machine_obj.drill_box.hand_grap_relax_half_time() is True:
            self.machine_obj.wrong_data.insert(0, [True, self.order_name_, self.into_truble_time, True, 300])
            # process result, trouble name, trouble start time, trouble end time,assessment time
            self.ProcessSendOrderToWindowPipe.send(("machine_obj.wrong_data", self.machine_obj.wrong_data))
            self.ProcessSendOrderToWindowPipe.send(("pushButton_184.setVisible(False))", True))
            # data = [None,self.order_name_,time.time(),None,None] self.write_all_message_box_every_data
            # (self.ui_widget_main.message_lable_menu, self.machine_obj.wrong_data,data)
            self.order_statue = ["first_point_coordinate_analysis_manual_process_ok", (
                False, "first_point_coordinate_analysis_manual_process_ok",
                self.into_truble_time, self.end_truble_time, self.assessment_time)]
            # result = True False or Concel
            self.ProcessSendOrderToWindowPipe.put(self.order_statue)
            if self.man_intervene_ is True:
                self.into_truble_time = None
                self.man_intervene_stop = False
                self.man_intervene_ = False
                self.end_truble_time = time.time()
                self.order_statue = ["first_point_coordinate_analysis_manual_process_ok", (
                    True, "first_point_coordinate_analysis_manual_process_ok",
                    self.into_truble_time, self.end_truble_time, self.assessment_time)]
                self.ProcessSendOrderToWindowPipe.send(self.order_statue)
                return self.parent
            else:
                if self.man_intervene_stop is False:
                    self.machine_obj.main_beam.move_stop(warterclose=True)
                    self.man_intervene_stop = True





class relax_strong_or_slight_(first_point_coordinate_):
    def run(self, *args):
        if self.over == True:
            self.will_run_step_obj = self.set_next_step()
            return self.will_run_step_obj
# up is the test code





        if self.run_begin_time == None:
            self.run_begin_time = time.time()

        try:
            if self.loop_times//2 ==1:
                    self.obj_result = self.machine_obj.drill_box.hand_grap_relax_half_time()
            else:
                self.obj_result = self.machine_obj.drill_box.beam_first_point_hand_grap_relax_greater_part_time()
        except AttributeError:
            self.obj_result = None
        finally:
            if self.obj_result == True:
                if len(self.childs_step) > 0:
                    self.will_run_step_obj = self.set_next_step()
                    return self.will_run_step_obj
                else:
                    self.over = True
                    self.loop_times = self.loop_times +1
            elif self.obj_result == False:
                self.over = False
                self.will_run_step_obj = self
            elif self.obj_result == None:
                self.will_run_step_obj = self
        self.run_time_delta = time.time() - self.run_begin_time
        if self.loop_max_times != None:
            if self.loop_max_times == self.loop_times:
                        self.loop_times = 0
                        return False
        return self.will_run_step_obj

