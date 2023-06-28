
# this used for machine
import pickle
from 主表 import *
from 主表2 import *
# class order_dicts_set():
#     def __init__(self, order_to_window, order_to_machine, receve_order_que, operator_obj):
#         self.parameter_reset_encodin_push_pull_rock_arm_obj = oldMachineProcess()
#         self.operator_obj = operator_obj
#         self.receve_order_que = receve_order_que
#         self.order_to_machine = order_to_machine
#         self.order_to_window = order_to_window
#         self.order_libary = {}
#         self.order_value = {}
#     def regist(self,order_obj):
#         self.order_libary[order_obj.order_name] = order_obj
#         self.order_value[order_obj.order_name] = (None, order_obj.order_name, None, None, 300)  #
#         # process result, trouble name, trouble start time, trouble end time,assessment time
#         self.save_dict()
#     def save_dict(self):
#         with open("order_recorder" "w+") as save_2:
#             pickle.dump(self.order_value, save_2)
#
#     def receve_and_excute_order(self):
#             while True:
#                recever_order = self.order_to_machine.get()
#                obj = self.order_libary.get(recever_order[0], None)
#                self.parameter_reset_encodin_push_pull_rock_arm_obj.set_zero_encodin_push_pull_equepment(
#                   new_parameter=recever_order)
#                if obj != None:
#                    self.receve_order_que.put(obj)
#
#                else:
#                    self.order_value[recever_order[0]] = recever_order[1]
#                with open("operator_operation_recorder.tex", "w+") as save3:
#                    pickle.dump(recever_order,save3)
# class every_order():
#     def __init__(self,libary_obj, order_name, order_obj, order_to_window, order_to_machine, interface_operator_obj):
#         self.interface_operator_obj = interface_operator_obj
#         self.will_run_obj = order_obj
#         self.order_to_window = order_to_window
#         self.order_to_machine = order_to_machine
#         self.order_name = order_name
#         self.library = libary_obj
#         self.time_out = None
#         self.order_begin_time = None
#         self.regist()
#     def regist(self):
#         self.library.regist(self)
#
#     def run(self, *args, **kwargs):
#         # arg[0] is the parameter data  send from windows  only tuple turn list
#         raise NotImplemented

# class all_interface_order_dict_collect():
#     # work in machine client receive window order  and send message to window
#     def __init__(self,interface_operator_obj,order_to_machine, order_to_window):
#         self.order_to_window = order_to_window
#         self.order_to_machine = order_to_machine
#         self.interface_operator_obj = interface_operator_obj
#         self.interface_order_libary_dict = order_dicts_set(order_to_window, order_to_machine, interface_operator_obj,)
#         # , order_to_window, order_to_machine, receve_order_que, operator_obj,
#         # parameter_reset_encodin_push_pull_rock_arm_obj
#         self.to_machine_set()
#
#
#     def to_machine_set(self):
#         # work in machine client
#         self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_34 = \
#             diesel_engine_power_prepare_window_order(
#                 "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_34", None,
#                self.interface_order_libary_dict, self.order_to_window,self.order_to_machine, self.interface_operator_obj)
#         self.interface_order_libary_dict.regist(
#             self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_34)
#
#         self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_35 = \
#             diesel_engine_power_prepare_window_order(
#                 "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35", None,
#                 self.interface_order_libary_dict, self.order_to_window,self.order_to_machine, self.interface_operator_obj)
#         self.interface_order_libary_dict.regist(self.uui_main_window_obj_ui_form_drill_box_every_pole_distance_pushButton_35)
#
#         self.test_every_pole_power_distance_ = test_every_pole_power_distance("test_every_pole_power_distance_", None,
#             self.interface_order_libary_dict, self.order_to_window,self.order_to_machine, self.interface_operator_obj)
#         self.interface_order_libary_dict.regist(self.test_every_pole_power_distance_)
#
#         # up is ole code must persist
#         self.first_point_coordinate_analysis_manual_process_ok = every_order(
#             "first_point_coordinate_analysis_manual_process_ok",
#             self.change_parameter_first_point_coordinate_analysis_manual_process_ok,
#             self.interface_order_libary_dict, self.order_to_window, self.order_to_machine,self.interface_operator_obj)
#
#         # pushButton_184    if pole truble is process ok  it's true
#
#         self.operator_top_forward = every_order(
#             "operator_top_forward",self.interface_operator_obj.operator_top_forward_auto.run,
#             self.interface_order_libary_dict, self.order_to_window, self.order_to_machine, self.interface_operator_obj)
#         # pushButton_165
#         self.operator_top_backward_auto = every_order(
#             "operator_top_backward_auto",  self.interface_operator_obj.operator_top_backward_auto.run,
#             self.interface_order_libary_dict, self.order_to_window, self.order_to_machine, self.interface_operator_obj
#
#                                                     )
#         # pushButton_152
#         self.operator_top_pause_stop = every_order(
#             "operator_top_backward_auto",self.interface_operator_obj.operator_top_pause_stop.run,
#             self.interface_order_libary_dict, self.order_to_window, self.order_to_machine, self.interface_operator_obj
#                                                  )
#         # pushButton_98
#
#
#
#
#
#
#     def to_window_set(self):
#         pass
#
#
#
#     def change_parameter_first_point_coordinate_analysis_manual_process_ok(self,*args):
#         self.interface_operator_obj.first_point_coordinate_analysis.man_intervene_ = args[0][0][1]
#
#
# class diesel_engine_power_prepare_window_order(every_order):
#     def __init__(self,ordername,order_obj,order_library_obj,order_to_window,order_to_machine,interface_operator_obj):
#         super(diesel_engine_power_prepare_window_order,self).__init__(
#             ordername,order_obj,order_library_obj, order_to_window, order_to_machine,interface_operator_obj)
#         self.real_target_coordinate = None
#
#         self.flag1 = False
#         self.flag2 = False
#
#     # follow is the condition change parameter
#     # it's used by function(parameter)  now self.parameter1 = False   self.parameter2 = True instead before parameter
#     # the follow notes is the before code
#         self.drill_box_grap_hand_speed_first_coordinate = 400
#         self.distance = 300
#         self.test = False
#         self.testsave = False
#         self.pushButton_121_test_on = False
#
#
#     def calclude(self,args,**kwargs):
#             if self.testsave == False:
#                 if self.test == True and self.testsave == False:
#                     with open("parameter_backup_data.tex", "rb") as parameter:
#                         old_data = pickle.load(parameter)
#                     with open("parameter_backup_data.tex", "wb") as parameter2:
#                         newdata = {
#                             "empty_load": (self.real_target_coordinate, self.speed)}
#                         old_data.update(newdata)
#                         pickle.dump(old_data, parameter2)
#
#                         # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText(
#                         #     str(self.real_target_coordinate))
#                         self.order_to_window.put(
#                             ("uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText",
#                              str(self.real_target_coordinate)))
#                         # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText(
#                         #     str(self.speed))
#                         self.order_to_window.put(
#                             ("uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText",
#                              str(self.speed)))
#                         self.save_as_standard = False
#                         self.testsave =True
#                         return True
#                 else:
#                     if self.order_name == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_34":
#                         # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_41.setText(
#                         #     "保存失败，测试未完成")
#                         self.order_to_window.put(
#                             ("uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_41.setText",
#                              "保存失败，测试未完成"))
#
#                         return True
#                     if self.order_name == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35":
#                         # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_42.setText(
#                         #     "保存失败，测试未完成")
#                         self.order_to_window.put(
#                             ("uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_42.setText",
#                              "保存失败，测试未完成"))
#                         return True
#             else:
#                 if self.test != False:
#                     self.test = False
#                     self.testsave = False
#                 if (self.flag1,self.flag2) == (False,False):
#                     # self.drill_box_grap_hand_speed_first_coordinate = self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.verticalSlider.value()
#                     # self.distance = int(self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_32.text())
#                     if self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.hand_run(self.drill_box_grap_hand_speed_first_coordinate) == True:
#                         self.drill_box_grap_hand_speed_first_coordinate_time_ = time.time()
#                         self.drill_box_grap_hand_speed_first_coordinate =  self.interface_operator_obj.machine_obj.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate
#                         self.target_coordinate = self.drill_box_grap_hand_speed_first_coordinate - self.distance
#                         self.flag1 = True
#                 if (self.flag1,self.flag2) == (True,False):
#                     if self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.hand_run(self.target_coordinate) == True:
#                         self.delata_time = time.time() - self.drill_box_grap_hand_speed_first_coordinate_time_
#                         self.real_target_coordinate  = self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate
#                         self.speed  = abs( self.real_target_coordinate -  self.drill_box_grap_hand_speed_first_coordinate)/self.delata_time
#                         if self.order_name == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_34":
#                             # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_37.setText(str( self.real_target_coordinate))
#                             # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_33.setText(str(self.speed))
#                             self.order_to_window.put(("ui_form_dirll_box_every_pole_distance.lineEdit_37.setText",
#                                                       str( self.real_target_coordinate)))
#                             self.order_to_window.put(("ui_form_dirll_box_every_pole_distance.lineEdit_33.setText",
#                                                       str(self.speed)))
#                             self.test = True
#                             return True
#                         elif self.order_name == "uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35":
#                             # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_36.setText(
#                             #     str(self.real_target_coordinate))
#                             # self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_35.setText(
#                             #     str(self.speed))
#                             self.order_to_window.put(("ui_form_dirll_box_every_pole_distance.lineEdit_36.setText",
#                                                       str(self.real_target_coordinate)))
#                             self.order_to_window.put(("ui_form_dirll_box_every_pole_distance.lineEdit_35.setText",
#                                                       str(self.speed)))
#                             self.test = True
#                             return True
#
#
#
#     def run(self,*args,**kwargs):
#         if self.time_out != None:
#            if  self.time_out < time.time() - self.order_begin_time:
#                return False
#         T = self.calclude(args[0],**kwargs)
#
#
#         return T
#
# class test_every_pole_power_distance(every_order):
#     def __init__(self,ordername,order_obj,order_library_obj, order_to_window,order_to_machine, interface_operator_obj):
#         super(test_every_pole_power_distance,self).__init__(
#             ordername,order_obj,order_library_obj, order_to_window, order_to_machine,interface_operator_obj)
#         # self.box_prepare_obj = box_prepare_obj
#         # self.uui_main_window_obj = uui_main_window_obj
#
#         self.pole_list = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
#                           (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
#                           (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10)]
#         self.flag = False
#         self.start_test_point_coordinate = 400
#         self.order_to_window.put(
#             ("ui_form_dirll_box_every_pole_distance.verticalSlider.setValue", self.start_test_point_coordinate))
#         self.test_begin_bottom_checked_value = False
#     def test(self,args,**kwargs):
#         if self.flag == False:
#             # self.start_test_point_coordinate  = self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.verticalSlider.value()
#             result = self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.hand_run(
#                 self.start_test_point_coordinate)
#             if result == True:
#                 self.flag = True
#
#         if self.flag == True:
#             # if self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_121.isChecked() == True:
#             if self.test_begin_bottom_checked_value == True:
#                 if 10 > args[0] >=0:
#                     target = self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.point1_coordinate
#                 elif 20 > args[0] >= 10:
#                     target = self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.point2_coordinate
#                 elif 30 > args[0] >= 20:
#                     target = self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.Equepment_drill_box_digit_piont.point3_coordinate
#                 else:
#                     return False
#                 result = self.interface_operator_obj.box_prepare_obj.machine_obj.drill_box.hand_run(target)
#                 self.flag = False
#                 return result
#
#
#
#     def run(self,*args,**kwargs):
#         if self.time_out != None:
#            if  self.time_out < time.time() - self.order_begin_time:
#                return False
#         T = self.test(args[0],**kwargs)
#
#
#         return T