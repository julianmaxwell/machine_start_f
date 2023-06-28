# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主表.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主表.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import inspect
import struct
import sys
import os
import time
import pickle
from multiprocessing import Pipe
import uuid
import threading
from functools import partial
sys.path.append(r"D:\comunication_ui_")
import communication_
import communication_setting
import communication_tools
import pandas
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIntValidator
from main_window2 import Ui_MainWindow
import guide_start_to_pole
import out_hole_guide
import guidin_control
import drill_box_every_pole_distance


import setting

machine_id = setting.bmachine_id
b_struct_code_0 = struct.pack("b", 0)
machine_ip = communication_setting.locale_lisen_ip
import seting
function_code6001 = communication_setting.function_code6001
function_code6002 = communication_setting.function_code6002
function_code6003 = communication_setting.function_code6003
function_code6004 = communication_setting.function_code6004
function_code8001 = communication_setting.function_code8001

"""
    target_obj.send_pipe = return_s
    target_obj.recve_pipe = return_r
"""


class UUi_MainWindow(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super(UUi_MainWindow, self).setupUi(MainWindow)
        super(UUi_MainWindow, self).retranslateUi(MainWindow)
        communication_.create_communication_thread(self)
        self.orderSendToMachineProcessPipe = None
        self.current_operator = True
        self.current_operate_machine_id = None
        self.permit_data = self.get_operator_data()
        self.parameter_backup_data = {}
        self.stacke_add()
        self.sendData = communication_tools.sendData
        self.set_widget_ui()
        self.single_connect()
        self.message_lable_menu = [
            [self.pushButton_297, self.label_230, self.label_227, self.label_228, self.label_229],
            [self.pushButton_298, self.label_233, self.label_231, self.label_232, self.label_234],
            [self.pushButton_299, self.label_237, self.label_235, self.label_236, self.label_238],
            [self.pushButton_300, self.label_241, self.label_239, self.label_240, self.label_242],
            [self.pushButton_301, self.label_245, self.label_243, self.label_244, self.label_246],
            [self.pushButton_302, self.label_249, self.label_247, self.label_248, self.label_250],
        ]

        self.init_message_box()
        self.pushButton_184.setVisible(False)
        self.function_code_map_function = {

            function_code8001: self.function_code8001,
            "comminication_connected_fail": self.comminication_connected_fail,
            "ui_window.lineEdit_5.setText": self.lineEdit_5.setText,
            "ui_window.lineEdit_6.setText": self.lineEdit_6.setText,
            "ui_window.lineEdit_14.setText": self.lineEdit_14.setText,
            "ui_window.lineEdit_15.setText": self.lineEdit_15.setText,
            "ui_window.lineEdit_8.setText": self.lineEdit_8.setText,
            "ui_window.lineEdit_9.setText": self.lineEdit_9.setText,
            "ui_window.lineEdit_10.setText": self.lineEdit_10.setText,
            "ui_window.lineEdit_23.setText": self.lineEdit_23.setText,
            "ui_window.lineEdit_31.setText": self.lineEdit_31.setText,
            "ui_window.lineEdit_28.setText": self.lineEdit_28.setText,
            "ui_window.pushButton_111.setText": self.pushButton_111.setText,
            "ui_window.pushButton_122.setText": self.pushButton_122.setText,
            "ui_window.pushButton_113.setText": self.pushButton_113.setText,
            "ui_window.pushButton_115.setText": self.pushButton_115.setText,
            "ui_window.pushButton_124.setText": self.pushButton_124.setText,
            "ui_window.pushButton_140.setText": self.pushButton_140.setText,
            "ui_window.pushButton_123.setText": self.pushButton_123.setText,
            "ui_window.pushButton_114.setText": self.pushButton_114.setText,
            "ui_window.pushButton_116.setText": self.pushButton_116.setText,
            "ui_window.pushButton_117.setText": self.pushButton_117.setText,
            "ui_window.pushButton_118.setText": self.pushButton_118.setText,
            "ui_window.pushButton_325.setText": self.pushButton_325.setText,
            "ui_window.pushButton_173.setText": self.pushButton_173.setText,
            "ui_window.pushButton_174.setText": self.pushButton_174.setText,
            "ui_window.pushButton_324.setText": self.pushButton_324.setText,
            "ui_window.pushButton_121.setText": self.pushButton_121.setText,
            "ui_window.pushButton_120.setText": self.pushButton_120.setText,
            "ui_window.lineEdit_34.setText": self.lineEdit_34.setText,
            "ui_window.lineEdit_37.setText": self.lineEdit_37.setText,
            "ui_window.lineEdit_38.setText": self.lineEdit_38.setText,
            "ui_window.lineEdit_76.setText": self.lineEdit_76.setText,
            "ui_window.lineEdit_89.setText": self.lineEdit_89.setText,
            "ui_window.lineEdit_90.setText": self.lineEdit_90.setText,
            "ui_window.lineEdit_91.setText": self.lineEdit_91.setText,
            "ui_window.lineEdit_75.setText": self.lineEdit_75.setText,
            "ui_window.lineEdit_79.setText": self.lineEdit_79.setText,
            "ui_window.lineEdit_82.setText": self.lineEdit_82.setText,
            "ui_window.lineEdit_109.setText": self.lineEdit_109.setText,
            "ui_window.lineEdit_77.setText": self.lineEdit_77.setText,
            "ui_window.lineEdit_80.setText": self.lineEdit_80.setText,
            "ui_window.lineEdit_84.setText": self.lineEdit_84.setText,
            "ui_window.lineEdit_92.setText": self.lineEdit_92.setText,
            "ui_window.lineEdit_93.setText": self.lineEdit_93.setText,
            "ui_window.lineEdit_94.setText": self.lineEdit_94.setText,
            "ui_window.lineEdit_78.setText": self.lineEdit_78.setText,
            "ui_window.lineEdit_81.setText": self.lineEdit_81.setText,
            "ui_window.lineEdit_85.setText": self.lineEdit_85.setText,
            "ui_window.lineEdit_110.setText": self.lineEdit_110.setText,
            "ui_window.lineEdit_111.setText": self.lineEdit_111.setText,
            "ui_window.lineEdit_135.setText": self.lineEdit_135.setText,
            "ui_window.lineEdit_136.setText": self.lineEdit_136.setText,
            "ui_window.lineEdit_86.setText": self.lineEdit_86.setText,
            "ui_window.lineEdit_87.setText": self.lineEdit_87.setText,
            "ui_window.lineEdit_88.setText": self.lineEdit_88.setText,
            # ui_form_dirll_box_every_pole_distance
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText":
                self.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText":
                self.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_41.setText":
                self.ui_form_dirll_box_every_pole_distance.pushButton_41.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_42.setText":
                self.ui_form_dirll_box_every_pole_distance.pushButton_42.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_37.setText":
                self.ui_form_dirll_box_every_pole_distance.lineEdit_37.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_33.setText":
                self.ui_form_dirll_box_every_pole_distance.lineEdit_33.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_36.setText":
                self.ui_form_dirll_box_every_pole_distance.lineEdit_36.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_35.setText":
                self.ui_form_dirll_box_every_pole_distance.lineEdit_35.setText,

            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.verticalSlider.setValue":
                self.ui_form_dirll_box_every_pole_distance.verticalSlider.setValue,

            "pushButton_184.setVisible(False))": self.pushButton_184.setVisible,
            "machine_obj.wrong_data": self.write_all_message_box_every_data,
            "machine_base_pin_instantaneous_read_data": self.window_show,
            "machine_equepment_instantaneous_read_data": self.window_show

        }


    def window_show(self, data):
        """
        it send map file is D:\machine\机器端\machine_high_lever_equepment.py  machine class colect_data_to_que method
        """
        self.label_221.setText(str(data["main_beam_coordinate_single1"]))
        self.label_222.setText(str(data["main_beam_cycle_number_coordinate_single1"]))

        self.label_223.setText(str(data["hand_grap_coordinate_single2"]))
        self.label_226.setText(str(data["main_beam_taile_20cm_single3"]))
        self.label_297.setText(str(data["main_beam_head_20cm_single4"]))
        self.label_313.setText(str(data["main_beam_pulpush_rocer_arm_coordinate_single5"]))
        self.label_315.setText(str(data["drill_rocker_arm_coordinate_single6"]))
        self.label_319.setText(str(data["pole_angle_single7"]))
        self.label_321.setText(str(data["warter_deep_coordinate_single8"]))
        self.label_332.setText(str(data["outer_tiger_rocker_arm_coordinate_single9"]))
        self.label_334.setText(str(data["inner_tiger_rocker_arm_coordinate_single10"]))
        self.label_336.setText(str(data["loose_tiger_rocker_arm_coordinate_single11"]))
        self.label_338.setText(str(data["water_pressure_single12"]))
        self.label_356.setText(str(data["push_pull_pressure_single13"]))
        self.label_358.setText(str(data["drill_pressure_single14"]))
        self.label_582.setText(str(data["dirll_box_up_dow_point_single15"]))
        self.label_54.setText(str(data["angle_0_corectting"]))
        self.lineEdit_75.setText(str(data["first_point_coordinate"]))
        self.lineEdit_77.setText(str(data["second_point_coordinate"]))
        self.lineEdit_78.setText(str(data["fourth_point_coordinate"]))
        self.lineEdit_86.setText(str(data["third_point_coordinate"]))
        self.lineEdit_92.setText(str(data["taile_thread_is_ok_point_coordinate"]))
        self.ui_form_dirll_box_every_pole_distance.label_3.setText(str(data["hand_grap_coordinate_single2"]))
        self.ui_form_dirll_box_every_pole_distance.label_4.setText(str(data["hand_grap_coordinate_single2"]))
        self.ui_form_dirll_box_every_pole_distance.label_11.setText(str(data["hand_grap_coordinate_single2"]))

    def function_code8001(self, data):
        print(__file__, inspect.currentframe().f_code.co_name, inspect.currentframe().f_lineno)
        print(data)
        if type(data) is str:
            function_ = self.function_code_map_function.get(data, None)
        else:
            function_ = self.function_code_map_function.get(data[0], None)
        if function_:
            if type(data) is str:
                function_()
            else:
                function_(data[1:])
        print(__file__, "return ui function act over")




    def init_parameter(self, r_cve, s_end):
        self.orderSendToMachineProcessPipe = s_end

    def single_connect(self):
        self.deepfirst = True

        self.ff = calclude_pole_guide_parameter()

        self.verticalSlider_6.valueChanged.connect(self.set_pole_out_thread)
        self.verticalSlider_24.valueChanged.connect(self.set_tiger_loose_time_)
        self.verticalSlider_25.valueChanged.connect(self.set_pole_taile_mother_thread_out_circle_)
        self.verticalSlider_26.valueChanged.connect(self.pole_taile_mother_thread_out_pressure)
        self.verticalSlider_13.valueChanged.connect(self.pole_and_pole_thread_connetct_max_pressure)
        self.verticalSlider_19.valueChanged.connect(self.pole_and_pole_thread_connetct_drill_level)
        self.verticalSlider_27.valueChanged.connect(self.pole_and_pole_thread_connetct_push_level)
        self.verticalSlider_40.valueChanged.connect(self.tiger_dirll_pole_pole_tight_push_max_pressure)
        self.verticalSlider_41.valueChanged.connect(self.tiger_forward_move_max_coordinate_)
        self.verticalSlider_42.valueChanged.connect(self.tiger_coordinate_beam_not_reach_beamself_slot_)
        self.verticalSlider_43.valueChanged.connect(self.tiger_coordinate_beam_reached_beamself_slot_)
        self.verticalSlider_28.valueChanged.connect(self.tiger_self_middle_zero_coordinate__)



        self.verticalSlider_18.valueChanged.connect(self.pole_loose_need_mini_circle)
        self.verticalSlider_20.valueChanged.connect(self.pole_loose_need_mini_circle_drill_level)
        self.verticalSlider_22.valueChanged.connect(self.set_drill_box_grap_hand_tight_slight)
        self.verticalSlider_21.valueChanged.connect(self.set_drill_box_grap_hand_tight_strong)
        self.verticalSlider_74.valueChanged.connect(self.set_drill_box_grap_hand_tight_greater_strong)

        self.verticalSlider_29.valueChanged.connect(self.set_drill_box_grap_hand_relax_full)
        self.verticalSlider_30.valueChanged.connect(self.set_drill_box_relax_half)
        self.verticalSlider_73.valueChanged.connect(self.set_drill_box_grap_hand_relax_greater_part)

        self.verticalSlider_23.valueChanged.connect(self.set_tiger_tight_time_)


        self.pushButton.clicked.connect(self.operator_top_forward_manual)
        # self.pushButton.pressed.connect()
        self.pushButton_2.clicked.connect(self.machine_pause_stop)
        self.pushButton_4.clicked.connect(self.manual_back_operator_top_backward_)
        self.pushButton_24.clicked.connect(self.operate_lock_pushButton_24)
        self.pushButton_67.clicked.connect(self.operate_lock_pushButton_67)

        self.pushButton_5.clicked.connect(self.set_parameters_middle_tigger_teeth)
        self.pushButton_6.clicked.connect(self.set_parameters_middle_tigger_back_20_thread)
        self.pushButton_7.clicked.connect(self.set_parameters__back_pole_taile_thread)
        self.pushButton_8.clicked.connect(self.set_parameters_back_taile_5cm)
        self.pushButton_9.clicked.connect(self.set_parameters_the_beam_point_box_hand_can_out_to_get_pole)
        self.pushButton_10.clicked.connect(self.set_parameters_the_last_come_back_pole_to_unload)
        self.pushButton_11.clicked.connect(self.the_drill_box_down_to_grap_hand_can_hold_point)
        self.pushButton_12.clicked.connect(self.the_drill_box_up_to_the_top)
        self.pushButton_13.clicked.connect(self.the_drill_box_down_the_bottom)
        self.pushButton_14.clicked.connect(self.set_parameter_the_man_let_pole_beam_point)
        self.pushButton_22.clicked.connect(self.man_let_pole_and_machin_back_the_last_point)
        self.pushButton_15.clicked.connect(self.the_beam_to_the_coordinate_man_can_get_out_pole)
        self.pushButton_16.clicked.connect(self.drill_box_1_coordinate_grap_hand_coordinate)
        self.pushButton_17.clicked.connect(self.drill_box_2_coordinate_grap_hand_coordinate)
        self.pushButton_18.clicked.connect(self.drill_box_3_coordinate_grap_hand_coordinate)
        self.pushButton_19.clicked.connect(self.dirll_box_grap_hand_to_beam_get_pole)
        self.pushButton_20.clicked.connect(self.dirll_box_grap_hand_to_beam_relax_hand_coordinate)
        self.pushButton_21.clicked.connect(self.dirll_box_grap_hand_to_beam_cant_stop_beam_coordinate)
        self.pushButton_40.clicked.connect(self.encode_distance_messuer_push_pull_start)
        self.pushButton_41.clicked.connect(self.encode_distance_messuer_push_pull_stop)
        self.pushButton_43.clicked.connect(self.encode_distance_messuer_push_pull_end)
        self.pushButton_58.clicked.connect(self.encode_distance_messuer_drill_rocker_arm_coordinate_start)
        self.pushButton_59.clicked.connect(self.encode_distance_messuer_drill_rocker_arm_coordinate_stop)
        self.pushButton_60.clicked.connect(self.encode_distance_messuer_drill_rocker_arm_coordinate_end)
        self.pushButton_64.clicked.connect(self.encode_distance_messuer_outer_tiger_arm_coordinate_start)
        self.pushButton_66.clicked.connect(self.encode_distance_messuer_outer_tiger_arm_coordinate_stop)
        self.pushButton_79.clicked.connect(self.encode_distance_messuer_outer_tiger_arm_coordinate_end)
        self.pushButton_82.clicked.connect(self.encode_distance_messuer_inner_tiger_arm_coordinate_start)
        self.pushButton_80.clicked.connect(self.encode_distance_messuer_inner_tiger_arm_coordinate_stop)
        self.pushButton_81.clicked.connect(self.encode_distance_messuer_inner_tiger_arm_coordinate_end)
        self.pushButton_53.clicked.connect(self.encode_distance_messuer_tiger_dirll_arm_coordinate_start)
        self.pushButton_54.clicked.connect(self.encode_distance_messuer_tiger_dirll_arm_coordinate_stop)
        self.pushButton_55.clicked.connect(self.encode_distance_messuer_tiger_dirll_arm_coordinate_end)
        self.pushButton_35.clicked.connect(self.guide_connect_start_into_hole)
        self.pushButton_36.clicked.connect(self.guide_connect_guiding)
        self.pushButton_39.clicked.connect(self.guide_connect_out_hole)
        self.pushButton_42.clicked.connect(self.Equepment_data_disaplay)
        self.pushButton_29.clicked.connect(self.save_parameter)
        self.pushButton_28.clicked.connect(self.load_parameter)
        self.pushButton_56.clicked.connect(self.lock_operation)
        self.pushButton_188.clicked.connect(self.mannual_data_use)

        self.pushButton_47.clicked.connect(self.set_current_rock_arm)
        self.pushButton_62.clicked.connect(self.set_parameters_pole_in_middle_tiger_tooth_to_taile_tofaward)
        self.pushButton_76.clicked.connect(self.drill_box_every_pole_distance)
        self.pushButton_157.clicked.connect(self.use_drill_box)
        self.pushButton_155.clicked.connect(self.use_drill_box2)
        self.pushButton_151.clicked.connect(self.use_drill_box2_back)
        self.pushButton_156.clicked.connect(self.use_drill_box2_set_derect_and_move)
        self.pushButton_147.clicked.connect(self.use_drill_box2_stop_forward)
        self.pushButton_121.clicked.connect(self.set_tiger_loose_time_set)

        self.pushButton_165.clicked.connect(self.operator_top_forward)

        self.pushButton_117.clicked.connect(self.set_drill_box_grap_hand_tight_strong_set)
        self.pushButton_325.clicked.connect(self.drill_box_grap_hand_tight_greater_strong_set)
        self.pushButton_173.clicked.connect(self.drill_box_grap_hand_relax_full)
        self.pushButton_174.clicked.connect(self.drill_box_relax_half)
        self.pushButton_324.clicked.connect(self.drill_box_grap_hand_relax_greater_part)

        self.horizontalSlider_2.valueChanged.connect(self.push_pull_leverl)
        self.horizontalSlider_4.valueChanged.connect(self.guide_turn_angle)

        self.pushButton_93.clicked.connect(self.manual_opration_turn)
        self.pushButton_94.clicked.connect(self.befor_opration_check)
        self.pushButton_92.clicked.connect(self.auto_operation)
        self.pushButton_111.clicked.connect(self.set_pole_out_thread_parameter)
        self.pushButton_122.clicked.connect(self.set_pole_taile_mother_thread_out_circle_numeber)
        self.pushButton_123.clicked.connect(self.set_pole_taile_mother_thread_out_pressure)
        self.pushButton_113.clicked.connect(self.set_pole_and_pole_thread_connetct_max_pressure)
        self.pushButton_115.clicked.connect(self.set_pole_and_pole_thread_connetct_max_drill_level)
        self.pushButton_124.clicked.connect(self.set_pole_and_pole_thread_connetct_max_push_level)
        self.pushButton_140.clicked.connect(self.set_tiger_dirll_pole_pole_tight_push_max_pressure)
        self.pushButton_141.clicked.connect(self.set_tiger_forward_move_max_coordinate)
        self.pushButton_142.clicked.connect(self.set_tiger_coordinate_beam_not_reach_beamself_slot)
        self.pushButton_143.clicked.connect(self.set_tiger_coordinate_beam_reached_beamself_slot)
        self.pushButton_125.clicked.connect(self.set_tiger_self_middle_zero_coordinate_)

        self.pushButton_114.clicked.connect(self.set_pole_loose_need_mini_circle)
        self.pushButton_116.clicked.connect(self.set_pole_loose_need_mini_circle_drill_level)
        self.pushButton_112.clicked.connect(self.pole_funtion_set)
        self.pushButton_268.clicked.connect(self.machin_delta_set)

        self.pushButton_119.clicked.connect(self.tigger_tight_functionset)
        self.pushButton_96.clicked.connect(self.drill_box_function_set)
        self.pushButton_97.clicked.connect(self.beam_base_function_set)
        self.pushButton_135.clicked.connect(self.interface_function_set)

        self.pushButton_120.clicked.connect(self.set_tiger_tight_time_set)
        self.pushButton_118.clicked.connect(self.set_drill_box_grap_hand_tight_slight_set)

        self.pushButton_128.clicked.connect(self.no_load_move_to_coordinnate_point_max_pressure)
        self.pushButton_129.clicked.connect(self.no_load_move_start_level)
        self.pushButton_130.clicked.connect(self.no_load_move_end_level)
        self.pushButton_132.clicked.connect(self.no_load_move_parameter_contrl_distance)

        self.pushButton_175.clicked.connect(self.tiger_touch_delta)
        self.pushButton_177.clicked.connect(self.beam_push_pull_in_tiger_step_distance)
        self.pushButton_179.clicked.connect(self.delta_contrast_beam_ruler_tiger_ruler_)



        self.pushButton_137.clicked.connect(self.first_point_coordinate)
        self.pushButton_144.clicked.connect(self.first_point_coordinate_delta)
        self.pushButton_149.clicked.connect(self.first_point_coordinate_map_tiger_ruler_range)
        self.pushButton_267.clicked.connect(self.first_point_characteristic_success_value)

        self.pushButton_138.clicked.connect(self.second_point_coordinate)
        self.pushButton_145.clicked.connect(self.second_point_coordinate_delta)
        self.pushButton_153.clicked.connect(self.second_point_coordinate_map_tiger_ruler_range)


        self.pushButton_181.clicked.connect(self.taile_thread_is_ok_point_coordinate)
        self.pushButton_182.clicked.connect(self.taile_thread_is_ok_point_coordinate_delat)
        self.pushButton_183.clicked.connect(self.taile_thread_is_ok_point_coordinate_map_tiger_ruler_range)




        self.pushButton_158.clicked.connect(self.third_point_coordinate)
        self.pushButton_162.clicked.connect(self.third_point_coordinate_delta)
        self.pushButton_172.clicked.connect(self.third_point_coordinate_map_tiger_ruler_range)

        self.pushButton_139.clicked.connect(self.fourth_point_coordinate)
        self.pushButton_146.clicked.connect(self.fourth_point_coordinate_delta)
        self.pushButton_154.clicked.connect(self.fourth_point_coordinate_map_tiger_ruler_range)

        self.pushButton_270.clicked.connect(self.Equepment_line_distance_measure_4m_beam_coordinate_delta)
        self.pushButton_272.clicked.connect(self.Equepment_line_distance_measure_beam_taile_coordinate_delta)
        self.pushButton_320.clicked.connect(self.Equepment_line_distance_measure_beam_head_coordinate_delta)
        self.pushButton_322.clicked.connect(self.Equepment_line_distance_measure_dirll_box_updown_coordinate_delta)
        self.pushButton_327.clicked.connect(self.dirllbox_1m_ruler)

        self.pushButton_184.clicked.connect(self.first_point_coordinate_analysis_manual_process_ok)






        self.ui_form_dirll_box_every_pole_distance.pushButton_114.clicked.connect(self.dirll_box_every_pole_distance_set_lock)
        self.ui_form_dirll_box_every_pole_distance.pushButton_10.clicked.connect(self.dirll_box_inner_column_1)
        self.ui_form_dirll_box_every_pole_distance.pushButton_9.clicked.connect(self.dirll_box_inner_column_2)
        self.ui_form_dirll_box_every_pole_distance.pushButton_8.clicked.connect(self.dirll_box_inner_column_3)
        self.ui_form_dirll_box_every_pole_distance.pushButton_7.clicked.connect(self.dirll_box_inner_column_4)
        self.ui_form_dirll_box_every_pole_distance.pushButton_6.clicked.connect(self.dirll_box_inner_column_5)
        self.ui_form_dirll_box_every_pole_distance.pushButton_5.clicked.connect(self.dirll_box_inner_column_6)
        self.ui_form_dirll_box_every_pole_distance.pushButton_4.clicked.connect(self.dirll_box_inner_column_7)
        self.ui_form_dirll_box_every_pole_distance.pushButton_3.clicked.connect(self.dirll_box_inner_column_8)
        self.ui_form_dirll_box_every_pole_distance.pushButton_2.clicked.connect(self.dirll_box_inner_column_9)
        self.ui_form_dirll_box_every_pole_distance.pushButton.clicked.connect(self.dirll_box_inner_column_10)
        self.ui_form_dirll_box_every_pole_distance.pushButton_23.clicked.connect(self.drill_box_middle_column_1)
        self.ui_form_dirll_box_every_pole_distance.pushButton_21.clicked.connect(self.drill_box_middle_column_2)
        self.ui_form_dirll_box_every_pole_distance.pushButton_17.clicked.connect(self.drill_box_middle_column_3)
        self.ui_form_dirll_box_every_pole_distance.pushButton_15.clicked.connect(self.drill_box_middle_column_4)
        self.ui_form_dirll_box_every_pole_distance.pushButton_16.clicked.connect(self.drill_box_middle_column_5)
        self.ui_form_dirll_box_every_pole_distance.pushButton_20.clicked.connect(self.drill_box_middle_column_6)
        self.ui_form_dirll_box_every_pole_distance.pushButton_22.clicked.connect(self.drill_box_middle_column_7)
        self.ui_form_dirll_box_every_pole_distance.pushButton_14.clicked.connect(self.drill_box_middle_column_8)
        self.ui_form_dirll_box_every_pole_distance.pushButton_19.clicked.connect(self.drill_box_middle_column_9)
        self.ui_form_dirll_box_every_pole_distance.pushButton_18.clicked.connect(self.drill_box_middle_column_10)
        self.ui_form_dirll_box_every_pole_distance.pushButton_33.clicked.connect(self.drill_box_outter_column_1)
        self.ui_form_dirll_box_every_pole_distance.pushButton_31.clicked.connect(self.drill_box_outter_column_2)
        self.ui_form_dirll_box_every_pole_distance.pushButton_27.clicked.connect(self.drill_box_outter_column_3)
        self.ui_form_dirll_box_every_pole_distance.pushButton_25.clicked.connect(self.drill_box_outter_column_4)
        self.ui_form_dirll_box_every_pole_distance.pushButton_26.clicked.connect(self.drill_box_outter_column_5)
        self.ui_form_dirll_box_every_pole_distance.pushButton_30.clicked.connect(self.drill_box_outter_column_6)
        self.ui_form_dirll_box_every_pole_distance.pushButton_32.clicked.connect(self.drill_box_outter_column_7)
        self.ui_form_dirll_box_every_pole_distance.pushButton_24.clicked.connect(self.drill_box_outter_column_8)
        self.ui_form_dirll_box_every_pole_distance.pushButton_29.clicked.connect(self.drill_box_outter_column_9)
        self.ui_form_dirll_box_every_pole_distance.pushButton_28.clicked.connect(self.drill_box_outter_column_10)
        self.ui_form_dirll_box_every_pole_distance.verticalSlider.valueChanged.connect(self.set_drillbox_begin_to_column_to_put_back_pole_coordinate)
        self.ui_form_dirll_box_every_pole_distance.pushButton_43.clicked.connect(self.grap_hand_start_run_point_set)


        self.ui_form_dirll_box_every_pole_distance.horizontalSlider.valueChanged.connect(self.set_drill_box_grap_hand_move_errow_range)
        self.ui_form_dirll_box_every_pole_distance.horizontalSlider_2.valueChanged.connect(self.set_drill_box_up_down_errow_range)
        self.ui_form_dirll_box_every_pole_distance.pushButton_36.clicked.connect(self.set_drill_box_staked_parameter)
        self.ui_form_dirll_box_every_pole_distance.pushButton_37.clicked.connect(self.set_drill_box_staked_parameter_result)
        self.ui_form_dirll_box_every_pole_distance.pushButton_38.clicked.connect(self.set_drill_box_stacked_parameter_distance)
        self.ui_form_dirll_box_every_pole_distance.pushButton_34.clicked.connect(self.test_diesel_engine_power)
        self.ui_form_dirll_box_every_pole_distance.pushButton_41.clicked.connect(self.save_standard_diesel_engine_power)
        self.ui_form_dirll_box_every_pole_distance.pushButton_35.clicked.connect(self.test_diesel_engine_load_test)
        self.ui_form_dirll_box_every_pole_distance.pushButton_42.clicked.connect(self.load_test_diesel_engine_load_test)
        self.ui_form_dirll_box_every_pole_distance.pushButton_118.clicked.connect(self.hand_box_run_uncoreccte_rangge)
        self.ui_form_dirll_box_every_pole_distance.pushButton_119.clicked.connect(self.drill_box_up_down_uncorecte_range)
        self.ui_form_dirll_box_every_pole_distance.radioButton.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_2.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_3.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_4.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_5.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_6.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_7.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_8.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_9.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_10.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_11.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_12.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_13.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_14.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_15.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_16.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_17.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_18.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_19.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_20.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_21.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_22.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_23.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_24.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_25.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_26.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_27.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_28.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_29.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.radioButton_30.clicked.connect(self.test_drill_box_every_pole_power)
        self.ui_form_dirll_box_every_pole_distance.pushButton_121.clicked.connect(self.test_begin__)

        self.pushButton_78.clicked.connect(self.angle_zero_correcting)


    def comminication_connected_fail(self):
        self.label_121.setText("连接错误， 对方机器不在线")

    def fourth_point_coordinate_delta(self):
        try:
            value = float(self.lineEdit_81.text())
        except:
            self.lineEdit_81.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_146.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(
                ("fourth_point_coordinate_delta", value))
            self.parameter_backup_data["fourth_point_coordinate_delta"] = value
            self.pushButton_146.setText("公头跑出虎头对应虎牙坐标误差范围" + str(value) + "已经保存")

    def fourth_point_coordinate_map_tiger_ruler_range(self):
        try:
            value = float(self.lineEdit_85.text())
        except:
            self.lineEdit_85.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_154.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("fourth_point_coordinate_map_tiger_ruler_range", value))
            self.parameter_backup_data["fourth_point_coordinate_map_tiger_ruler_range"] = value
            self.pushButton_154.setText("公头跑出虎头对应虎牙尺特征值" + str(value) + "已经保存")

    def Equepment_line_distance_measure_4m_beam_coordinate_delta(self):
        try:
            value = float(self.lineEdit_110.text())
        except:
            self.lineEdit_110.setText("数据错误,取缺省值5")
            value = 120
        if self.pushButton_270.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("Equepment_line_distance_measure_4m_beam_coordinate_delta", value))
            self.parameter_backup_data["Equepment_line_distance_measure_4m_beam_coordinate_delta"] = value
            self.pushButton_270.setText("大梁移动测量误差范围" + str(value) + "已经保存")

    def Equepment_line_distance_measure_beam_taile_coordinate_delta(self):
        try:
            value = float(self.lineEdit_111.text())
        except:
            self.lineEdit_111.setText("数据错误,取缺省值5")
            value = 120
        if self.pushButton_272.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("Equepment_line_distance_measure_beam_taile_coordinate_delta", value))
            self.parameter_backup_data["Equepment_line_distance_measure_beam_taile_coordinate_delta"] = value
            self.pushButton_272.setText("大梁尾部尺子测量误差" + str(value) + "已经保存")

    def Equepment_line_distance_measure_beam_head_coordinate_delta(self):
        try:
            value = float(self.lineEdit_135.text())
        except:
            self.lineEdit_135.setText("数据错误,取缺省值5")
            value = 120
        if self.pushButton_320.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("Equepment_line_distance_measure_beam_head_coordinate_delta", value))
            self.parameter_backup_data["Equepment_line_distance_measure_beam_head_coordinate_delta"] = value
            self.pushButton_320.setText("大梁尾部尺子测量误差" + str(value) + "已经保存")

    def Equepment_line_distance_measure_dirll_box_updown_coordinate_delta(self):
        try:
            value = float(self.lineEdit_136.text())
        except:
            self.lineEdit_136.setText("数据错误,取缺省值5")
            value = 120
        if self.pushButton_322.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("Equepment_line_distance_measure_dirll_box_updown_coordinate_delta", value))
            self.parameter_backup_data["Equepment_line_distance_measure_dirll_box_updown_coordinate_delta"] = value
            self.pushButton_322.setText("大梁尾部尺子测量误差" + str(value) + "已经保存")

    def dirllbox_1m_ruler(self):
        try:
            value = float(self.lineEdit_137.text())
        except:
            self.lineEdit_137.setText("数据错误,取缺省值5")
            value = 10
        if self.pushButton_327.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("drill_box.Equepment_drill_box_digit_piont.pole_point_delta", value))
            self.parameter_backup_data["drill_box.Equepment_drill_box_digit_piont.pole_point_delta"] = value
            self.pushButton_327.setText("钻箱1米尺子测量误差" + str(value) + "已经保存")


    def first_point_coordinate_analysis_manual_process_ok(self):
        if self.pushButton_184.isChecked() is True:
            self.orderSendToMachineProcessPipe.send(("first_point_coordinate_analysis_manual_process_ok", True))
        else:
            self.orderSendToMachineProcessPipe.send(("first_point_coordinate_analysis_manual_process_ok", False))



    def fourth_point_coordinate(self):
        try:
            value = float(self.lineEdit_78.text())
        except:
            self.lineEdit_78.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_139.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("fourth_point_coordinate", value))
            self.parameter_backup_data["fourth_point_coordinate"] = value
            self.pushButton_139.setText("公头跑出虎头特征值" + str(value) + "已经保存")
            self.label_109.setText(str(value))



    def third_point_coordinate(self):
        try:
            value = float(self.lineEdit_86.text())
        except:
            self.lineEdit_86.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_158.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("third_point_coordinate", value))
            self.parameter_backup_data["third_point_coordinate"] = value
            self.pushButton_158.setText("成功到达虎牙中特征值" + str(value) + "已经保存")
            self.label_111.setText(str(value))





    def third_point_coordinate_delta(self):
        try:
            value = float(self.lineEdit_87.text())
        except:
            self.lineEdit_87.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_162.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("third_point_coordinate_delta", value))
            self.parameter_backup_data["third_point_coordinate_delta"] = value
            self.pushButton_162.setText("成功到达虎牙中特征值误差" + str(value) + "已经保存")

    def third_point_coordinate_map_tiger_ruler_range(self):
        try:
            value = float(self.lineEdit_88.text())
        except:
            self.lineEdit_88.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_172.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("third_point_coordinate_map_tiger_ruler_range", value))
            self.parameter_backup_data["third_point_coordinate_map_tiger_ruler_range"] = value
            self.pushButton_172.setText("成功到达虎牙中虎牙尺子特征值误差" + str(value) + "已经保存")





    def second_point_coordinate(self):
        try:
            value = float(self.lineEdit_77.text())
        except:
            self.lineEdit_77.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_138.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("second_point_coordinate", value))
            self.parameter_backup_data["second_point_coordinate"] = value
            self.pushButton_138.setText("前公头没接进去特征值" + str(value) + "已经保存")


            self.label_100.setText(str(value))



    def second_point_coordinate_delta(self):
        try:
            value = float(self.lineEdit_80.text())
        except:
            self.lineEdit_80.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_145.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("second_point_coordinate_delta", value))
            self.parameter_backup_data["second_point_coordinate_delta"] = value
            self.pushButton_145.setText("前公头没接进去特征值误差" + str(value) + "已经保存")
            self.label_100.setText(str(value))

    def second_point_coordinate_map_tiger_ruler_range(self):
        try:
            value = float(self.lineEdit_84.text())
        except:
            self.lineEdit_84.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_153.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("second_point_coordinate_map_tiger_ruler_range", value))
            self.parameter_backup_data["second_point_coordinate_map_tiger_ruler_range"] = value
            self.pushButton_153.setText("尾部没接进虎牙特征值误差" + str(value) + "已经保存")


    def taile_thread_is_ok_point_coordinate(self):
        try:
            value = float(self.lineEdit_92.text())
        except:
            self.lineEdit_92.setText("数据错误,取缺省值120")
            value = 1120
        if self.pushButton_181.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("taile_thread_is_ok_point_coordinate", value))
            self.parameter_backup_data["taile_thread_is_ok_point_coordinate"] = value
            self.pushButton_181.setText("钻杆尾部母丝和短接连接完毕" + str(value) + "已经保存")


    def taile_thread_is_ok_point_coordinate_delat(self):
        try:
            value = float(self.lineEdit_93.text())
        except:
            self.lineEdit_93.setText("数据错误,取缺省值120")
            value = 20
        if self.pushButton_182.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("taile_thread_is_ok_point_coordinate_delat", value))
            self.parameter_backup_data["taile_thread_is_ok_point_coordinate_delat"] = value
            self.pushButton_182.setText("钻杆尾部母丝和短接连接误差" + str(value) + "已经保存")

    def taile_thread_is_ok_point_coordinate_map_tiger_ruler_range(self):
        try:
            value = float(self.lineEdit_94.text())
        except:
            self.lineEdit_94.setText("数据错误,取缺省值120")
            value = 20
        if self.pushButton_183.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("taile_thread_is_ok_point_coordinate_map_tiger_ruler_range", value))
            self.parameter_backup_data["taile_thread_is_ok_point_coordinate_map_tiger_ruler_range"] = value
            self.pushButton_183.setText("钻杆尾部母丝和短接连接对应小尺误差" + str(value) + "已经保存")






    def first_point_coordinate(self):
        try:
            value = float(self.lineEdit_75.text())
        except:
            self.lineEdit_75.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_137.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("first_point_coordinate", value))
            self.parameter_backup_data["first_point_coordinate"] = value
            self.pushButton_137.setText("两头都没接进去特征值" + str(value) + "已经保存")
            self.label_94.setText(str(value))

    def first_point_coordinate_delta(self):
        try:
            value = float(self.lineEdit_79.text())
        except:
            self.lineEdit_79.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_144.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("first_point_coordinate_delta", value))
            self.parameter_backup_data["first_point_coordinate_delta"] = value
            self.pushButton_144.setText("两头都没接进去特征值" + str(value) + "已经保存")

    def first_point_coordinate_map_tiger_ruler_range(self):
        try:
            value = float(self.lineEdit_82.text())
        except:
            self.lineEdit_82.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_149.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("first_point_coordinate_map_tiger_ruler_range", value))
            self.parameter_backup_data["first_point_coordinate_map_tiger_ruler_range"] = value
            self.pushButton_149.setText("两头都没接进去虎牙尺特征值" + str(value) + "已经保存")

    def first_point_characteristic_success_value(self):
        try:
            value = float(self.lineEdit_109.text())
        except:
            self.lineEdit_109.setText("数据错误,取缺省值120")
            value = 120
        if self.pushButton_267.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("first_point_characteristic_success_value", value))
            self.parameter_backup_data["first_point_characteristic_success_value"] = value
            self.pushButton_267.setText("两头都没接进去修正成功特征值" + str(value) + "已经保存")

    def no_load_move_parameter_contrl_distance(self):
        try:
            value = float(self.lineEdit_76.text())
        except:
            self.lineEdit_76.setText("数据错误,取缺省值2")
            value = 2
        if self.pushButton_132.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("no_load_move_parameter_contrl_distance", value))
            self.parameter_backup_data["no_load_move_parameter_contrl_distance"] = value
            self.pushButton_132.setText("接近目标档位" + str(value) + "已经保存")

    def tiger_touch_delta(self):
        try:
            value = float(self.lineEdit_89.text())
        except:
            self.lineEdit_89.setText("数据错误,取缺省值2")
            value = 2
        if self.pushButton_175.isChecked() == True:
            try:
                self.orderSendToMachineProcessPipe.send(("tiger_touch_delta", value))
                self.parameter_backup_data["tiger_touch_delta"] = value
                self.pushButton_175.setText("触动标识距离" + str(value) + "已经保存")
            except Exception as ff:
                print("ooooooooooooooooooooooooooooooooooooommmmmmmmmmmmmmmmmmmmmm2")
                print(ff)

    def beam_push_pull_in_tiger_step_distance(self):
        try:
            value = float(self.lineEdit_90.text())
        except:
            self.lineEdit_90.setText("数据错误,取缺省值2")
            value = 40
        if self.pushButton_177.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("beam_push_pull_in_tiger_step_distance", value))
            self.parameter_backup_data["beam_push_pull_in_tiger_step_distance"] = value
            self.pushButton_177.setText("钻杆虎牙移动步长" + str(value) + "已经保存")


    def delta_contrast_beam_ruler_tiger_ruler_(self):
        try:
            value = float(self.lineEdit_91.text())
        except:
            self.lineEdit_91.setText("数据错误,取缺省值2")
            value = 6
        if self.pushButton_179.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("delta_contrast_beam_ruler_tiger_ruler", value))
            self.parameter_backup_data["delta_contrast_beam_ruler_tiger_ruler"] = value
            self.pushButton_179.setText("大梁尺子和虎牙尺子一样值的误差" + str(value) + "已经保存")







    def  no_load_move_end_level(self):
        try:
            value = float(self.lineEdit_38.text())
        except:
            self.lineEdit_38.setText("数据错误,取缺省值2")
            value = 2
        if self.pushButton_130.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("no_load_move_end_level", value))
            self.parameter_backup_data["no_load_move_end_level"] = value
            self.pushButton_130.setText("j接近目标档位" + str(value) + "已经保存")



    def no_load_move_start_level(self):
        try:
            value = float(self.lineEdit_37.text())
        except:
            self.lineEdit_37.setText("数据错误,取缺省值2")
            value = 2
        if self.pushButton_129.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("no_load_move_start_level", value))
            self.parameter_backup_data["no_load_move_start_level"] = value
            self.pushButton_129.setText("最快速度档位" + str(value) + "已经保存")



    def no_load_move_to_coordinnate_point_max_pressure(self):

        try:
            value = float(self.lineEdit_34.text())
        except:
            self.lineEdit_34.setText("数据错误,取缺省值2")
            value = 2
        if self.pushButton_128.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("no_load_move_to_coordinnate_point_max_pressure", value))
            self.parameter_backup_data["no_load_move_to_coordinnate_point_max_pressure"] = value
            self.pushButton_128.setText("疑似故障压力门限设置" + str(value) + "已经保存")




    def drill_box_function_set(self):
        if self.pushButton_96.isChecked() == True:
            self.stackedWidget_2.setCurrentIndex(3)

    def beam_base_function_set(self):
        if self.pushButton_97.isChecked() == True:
            self.stackedWidget_2.setCurrentIndex(4)

    def interface_function_set(self):
        if self.pushButton_135.isChecked() == True:
            self.stackedWidget_2.setCurrentIndex(5)

    def tigger_tight_functionset(self):
         if self.pushButton_119.isChecked() == True:
             self.stackedWidget_2.setCurrentIndex(2)


    def pole_funtion_set(self):
        if self.pushButton_112.isChecked() == True:
            self.stackedWidget_2.setCurrentIndex(1)

    def machin_delta_set(self):
        if self.pushButton_268.isChecked() == True:
            self.stackedWidget_2.setCurrentIndex(6)


    def set_pole_loose_need_mini_circle_drill_level(self):    # buttom yes 122
        value = self.verticalSlider_20.value()
        if self.pushButton_116.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("pole_loose_need_mini_circle_drill_level", value))
            self.parameter_backup_data["pole_loose_need_mini_circle_drill_level"] = value
            self.pushButton_116.setText("最小圈退丝最佳档位设置" + str(value) + "已经保存")

    def pole_loose_need_mini_circle_drill_level(self):
        value = self.verticalSlider_20.value()
        self.pushButton_116.setText("最小圈退丝最佳档位设置" + str(value))












    def set_pole_loose_need_mini_circle(self):    # buttom yes 122
        value = self.verticalSlider_18.value()
        if self.pushButton_114.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("pole_loose_need_mini_circle", value))
            self.parameter_backup_data["pole_loose_need_mini_circle"] = value
            self.pushButton_114.setText("钻杆退丝退松最小圈数" + str(value) + "已经保存")

    def pole_loose_need_mini_circle(self):
        value = self.verticalSlider_18.value()
        self.pushButton_114.setText("钻杆退丝退松最小圈数" + str(value))







    def set_pole_and_pole_thread_connetct_max_drill_level(self):    # buttom yes 122
        value = self.verticalSlider_19.value()
        if self.pushButton_115.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_dirll_pole_pole_tight_max_pressure_level", value))
            self.parameter_backup_data["tiger_dirll_pole_pole_tight_max_pressure_level"] = value
            self.pushButton_115.setText("虎牙钻杆连接操作最大旋转档位" + str(value) + "已经保存")

    def pole_and_pole_thread_connetct_drill_level(self):
        value = self.verticalSlider_19.value()
        self.pushButton_115.setText("虎牙钻杆连接操作最大旋转档位" + str(value))





    def set_pole_and_pole_thread_connetct_max_push_level(self):    # buttom yes 122
        value = self.verticalSlider_27.value()
        if self.pushButton_124.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_dirll_pole_pole_tight_push_max_pressure_level", value))
            self.parameter_backup_data["tiger_dirll_pole_pole_tight_push_max_pressure_level"] = value
            self.pushButton_124.setText("虎牙钻杆连接操作最佳推拉档位" + str(value) + "已经保存")


    def pole_and_pole_thread_connetct_push_level(self):
        value = self.verticalSlider_27.value()
        self.pushButton_124.setText("虎牙钻杆连接操作最佳推拉档位" + str(value))




    def set_tiger_dirll_pole_pole_tight_push_max_pressure(self):  # buttom yes 122
        value = self.verticalSlider_40.value()
        if self.pushButton_140.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(
                ("tiger_dirll_pole_pole_tight_push_max_pressure", value))
            self.parameter_backup_data["tiger_dirll_pole_pole_tight_push_max_pressure"] = value
            self.pushButton_140.setText("虎牙钻杆连接操作最佳推拉压力" + str(value) + "已经保存")

    def tiger_dirll_pole_pole_tight_push_max_pressure(self):
        value = self.verticalSlider_40.value()
        self.pushButton_140.setText("虎牙钻杆连接操作最佳推拉压力" + str(value))


    def set_tiger_forward_move_max_coordinate(self):    # buttom yes 122
        value = self.verticalSlider_41.value()
        if self.pushButton_141.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_forward_move_max_coordinate", value))
            self.parameter_backup_data["tiger_forward_move_max_coordinate"] = value
            self.pushButton_141.setText("前虎牙偏移最大值" + str(value) + "已经保存")


    def tiger_forward_move_max_coordinate_(self):
        value = self.verticalSlider_41.value()
        self.pushButton_141.setText("前虎牙偏移最大值" + str(value))



    def set_tiger_coordinate_beam_not_reach_beamself_slot(self):    # buttom yes 122
        value = self.verticalSlider_42.value()
        if self.pushButton_142.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_coordinate_beam_not_reach_beamself_slot", value))
            self.parameter_backup_data["tiger_coordinate_beam_not_reach_beamself_slot"] = value
            self.pushButton_142.setText("大梁未到达自己槽前端的前虎牙位移坐标" + str(value) + "已经保存")


    def tiger_coordinate_beam_not_reach_beamself_slot_(self):
        value = self.verticalSlider_42.value()
        self.pushButton_142.setText("大梁未到达自己槽前端的前虎牙位移坐标" + str(value))


    def set_tiger_coordinate_beam_reached_beamself_slot(self):    # buttom yes 122
        value = self.verticalSlider_43.value()
        if self.pushButton_143.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_coordinate_beam_reached_beamself_slot", value))
            self.parameter_backup_data["tiger_coordinate_beam_reached_beamself_slot"] = value
            self.pushButton_143.setText("大梁未到达自己槽前端的前虎牙位移坐标" + str(value) + "已经保存")


    def tiger_coordinate_beam_reached_beamself_slot_(self):
        value = self.verticalSlider_43.value()
        self.pushButton_143.setText("大梁未到达自己槽前端的前虎牙位移坐标" + str(value))





    def set_tiger_self_middle_zero_coordinate_(self):
        value = self.verticalSlider_28.value()
        if self.pushButton_125.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_self_middle_zero_coordinate_", value))
            self.parameter_backup_data["tiger_self_middle_zero_coordinate_"] = value
            self.pushButton_125.setText("整个虎牙中点坐标" + str(value) + "已经保存")


    def tiger_self_middle_zero_coordinate__(self):
        value = self.verticalSlider_28.value()
        self.pushButton_125.setText("整个虎牙中点坐标" + str(value))



    def set_pole_and_pole_thread_connetct_max_pressure(self):    # buttom yes 122
        value = self.verticalSlider_13.value()
        if self.pushButton_113.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_dirll_pole_pole_tight_max_pressure", value))
            self.parameter_backup_data["tiger_dirll_pole_pole_tight_max_pressure"] = value
            self.pushButton_113.setText("虎牙钻杆对接最大压力值" + str(value) + "已经保存")

    def pole_and_pole_thread_connetct_max_pressure(self):
        value = self.verticalSlider_13.value()
        self.pushButton_113.setText("虎牙钻杆对接最大压力值" + str(value))








    def set_pole_taile_mother_thread_out_pressure(self):    # buttom yes 122
        value = self.verticalSlider_26.value()
        if self.pushButton_123.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("pole_taile_mother_thread_out_pressure", value))
            self.parameter_backup_data["pole_taile_mother_thread_out_pressure"] = value
            self.pushButton_123.setText("尾部钻杆退丝需要压力" + str(value) + "已经保存")

    def pole_taile_mother_thread_out_pressure(self):
        value = self.verticalSlider_26.value()
        self.pushButton_123.setText("尾部钻杆退丝需要压力" + str(value))



    def set_pole_taile_mother_thread_out_circle_numeber(self):    # buttom yes 122
        value = self.verticalSlider_25.value()

        if self.pushButton_122.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("pole_taile_mother_thread_out_circle_numeber", value))
            self.parameter_backup_data["pole_taile_mother_thread_out_circle_numeber"] = value

            self.pushButton_122.setText("钻杆尾部退丝圈数" + str(value) + "已经保存")


    def set_pole_taile_mother_thread_out_circle_(self):
        value = self.verticalSlider_25.value()
        self.pushButton_122.setText("钻杆尾部退丝圈数" + str(value))




# ----------------------------------------------------------------------------------------------------


    def set_drill_box_grap_hand_tight_slight_set(self):
        value = self.verticalSlider_22.value()
        if self.pushButton_118.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("_drill_box_grap_hand_tight_slight", value))
            self.parameter_backup_data["_drill_box_grap_hand_tight_slight"] = value
            self.pushButton_118.setText("钻箱抓手松抓" + str(value) + "已经保存")

    def set_drill_box_grap_hand_tight_slight(self):
        value = self.verticalSlider_22.value()
        self.pushButton_118.setText("钻箱抓手松抓时间" + str(value))





    def set_drill_box_grap_hand_tight_strong_set(self):
        value = self.verticalSlider_21.value()
        if self.pushButton_117.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("box_grap_hand_tight_strong", value))
            self.parameter_backup_data["box_grap_hand_tight_strong"] = value
            self.pushButton_117.setText("钻箱抓手紧抓" + str(value) + "已经保存")

    def set_drill_box_grap_hand_tight_strong(self):
        value = self.verticalSlider_21.value()
        self.pushButton_117.setText("钻箱抓手紧抓时间" + str(value))


    def drill_box_grap_hand_tight_greater_strong_set(self):
        value = self.verticalSlider_74.value()
        if self.pushButton_325.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("drill_box_grap_hand_tight_greater_strong", value))
            self.parameter_backup_data["drill_box_grap_hand_tight_greater_strong"] = value
            self.pushButton_325.setText("钻箱抓手大半紧抓" + str(value) + "已经保存")

    def set_drill_box_grap_hand_tight_greater_strong(self):
        value = self.verticalSlider_74.value()
        self.pushButton_325.setText("钻箱抓手大半紧抓时间" + str(value))







    def drill_box_grap_hand_relax_full(self):
        value = self.verticalSlider_29.value()
        if self.pushButton_173.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("drill_box_grap_hand_relax_full", value))
            self.parameter_backup_data["drill_box_grap_hand_relax_full"] = value
            self.pushButton_173.setText("钻箱抓手完全松开时间" + str(value) + "已经保存")

    def set_drill_box_grap_hand_relax_full(self):
        value = self.verticalSlider_29.value()
        self.pushButton_173.setText("钻箱抓手完全松开时间" + str(value))


    def drill_box_relax_half(self):
        value = self.verticalSlider_30.value()
        if self.pushButton_174.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("drill_box_grap_hand_relax_half", value))
            self.parameter_backup_data["drill_box_grap_hand_relax_half"] = value
            self.pushButton_174.setText("钻箱抓手半松开时间" + str(value) + "已经保存")


    def set_drill_box_relax_half(self):
        value = self.verticalSlider_30.value()
        self.pushButton_174.setText("钻箱抓手半松开时间" + str(value))







    def drill_box_grap_hand_relax_greater_part(self):
        value = self.verticalSlider_73.value()
        if self.pushButton_324.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("drill_box_grap_hand_relax_greater_part", value))
            self.parameter_backup_data["drill_box_grap_hand_relax_greater_part"] = value
            self.pushButton_324.setText("钻箱抓手完全松开时间" + str(value) + "已经保存")


    def set_drill_box_grap_hand_relax_greater_part(self):
        value = self.verticalSlider_73.value()
        self.pushButton_324.setText("钻箱抓手大半放松" + str(value))





#--------------------------------------------------------------------------------------------------


    def set_tiger_tight_time_set(self):
        value = self.verticalSlider_23.value()
        if self.pushButton_120.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_tight_time_", value))
            self.parameter_backup_data["tiger_tight_time_"] = value
            self.pushButton_120.setText("虎牙紧（松）时间" + str(value) + "已经保存")

    def set_tiger_tight_time_(self):
        value = self.verticalSlider_23.value()
        self.pushButton_120.setText("虎牙紧（松）时间" + str(value))







    def set_tiger_loose_time_set(self):
        value = self.verticalSlider_24.value()
        if self.pushButton_121.isChecked() == True:
            self.orderSendToMachineProcessPipe.send(("tiger_loose_time_", value))
            self.parameter_backup_data["tiger_loose_time_"] = value
            self.pushButton_121.setText("虎牙旋紧（松）时间" + str(value) + "已经保存")

    def set_tiger_loose_time_(self):
        value = self.verticalSlider_24.value()
        self.pushButton_121.setText("虎牙旋紧（松）时间" + str(value))



    def operator_top_forward(self):

        if self.pushButton_165.isChecked() == True:

            value = (False, "operator_top_forward", time.time(), None, 7200)
            self.orderSendToMachineProcessPipe.send(("operator_top_forward", value))
            self.parameter_backup_data["operator_top_forward"] = value
            self.pushButton_165.setText("自动前进..运行中" )

###############################################################################above is this time not do

    def set_pole_out_thread_parameter(self):
        if self.pushButton_165.isChecked() == True:
            value = (False, "operator_top_forward", time.time(), None, 7200)
            self.orderSendToMachineProcessPipe.send(("operator_top_forward", value))
            self.parameter_backup_data["operator_top_forward"] = value
            self.pushButton_165.setText("自动前进..运行中" )




    def set_pole_out_thread(self):
        value = self.verticalSlider_6.value()
        self.pushButton_111.setText("钻杆对接退丝需要圈数" + str(value))


    def auto_operation(self):
        self.stackedWidget_3.setCurrentIndex(0)


    def befor_opration_check(self):
        self.stackedWidget_3.setCurrentIndex(2)

    def manual_opration_turn(self):
        self.stackedWidget_3.setCurrentIndex(1)

    def push_pull_leverl(self):
        value = self.horizontalSlider_2.value()

        if value > 0:
            self.label_88.setText("前进档位" + str(value))

        if value == 0:

            self.label_88.setText("停止" + str(value))
        if value < 0:

            self.label_88.setText("后退档位" + str(value))

    def guide_turn_angle(self):
        value = self.horizontalSlider_4.value()
        if value > 0:
            self.label_85.setText("正时钟方向转档位" + str(value))
        if value == 0:
            self.label_85.setText("停止旋转档位" + str(value))
        if value < 0:
            self.label_85.setText("反时针旋转档位" + str(value))
    def use_drill_box2_stop_forward(self):

            if self.pushButton_147.isChecked() == True:
                self.pushButton_155.setChecked(False)
                self.pushButton_156.setChecked(False)
                self.pushButton_151.setChecked(False)
                self.stackedWidget_4.setCurrentIndex(3)
            elif self.pushButton_151.isChecked() == False and self.pushButton_156.isChecked() == False and self.pushButton_147.isChecked() == False and self.pushButton_155.isChecked() == False:
                self.stackedWidget_4.setCurrentIndex(3)






    def use_drill_box2_set_derect_and_move(self):
        if self.pushButton_156.isChecked() == True:
            self.pushButton_155.setChecked(False)
            self.pushButton_156.setChecked(False)
            self.pushButton_147.setChecked(False)
            self.stackedWidget_4.setCurrentIndex(1)
        elif self.pushButton_151.isChecked() == False and  self.pushButton_156.isChecked() == False and  self.pushButton_147.isChecked() == False  and  self.pushButton_155.isChecked() == False:
            self.stackedWidget_4.setCurrentIndex(3)



    def use_drill_box2_back(self):
        if self.pushButton_151.isChecked() == True:   #yes
            self.pushButton_155.setChecked(False)
            self.pushButton_156.setChecked(False)
            self.pushButton_147.setChecked(False)
        if self.pushButton_151.isChecked() is True and self.pushButton_157.isChecked() is True:
            self.stackedWidget_4.setCurrentIndex(5)
        elif self.pushButton_151.isChecked() is True and self.pushButton_157.isChecked() is False:
            self.stackedWidget_4.setCurrentIndex(4)
        elif self.pushButton_151.isChecked() is False and  self.pushButton_156.isChecked() is False and self.pushButton_147.isChecked() is False  and  self.pushButton_155.isChecked() is False:
            self.stackedWidget_4.setCurrentIndex(3)

    def use_drill_box2(self):    #yes
        if self.pushButton_155.isChecked() == True:
                self.pushButton_151.setChecked(False)
                self.pushButton_156.setChecked(False)
                self.pushButton_147.setChecked(False)
        if self.pushButton_157.isChecked() == True:
            self.stackedWidget_4.setCurrentIndex(0)
        if self.pushButton_157.isChecked() == False:
            self.stackedWidget_4.setCurrentIndex(2)
        elif self.pushButton_151.isChecked() is False and  self.pushButton_156.isChecked() is False and  self.pushButton_147.isChecked() is False  and  self.pushButton_155.isChecked() is False:
            self.stackedWidget_4.setCurrentIndex(3)




    def use_drill_box(self):     ##   y es
        if self.pushButton_157.isChecked() is True:
            self.pushButton_157.setText("使用钻杆箱")
        else:
            self.pushButton_157.setText("不使用钻杆箱")
        if self.pushButton_155.isChecked()is False and self.pushButton_151.isChecked() is True and self.pushButton_156.isChecked() == True  and self.pushButton_147.isChecked() == True:
            self.stackedWidget_4.setCurrentIndex(3)
        if self.pushButton_155.isChecked() is True and  self.pushButton_157.isChecked() is True:   #yes
            self.stackedWidget_4.setCurrentIndex(0)
        elif self.pushButton_155.isChecked() is True and  self.pushButton_157.isChecked() is False: #yes
            self.stackedWidget_4.setCurrentIndex(2)
        elif self.pushButton_151.isChecked() is True and  self.pushButton_157.isChecked() is True:
            self.stackedWidget_4.setCurrentIndex(5)
        elif self.pushButton_151.isChecked() is True and  self.pushButton_157.isChecked() is False:
            self.stackedWidget_4.setCurrentIndex(4)
        elif self.pushButton_156.isChecked() is True :
            self.stackedWidget_4.setCurrentIndex(1)

    def test_begin__(self):
        if self.ui_form_dirll_box_every_pole_distance.pushButton_121.isChecked() is True:
            self.ui_form_dirll_box_every_pole_distance.pushButton_121.setText("测试已经开始")
        else:
            self.ui_form_dirll_box_every_pole_distance.pushButton_121.setText("测试已经结束")

    def test_drill_box_every_pole_power(self):


            radio = self.set_window.sender()
            index_value = float(radio.text())-1
            self.orderSendToMachineProcessPipe.send(
                ("test_every_pole_power_distance_", index_value))


    def drill_box_up_down_uncorecte_range(self):
        value = self.ui_form_dirll_box_every_pole_distance.horizontalSlider_2.value()
        self.orderSendToMachineProcessPipe.send(("drill_box_up_down_uncorecte_range",value))

    def hand_box_run_uncoreccte_rangge(self):
        value =  self.ui_form_dirll_box_every_pole_distance.horizontalSlider.value()
        if self.pushButton_118.isChecked() is True:
            self.orderSendToMachineProcessPipe.send(("hand_box_run_uncoreccte_rangge",value))
            self.pushButton_118.setText("抓手强度弱设置" + str(value) + "成功")
            self.parameter_backup_data["hand_box_run_uncoreccte_rangge"] = value

    def load_test_diesel_engine_load_test(self):
        self.orderSendToMachineProcessPipe.send(
            ("uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35", "save_as_standard"))


    def test_diesel_engine_load_test(self):
        self.orderSendToMachineProcessPipe.send(
            ("uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_35", "load_data__save",))

    def save_standard_diesel_engine_power(self):
        if   self.ui_form_dirll_box_every_pole_distance.pushButton_34 is True:
            self.orderSendToMachineProcessPipe.send(
                ("uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_41", "no load test save"))


    def test_diesel_engine_power(self):
        self.orderSendToMachineProcessPipe.send(
            ("uui_main_window_obj_ui_form_dirll_box_every_pole_distance_pushButton_34", "no_load_test_begin"))


    def set_drill_box_stacked_parameter_distance(self):
        self.ui_form_dirll_box_every_pole_distance.stackedWidget.setCurrentIndex(0)
        self.ui_form_dirll_box_every_pole_distance.stackedWidget.show()

    def set_drill_box_staked_parameter_result(self):

        self.ui_form_dirll_box_every_pole_distance.stackedWidget.setCurrentIndex(2)
        self.ui_form_dirll_box_every_pole_distance.stackedWidget.show()

    def set_drill_box_staked_parameter(self):


        self.ui_form_dirll_box_every_pole_distance.stackedWidget.setCurrentIndex(1)
        self.ui_form_dirll_box_every_pole_distance.stackedWidget.show()


    def set_drill_box_up_down_errow_range(self):
        value =  self.ui_form_dirll_box_every_pole_distance.horizontalSlider_2.value()
        self.ui_form_dirll_box_every_pole_distance.label_2.setText(str(value) + "毫米")


    def  set_drill_box_grap_hand_move_errow_range(self):
        value = self.ui_form_dirll_box_every_pole_distance.horizontalSlider.value()


        self.ui_form_dirll_box_every_pole_distance.label.setText(str(value) + "毫米")

    def set_drillbox_begin_to_column_to_put_back_pole_coordinate(self):
        value = self.ui_form_dirll_box_every_pole_distance.verticalSlider.value()
        self.ui_form_dirll_box_every_pole_distance.label_12.setText(str(value) + "毫米")
        self.ui_form_dirll_box_every_pole_distance.lineEdit_31.setText(str(value))

    def grap_hand_start_run_point_set(self):
        value = self.ui_form_dirll_box_every_pole_distance.verticalSlider.value()
        self.orderSendToMachineProcessPipe.send(("angle_0_corectting", "zero_angle"))



    def angle_zero_correcting(self):
        if self.pushButton_56.isChecked():

            value = self.label_54.text()
            self.lineEdit_62.setText(value)
            self.parameter_backup_data["angle_0_corectting"] = value     ### n
            self.orderSendToMachineProcessPipe.send(("angle_0_corectting", "zero_angle"))


    def drill_box_outter_column_10(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_27.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_10_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_10_distance", ))

    def drill_box_outter_column_9(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_29.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_9_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_9_distance", ))

    def drill_box_outter_column_8(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_26.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_8_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_8_distance", ))

    def drill_box_outter_column_7(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_22.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_7_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_7_distance", ))

    def drill_box_outter_column_6(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_28.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_6_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_6_distance", ))

    def drill_box_outter_column_5(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_23.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_5_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_5_distance", ))

    def drill_box_outter_column_4(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_24.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_4_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_4_distance", ))

    def drill_box_outter_column_3(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_21.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_3_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_3_distance", ))

    def drill_box_outter_column_2(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_25.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_2_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_2_distance", ))

    def drill_box_outter_column_1(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_30.setText(value)
            self.parameter_backup_data["dirll_box_outter_column_1_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_outter_column_1_distance", ))

    def drill_box_middle_column_10(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_17.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_10_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_10_distance", ))

    def drill_box_middle_column_9(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_19.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_9_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_9_distance", ))


    def drill_box_middle_column_8(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_16.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_8_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_8_distance", ))

    def drill_box_middle_column_7(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_12.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_7_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_7_distance", ))

    def drill_box_middle_column_6(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_18.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_6_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_6_distance", ))

    def drill_box_middle_column_5(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_13.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_5_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_5_distance", ))

    def drill_box_middle_column_4(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_14.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_4_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_4_distance", ))


    def drill_box_middle_column_3(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_11.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_3_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_3_distance", ))


    def drill_box_middle_column_2(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_15.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_2_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_2_distance", ))


    def drill_box_middle_column_1(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_20.setText(value)
            self.parameter_backup_data["dirll_box_middle_column_1_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_middle_column_1_distance", ))

    def dirll_box_inner_column_10(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_10_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_10_distance", ))


    def dirll_box_inner_column_9(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_2.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_9_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_9_distance", ))


    def dirll_box_inner_column_8(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_3.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_8_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_8_distance", ))


    def dirll_box_inner_column_7(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_4.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_7_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_7_distance", ))



    def dirll_box_inner_column_6(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_5.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_6_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_6_distance", ))

    def dirll_box_inner_column_5(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_6.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_5_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_5_distance", ))


    def dirll_box_inner_column_4(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_7.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_4_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_4_distance", ))



    def dirll_box_inner_column_3(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_8.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_3_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_3_distance", ))



    def dirll_box_inner_column_2(self):
        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_9.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_2_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_2_distance", ))

    def dirll_box_inner_column_1(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_10.text())
            except Exception:
                self.lineEdit_10.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_coordinate"] = value
            print(("beam_taile_5cm_coordinate", value))
            try:
                value = float(self.lineEdit_104.text())
            except Exception:
                self.lineEdit_104.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_cycle_number"] = value
            print(("beam_taile_5cm_cycle_number", value))
        else:
            value = self.label_221.text()
            self.lineEdit_10.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_10.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_coordinate"] = value
            value = self.label_222.text()
            self.lineEdit_104.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_104.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_cycle_number"] = value



        value = self.label_224.text()
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.lineEdit_10.setText(value)
            self.parameter_backup_data["dirll_box_inner_column_1_distance"] = value
            self.orderSendToMachineProcessPipe.send(("dirll_box_inner_column_1_distance", ))


    def dirll_box_every_pole_distance_set_lock(self):
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == True:
            self.ui_form_dirll_box_every_pole_distance.pushButton_114.setText("设置锁定解除")
        if self.ui_form_dirll_box_every_pole_distance.pushButton_114.isChecked() == False:

            self.ui_form_dirll_box_every_pole_distance.pushButton_114.setText("设置已经锁定")



    def drill_box_every_pole_distance(self):

        # cc = QtWidgets.QApplication()
        self.set_window.show()
        # sys.exit(cc.exec_())
    def set_widget_ui(self):
        self.set_window = QtWidgets.QWidget()

        self.set_window.setWindowTitle("钻箱每根钻杆距离设置")
        self.ui_form_dirll_box_every_pole_distance = drill_box_every_pole_distance.Ui_Form()
        self.ui_form_dirll_box_every_pole_distance.setupUi(self.set_window)



    def  set_parameters_pole_in_middle_tiger_tooth_to_taile_tofaward(self):
        if self.pushButton_188.isChecked():
                try:
                    value = float(self.lineEdit_15.text())
                except Exception:
                    self.lineEdit_15.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate", value))
                # print(("pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate", value))
                try:
                    value = float(self.lineEdit_101.text())
                except Exception:
                    self.lineEdit_101.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number", value))
                print(("pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number", value))
        else:
                value = self.label_221.text()
                self.lineEdit_15.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_15.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate", value))
                value = self.label_222.text()
                self.lineEdit_101.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_101.setText("重新输入")
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number", value))


    def set_current_rock_arm(self):
        if self.pushButton_56.isChecked():
            self.orderSendToMachineProcessPipe.send(("set_stop_current_value",True))

    def lock_operation(self):
        if self.pushButton_56.isChecked():
            self.pushButton_56.setText("已经解除锁定")
            self.orderSendToMachineProcessPipe.send(("lock_operation", True))
        else:
            self.orderSendToMachineProcessPipe.send(("lock_operation", False))
            self.pushButton_56.setText("已经锁定")
    def mannual_data_use(self):
        if self.pushButton_188.isChecked():
            self.pushButton_188.setText("采用手工填写数据")
            # self.orderSendToMachineProcessPipe.send(("lock_operation", True))
        else:
            # self.orderSendToMachineProcessPipe.send(("lock_operation", False))
            self.pushButton_188.setText("不采用手工填写数据")

    def load_parameter(self):
        print(f"{inspect.currentframe().f_code.co_name} is run {inspect.currentframe().f_lineno}")
        if self.pushButton_56.isChecked():
            self.orderSendToMachineProcessPipe.send(("load_parameter",))
            old_data = seting.parameter_load_data
            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx1")
            self.lineEdit_5.setText(str(old_data.get("pole_in_middle_tiger_tooth", 0)))
            self.lineEdit_98.setText(str(old_data.get("pole_in_middle_tiger_tooth_cycle_number", 0)))
            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx2")
            self.lineEdit_6.setText(str(old_data.get("pole_in_middle_tiger_tooth_tiggerback", 0)))
            self.lineEdit_99.setText(str(old_data.get("pole_in_middle_tiger_tooth_tiggerback_cycle_number", 0)))
            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx3")
            self.lineEdit_14.setText(str(old_data.get("pole_in_middle_tiger_tooth_to_taile", 0)))
            self.lineEdit_100.setText(str(old_data.get("pole_in_middle_tiger_tooth_to_taile_cycle_number", 0)))
            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx4")
            self.lineEdit_15.setText(str(old_data.get("pole_in_middle_tiger_tooth_to_taile_tofaward", 0)))
            self.lineEdit_101.setText(str(old_data.get("pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number", 0)))
            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx5")
            self.lineEdit_8.setText(str(old_data.get("beam_taile_5cm", 0)))
            self.lineEdit_102.setText(str(old_data.get("beam_taile_5cm_cycle_number", 0)))

            self.lineEdit_9.setText(str(old_data.get("pole_pull_back_can_out_box_hand_to_grap_coordinate", 0)))
            self.lineEdit_103.setText(str(old_data.get("pole_pull_back_can_out_box_hand_to_grap_cycle_number", 0)))

            self.lineEdit_10.setText(str(old_data.get("main_beam_last_pole_up_down_expangd_hole_coordinate", 0)))
            self.lineEdit_104.setText(str(old_data.get("main_beam_last_pole_up_down_expangd_hole_cycle_number", 0)))

            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx6")
            self.lineEdit_113.setText(str(old_data.get("box_updown_column_can_grap_coordinate", 0)))
            self.lineEdit_108.setText(str(old_data.get("box_updown_column_up", 0)))
            self.lineEdit_112.setText(str(old_data.get("box_updown_bottom", 0)))

            self.lineEdit_23.setText(str(old_data.get("man_give_pole_place", 0)))
            self.lineEdit_105.setText(str(old_data.get("man_give_pole_place_cycle_number", 0)))

            self.lineEdit_31.setText(str(old_data.get("man_give_pole_place_back_last_point_coordinate", 0)))
            self.lineEdit_106.setText(str(old_data.get("man_give_pole_place_back_last_point_cycle_number", 0)))

            self.lineEdit_28.setText(str(old_data.get("the_new_point_man_can_let_pole_out_beam_coordinate", 0)))
            self.lineEdit_107.setText(str(old_data.get("the_new_point_man_can_let_pole_out_beam_cycle_number", 0)))

            self.lineEdit_27.setText(str(old_data.get("point1_coordinate", 0)))
            self.lineEdit_114.setText(str(old_data.get("point1_cycle_number", 0)))
            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx7")
            self.lineEdit_29.setText(str(old_data.get("point2_coordinate", 0)))
            self.lineEdit_115.setText(str(old_data.get("point2_cycle_number", 0)))

            self.lineEdit_25.setText(str(old_data.get("point3_coordinate", 0)))
            self.lineEdit_116.setText(str(old_data.get("point3_cycle_number", 0)))

            self.lineEdit_30.setText(str(old_data.get("point_beam_grap_coordinate", 0)))
            self.lineEdit_117.setText(str(old_data.get("point_beam_grap_cycle_number", 0)))

            self.lineEdit_26.setText(str(old_data.get("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate", 0)))
            self.lineEdit_118.setText(str(old_data.get("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number", 0)))

            print("load xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx8")
            self.lineEdit_24.setText(str(old_data.get("point_unstop_beam_coordinate", 0)))
            self.lineEdit_119.setText(str(old_data.get("point_unstop_beam_cycle_number", 0)))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

# *******************************coordinate************************************

            Equepment_pole_push_pull_data_coordinate = old_data.get("Equepment_pole_push_pull_data_coordinate", [0, 0, 0])
            print(Equepment_pole_push_pull_data_coordinate)
            self.lineEdit_22.setText(str(Equepment_pole_push_pull_data_coordinate[0]))
            self.lineEdit_32.setText(str(Equepment_pole_push_pull_data_coordinate[1]))
            self.lineEdit_35.setText(str(Equepment_pole_push_pull_data_coordinate[2]))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk1")

            Equepment_pole_dirll_coordinate = old_data.get("Equepment_pole_dirll_coordinate", [0, 0, 0])
            print(Equepment_pole_dirll_coordinate)
            self.lineEdit_48.setText(str(Equepment_pole_dirll_coordinate[0]))
            self.lineEdit_49.setText(str(Equepment_pole_dirll_coordinate[1]))
            self.lineEdit_50.setText(str(Equepment_pole_dirll_coordinate[2]))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk2")


            Equepment_tigger_tooch_f_coordinate = old_data.get("Equepment_tigger_tooch_f_coordinate", [0, 0, 0])
            self.lineEdit_51.setText(str(Equepment_tigger_tooch_f_coordinate[0]))
            self.lineEdit_52.setText(str(Equepment_tigger_tooch_f_coordinate[1]))
            self.lineEdit_53.setText(str(Equepment_tigger_tooch_f_coordinate[2]))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk3")
            Equepment_tigger_tooch_b_coordinate = old_data.get("Equepment_tigger_tooch_b", [0, 0, 0])
            self.lineEdit_56.setText(str(Equepment_tigger_tooch_b_coordinate[0]))
            self.lineEdit_55.setText(str(Equepment_tigger_tooch_b_coordinate[1]))
            self.lineEdit_54.setText(str(Equepment_tigger_tooch_b_coordinate[2]))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk4")
            Equepment_tigger_drill_coordinate = old_data.get("Equepment_tigger_drill", [0, 0, 0])
            self.lineEdit_45.setText(str(Equepment_tigger_drill_coordinate[0]))
            self.lineEdit_46.setText(str(Equepment_tigger_drill_coordinate[1]))
            self.lineEdit_47.setText(str(Equepment_tigger_drill_coordinate[2]))


            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk10")
            self.lineEdit_62.setText(str(old_data.get(("angle_0_corectting",),0)))



            self.ui_form_dirll_box_every_pole_distance.lineEdit_10.setText(str(old_data.get("dirll_box_inner_column_1_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_9.setText(str(old_data.get("dirll_box_inner_column_2_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_8.setText(str(old_data.get("dirll_box_inner_column_3_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_7.setText(str(old_data.get("dirll_box_inner_column_4_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_6.setText(str(old_data.get("dirll_box_inner_column_5_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_5.setText(str(old_data.get("dirll_box_inner_column_6_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_4.setText(str(old_data.get("dirll_box_inner_column_7_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_3.setText(str(old_data.get("dirll_box_inner_column_8_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_2.setText(str(old_data.get("dirll_box_inner_column_9_distance",0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit.setText(str(old_data.get("dirll_box_inner_column_10_distance",0)))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk11")
            self.ui_form_dirll_box_every_pole_distance.lineEdit_20.setText(str(old_data.get("dirll_box_middle_column_1_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_15.setText(str(old_data.get("dirll_box_middle_column_2_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_11.setText(str(old_data.get("dirll_box_middle_column_3_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_14.setText(str(old_data.get("dirll_box_middle_column_4_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_13.setText(str(old_data.get("dirll_box_middle_column_5_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_18.setText(str(old_data.get("dirll_box_middle_column_6_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_12.setText(str(old_data.get("dirll_box_middle_column_7_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_16.setText(str(old_data.get("dirll_box_middle_column_8_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_19.setText(str(old_data.get("dirll_box_middle_column_9_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_17.setText(str(old_data.get("dirll_box_middle_column_10_distance", 0)))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk12")
            self.ui_form_dirll_box_every_pole_distance.lineEdit_30.setText(str(old_data.get("dirll_box_outter_column_1_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_25.setText(str(old_data.get("dirll_box_outter_column_2_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_21.setText(str(old_data.get("dirll_box_outter_column_3_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_24.setText(str(old_data.get("dirll_box_outter_column_4_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_23.setText(str(old_data.get("dirll_box_outter_column_5_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_28.setText(str(old_data.get("dirll_box_outter_column_6_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_22.setText(str(old_data.get("dirll_box_outter_column_7_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_26.setText(str(old_data.get("dirll_box_outter_column_8_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_29.setText(str(old_data.get("dirll_box_outter_column_9_distance", 0)))
            self.ui_form_dirll_box_every_pole_distance.lineEdit_27.setText(str(old_data.get("dirll_box_outter_column_10_distance", 0)))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk13")





            self.verticalSlider_6.setValue(old_data.get("polethread_out_circle_number", 0))
            self.pushButton_111.setText("取出保存数据" + str(old_data.get("polethread_out_circle_number", 0)))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk14")
            self.verticalSlider_25.setValue(old_data.get("pole_taile_mother_thread_out_circle_numeber", 0))
            self.pushButton_122.setText("取出保存数据" + str(old_data.get("pole_taile_mother_thread_out_circle_numeber", 0)))

            self.verticalSlider_13.setValue(old_data.get("tiger_dirll_pole_pole_tight_max_pressure", 0))
            self.pushButton_113.setText("取出保存数据" + str(old_data.get("tiger_dirll_pole_pole_tight_max_pressure", 0)))

            self.verticalSlider_19.setValue(old_data.get("tiger_dirll_pole_pole_tight_max_pressure_level", 0))
            self.pushButton_115.setText("取出保存数据" + str(old_data.get("tiger_dirll_pole_pole_tight_max_pressure_level", 0)))
            print(inspect.currentframe().f_lineno, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk15")
            self.verticalSlider_27.setValue(old_data.get("tiger_dirll_pole_pole_tight_push_max_pressure_level", 0))
            self.pushButton_124.setText("取出保存数据" + str(old_data.get("tiger_dirll_pole_pole_tight_push_max_pressure_level", 0)))

            self.verticalSlider_40.setValue(old_data.get("tiger_dirll_pole_pole_tight_push_max_pressure", 0))
            self.pushButton_140.setText("取出保存数据" + str(old_data.get("tiger_dirll_pole_pole_tight_push_max_pressure", 0)))

            self.verticalSlider_41.setValue(old_data.get("tiger_forward_move_max_coordinate", 0))
            self.pushButton_141.setText( "取出保存数据" + str(old_data.get("tiger_forward_move_max_coordinate", 0)))

            self.verticalSlider_42.setValue(old_data.get("tiger_coordinate_beam_not_reach_beamself_slot", 0))
            self.pushButton_142.setText( "取出保存数据" + str(old_data.get("tiger_coordinate_beam_not_reach_beamself_slot", 0)))

            self.verticalSlider_43.setValue(old_data.get("tiger_coordinate_beam_reached_beamself_slot", 0))
            self.pushButton_143.setText( "取出保存数据" + str(old_data.get("tiger_coordinate_beam_reached_beamself_slot", 0)))

            self.verticalSlider_28.setValue(old_data.get("tiger_self_middle_zero_coordinate_", 0))
            self.pushButton_125.setText( "取出保存数据" + str(old_data.get("tiger_self_middle_zero_coordinate_", 0)))



            self.verticalSlider_26.setValue(old_data.get("pole_taile_mother_thread_out_pressure", 0))
            self.pushButton_123.setText("取出保存数据" + str(old_data.get("pole_taile_mother_thread_out_pressure", 0)))

            self.verticalSlider_18.setValue(old_data.get("pole_loose_need_mini_circle", 0))
            self.pushButton_114.setText("取出保存数据" + str(old_data.get("pole_loose_need_mini_circle", 0)))

            self.verticalSlider_20.setValue(old_data.get("pole_loose_need_mini_circle_drill_level", 0))
            self.pushButton_116.setText("取出保存数据" + str(old_data.get("pole_loose_need_mini_circle_drill_level", 0)))




            self.verticalSlider_21.setValue(old_data.get("box_grap_hand_tight_strong", 0))
            self.pushButton_117.setText("取出保存数据" + str(old_data.get("box_grap_hand_tight_strong", 0)))


            self.verticalSlider_22.setValue(old_data.get("_drill_box_grap_hand_tight_slight", 0))
            self.pushButton_118.setText("取出保存数据" + str(old_data.get("_drill_box_grap_hand_tight_slight", 0)))



            self.verticalSlider_74.setValue(old_data.get("drill_box_grap_hand_tight_greater_strong", 0))
            self.pushButton_325.setText("取出保存数据" + str(old_data.get("_drill_box_grap_hand_tight_slight", 0)))

            self.verticalSlider_29.setValue(old_data.get("drill_box_grap_hand_relax_full", 0))
            self.pushButton_173.setText("取出保存数据" + str(old_data.get("drill_box_grap_hand_relax_full", 0)))

            self.verticalSlider_30.setValue(old_data.get("drill_box_grap_hand_relax_half", 0))
            self.pushButton_174.setText("取出保存数据" + str(old_data.get("drill_box_grap_hand_relax_half", 0)))

            self.verticalSlider_73.setValue(old_data.get("drill_box_grap_hand_relax_greater_part", 0))
            self.pushButton_324.setText("取出保存数据" + str(old_data.get("drill_box_grap_hand_relax_greater_part", 0)))




            self.verticalSlider_23.setValue(old_data.get("tiger_tight_time_", 0))
            self.pushButton_120.setText("取出保存数据" + str(old_data.get("tiger_tight_time_", 0)))

            self.verticalSlider_24.setValue(old_data.get("tiger_loose_time_", 0))
            self.pushButton_121.setText("取出保存数据" + str(old_data.get("tiger_loose_time_", 0)))


            self.pushButton_128.setText("取出保存数据" + str(old_data.get("no_load_move_to_coordinnate_point_max_pressure", 0)))
            self.pushButton_129.setText("取出保存数据" + str(old_data.get("no_load_move_start_level", 0)))
            self.pushButton_130.setText("取出保存数据" + str(old_data.get("no_load_move_end_level", 0)))
            self.pushButton_132.setText("取出保存数据" + str(old_data.get("no_load_move_parameter_contrl_distance", 0)))


            self.pushButton_175.setText("取出保存数据" + str(old_data.get("tiger_touch_delta", 0)))
            self.pushButton_177.setText("取出保存数据" + str(old_data.get("beam_push_pull_in_tiger_step_distance", 0)))
            self.pushButton_179.setText("取出保存数据" + str(old_data.get("delta_contrast_beam_ruler_tiger_ruler", 0)))



            self.pushButton_137.setText("取出保存数据" + str(old_data.get("first_point_coordinate", 0)))
            self.label_94.setText("取出保存数据" + str(old_data.get("first_point_coordinate", 0)))
            self.pushButton_144.setText("取出保存数据" + str(old_data.get("first_point_coordinate_delta", 0)))
            self.pushButton_149.setText("取出保存数据" + str(old_data.get("first_point_coordinate_map_tiger_ruler_range", 0)))
            self.pushButton_267.setText("取出保存数据" + str(old_data.get("first_point_characteristic_success_value", 0)))



            self.pushButton_138.setText("取出保存数据" + str(old_data.get("second_point_coordinate", 0)))
            self.label_100.setText("取出保存数据" + str(old_data.get("second_point_coordinate", 0)))
            self.pushButton_145.setText("取出保存数据" + str(old_data.get("second_point_coordinate_delta", 0)))
            self.pushButton_153.setText("取出保存数据" + str(old_data.get("second_point_coordinate_map_tiger_ruler_range", 0)))
            self.pushButton_181.setText("取出保存数据" + str(old_data.get("taile_thread_is_ok_point_coordinate", 0)))
            self.pushButton_182.setText("取出保存数据" + str(old_data.get("taile_thread_is_ok_point_coordinate_delat", 0)))
            self.pushButton_183.setText("取出保存数据" + str(old_data.get("taile_thread_is_ok_point_coordinate_map_tiger_ruler_range", 0)))




            self.pushButton_139.setText("取出保存数据" + str(old_data.get("fourth_point_coordinate", 0)))
            self.label_109.setText("取出保存数据" + str(old_data.get("fourth_point_coordinate", 0)))
            self.pushButton_146.setText("取出保存数据" + str(old_data.get("fourth_point_coordinate_delta", 0)))
            self.pushButton_154.setText("取出保存数据" + str(old_data.get("fourth_point_coordinate_map_tiger_ruler_range", 0)))
            self.pushButton_269.setText("取出保存数据" + str(old_data.get("Equepment_line_distance_measure_4m_beam_coordinate_delta", 0)))
            self.pushButton_271.setText("取出保存数据" + str(old_data.get("Equepment_line_distance_measure_beam_taile_coordinate_delta", 0)))
            self.pushButton_321.setText("取出保存数据" + str(old_data.get("Equepment_line_distance_measure_beam_head_coordinate_delta", 0)))
            self.pushButton_323.setText("取出保存数据" + str(old_data.get("Equepment_line_distance_measure_dirll_box_updown_coordinate_delta", 0)))
            self.pushButton_326.setText("取出保存数据" + str(old_data.get("drill_box.Equepment_drill_box_digit_piont.pole_point_delta", 0)))







            self.pushButton_158.setText("取出保存数据" + str(old_data.get("third_point_coordinate", 0)))
            self.label_111.setText("取出保存数据" + str(old_data.get("third_point_coordinate", 0)))
            self.pushButton_162.setText("取出保存数据" + str(old_data.get("third_point_coordinate_delta", 0)))
            self.pushButton_172.setText("取出保存数据" + str(old_data.get("third_point_coordinate_map_tiger_ruler_range", 0)))

    def save_parameter(self):
        if self.pushButton_56.isChecked():

            self.pushButton_56.setText("已经解除锁定")
            old_data = {}
            try:
                with open("parameter_backup_data.tex", "rb") as parameter:
                    old_data = pickle.load(parameter)
                    if len(old_data) == 0:
                        old_data = {}
                    # old_data.update(self.parameter_backup_data)
                    old_data = dict(old_data, **self.parameter_backup_data)
            except Exception:
                pass
            # with open("parameter_backup_data.tex", "wb") as parameter2:
                # pickle.dump(old_data, parameter2)
            self.orderSendToMachineProcessPipe.send(("save",))

    def stacke_add(self):
        self.guide_start_to_pole = guide_start_to_pole.Ui_Form()
        self.start_guide_to_pole_dialog = QtWidgets.QWidget()
        self.start_guide_to_pole_dialog.resize(681,321)
        self.guide_start_to_pole.setupUi(self.start_guide_to_pole_dialog)


        self.out_hole_guide_ = out_hole_guide.Ui_Form()
        self.guide_out_hole_dialog = QtWidgets.QWidget()
        self.guide_out_hole_dialog.resize(681, 321)
        self.out_hole_guide_.setupUi(self.guide_out_hole_dialog)

        self.guidin_control_ = guidin_control.Ui_Form()
        self.guidin_control_dialog = QtWidgets.QWidget()
        self.guidin_control_dialog.resize(681, 321)
        self.guidin_control_.setupUi(self.guidin_control_dialog)




        self.stacke_guide = QtWidgets.QStackedWidget()
        self.stacke_guide.addWidget(self.start_guide_to_pole_dialog)
        self.stacke_guide.addWidget(self.guide_out_hole_dialog)
        self.stacke_guide.addWidget(self.guidin_control_dialog)


    def guide_connect_start_into_hole(self):
        self.stacke_guide.setCurrentIndex(0)
        self.stacke_guide.show()

    def guide_connect_guiding(self):

        self.stacke_guide.setCurrentIndex(2)
        self.stacke_guide.show()

    def guide_connect_out_hole(self):
        self.stacke_guide.setCurrentIndex(1)
        self.stacke_guide.show()

    def encode_distance_messuer_tiger_dirll_arm_coordinate_end(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_47.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill", "end"), value))
                    print((("Equepment_tigger_tooch_f", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_47.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill_cycle_number", "end"), value))
                    print((("Equepment_tigger_tooch_f_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_336.text()
                self.lineEdit_47.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill", "end"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_336.text()
                self.lineEdit_47.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill_cycle_number", "end"), value))


    def encode_distance_messuer_tiger_dirll_arm_coordinate_stop(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_46.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill", "stop"), value))
                    print((("Equepment_tigger_drill", "stop"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_46.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill_cycle_number", "stop"), value))
                    print((("Equepment_tigger_drill_cycle_number", "stop"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_336.text()
                self.lineEdit_46.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill", "stop"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_336.text()
                self.lineEdit_46.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill_cycle_number", "stop"), value))


    def encode_distance_messuer_tiger_dirll_arm_coordinate_start(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_45.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill", "start"), value))
                    print((("Equepment_tigger_tooch_f", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_45.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill_cycle_number", "start"), value))
                    print((("Equepment_tigger_tooch_f_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_336.text()
                self.lineEdit_45.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill", "start"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_336.text()
                self.lineEdit_45.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_drill_cycle_number", "start"), value))


    def encode_distance_messuer_inner_tiger_arm_coordinate_end(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_54.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "end"), value))
                    print((("Equepment_tigger_tooch_b", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_54.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "end"), value))
                    print((("Equepment_tigger_tooch_b_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_334.text()
                self.lineEdit_54.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "end"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_334.text()
                self.lineEdit_54.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "end"), value))


    def encode_distance_messuer_inner_tiger_arm_coordinate_stop(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_55.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "stop"), value))
                    print((("Equepment_tigger_tooch_f", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_55.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "stop"), value))
                    print((("Equepment_tigger_tooch_f_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_334.text()
                self.lineEdit_55.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "stop"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_334.text()
                self.lineEdit_55.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "stop"), value))




    def encode_distance_messuer_inner_tiger_arm_coordinate_start(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_56.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "start"), value))
                    print((("Equepment_tigger_tooch_f", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_56.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "start"), value))
                    print((("Equepment_tigger_tooch_f_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_334.text()
                self.lineEdit_56.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "start"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_334.text()
                self.lineEdit_56.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "start"), value))








    def encode_distance_messuer_outer_tiger_arm_coordinate_end(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_53.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f", "end"), value))
                    print((("Equepment_tigger_tooch_f", "end"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_53.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f_cycle_number", "end"), value))
                    print((("Equepment_tigger_tooch_f_cycle_number", "end"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_332.text()
                self.lineEdit_53.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f", "end"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_332.text()
                self.lineEdit_53.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f_cycle_number", "end"), value))



    def encode_distance_messuer_outer_tiger_arm_coordinate_stop(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_52.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f", "stop"), value))
                    print((("Equepment_tigger_tooch_f", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_52.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f_cycle_number", "stop"), value))
                    print((("Equepment_tigger_tooch_f_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_332.text()
                self.lineEdit_52.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f", "stop"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_332.text()
                self.lineEdit_52.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_f_cycle_number", "stop"), value))




    def encode_distance_messuer_outer_tiger_arm_coordinate_start(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_51.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "start"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_51.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "start"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_332.text()
                self.lineEdit_51.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b", "start"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_332.text()
                self.lineEdit_51.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_tigger_tooch_b_cycle_number", "start"), value))



    def encode_distance_messuer_drill_rocker_arm_coordinate_end(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_50.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_coordinate", "end"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_50.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_cycle_number", "end"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_315.text()
                self.lineEdit_50.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_coordinate", "end"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_315.text()
                self.lineEdit_50.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_cycle_number", "end"), value))


    def encode_distance_messuer_drill_rocker_arm_coordinate_stop(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_49.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_coordinate", "stop"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_49.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_cycle_number", "stop"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_315.text()
                self.lineEdit_49.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_coordinate", "stop"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_315.text()
                self.lineEdit_49.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_cycle_number", "stop"), value))



    def encode_distance_messuer_drill_rocker_arm_coordinate_start(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_48.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_coordinate", "start"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_48.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_cycle_number", "start"), value))
                    print((("Equepment_pole_dirll_cycle_number", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_315.text()
                self.lineEdit_22.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_coordinate", "start"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_315.text()
                self.lineEdit_22.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_dirll_cycle_number", "start"), value))

    def encode_distance_messuer_push_pull_end(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_35.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_coordinate", "end"), value))
                    print((("Equepment_pole_push_pull_data_coordinate", "end"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_35.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_cycle_number", "end"), value))
                    print((("Equepment_pole_push_pull", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_313.text()
                self.lineEdit_35.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_coordinate", "end"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_313.text()
                self.lineEdit_35.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_cycle_number", "end"), value))



    def encode_distance_messuer_push_pull_stop(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_32.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_coordinate", "stop"), value))
                    print((("Equepment_pole_push_pull_data_coordinate", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_32.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_cycle_number", "stop"), value))
                    print((("Equepment_pole_push_pull", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_313.text()
                self.lineEdit_32.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_coordinate", "stop"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_313.text()
                self.lineEdit_32.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_cycle_number", "stop"), value))






    def encode_distance_messuer_push_pull_start(self):
        if self.pushButton_188.isChecked():
            try:
                if self.comboBox.currentText() == "拉线485传感器":
                    value = float(self.lineEdit_22.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_coordinate", "start"), value))
                    print((("Equepment_pole_push_pull_data_coordinate", "start"), value))
                elif self.comboBox.currentText() == "绝对485编码器":
                    value = float(self.lineEdit_22.text())
                    self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_cycle_number", "start"), value))
                    print((("Equepment_pole_push_pull", "start"), value))
            except Exception as ff:
                print(inspect.currentframe().f_lineno, __class__)
                pass
        else:
            if self.comboBox.currentText() == "拉线485传感器":
                value = self.label_313.text()
                self.lineEdit_22.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_coordinate", "start"), value))
            elif self.comboBox.currentText() == "绝对485编码器":
                value = self.label_313.text()
                self.lineEdit_22.setText(value)
                value = float(value)
                self.orderSendToMachineProcessPipe.send((("Equepment_pole_push_pull_data_cycle_number", "start"), value))

    def dirll_box_grap_hand_to_beam_cant_stop_beam_coordinate(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_24.text())
            except Exception:
                self.lineEdit_24.setText("重新输入")
                return
            self.parameter_backup_data["point_unstop_beam_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point_unstop_beam_coordinate", value))
            print(("point_unstop_beam_coordinate", value))
            try:
                value = float(self.lineEdit_119.text())
            except Exception:
                self.lineEdit_119.setText("重新输入")
                return
            self.parameter_backup_data["point_unstop_beam_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point_unstop_beam_cycle_number", value))
            print(("point_unstop_beam_cycle_number", value))
        else:
            value = self.label_223.text()
            self.lineEdit_24.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_24.setText("重新输入")
                return
            self.parameter_backup_data["point_unstop_beam_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point_unstop_beam_coordinate", value))
            value = self.label_224.text()
            self.lineEdit_119.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_119.setText("重新输入")
                return
            self.parameter_backup_data["point_unstop_beam_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point_unstop_beam_cycle_number", value))





    def dirll_box_grap_hand_to_beam_relax_hand_coordinate(self):  # didnt find the data
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_26.text())
            except Exception:
                self.lineEdit_26.setText("重新输入")
                return
            self.parameter_backup_data["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate", value))
            print(("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate", value))
            try:
                value = float(self.lineEdit_118.text())
            except Exception:
                self.lineEdit_118.setText("重新输入")
                return
            self.parameter_backup_data["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number", value))

            print(("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number", value))
        else:
            value = self.label_223.text()
            self.lineEdit_26.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_26.setText("重新输入")
                return
            self.parameter_backup_data["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate", value))

            value = self.label_224.text()
            self.lineEdit_118.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_118.setText("重新输入")
                return
            self.parameter_backup_data["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number", value))



    def dirll_box_grap_hand_to_beam_get_pole(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_30.text())
            except Exception:
                self.lineEdit_30.setText("重新输入")
                return
            self.parameter_backup_data["point_beam_grap_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point_beam_grap_coordinate", value))

            print(("point_beam_grap_coordinate", value))
            try:
                value = float(self.lineEdit_117.text())
            except Exception:
                self.lineEdit_117.setText("重新输入")
                return
            self.parameter_backup_data["point_beam_grap_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point_beam_grap_cycle_number", value))

            print(("point_beam_grap_cycle_number", value))
        else:
            value = self.label_223.text()
            self.lineEdit_30.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_30.setText("重新输入")
                return
            self.parameter_backup_data["point_beam_grap_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point_beam_grap_coordinate", value))

            value = self.label_224.text()
            self.lineEdit_117.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_117.setText("重新输入")
                return
            self.parameter_backup_data["point_beam_grap_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point_beam_grap_cycle_number", value))




    def drill_box_3_coordinate_grap_hand_coordinate(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_25.text())
            except Exception:
                self.lineEdit_25.setText("重新输入")
                return
            self.parameter_backup_data["point3_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point3_coordinate", value))

            print(("point2_coordinate", value))
            try:
                value = float(self.lineEdit_116.text())
            except Exception:
                self.lineEdit_116.setText("重新输入")
                return
            self.parameter_backup_data["point3_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point3_cycle_number", value))

            print(("point3_cycle_number", value))
        else:
            value = self.label_223.text()
            self.lineEdit_25.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_25.setText("重新输入")
                return
            self.parameter_backup_data["point3_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point3_coordinate", value))

            value = self.label_224.text()
            self.lineEdit_116.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_116.setText("重新输入")
                return
            self.parameter_backup_data["point3_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point3_cycle_number", value))


    def drill_box_2_coordinate_grap_hand_coordinate(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_29.text())
            except Exception:
                self.lineEdit_29.setText("重新输入")
                return
            self.parameter_backup_data["point2_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point2_coordinate", value))

            print(("point2_coordinate", value))
            try:
                value = float(self.lineEdit_115.text())
            except Exception:
                self.lineEdit_115.setText("重新输入")
                return
            self.parameter_backup_data["point2_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point2_cycle_number", value))

            print(("point2_cycle_number", value))
        else:
            value = self.label_223.text()
            self.lineEdit_29.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_29.setText("重新输入")
                return
            self.parameter_backup_data["point2_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point2_coordinate", value))

            value = self.label_224.text()
            self.lineEdit_115.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_115.setText("重新输入")
                return
            self.parameter_backup_data["point2_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point2_cycle_number", value))



    def drill_box_1_coordinate_grap_hand_coordinate(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_27.text())
            except Exception:
                self.lineEdit_27.setText("重新输入")
                return
            self.parameter_backup_data["point1_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point1_coordinate", value))

            print(("point1_coordinate", value))
            try:
                value = float(self.lineEdit_114.text())
            except Exception:
                self.lineEdit_114.setText("重新输入")
                return
            self.parameter_backup_data["point1_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point1_cycle_number", value))

            print(("point1_cycle_number", value))
        else:
            value = self.label_223.text()
            self.lineEdit_27.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_27.setText("重新输入")
                return
            self.parameter_backup_data["point1_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("point1_coordinate", value))

            value = self.label_224.text()
            self.lineEdit_114.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_114.setText("重新输入")
                return
            self.parameter_backup_data["point1_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("point1_cycle_number", value))





    def the_beam_to_the_coordinate_man_can_get_out_pole(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_28.text())
            except Exception:
                self.lineEdit_28.setText("重新输入")
                return
            self.parameter_backup_data["the_new_point_man_can_let_pole_out_beam_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("the_new_point_man_can_let_pole_out_beam_coordinate", value))

            print(("beam_taile_5cm_coordinate", value))
            try:
                value = float(self.lineEdit_107.text())
            except Exception:
                self.lineEdit_107.setText("重新输入")
                return
            self.parameter_backup_data["the_new_point_man_can_let_pole_out_beam_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("the_new_point_man_can_let_pole_out_beam_cycle_number", value))

            print(("beam_taile_5cm_cycle_number", value))
        else:
            value = self.label_221.text()
            self.lineEdit_28.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_28.setText("重新输入")
                return
            self.parameter_backup_data["the_new_point_man_can_let_pole_out_beam_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("the_new_point_man_can_let_pole_out_beam_coordinate", value))

            value = self.label_222.text()
            self.lineEdit_107.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_107.setText("重新输入")
                return
            self.parameter_backup_data["the_new_point_man_can_let_pole_out_beam_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("the_new_point_man_can_let_pole_out_beam_cycle_number", value))


    def man_let_pole_and_machin_back_the_last_point(self): # man_give_pole_place_back_last_point cant back,and wait the order to farward  not  finished
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_31.text())
            except Exception:
                self.lineEdit_31.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place_back_last_point_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place_back_last_point_coordinate", value))

            print(("beam_taile_5cm_coordinate", value))
            try:
                value = float(self.lineEdit_106.text())
            except Exception:
                self.lineEdit_106.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place_back_last_point_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place_back_last_point_cycle_number", value))

            print(("beam_taile_5cm_cycle_number", value))
        else:
            value = self.label_221.text()
            self.lineEdit_31.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_31.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place_back_last_point_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place_back_last_point_coordinate", value))

            value = self.label_222.text()
            self.lineEdit_106.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_106.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place_back_last_point_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place_back_last_point_cycle_number", value))



    def set_parameter_the_man_let_pole_beam_point(self):   ## let pole in beam
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_23.text())
            except Exception:
                self.lineEdit_23.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place", value))

            print(("man_give_pole_place", value))
            try:
                value = float(self.lineEdit_105.text())
            except Exception:
                self.lineEdit_105.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place_cycle_number", value))

            print(("man_give_pole_place_cycle_number", value))
        else:
            value = self.label_221.text()
            self.lineEdit_23.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_23.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place", value))

            value = self.label_222.text()
            self.lineEdit_105.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_105.setText("重新输入")
                return
            self.parameter_backup_data["man_give_pole_place_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("man_give_pole_place_cycle_number", value))



    def the_drill_box_down_the_bottom(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_112.text())
            except Exception:
                self.lineEdit_112.setText("重新输入")
                return
            self.parameter_backup_data["box_updown_bottom"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_bottom", value))

        else:
            value = self.label_582.text()
            self.lineEdit_112.setText(value)
            try:
                value = float(value)
            except Exception:

                return
            self.parameter_backup_data["box_updown_bottom"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_bottom", value))



    def the_drill_box_up_to_the_top(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_108.text())
            except Exception:
                self.lineEdit_108.setText("重新输入")
                return
            self.parameter_backup_data["box_updown_column_up"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_column_up", value))

        else:
            value = self.label_582.text()
            self.lineEdit_108.setText(value)
            try:
                value = float(value)
            except Exception:

                return
            self.parameter_backup_data["box_updown_column_up"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_column_up", value))


    def the_drill_box_down_to_grap_hand_can_hold_point(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_113.text())
            except Exception:
                self.lineEdit_113.setText("重新输入")
                return
            self.parameter_backup_data["box_updown_column_can_grap_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_column_can_grap_coordinate", value))

            print(("box_updown_column_can_grap_coordinate", value))
            try:
                value = float(self.lineEdit_113.text())
            except Exception:
                self.lineEdit_113.setText("重新输入")
                return
            self.parameter_backup_data["box_updown_column_can_grap_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_column_can_grap_cycle_number", value))

            print(("box_updown_column_can_grap_cycle_number", value))
        else:
            value = self.label_223.text()
            self.lineEdit_113.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_113.setText("重新输入")
                return
            self.parameter_backup_data["box_updown_column_can_grap_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_column_can_grap_coordinate", value))

            value = self.label_224.text()
            self.lineEdit_113.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_113.setText("重新输入")
                return
            self.parameter_backup_data["box_updown_column_can_grap_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("box_updown_column_can_grap_cycle_number", value))



    def set_parameters_the_last_come_back_pole_to_unload(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_10.text())
            except Exception:
                self.lineEdit_10.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("main_beam_last_pole_up_down_expangd_hole_coordinate", value))

            print(("beam_taile_5cm_coordinate", value))
            try:
                value = float(self.lineEdit_104.text())
            except Exception:
                self.lineEdit_104.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("main_beam_last_pole_up_down_expangd_hole_cycle_number", value))

            print(("beam_taile_5cm_cycle_number", value))
        else:
            value = self.label_221.text()
            self.lineEdit_10.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_10.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("main_beam_last_pole_up_down_expangd_hole_coordinate", value))

            value = self.label_222.text()
            self.lineEdit_104.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_104.setText("重新输入")
                return
            self.parameter_backup_data["main_beam_last_pole_up_down_expangd_hole_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("main_beam_last_pole_up_down_expangd_hole_cycle_number", value))





    def set_parameters_the_beam_point_box_hand_can_out_to_get_pole(self):
        if self.pushButton_188.isChecked():
            try:
                value = float(self.lineEdit_9.text())
            except Exception:
                self.lineEdit_9.setText("重新输入")
                return
            self.parameter_backup_data["pole_pull_back_can_out_box_hand_to_grap_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("pole_pull_back_can_out_box_hand_to_grap_coordinate", value))

            print(("pole_pull_back_can_out_box_hand_to_grap_coordinate", value))
            try:
                value = float(self.lineEdit_103.text())
            except Exception:
                self.lineEdit_103.setText("重新输入")
                return
            self.parameter_backup_data["pole_pull_back_can_out_box_hand_to_grap_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("pole_pull_back_can_out_box_hand_to_grap_cycle_number", value))

            print(("pole_pull_back_can_out_box_hand_to_grap_cycle_number", value))
        else:
            value = self.label_221.text()
            self.lineEdit_9.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_9.setText("重新输入")
                return
            self.parameter_backup_data["pole_pull_back_can_out_box_hand_to_grap_coordinate"] = value
            self.orderSendToMachineProcessPipe.send(("pole_pull_back_can_out_box_hand_to_grap_coordinate", value))

            value = self.label_222.text()
            self.lineEdit_103.setText(value)
            try:
                value = float(value)
            except Exception:
                self.lineEdit_103.setText("重新输入")
                return
            self.parameter_backup_data["pole_pull_back_can_out_box_hand_to_grap_cycle_number"] = value
            self.orderSendToMachineProcessPipe.send(("pole_pull_back_can_out_box_hand_to_grap_cycle_number", value))


    def set_parameters_back_taile_5cm(self):
        if self.pushButton_188.isChecked():
                try:
                    value = float(self.lineEdit_8.text())
                except Exception:
                    self.lineEdit_8.setText("重新输入")
                    return
                self.parameter_backup_data["beam_taile_5cm_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("beam_taile_5cm_coordinate", value))

                print(("beam_taile_5cm_coordinate", value))
                try:
                    value = float(self.lineEdit_102.text())
                except Exception:
                    self.lineEdit_102.setText("重新输入")
                    return
                self.parameter_backup_data["beam_taile_5cm_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("beam_taile_5cm_cycle_number", value))

                print(("beam_taile_5cm_cycle_number", value))
        else:
                value = self.label_221.text()
                self.lineEdit_8.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_8.setText("重新输入")
                    return
                self.parameter_backup_data["beam_taile_5cm_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("beam_taile_5cm_coordinate", value))

                value = self.label_222.text()
                self.lineEdit_102.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_102.setText("重新输入")
                    return
                self.parameter_backup_data["beam_taile_5cm_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("beam_taile_5cm_cycle_number", value))





    def set_parameters__back_pole_taile_thread(self):
        if self.pushButton_188.isChecked():
                try:
                    value = float(self.lineEdit_14.text())
                except Exception:
                    self.lineEdit_14.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_coordinate", value))

                print(("Equepment_pole_push_pull_data_coordinate", value))
                try:
                    value = float(self.lineEdit_100.text())
                except Exception:
                    self.lineEdit_100.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_cycle_number", value))

                print(("pole_in_middle_tiger_tooth_cycle_number", value))

        else:
                value = self.label_221.text()
                self.lineEdit_14.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_14.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_coordinate", value))

                value = self.label_222.text()
                self.lineEdit_100.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_100.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_to_taile_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_to_taile_cycle_number", value))

    def get_operator_data(self):
        permit_file_name = os.path.join(os.getcwd(), "permit_file_name.csv")
        data = pandas.read_csv(permit_file_name, header=0, )
        return data


    def operate_lock_pushButton_24(self):
        if self.pushButton_24.isChecked():
            self.pushButton_24.setText("手动操作1已解锁")
        else:
            self.pushButton_24.setText("手动操作1锁定中")

    def operate_lock_pushButton_67(self):
        if self.pushButton_67.isChecked():
            self.pushButton_67.setText("手动操作2已解锁")
        else:
            self.pushButton_67.setText("手动操作2锁定中")

    def manual_back_operator_top_backward_(self):
        """
                send_data = self.sendData(target_ip, function_name, forword_step_distance)
                print(send_data)

        """
        if (self.pushButton_24.isChecked())&(self.pushButton_67.isChecked()):
            if self.current_operator:
                function_name = "manual_back_operator_top_backward_"
                try:
                    forword_step_distance = self.lineEdit_121.text()
                except Exception as ff:
                    forword_step_distance = 50
                send_data = self.sendData(communication_setting.locale_lisen_ip, function_name, forword_step_distance)
                self.orderSendToMachineProcessPipe.send(send_data)

    def machine_pause_stop(self):
        if (self.pushButton_24.isChecked()) & (self.pushButton_67.isChecked()):
            if self.current_operator:
                operator_ = self.current_operator
                target_machine_id = self.current_operate_machine_id

                function_name = "machine_pause_stop"
                try:
                    forword_step_distance = self.lineEdit_121.text()
                except Exception as ff:
                    forword_step_distance = 50
                send_data = self.sendData(machine_ip, function_name, forword_step_distance)

                self.orderSendToMachineProcessPipe.send(send_data)

    def get_target_ip(self):
        text = self.lineEdit_122.text()
        # if text:
        #     ip = eval(text)
        # else:
        #     ip = communication_setting.window_ip

        return communication_setting.locale_lisen_ip

    def sendData(self, target_ip, function_name, arges):
        """
        sendData format is uuid, machine_id, function_code, target_obj_code, target_ip, function_name, arges

        """

        function_code = function_code6001
        target_obj_code = function_code8001
        send_data = (
        str(uuid.uuid1()), machine_id, function_code, target_obj_code, target_ip, function_name, arges)
        return send_data

    def operator_top_forward_manual(self):
        if (self.pushButton_24.isChecked())&(self.pushButton_67.isChecked()):
            if self.current_operator:
                target_ip = self.get_target_ip()
                function_name = "operator_top_forward_manual"
                try:
                    forword_step_distance = self.lineEdit_121.text()
                except Exception as ff:
                    forword_step_distance = 50
                send_data = self.sendData(target_ip, function_name, forword_step_distance)
                print(send_data)
                print(f"this is the ui clicked send data send file is {__file__} current line is {inspect.currentframe().f_lineno} / \n"
                      f"data for mat is 'uuid, machine_id, function_code, target_obj_code, target_ip, function_name, arges '"
                      )
                self.orderSendToMachineProcessPipe.send(send_data)

    def set_parameters_middle_tigger_teeth(self):
        if self.pushButton_188.isChecked():
                try:
                    value = float(self.lineEdit_5.text())
                except Exception:
                    self.lineEdit_5.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_coordinate", value))
                print(("Equepment_pole_push_pull_data_coordinate", value))
                try:
                    value = float(self.lineEdit_98.text())
                except Exception:
                    self.lineEdit_98.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_cycle_number", value))

                print(("pole_in_middle_tiger_tooth_cycle_number", value))

        else:
                value = self.label_221.text()
                self.lineEdit_5.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_5.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_coordinate", value))

                value = self.label_222.text()
                self.lineEdit_98.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_98.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_cycle_number", value))


    def set_parameters_middle_tigger_back_20_thread(self):      ## back20thread_pole
        if self.pushButton_188.isChecked():

                try:
                    value = float(self.lineEdit_6.text())
                except Exception:
                    self.lineEdit_6.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_tiggerback_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_tiggerback_coordinate", value))

                print(("Equepment_pole_push_pull_data_coordinate", value))
                try:
                    value = float(self.lineEdit_99.text())
                except Exception:
                    self.lineEdit_99.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_tiggerback_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_tiggerback_cycle_number", value))

                print(("pole_in_middle_tiger_tooth_tiggerback_cycle_number", value))

        else:
                value = self.label_221.text()
                self.lineEdit_6.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_6.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_tiggerback_coordinate"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_tiggerback_coordinate", value))

                value = self.label_222.text()
                self.lineEdit_99.setText(value)
                try:
                    value = float(value)
                except Exception:
                    self.lineEdit_99.setText("重新输入")
                    return
                self.parameter_backup_data["pole_in_middle_tiger_tooth_tiggerback_cycle_number"] = value
                self.orderSendToMachineProcessPipe.send(("pole_in_middle_tiger_tooth_tiggerback_cycle_number", value))


    def valuechangged(self):
        value = self.verticalSlider_47.value()   # value is the current point to out hole distance.

        self.lineEdit_361.setText(str(value))
        return value

    def valuechangged45(self):
        value = self.verticalSlider_45.value()

        self.lineEdit_365.setText(str(value))
        return value

    def valuechangged44(self):
        value = self.verticalSlider_44.value()

        self.lineEdit_364.setText(str(value))
        return value

    def valuechangged46(self):
        value = self.verticalSlider_46.value()

        self.lineEdit_377.setText(str(value))
        return value

    def radiobotton(self):
        radiobutton = self.tabWidget.sender()

        if radiobutton.isChecked() == True:

            self.deepfirst = False

        return self.deepfirst

    def radiobotton2(self):
        radiobutton = self.tabWidget.sender()
        if radiobutton.isChecked() == True:
            self.deepfirst = True

    def value_lineEdit_376(self):
        if self.lineEdit_376.text() == "":
            n = 0
        else:
            try:
                n = float(self.lineEdit_376.text())
            except:
                n = 0
        return n

    def value_lineEdit_375(self):
        if self.lineEdit_375.text() == "":
            n = 0
        else:
            try:
                n = float(self.lineEdit_375.text())
            except:
                n = 0
        return n

    def value_lineEdit_360(self):
        if self.lineEdit_360.text() == "":
            n = 0
        else:
            try:
                n = float(self.lineEdit_360.text())
            except:
                n = 0
        return n

    def value_lineEdit_359(self):
        if self.lineEdit_359.text() == "":
            n = 0
        else:
            try:
                n = float(self.lineEdit_359.text())
            except:
                n = 0
        return n

        # self.lineEdit_362.textChanged.connect(self.value_lineEdit_362)

    def value_lineEdit_362(self):
        if self.lineEdit_362.text() == "":
            n = 0
        else:
            try:
                n = float(self.lineEdit_362.text())
            except:
                n = 0
        if n > self.verticalSlider_47.value()/3:
                return float(self.verticalSlider_47.value()/3)
        return n

    def Equepment_data_disaplay(self):
            data = {"main_beam_coordinate_single1": 1, "hand_grap_coordinate_single2": 2, }
            time.sleep(0.2)
            self.label_221.setText(str(data["main_beam_coordinate_single1"] ))
            self.label_223.setText(str(data["hand_grap_coordinate_single2"] ))


    def messge_box_wrongdata(self,uui,setdata,outdata=None):
       uui.setVisible(setdata)
       if outdata != None:
           uui.setText(str(outdata))
    def write_message_box_every_data(self,uui,setdata,outdata=(None,None,None,None,None)):
        x = list(map(self.messge_box_wrongdata,uui,setdata,outdata))
    def write_all_message_box_every_data(self,setdata,outdata=(None,None,None,None,None)):
        ui_index = 0
        for every_ in setdata:
            self.write_message_box_every_data(self.message_lable_menu[ui_index],every_,outdata)
            if ui_index == 5:
                break
            ui_index = ui_index + 1
        if len(setdata) < 6:
            index2 = len(setdata)
            while index2 < 6:
                self.write_message_box_every_data(self.message_lable_menu[index2],[False,False,False,False,False],outdata)
                index2 = index2 +1
                if index2 > 5:
                    break
    def init_message_box(self):

        for every in range(len(self.message_lable_menu)):
            self.write_message_box_every_data(self.message_lable_menu[every],(False,False,False,False,False))



class calclude_pole_guide_parameter():
    def __init__(self):
        self.plan_angle = 3

        self.every_degrees_distance = 17
        self.safe_angle = 2.5
        self.paralle_width = 200
        self.totle_angle = 14
        self.target_changge_distance = 0
        self.mini_pole_number = 0
        self.mini_distance = 0
        self.actual_distance = 0
        self.av_angle = 2.5
        self.out_angle = 15
        self.out_high = 1.3
        self.current_high = 22
        self.current_angle = 0
        self.data = {}



    def calclude_parameter(self,totle_angle,paralle_width):
        self.totle_angle = totle_angle
        self.paralle_width = paralle_width
        return True

    def calclude_pole_number_min(self):
        if self.mini_pole_number*3 < self.actual_distance:
            self.mini_pole_number = self.totle_angle/self.safe_angle
            self.mini_distance = self.mini_pole_number*3

    def  takeSecond(self,elem):
        return abs(elem[1] -self.out_high)


    def  takeangle(self,elem):
        return abs(elem[2]-self.out_angle)

    def calclude_use_high_lenth(self,n,high_range=15,angle_rangge=2,angle_fist = True):

            totle_angle = self.out_angle - self.current_angle
            self.angle_range = angle_rangge
            self.highrange = high_range
            recommend_data2 = []
            recommend_data = []
            for  pole_1 in range(self.plan_angle +1):
                for pole_2  in range(self.plan_angle +1):
                    for pole_3 in range(self.plan_angle + 1):
                        for pole_4 in range(self.plan_angle + 1):
                            for pole_5 in range(self.plan_angle + 1):
                                for pole_6 in range(self.plan_angle + 1):
                                    if abs((pole_1 + pole_2+pole_3+pole_4+pole_5 + pole_6)- self.totle_angle) < angle_rangge:
                                        high = (self.current_angle+pole_1)*5.1 + (self.current_angle+pole_1+pole_2)*5.1 +(self.current_angle+pole_1+pole_2 + pole_3)*5.1 + (self.current_angle+pole_1+pole_2 + pole_3 + pole_4) * 5.1 + (self.current_angle+pole_1+pole_2 + pole_3 + pole_4 + pole_5) * 5.1 +(self.current_angle+pole_1+pole_2 + pole_3 + pole_4 + pole_5 + pole_6)*5.1
                                        self.data[(pole_1,pole_2,pole_3,pole_4,pole_5,pole_6)] = high
                                        angle = pole_1 + pole_2 + pole_3 + pole_4 + pole_5 + pole_6
                                        if abs((high +self.out_high*10)-self.current_high*10) < high_range and abs(angle-self.out_angle) < angle_rangge:
                                           recommend_data.append(((pole_1,pole_2,pole_3,pole_4,pole_5,pole_6),int(self.current_high-high/10)/10,angle))
            if n == 1:
                for every in recommend_data:
                    if every[0] <= (0,0,0,0,0,self.plan_angle):
                        recommend_data2.append(every)
            if n == 2:

                for every in recommend_data:
                    if every[0] <= (0,0,0,0,self.plan_angle,self.plan_angle):
                        recommend_data2.append(every)
            if n == 3:

                for every in recommend_data:
                    if every[0] <= (0,0,0,self.plan_angle,self.plan_angle,self.plan_angle):

                        recommend_data2.append(every)
            if n == 4:

                for every in recommend_data:
                    if every[0] <= (0,0,self.plan_angle,self.plan_angle,self.plan_angle,self.plan_angle):
                        recommend_data2.append(every)
            if n == 5:
                for every in recommend_data:
                    if every[0] <= (0, self.plan_angle, self.plan_angle, self.plan_angle, self.plan_angle, self.plan_angle):
                        recommend_data2.append(every)

            if n == 6:
                for every in recommend_data:
                    if every[0] <= (self.plan_angle, self.plan_angle, self.plan_angle, self.plan_angle, self.plan_angle, self.plan_angle):
                        recommend_data2.append(every)
            if angle_fist == True:
                recommend_data2.sort(key=self.takeSecond)
            else:
                recommend_data2.sort(key=self.takeangle)

            return recommend_data2[:4]

    def sort_distance(self,data):
        return data[1]

    def calclude_relative_point(self,plan_poles,plan_angle,angle_to_target_paralle_line,vertical_distance_to_target_paralle_line,distance_delta_rangge = 15):
        data = []
        data2 = []
        mud_distance = 0
        all_angle = 0
        for pole1 in range(plan_angle+1):
            for pole2 in range(plan_angle+1):
                for pole3 in range(plan_angle+1):
                    for pole4 in range(plan_angle+1):
                        for pole5 in range(plan_angle+1):
                            for pole6 in  range(-plan_angle, 1):
                                for pole7 in range(-plan_angle, 1):
                                    for pole8 in range(-plan_angle, 1):
                                        for pole9 in range(-plan_angle, 1):
                                            for pole10 in range(-plan_angle, 1):
                                                plan_distance = (pole1 + angle_to_target_paralle_line)*5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4 + pole5) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4 + pole5 + pole6) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4 + pole5 + pole6 + pole7) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4 + pole5 + pole6 + pole7 + pole8) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4 + pole5 + pole6 + pole7 + pole8 + pole9) * 5.1 + \
                                                                (pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4 + pole5 + pole6 + pole7 + pole8 + pole9 + pole10) * 5.1
                                                mud_distance = abs(plan_distance-vertical_distance_to_target_paralle_line)
                                                all_angle = pole1 + angle_to_target_paralle_line + pole2 + pole3 + pole4 + pole5 + pole6 + pole7 + pole8 + pole9 + pole10
                                                if abs(mud_distance) < distance_delta_rangge:
                                                    data.append((pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10),mud_distance,all_angle)
        if plan_poles == 6:
            for every_pole in data:
                if(0,0,pole3,pole4,pole5,pole6,pole7,pole8,0,0)< every_pole[0]<= (0,0,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10):
                    data2.append(every_pole)
        if plan_poles == 8:
            for every_pole in data:
                if (0, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, 0) < every_pole[0] <= ( 0, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, pole10):
                    data2.append(every_pole)
        if plan_poles == 4:
            for every_pole in data:
                if(0,0,0,pole4,pole5,pole6,pole7,0,0,0)< every_pole[0]<= (0,0,0,pole4,pole5,pole6,pole7,pole8,pole9,pole10):
                    data2.append(every_pole)
        data2.sort(key=self.sort_distance)
        return data2[0:4]



def wiget_run(ui_widget_main,machine_equepment_read_data,machine_board_read_data,order_to_machine):
    application = QtWidgets.QApplication(sys.argv)
    widget_main = QtWidgets.QMainWindow()
    setattr(ui_widget_main, "machine_equepment_read_data", machine_equepment_read_data)
    setattr(ui_widget_main, "machine_board_read_data", machine_board_read_data)
    setattr(ui_widget_main, "order_to_machine", order_to_machine)
    ui_widget_main.setupUi(widget_main)
    widget_main.show()
    sys.exit(application.exec_())

def window_run(orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe):
    application = QtWidgets.QApplication(sys.argv)
    widget_main = QtWidgets.QMainWindow()
    ui_widget_main = UUi_MainWindow()
    ui_widget_main.setupUi(widget_main, orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe)
    widget_main.show()
    sys.exit(application.exec_())

if __name__ == "__main__":
    # wiget_run(7,8)
    pipr, pips = Pipe()
    application = QtWidgets.QApplication(sys.argv)
    widget_main = QtWidgets.QMainWindow()
    ui_widget_main = UUi_MainWindow()
    ui_widget_main.setupUi(widget_main, pips)
    widget_main.show()
    sys.exit(application.exec_())
