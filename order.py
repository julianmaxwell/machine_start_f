#### send order ,  parse back result  send new order
import asyncio
import inspect
import sys
import time
import uuid
import pickle
import pandas
import simulate_single
import operation_interface
from order_abc import every_order, EveryMachineRunOrder

import queue


import seting

sys.path.append("D:\comunication_ui_")
import communication_setting
machine_id = communication_setting.bmachine_id

function_code6001 = communication_setting.function_code6001
function_code8001 = communication_setting.function_code8001

action_asociated_data = pandas.read_csv("D:\machine\机器端\machine_action_order.csv", index_col=None)
action_asociated_data = action_asociated_data.set_index(["action_obj_name", "associated_action_name"], drop=False)

from abs_task_step import oldMachineProcess

class order_library():
    def __init__(self):
        self.interface_operator_obj = operation_interface.operator()
        self.processSendToCommunicationPipe = None
        self.parameter_reset_encodin_push_pull_rock_arm_obj = oldMachineProcess()

        self.ProcessSendOrderToWindowPipe = None
        self.machineProcessGetOrderPipe = None
        self.distribute_que = queue.Queue()
        self.running_action = {}
        self.set_temporary_parameter_opeation_obj_over_dict = {
            'operatar_value_change__over': self.interface_operator_obj.will_run_obj,
            'test_machine_operator__point1': self.interface_operator_obj.will_run_obj,
            'test_machine_operator__point2': self.interface_operator_obj.will_run_obj,
            'test_machine_operator__point3': self.interface_operator_obj.will_run_obj,
            '__manual_rotate_forward_man_prepared_over': self.interface_operator_obj,

            'drill_army_move_forward': self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.forward_operation,
            'drill_army_move_stop': self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.stop_action,
            'drill_army_move_backward': self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.back_operation,


        }

        self.order_libary = {
            "set_temporary_parameter_opeation_obj_over": self.set_temporary_parameter_opeation_obj_over,
        }
        self.order_value = {}
        self.exclusive_run_flag = False
        self.pause_run_flag = True


    def init_parameter(self, r_cve, s_end):
        self.processSendToCommunicationPipe = s_end
        self.ProcessSendOrderToWindowPipe = s_end
        self.machineProcessGetOrderPipe = r_cve


    def stop(self, data):
        # find the master_flag ,
        # run the master_obj.stop
        pass

    def pause(self, data):
        for every_action_name, action_obj in self.order_libary.items():
            action_obj.pause_run_flag = True
            action_obj.pause()

    def unpause(self, data):
        #master action_obj run.
        #master_ pause_flag = False
        pass

    def cancel(self, data):
        # find the master_flag ,
        # run the master_obj.cancel
        pass


    def set_order_step_stop_pause_flag2(self,excutin_order_funtion, order_data):
        if "set_order_step_stop_pause_flag2" == order_data[0]:
            task_obj_name = order_data[1]
            task_obj_name_args_value = order_data[2]
            task_obj = excutin_order_funtion
            if hasattr(task_obj, "exclusive_run_flag"):
                setattr(task_obj, "exclusive_run_flag", task_obj_name_args_value[0])
                print("i changed ok  order_instead_model ", task_obj_name_args_value[1])
                return True
            if hasattr(task_obj, "pause_run_flag"):
                setattr(task_obj, "pause_run_flag", order_data[1][1])
                print("i changed ok  order_pause_model : ", task_obj_name_args_value[1])
                return True

    def set_order_step_stop_pause_flag(self, order_function):

            if order_function[0] == "order_instead_model":
                self.exclusive_run_flag = order_function[1]
                return True
            if order_function[0] == "order_pause_model":
                self.pause_run_flag = order_function[1]
                return True

    def set_temporary_parameter_opeation_obj_over(self, new_parameter):
        act_ = self.set_temporary_parameter_opeation_obj_over_dict[new_parameter[0]]
        if inspect.isfunction(act_):
            act_()
        else:
            attr_name = new_parameter[0].split("__")[-1]
            setattr(act_, attr_name, new_parameter[1])


    def regist(self, order_obj):
        self.main_slave_id_map_obj = {}
        self.order_libary[order_obj.order_name_] = order_obj
        print("order : ", order_obj.order_name_, "  registed  at ", __file__, inspect.currentframe().f_lineno)
        self.order_value[order_obj.order_name_] = (None, order_obj.order_name_, None, None, 300)  #
        print(self.order_value[order_obj.order_name_],(None, order_obj.order_name_, None, None, 300))
        self.save_dict()


    def save_dict(self):
        try:
            with open("order_recorder.tex", "wb+") as save_2:
                pickle.dump(self.order_value, save_2)
        except FileNotFoundError:
            with open("order_recorder.tex", "wb") as save_2:
                pickle.dump(self.order_value, save_2)



class order_loop_():
    def __init__(self):
        self.order_dict = all_interface_order_dict_collect()
        self.distribute_que = self.order_dict.interface_order_libary_dict.distribute_que

        self.excuting_que = queue.Queue()
        self.canceld_que = queue.Queue()
        self.overed_que = queue.Queue()

        self.running_in_loop_objs_dict = {}

        self.running_async_loop_que = asyncio.Queue()
        self.canceld_async_loop_que = asyncio.Queue()
        self.overed_async_loop_que = asyncio.Queue()
        self.faild_async_loop_que = asyncio.Queue()
        self.errors_async_loop_que = asyncio.Queue()

        self.running_async_loop_event = asyncio.Event()
        self.canceld_async_loop_event = asyncio.Event()
        self.overed_async_loop_event = asyncio.Event()
        self.faild_async_loop_event = asyncio.Event()
        self.errors_async_loop_event = asyncio.Event()


        self.last_obj = None

        self.run_loop_exclusive_order = False
        self.run_loop_pause_order = False

        self.absolute_rights = None

        self.function_code_map_function = {
            function_code8001: self.function_code8001,
        }

    def send_machine_statue(self, flag=False):
        self.order_dict.run_order_order_library.interface_operator_obj.machine_obj.oberservation.send_statue_event_flag=flag

    def function_code8001(self, function_name, args):
        print("function name is ", inspect.currentframe().f_code.co_name, " line is : ",inspect.currentframe().f_lineno)
        print(function_name, args[0])

        # self.machine_ = self.order_dict.interface_order_libary_dict.interface_operator_obj.machine_obj
        function_ = self.order_dict.interface_order_libary_dict.order_libary[function_name]
        function_.args = args

        self.put_loop(function_)
        print("order run over")
        # function_(args[0])

    def put_loop(self, order_obj):
        self.distribute_que.put_nowait(order_obj)
        order_obj.order_begin = True
        order_obj.order_begin_time = time.time()

    def stop_obj(self):
        pass

    def over_obj(self):
        pass

    def cancel_obj(self):
        pass

    def get_new_parameter(self, data):
        pass

    def errors_process(self):
        pass



    async def get_machine_process_pipe_send_que_order(self):
        running_in_loop_objs_dict = self.running_in_loop_objs_dict
        distribute_que = self.distribute_que
        running_async_loop_que = self.running_async_loop_que

        running_async_loop_que_empty = self.running_async_loop_que.empty
        canceld_async_loop_que_empty = self.canceld_async_loop_que.empty
        overed_async_loop_que_empty = self.overed_async_loop_que.empty
        faild_async_loop_que_empty = self.faild_async_loop_que.empty
        errors_async_loop_que_empty = self.errors_async_loop_que.empty

        running_async_loop_event = self.running_async_loop_event.set
        canceld_async_loop_event = self.canceld_async_loop_event.set
        overed_async_loop_event = self.overed_async_loop_event.set
        faild_async_loop_event = self.faild_async_loop_event.set
        errors_async_loop_event = self.errors_async_loop_event.set
        sleep_ = asyncio.sleep
        import os
        while True:
            if distribute_que.empty() is False:
                data = distribute_que.get()
                try:
                    exe_obj, *args = data
                    args = args[0]
                except Exception:
                    exe_obj = data
                    args = None
                data = [exe_obj, args]
                print(data)
                print(__file__, inspect.currentframe().f_lineno)
                if exe_obj.order_name_ not in running_in_loop_objs_dict.keys():
                    running_in_loop_objs_dict[exe_obj.order_name_] = exe_obj
                    exe_obj.current_loop_run_statue = True
                    await running_async_loop_que.put(data)
                    print("distribute_que send running_async_loop_que action order_name_ is ", exe_obj.order_name_)
                else:
                    print(__file__, inspect.currentframe().f_lineno)
                    print(f"machine task has run {inspect.currentframe().f_lineno}")
                    exe_obj.current_loop_run_statue = True
                    running_in_loop_objs_dict[exe_obj.order_name_] = exe_obj
                    await running_async_loop_que.put(data)
                    print(__file__, inspect.currentframe().f_lineno)
                    print("machine task has run 422  i send data is ", exe_obj.order_name_)
            await asyncio.sleep(0)

    async def process_machine_monitor_data(self):

        pass

    async def process_errors_asyncque(self):
        errors_async_loop_que = self.errors_async_loop_que
        errors_process = self.errors_process
        while True:
                data_obj = await errors_async_loop_que.get()
                print("im run 4444444, ", __class__, inspect.currentframe().f_lineno)
                if hasattr(data_obj, "errors_process"):
                    data_obj.errors_process()
                else:
                    errors_process()


    async def process_cancel_asyncque(self):
        canceld_async_loop_que = self.canceld_async_loop_que
        while True:
                cancel_obj = await canceld_async_loop_que.get()
                print("im run 333333, ", __class__, inspect.currentframe().f_lineno)
                cancel_obj.run()


    async def process_over_asyncque(self):
        overed_async_loop_que = self.overed_async_loop_que
        sleep_ = asyncio.sleep
        while True:
                overed_obj = await overed_async_loop_que.get()
                overed_obj.run()


    async def process_running_asyncque(self):
        running_async_loop_que_put = self.running_async_loop_que.put
        running_async_loop_que = self.running_async_loop_que
        running_async_loop_que_get = self.running_async_loop_que.get
        canceld_async_loop_que_put = self.canceld_async_loop_que.put
        overed_async_loop_que_put = self.overed_async_loop_que.put
        faild_async_loop_que_put = self.faild_async_loop_que.put
        errors_async_loop_que_put = self.errors_async_loop_que.put
        running_in_loop_objs_dict = self.running_in_loop_objs_dict
        sleep_ = asyncio.sleep
        import os
        while True:
            # if running_async_loop_que.empty() is False:
                print(inspect.currentframe().f_lineno, "task running  pid is ", os.getpid())
                exe_obj_data = await running_async_loop_que.get()
                try:
                    exe_obj_data, args = exe_obj_data
                except Exception:
                    args = None
                if args:
                    exe_obj_data.args = args
                print(inspect.currentframe().f_lineno, "task running.......  ", exe_obj_data, exe_obj_data.order_name_)
                if exe_obj_data.current_loop_run_statue is not True:
                    try:
                        if inspect.isfunction(exe_obj_data):
                                result = exe_obj_data.run()
                        else:
                            result = await exe_obj_data()

                        if result is True:
                            del running_in_loop_objs_dict[exe_obj_data.order_name_]
                            exe_obj_data.current_loop_run_statue = False
                            await overed_async_loop_que_put(exe_obj_data)
                        elif result is False:
                            del running_in_loop_objs_dict[exe_obj_data.order_name_]
                            exe_obj_data.current_loop_run_statue = False
                            await faild_async_loop_que_put(exe_obj_data)
                        elif result == "canceld_" or exe_obj_data.cancel_flag is True:
                            del running_in_loop_objs_dict[exe_obj_data.order_name_]
                            exe_obj_data.current_loop_run_statue = False
                            await canceld_async_loop_que_put(exe_obj_data)
                        elif (result is None) or (exe_obj_data.run_flag is True):
                            print(f"im in task loop que,  {exe_obj_data.order_name_} will run, im in file {__file__}'s {__class__}  lines is {inspect.currentframe().f_lineno}", )
                            print(f"result is {result}   action run_flag is {exe_obj_data.run_flag}")
                            await running_async_loop_que_put(exe_obj_data)
                    except Exception as ff:
                        del running_in_loop_objs_dict[exe_obj_data.order_name_]
                        exe_obj_data.current_loop_run_statue = False
                        await errors_async_loop_que_put(exe_obj_data)
                else:
                        exe_obj_data.current_loop_run_statue = True
                        await running_async_loop_que_put(exe_obj_data)
                        print("order is running , name is ", exe_obj_data.order_name_, "     ok eeeeeeeeeeeeeeeeeeeee888882")
                        print("im run , ", __class__, inspect.currentframe().f_lineno)



    def init_parameter(self, r_cve, s_end):
        self.order_dict.init_parameter(r_cve, s_end)


    def run_loop(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.get_machine_process_pipe_send_que_order())
        loop.create_task(self.process_errors_asyncque())
        loop.create_task(self.process_over_asyncque())
        loop.create_task(self.process_running_asyncque())
        loop.run_forever()


class all_interface_order_dict_collect():
    # work in machine client receive window order  and send message to window
    def __init__(self):
        self.run_order_order_library = order_library()
        self.order_related_function_set = pandas.read_csv("D:\machine\机器端\machine_action_order.csv")
        self.processSendToCommunicationPipe = None
        self.ProcessSendOrderToWindowPipe = None
        self.interface_operator_obj = self.run_order_order_library.interface_operator_obj
        self.interface_order_libary_dict = self.run_order_order_library
        self.equepmentSingleManager_ = simulate_single.equepmentSingleManager(self.interface_operator_obj)

        print("all interface_order_dict_collect init is over", self.interface_order_libary_dict.order_libary)

    def init_parameter(self, r_cve, s_end):
        self.processSendToCommunicationPipe = s_end
        self.ProcessSendOrderToWindowPipe = s_end
        self.run_order_order_library.init_parameter(r_cve, s_end)
        self.to_machine_set()
        self.obj_need_parameter_set()

    def to_machine_set(self):

        # function_code, function_name, target_ip, send_data
        self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_34 = \
            diesel_engine_power_prepare_window_order(
                "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_34", None,
               self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_34.regist()

        self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_35 = \
            diesel_engine_power_prepare_window_order(
                "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35", None,
                self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(
            self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_35)

        self.test_every_pole_power_distance_ = test_every_pole_power_distance("test_every_pole_power_distance_", None,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.test_every_pole_power_distance_)


        # up is ole code must persist
        self.first_point_coordinate_analysis_manual_process_ok = every_order(
            "first_point_coordinate_analysis_manual_process_ok",
            self.change_parameter_first_point_coordinate_analysis_manual_process_ok,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.first_point_coordinate_analysis_manual_process_ok)
        # pushButton_184    if pole truble is process ok  it's true


        self.operator_top_forward_auto_ = EveryMachineRunOrder(
            "operator_top_forward", self.interface_operator_obj.run,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)
        self.operator_top_forward_manual = EveryMachineRunOrder(
            "operator_top_forward_manual", self.interface_operator_obj.run,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)
        self.operator_top_backward_auto = EveryMachineRunOrder(
            "operator_top_backward_auto", self.interface_operator_obj.run,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)
        self.manual_back_operator_top_backward_ = EveryMachineRunOrder(
            "manual_back_operator_top_backward_", self.interface_operator_obj.run,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)
# ----------------------------- today work ------------------------------
        self.beam_hydraulic_poer_head_both_rotate_and_pull_push = EveryMachineRunOrder(
            "beam_hydraulic_poer_head_both_rotate_and_pull_push", self.beam_hydraulic_power_head_both_rotate_and_pull_push_,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)

        self.horizontalslider_operation_push_pull_gear = EveryMachineRunOrder(
            "horizontalslider_operation_push_pull_gear", self.horizontalslider_operation_push_pull_gear_,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)

        self.horizontalslider_operation_drill_gear = EveryMachineRunOrder(
            "horizontalslider_operation_drill_gear", self.horizontalslider_operation_drill_gear_,
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)


        self.machine_pause_stop = EveryMachineRunOrder(
            "horizontalslider_operation_drill_gear", "stop",
            self.interface_order_libary_dict, self.ProcessSendOrderToWindowPipe, self.interface_operator_obj)
        self.interface_order_libary_dict.regist(self.operator_top_forward_auto_)



    def obj_need_parameter_set(self):
        self.horizontalslider_operation_push_pull_gear_last_point = None


    def horizontalslider_operation_drill_gear_(self, *args):
        current_drill_gear = self.interface_operator_obj.machine_obj.main_beam.current_gear_of_push_pull_rocker(
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.get_current_gear)
        if current_drill_gear < 6:
            current_drill_gear = abs(current_drill_gear - 6)
        elif current_drill_gear == 6:
            current_drill_gear = 0
        else:
            current_drill_gear = current_drill_gear - 6
        parmeter = args[0][0]
        gear_value = parmeter[0]

        if 0 < gear_value <= 6:
            gear_index = abs(gear_value - 6)
        else:
            gear_index = gear_value + 6

        clock_value = parmeter[1]
        rotate_circle = parmeter[2]
        paralle_slider_angle_value = parmeter[3]
        print(" gear_value : {}, clock_value :  {}, rotate_circle : {} ".format(parmeter[0], parmeter[1], parmeter[2],))
        if paralle_slider_angle_value != current_drill_gear:
            self.ProcessSendOrderToWindowPipe.send((
            send_function_code,
            window_ip,
            target_work_code,
            "horizontalSlider_5.setValue",
            current_drill_gear))

        if clock_value == "N" and rotate_circle == "N":
           self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
               self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[gear_index]
           )
        elif clock_value != "N":
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[gear_index]
            )
            if self.interface_operator_obj.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle is None:
                self.interface_operator_obj.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle = 0
            if clock_value == self.interface_operator_obj.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle:
                flag = self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
                    self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[6]
                )
                if flag == True:
                    return True
        elif rotate_circle != "N" and clock_value == "N":
            self.interface_operator_obj.tools_detect_tiger_pole_tight_angle3.current_angle = \
                self.interface_operator_obj.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.interface_operator_obj.tools_detect_tiger_pole_tight_angle3.beam_angle_speed_calclude_and_rotate_number()
            current_rotate_circle_number = self.interface_operator_obj.tools_detect_tiger_pole_tight_angle3.rotate_number
            if current_rotate_circle_number == rotate_circle:
                self.interface_operator_obj.tools_detect_tiger_pole_tight_angle3.calculation_over_re_init()
                return True


    def horizontalslider_operation_push_pull_gear_(self, *args):
        current_push_pull_gear = self.interface_operator_obj.machine_obj.main_beam.current_gear_of_push_pull_rocker(
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull)
        if current_push_pull_gear < 6:
            current_push_pull_gear = abs(current_push_pull_gear-6)
        elif current_push_pull_gear == 6:
            current_push_pull_gear = 0
        else:
            current_push_pull_gear = current_push_pull_gear - 6
        parmeter = args[0][0]
        print(parmeter, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        gear_value = parmeter[0]
        if 0 < gear_value <= 6:
            gear_index = abs(gear_value - 6)
        else:
            gear_index = gear_value + 6
        move_ditance = parmeter[1]
        paralle_slider3_value = parmeter[2]
        move_coordinate = parmeter[3]
        print("current_push_pull_gear ======>", current_push_pull_gear)
        print("paralle_slider3_value ======>", paralle_slider3_value)
        if paralle_slider3_value != current_push_pull_gear:
            self.ProcessSendOrderToWindowPipe.send((
            send_function_code,
            window_ip,
            target_work_code,
            "horizontalSlider_3.setValue",
            current_push_pull_gear))


        if gear_value > 0:
            if self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_push_pull.pressure > \
                    self.interface_operator_obj.machine_obj.main_beam.MAX_PUSH_PRESSURE:
                self.ProcessSendOrderToWindowPipe.send((
                    send_function_code,
                    window_ip,
                    target_work_code,
                    "push_pressure_over_push_pressure_over_pushButton_105",
                    "推力超标"))
                if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[6]) is True:
                    return False
        if gear_value < 0:
            if self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_push_pull.pressure > \
                    self.interface_operator_obj.machine_obj.main_beam.MAX_PULL_PRESSURE:
                self.ProcessSendOrderToWindowPipe.send((
                    send_function_code,
                    window_ip,
                    target_work_code,
                    "pull_pressure_over_push_pressure_over_pushButton_105",
                    "拉力超标"))
                if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                    self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[6]) is True:
                    return False

        if self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate > 800:
            if self.interface_operator_obj.machine_obj.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate > 400:
                if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                     self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[6]) is True:
                    return False



        if move_ditance == "N" and move_coordinate == "N":
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[gear_index])
        elif move_ditance != "N" and move_coordinate == "N":
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[gear_index])
            if self.horizontalslider_operation_push_pull_gear_last_point == None:
                self.horizontalslider_operation_push_pull_gear_last_point = \
                    self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate
            if abs(self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate -
                    self.horizontalslider_operation_push_pull_gear_last_point) > move_ditance:
                if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[
                            6]) is True:
                    return True
        elif move_ditance == "N" and move_coordinate != "N":
            str_parameter_code = "self.interface_operator_obj.machine_obj.main_beam." + move_coordinate
            target_coordinate = eval(str_parameter_code)
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[gear_index])
            if abs(self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - \
                    target_coordinate) < self.interface_operator_obj.machine_obj.main_beam.self.main_beam_of_the_tigger_point_delta:
                if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[
                            6]) is True:
                    return True
        else:
            self.ProcessSendOrderToWindowPipe.send((
            send_function_code,
            window_ip,
            target_work_code,
            "parameter_set_wrong_pushButton_105",
            "设置错误"))
            if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                    self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[6]) is True:
                return False


        # else:
        #     self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
        #         self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[6])

    def beam_hydraulic_power_head_both_rotate_and_pull_push_(self, *args):

        current_push_pull_gear = self.interface_operator_obj.machine_obj.main_beam.current_gear_of_push_pull_rocker(
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull)
        if current_push_pull_gear < 6:
            current_push_pull_gear = abs(current_push_pull_gear-6)
        elif current_push_pull_gear == 6:
            current_push_pull_gear = 0
        else:
            current_push_pull_gear = current_push_pull_gear - 6
        current_drill_gear = self.interface_operator_obj.machine_obj.main_beam.current_gear_of_push_pull_rocker(
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll)
        if current_drill_gear < 6:
            current_drill_gear = abs(current_drill_gear - 6)
        elif current_drill_gear == 6:
            current_drill_gear = 0
        else:
            current_drill_gear = current_drill_gear - 6
        parmeter = args[0][0]
        print("im beam_hydraulic_power_head_both_rotate_and_pull_push_, i receive arg is {arg} ".format(arg=parmeter))
        drill_gear = parmeter[0]
        if 0 < drill_gear <= 6:
            drill_gear_index = abs(drill_gear - 6)
        else:
            drill_gear_index = drill_gear + 6
        clock_value = parmeter[1]
        rotate_circle = parmeter[2]
        pull_push_gear = parmeter[3]
        if 0 < pull_push_gear <= 6:
            pull_push_gear_index = abs(pull_push_gear - 6)
        else:
            pull_push_gear_index = pull_push_gear + 6
        move_ditance = parmeter[4]
        paralle_slider3_value = parmeter[5]
        paralle_slider_angle_value = parmeter[6]
        move_coordinate = parmeter[7]

        if paralle_slider3_value != current_push_pull_gear:
            self.ProcessSendOrderToWindowPipe.send((
            send_function_code,
            window_ip,
            target_work_code,
            "horizontalSlider_3.setValue",
            current_push_pull_gear))
        if paralle_slider_angle_value != current_drill_gear:
            self.ProcessSendOrderToWindowPipe.send((
            send_function_code,
            window_ip,
            target_work_code,
            "horizontalSlider_5.setValue",
            current_push_pull_gear))

        if move_ditance == "N" and move_coordinate == "N":
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[pull_push_gear_index])
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[drill_gear_index]
            )


        elif move_ditance != "N" and move_coordinate == "N":

            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[drill_gear_index]
            )
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[pull_push_gear_index])
            if self.horizontalslider_operation_push_pull_gear_last_point == None:
                self.horizontalslider_operation_push_pull_gear_last_point = \
                    self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate
            if abs(self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate -
                   self.horizontalslider_operation_push_pull_gear_last_point) > move_ditance:
                if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[
                            6]) is True and self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[6]) is True:
                    return True
        elif move_ditance == "N" and move_coordinate != "N":
            str_parameter_code = "self.interface_operator_obj.machine_obj.main_beam." + move_coordinate
            target_coordinate = eval(str_parameter_code)
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[pull_push_gear_index])
            self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.operation_target_coordinate(
                self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[drill_gear_index])

            if abs(self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate - \
                   target_coordinate) < self.interface_operator_obj.machine_obj.main_beam.self.main_beam_of_the_tigger_point_delta:
                if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[
                            6]) is True and self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[6]) is True:
                    return True
        else:
            self.ProcessSendOrderToWindowPipe.send((
            send_function_code,
            window_ip,
            target_work_code,
            "parameter_set_wrong_pushButton_105", "设置错误"))
            if self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                    self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.gear_list[6]) is True and \
                    self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.operation_target_coordinate(
                        self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.gear_list[6]) is True:
                return False

    def to_window_set(self):
        pass

    def equepmentSingleSimulate(self, single_name, order_name, pause_flag, run_flag,):
        self.equepmentSingleManager_.run()




    def change_parameter_first_point_coordinate_analysis_manual_process_ok(self,*args):
        self.interface_operator_obj.first_point_coordinate_analysis.man_intervene_ = args[0][0][1]
        self.interface_operator_obj.manual_rotate_forward_man_prepared_over = args[0][0][1]



class speed_calclude ():
    def __init__(self):
        self.drill_box_grap_hand_speed_first_coordinate = None
        self.drill_box_grap_hand_speed_first_coordinate_time_ = None
        self.current_coordinate = None
        self.current_coordinate_time_ = None
        self.last_speed = None

    def drill_box_power_calclude(self,delt_time):
       self.delta_time = self.current_coordinate_time_ - self.drill_box_grap_hand_speed_first_coordinate_time_
       if self.delta_time > delt_time:
           delta_s = self.current_coordinate - self.drill_box_grap_hand_speed_first_coordinate
           speed = delta_s/self.delta_time
           self.drill_box_grap_hand_speed_first_coordinate_time_ = self.current_coordinate_time_
           self.drill_box_grap_hand_speed_first_coordinate = self.current_coordinate
           self.last_speed = speed
           return speed


class diesel_engine_power_prepare_window_order(every_order):
    def __init__(self, ordername, action_obj, order_library_obj,ProcessSendOrderToWindowPipe,interface_operator_obj):
        super(diesel_engine_power_prepare_window_order,self).__init__(
            ordername,action_obj,order_library_obj, ProcessSendOrderToWindowPipe,interface_operator_obj)
        self.real_target_coordinate = None

        self.flag1 = False
        self.flag2 = False

    # follow is the condition change parameter
    # it's used by function(parameter)  now self.parameter1 = False   self.parameter2 = True instead before parameter
    # the follow notes is the before code
        self.drill_box_grap_hand_speed_first_coordinate = 400
        self.distance = 300
        self.test = False
        self.testsave = False
        self.pushButton_121_test_on = False


    def calclude(self,args,**kwargs):
            if self.testsave == False:

                if self.test == True and self.testsave == False:
                    with open("parameter_backup_data.tex", "rb") as parameter:
                        old_data = pickle.load(parameter)
                    with open("parameter_backup_data.tex", "wb") as parameter2:
                        newdata = {
                            "empty_load": (self.real_target_coordinate, self.speed)}
                        old_data.update(newdata)
                        pickle.dump(old_data, parameter2)

                        # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText(
                        #     str(self.real_target_coordinate))
                        self.ProcessSendOrderToWindowPipe.send(
                            (
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText",
                             str(self.real_target_coordinate)))
                        # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText(
                        #     str(self.speed))
                        self.ProcessSendOrderToWindowPipe.send(
                            (
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText",
                             str(self.speed)))
                        self.save_as_standard = False
                        self.testsave = True
                        return True
                else:
                    if self.order_name_ == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_34":
                        # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_41.setText(
                        #     "保存失败，测试未完成")
                        self.ProcessSendOrderToWindowPipe.send((
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_41.setText",
                             "保存失败，测试未完成"))


                    if self.order_name_ == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35":
                        # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_42.setText(
                        #     "保存失败，测试未完成")
                        self.ProcessSendOrderToWindowPipe.send((
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_42.setText",
                             "保存失败，测试未完成"))

            else:
                if self.test != False:
                    self.test = False
                    self.testsave = False
                if (self.flag1, self.flag2) == (False,False):
                    if self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.hand_run(self.drill_box_grap_hand_speed_first_coordinate) == True:
                        self.drill_box_grap_hand_speed_first_coordinate_time_ = time.time()
                        self.drill_box_grap_hand_speed_first_coordinate =  self.interface_operator_obj.machine_obj.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate
                        self.target_coordinate = self.drill_box_grap_hand_speed_first_coordinate - self.distance
                        self.flag1 = True
                if (self.flag1,self.flag2) == (True,False):
                    if self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.hand_run(self.target_coordinate) == True:
                        self.delata_time = time.time() - self.drill_box_grap_hand_speed_first_coordinate_time_
                        self.real_target_coordinate  = self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate
                        self.speed  = abs( self.real_target_coordinate -  self.drill_box_grap_hand_speed_first_coordinate)/self.delata_time
                        if self.order_name_ == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_34":
                            # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_37.setText(str( self.real_target_coordinate))
                            # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_33.setText(str(self.speed))
                            self.ProcessSendOrderToWindowPipe.send((
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "ui_form_dirll_box_every_pole_distance.lineEdit_37.setText",
                                                      str( self.real_target_coordinate)))
                            self.ProcessSendOrderToWindowPipe.send((
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "ui_form_dirll_box_every_pole_distance.lineEdit_33.setText",
                                                      str(self.speed)))
                            self.test = True
                            return True
                        elif self.order_name_ == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35":
                            self.ProcessSendOrderToWindowPipe.send((
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "ui_form_dirll_box_every_pole_distance.lineEdit_36.setText",
                                                      str(self.real_target_coordinate)))
                            self.ProcessSendOrderToWindowPipe.send((
                                send_function_code,
                                window_ip,
                                target_work_code,
                                "ui_form_dirll_box_every_pole_distance.lineEdit_35.setText",
                                                      str(self.speed)))
                            self.test = True
                            return True

    def run(self, *args):

        if self.time_out != None:
           if  self.time_out < time.time() - self.order_begin_time:
               return False
        T = self.calclude(args[0])


        return T

sys.path.insert(0, "D:\comunication_ui_")
import communication_setting
import communication_tools
send_function_code = communication_setting.function_code6001
window_ip = communication_setting.window_ip
target_work_code = seting.function_code8001
sendData_towin = communication_tools.sendData


class test_every_pole_power_distance(every_order):
    def __init__(self, ordername, action_obj, libaray_obj, ProcessSendOrderToWindowPipe, interface_operator_obj):
        super(test_every_pole_power_distance, self).__init__(ordername, action_obj, libaray_obj, ProcessSendOrderToWindowPipe,
                                                             interface_operator_obj)
        self.box_prepare_obj = interface_operator_obj.box_prepare_obj

        self.ui_form_dirll_box_every_pole_distance_verticalSlider_start_point_coordinate = 300
        self.uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_121_isChecked = False
        data = (
            send_function_code,
            window_ip,
            target_work_code,
            "ui_form_dirll_box_every_pole_distance.verticalSlider_start_point_coordinate",
                             self.ui_form_dirll_box_every_pole_distance_verticalSlider_start_point_coordinate)
        datas = sendData_towin(window_ip, "ui_form_dirll_box_every_pole_distance.verticalSlider_start_point_coordinate",
                                        self.ui_form_dirll_box_every_pole_distance_verticalSlider_start_point_coordinate,)

        self.ProcessSendOrderToWindowPipe.send(datas)
        # self.uui_main_window_obj = uui_main_window_obj

        self.pole_list = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
                          (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
                          (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10)]
        self.flag = False


    def test(self, args):
        print(args[0], args[1], "im in drill column point test")
        if self.flag == False:
            # value = self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.verticalSlider.value()
            result = self.box_prepare_obj.machine_obj.drill_box.hand_run(
                self.ui_form_dirll_box_every_pole_distance_verticalSlider_start_point_coordinate)
            if result == True:
                self.flag = True

        if self.flag == True:
            # if self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_121.isChecked() == True:
            if self.uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_121_isChecked == True:
                if 10 > args[1] >= 0:
                    target = self.box_prepare_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.point1_coordinate
                elif 20 > args[1] >= 10:
                    target = self.box_prepare_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.point2_coordinate
                elif 30 > args[1] >= 20:
                    target = self.box_prepare_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.point3_coordinate
                else:
                    return False
                result = self.box_prepare_obj.machine_obj.drill_box.hand_run(target)
                self.flag = False
                return result

        # args = [7] simple
        # self.radioButton.isChecked()
        # self.radioButton.setChecked()
        # self.radioButton.text()
       # self.set_window.sender()
    # radiobutton = self.tabWidget.sender()

    def run(self, *args):
        if self.time_out != None:
           if  self.time_out < time.time() - self.order_begin_time:
               return False

        t = self.test(args[0])
        return t


class send_machine_single_to_window_communication(every_order):
    pass