import time
import inspect

import pandas


class every_order():
    def __init__(self, order_name_, action_obj, libary_obj, ProcessSendOrderToWindowPipe, interface_operator_obj):
            self.ProcessSendOrderToWindowPipe = ProcessSendOrderToWindowPipe
            self.interface_operator_obj = interface_operator_obj
            self.current_loop_run_statue = False
            self.libary_obj = libary_obj
            self.order_name_ = order_name_
            self.order_begin = None
            self.order_over = None
            if type(action_obj) is str:
                self.action_obj = getattr(self, action_obj)
            else:
                self.action_obj = action_obj
            self.order_runing = None
            self.order_begin_time = None
            self.order_stop_time = None
            self.order_result = None
            self.order_canceled = None
            self.stop_order = False
            self.order_key = (self.order_name_, self.order_begin_time)
            self.excute_time_delta = None

            self.sleep_time_first = 0
            self.sleep_time_current = 0
            self.sleep_time = 0
            self.time_out = None
            self.autoexclusive = True
            self.regist()
            self.action_name_map_action_obj = self.libary_obj.order_libary

            self.data_machine_empty_recorde_pandas = 1

            self.args = None

    def pause_obj(self):
        # self.pause_flag = True
        # self.action_name_map_action_obj
        #
        # pause_dict = {}
        pass

    def stop_obj(self):
        self.stop_flag = True
        pass

    def over_obj(self):
        self.over_flag = True
        pass

    def cancel_obj(self):
        if self.cancel_flag is False:
            self.cancel_flag = self.stop_obj()

    def get_new_parameter(self, data):
        pass

    def errors_process(self):
        self.errors_flag = True
        pass

    def run(self, *args, **kwargs):
        print("order_loop : {args_}  is  the parameter give to the order.run load operation obj parameter ".format(
            args_=args))
        T = None
        if self.current_loop_run_statue is False:
            if self.action_obj != None:
                print("order_loop : 当前order_run运行任务名称", self.order_name_)
                # print(args[0][0][1])
                print(args, "： this is the parameter received")
                print("totle name,obj dict of order.py... all_interface_order_dict_collect class --> "
                      "obj interface_order_libary_dict  attribute (it's a class creat obj ,it has "
                      "a dict attribute order_libary", args[1].interface_order_libary_dict.order_libary)
                if self.args:
                    T = self.action_obj(self.args)
                else:
                    T = self.action_obj()
                self.back_recorde_data()
            return T



    def sleep_(self):
        if self.sleep_time_first == 0:
            self.sleep_time_first = time.time()
        self.sleep_time_current = time.time()
        if self.sleep_time_current > self.sleep_time_first:
            return True

    def regist(self):
        self.libary_obj.regist(self)

    def back_recorde_data(self):

        result1 = self.interface_operator_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop()
        result2 = self.interface_operator_obj.machine_obj.main_beam.move_stop()
        order_name = self.order_name_
        order_parameter = None
        current_push_pull_gear = self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.get_current_gear
        current_push_pull_gear_coordinate = self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.coordinate
        push_pull_coordinate_begin = self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.coordinate_start
        push_pull_coordinate_stop = self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.coordinate_stop

        current_drill_gear = self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.get_current_gear
        current_drill_gear_coordinate = self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.coordinate


        tigger_head_move_coordinate = self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate
        tigger_head_move_coordinate_middle = self.interface_operator_obj.machine_obj.main_beam.tiger_self_middle_zero_coordinate_


        tigger_outer_coordinate = self.interface_operator_obj.machine_obj.main_beam.Equepment_tigger_tooch_f.coordinate
        tigger_outer_full_open_coordinate = self.interface_operator_obj.machine_obj.main_beam.tiger_outer_rule_relax
        tigger_outer_full_grap_coordinate = self.interface_operator_obj.machine_obj.main_beam.tiger_outer_rule_grap

        tigger_inner_grap_coordinate = self.interface_operator_obj.machine_obj.main_beam.tiger_inner_rule_grap
        tigger_inner_relax_coordinate = self.interface_operator_obj.machine_obj.main_beam.tiger_outer_rule_grap
        tigger_inner_coordinate = self.interface_operator_obj.machine_obj.main_beam.Equepment_tigger_tooch_b.coordinate

        tigger_inner_drill_relax = True

        messure_push_pull = self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_push_pull.pressure
        messure_drill = self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_torque.pressure
        messure_water = self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_warter.pressure


        warter_deep = self.interface_operator_obj.machine_obj.main_beam.Equepment_warter_deep_measure.water_deep_number


        beam_coordinate = self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate
        hand_coordinate = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate


        hand_get_pole_at_beam_coordinate = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point_beam_grap_coordinate
        hand_box_unstop_beam_driving_coordinate = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point_unstop_beam_coordinate
        hand_box_inner_cloumns_1_coordinate = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point1_coordinate
        hand_box_inner_cloumns_3_coordinate = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point3_coordinate

        beam_head_coordinate = self.interface_operator_obj.machine_obj.main_beam.beam_begin
        beam_tail_coordinate = self.interface_operator_obj.machine_obj.main_beam.beam_end

        MAX_PUSH_QUICK_PRESSURE = self.interface_operator_obj.machine_obj.main_beam.MAX_PUSH_QUICK_PRESSURE
        MAX_PUSH_SLOW_PRESSURE = self.interface_operator_obj.machine_obj.main_beam.MAX_PUSH_SLOW_PRESSURE
        MAX_DRILL_QUICK_PRESSURE = self.interface_operator_obj.machine_obj.main_beam.MAX_DRILL_QUICK_PRESSURE
        MAX_DRILL_SLOW_PRESSURE = self.interface_operator_obj.machine_obj.main_beam.MAX_DRILL_SLOW_PRESSURE


        box_updown_column_up = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.box_updown_column_up
        box_half_up_coordinate = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.box_updown_colbox_updown_column_can_grapumn_up
        box_updown_bottom = self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.box_updown_bottom
        pole_angle_at_machine = self.interface_operator_obj.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle
        current_pole_number_in_hole = self.interface_operator_obj.machine_obj.main_beam.current_pole_number_in_hole
        current_pole_distance_not_in_hole = self.interface_operator_obj.machine_obj.main_beam.current_pole_distance_not_in_hole
        data_d = {
            "order_name": order_name,
            "order_parameter": None,
            "current_push_pull_gear": current_push_pull_gear,
            "current_push_pull_gear_coordinate": current_push_pull_gear_coordinate,
            "current_drill_gear": current_drill_gear,
            "current_drill_gear_coordinate": current_drill_gear_coordinate,
            "push_pull_coordinate_begin": push_pull_coordinate_begin,
            "push_pull_coordinate_stop": push_pull_coordinate_stop,
            "tigger_head_move_coordinate": tigger_head_move_coordinate,
            "tigger_head_move_coordinate_middle": tigger_head_move_coordinate_middle,
            "tigger_outer_coordinate": tigger_outer_coordinate,
            "tigger_outer_full_open_coordinate": tigger_outer_full_open_coordinate,
            "tigger_outer_full_grap_coordinate": tigger_outer_full_grap_coordinate,
            "tigger_inner_coordinate": tigger_inner_coordinate,
            "tigger_inner_grap_coordinate": tigger_inner_grap_coordinate,
            "tigger_inner_relax_coordinate": tigger_inner_relax_coordinate,
            "tigger_inner_drill_relax": True,
            "current_pole_number_in_hole": current_pole_number_in_hole,
            "current_pole_distance_not_in_hole": current_pole_distance_not_in_hole,
            "messure_push_pull": messure_push_pull,
            "messure_drill": messure_drill,
            "messure_water": messure_water,
            "water_deep": warter_deep,
            "MAX_PUSH_QUICK_PRESSURE": MAX_PUSH_QUICK_PRESSURE,
            "MAX_PUSH_SLOW_PRESSURE": MAX_PUSH_SLOW_PRESSURE,
            "MAX_DRILL_QUICK_PRESSURE": MAX_DRILL_QUICK_PRESSURE,
            "MAX_DRILL_SLOW_PRESSURE": MAX_DRILL_SLOW_PRESSURE,
            "oil_deep": 70,
            "beam_coordinate": beam_coordinate,
            "hand_coordinate": hand_coordinate,
            "hand_get_pole_at_beam_coordinate": hand_get_pole_at_beam_coordinate,
            "hand_box_unstop_beam_driving_coordinate": hand_box_unstop_beam_driving_coordinate,
            "hand_box_cloumns_1_coordinate": hand_box_inner_cloumns_1_coordinate,
            "hand_box_cloumns_3_coordinate": hand_box_inner_cloumns_3_coordinate,
            "beam_head_coordinate": beam_head_coordinate,
            "beam_tail_coordinate": beam_tail_coordinate,
            "box_up_coordinate": box_updown_column_up,
            "box_half_up_coordinate": box_half_up_coordinate,
            "box_updown_bottom": box_updown_bottom,

            "box_hand_relax_grap": True,
            "machine_angle_H": 0,
            "machine_angle_V": 0,
            "pole_angle_at_machine": pole_angle_at_machine,
            "pole_angle_at_machine_12colock": 10,
            "pole_angle_at_remote": 20,
            "time_": time.time(),
            "pic_box_colum1_pole_number": None,
            "pic_hand_grap_faild": None,
            "pic_file": None,
            "action_apraise_recorder": 5,
        }
        data_machine_empty_recorde_pandas

class EveryMachineRunOrder(every_order):
    """
    self.pused_stop_is_run_ok  self.stop_stop_is_run_ok used in the order_loop , if the  self.exclusive_run_flag  is
    True, the  current action_obj will run current_obj.stop  untill the   self.stop_stop_is_run_ok  be equal to True

    if the  self.pused_stop_is_run_ok  is True, the current action_obj will run current_obj.pause, untill the
    self.pused_stop_is_run_ok  is True.

    """
    main_slave_id = "EveryMachineRunOrder_1"
    def __init__(self, order_name_, action_obj, libary_obj, ProcessSendOrderToWindowPipe,
                 interface_operator_obj, pause_obj=None, stop_obj=None):
        # print(f"{order_name_}  kkkkkwwwwwwmmmmmmmmmmmmmmmmmmmmm")
        # if EveryMachineRunOrder.has_obj_flag is False:
            super(EveryMachineRunOrder, self).__init__(
                order_name_, action_obj, libary_obj, ProcessSendOrderToWindowPipe, interface_operator_obj)
            if pause_obj == None:
                self.pause_obj = self.stop_pause_obj
            else:
                self.pause_obj = pause_obj

            if stop_obj == None:
                self.stop_obj = self.stop_pause_obj
            else:
                self.stop_obj = stop_obj
            try:
                self.asocieated_action_obj_name = action_asociated_data[action_asociated_data.loc[:, "action_obj_name"] == self.order_name_]
            except Exception:
                self.asocieated_action_obj_name = None
            self.exclusive_run_flag = False   #it mean  this task in the loop.
            self.pause_flag_true_times=0
            if self.pause_flag_true_times > 0:
                self.pause_run_flag = True
            else:
                self.pause_run_flag = False

            self.run_flag = False    #task run must self.run_flag is True.  and the self.pause_run_flag is False.
            self.pused_stop_is_run_ok1 = False
            self.pused_stop_is_run_ok = False
            self.stop_stop_is_run_ok = False
            self.absolute_begin = False
            self.regist()

    @staticmethod
    def pause_apply(dataframe, self):
        asociate_obj_name = dataframe["associated_action_name"]
        asocieated_obj = self.action_name_map_action_obj[asociate_obj_name]
        new_times = asocieated_obj.pause_flag_true_times + 1
        self.asocieated_action_obj_name.loc[dataframe.index, "associated_action_attr_pause_flag_true_times"] = new_times
        asocieated_obj.pause_flag_true_times = new_times
        if asocieated_obj.pause_flag_true_times > 0:
            asocieated_obj.pause_run_flag = True
            asocieated_obj.run_flag = False
        else:
            asocieated_obj.pause_run_flag = False
        global action_asociated_data
        action_asociated_data.update(self.asocieated_action_obj_name)


    def get_associated_action_data(self):
        if self.asocieated_action_obj_name:
            self.asocieated_action_obj_name.apply(self.pause_apply, axis=1, args=(self, ))
        return True
    @staticmethod
    def unpause_apply(dataframe, self):
        asociate_obj_name = dataframe["associated_action_name"]
        asocieated_obj = self.action_name_map_action_obj[asociate_obj_name]
        new_times = asocieated_obj.pause_flag_true_times - 1 if asocieated_obj.pause_flag_true_times >= 1 else 0
        self.asocieated_action_obj_name.loc[dataframe.index, "associated_action_attr_pause_flag_true_times"] = new_times
        asocieated_obj.pause_flag_true_times = new_times
        if asocieated_obj.pause_flag_true_times > 0:
            asocieated_obj.pause_run_flag = True
            asocieated_obj.run_flag = False
        else:
            asocieated_obj.pause_run_flag = False
        global action_asociated_data
        action_asociated_data.update(self.asocieated_action_obj_name)

    @staticmethod
    def pause_ok_check(dataframe, self):
        asociate_obj_name = dataframe["associated_action_name"]
        asocieated_obj = self.action_name_map_action_obj[asociate_obj_name]
        if asocieated_obj.run_flag:
            if (asocieated_obj.pause_run_flag, asocieated_obj.pused_stop_is_run_ok1, asocieated_obj.pused_stop_is_run_ok) == (True, True, False):
                return False
            elif (asocieated_obj.pause_run_flag, asocieated_obj.pused_stop_is_run_ok1, asocieated_obj.pused_stop_is_run_ok) == (True, True, True):
                return True
            else:
                raise Exception
        else:
            return True

    def unpause(self):
        if self.asocieated_action_obj_name:
            self.asocieated_action_obj_name.apply(self.unpause_apply, axis=1, args=(self,))



    def pause(self):
        if (self.pause_run_flag, self.pused_stop_is_run_ok1) == (True, False):
            self.pused_stop_is_run_ok1 = self.get_associated_action_data()
        elif (self.pause_run_flag, self.pused_stop_is_run_ok1) == (True, True):
            if self.asocieated_action_obj_name.apply(self.pause_ok_check, axis=1, args=(self,)).all():
                if self.pused_stop_is_run_ok is True:
                    self.pause_run_flag = False
                    self.pused_stop_is_run_ok = False
                    return True

    def stop(self):
        if (self.cancel_flag, self.stop_stop_is_run_ok) == (True, False):
            if self.stop_pause_obj() == True:
                self.cancel_flag = False
                self.pause_flag_true_times = 0
                self.asocieated_action_obj_name.loc[:, "associated_action_attr_pause_flag_true_times"] = 0
                self.run_flag = False
                self.pause_run_flag = False
                self.stop_stop_is_run_ok = False
                return True

    def stop_pause_obj(self):
        result1 = self.interface_operator_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.grap_hand_stop()
        result2 = self.interface_operator_obj.machine_obj.main_beam.move_stop()
        if (result1, result2) == (True, True):
            return True

    def run(self, *args, **kwargs):
        print("order_loop : {args_}  is  the parameter give to the order.run load operation obj parameter ".format(
            args_=args))
        order_flag = (self.pause_run_flag, self.run_flag, self.cancel_flag)
        if self.cancel_flag is True:
            T = self.stop()
            # will do nothing
            return T
        else:
            if self.pause_run_flag is True:
                if order_flag == (True, False, False):
                    if self.pused_stop_is_run_ok is False:
                        if self.pause_obj(*args):
                            self.pused_stop_is_run_ok = True
            else:

                if order_flag == (False, True, False):
                    if inspect.ismethod(self.action_obj):
                        T =self.action_obj(*args, **kwargs)
                        print("order_loop : 当前order_run运行任务名称", self.order_name_, __file__, inspect.currentframe().f_lineno)
                        return T
                    else:
                        T =self.action_obj.run(*args, **kwargs)
                        print("order_loop : 当前order_run运行任务名称", self.order_name_, __file__, inspect.currentframe().f_lineno)
                        return T