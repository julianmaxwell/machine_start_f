import pandas
import numpy
pandas.set_option("display.max_rows", 10000)
pandas.set_option("display.max_columns", 300)
pandas.set_option("display.width", 15000)
path_ = "D:\machine\机器端\machine_run_recorder.csv"
data = pandas.read_csv(path_)
import time
# print(data)
# for d in data.columns:
#     print(d)
# print(len(data.columns))
"""

"""
def creat_new_data():
    # in class every_order
    data_d = {
        "order_name": "self.order_name",
        "order_parameter": None,
        "current_push_pull_gear": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.get_current_gear",
        "current_push_pull_gear_coordinate": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.coordinate",
        "current_drill_gear": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.get_current_gear",
        "current_drill_gear_coordinate": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_dirll.coordinate",
        "push_pull_coordinate_begin": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.coordinate_start",
        "push_pull_coordinate_stop": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pole_push_pull.coordinate_stop",
        "tigger_head_move_coordinate": "self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate",
        "tigger_head_move_coordinate_middle": "self.interface_operator_obj.machine_obj.main_beam.tiger_self_middle_zero_coordinate_",
        "tigger_coordinate_outer": "self.interface_operator_obj.machine_obj.main_beam.Equepment_tigger_tooch_f.coordinate",
        "tigger_outer_full_open_coordinate": "self.interface_operator_obj.machine_obj.main_beam.tiger_outer_rule_relax",
        "tigger_outer_full_grap_coordinate": "self.interface_operator_obj.machine_obj.main_beam.tiger_outer_rule_grap",
        "tigger_inner_coordinate": "self.interface_operator_obj.machine_obj.main_beam.Equepment_tigger_tooch_b.coordinate",
        "tigger_inner_grap_coordinate": "self.interface_operator_obj.machine_obj.main_beam.tiger_inner_rule_grap",
        "tigger_inner_relax_coordinate": "self.interface_operator_obj.machine_obj.main_beam.tiger_outer_rule_grap",
        "tigger_inner_drill_relax": "self.interface_operator_obj.machine_obj.main_beam.tigger_inner_drill_relax",
        "current_pole_number_in_hole": "self.interface_operator_obj.machine_obj.main_beam.current_pole_number_in_hole",
        "current_pole_distance_not_in_hole": "self.interface_operator_obj.machine_obj.main_beam.current_pole_distance_not_in_hole",
        "messure_push_pull": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_push_pull.pressure",
        "messure_drill": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_torque.pressure",
        "messure_water": "self.interface_operator_obj.machine_obj.main_beam.Equepment_pressure_warter.pressure",
        "water_deep": "self.interface_operator_obj.machine_obj.main_beam.Equepment_warter_deep_measure.water_deep_number",
        "oil_deep": 70,
        "beam_coordinate": "self.interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate",
        "hand_coordinate": "self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_line_distance_measure_1m_drill_box.coordinate",
        "hand_get_pole_at_beam_coordinate": "self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point_beam_grap_coordinate",
        "hand_box_unstop_beam_driving_coordinate": "self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point_unstop_beam_coordinate",
        "hand_box_cloumns_1_coordinate": "self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point1_coordinate",
        "hand_box_cloumns_3_coordinate": "self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.point3_coordinate",
        "beam_head_coordinate": "self.interface_operator_obj.machine_obj.main_beam.beam_begin",
        "beam_tail_coordinate": "self.interface_operator_obj.machine_obj.main_beam.beam_end",
        "box_up_coordinate": "self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.box_updown_column_up",
        "box_half_up_coordinate": "self.interface_operator_obj.machine_obj.main_beam.drill_box.Equepment_drill_box_digit_piont.box_updown_colbox_updown_column_can_grapumn_up",
        "box_hand_relax_grap": 0, # the percent 0 ~ 100
        "machine_angle_H": 0,
        "machine_angle_V": 0,
        "pole_angle_at_machine": "self.interface_operator_obj.machine_obj.main_beam.Equepment_angle_torque_to_pole.angle",
        "pole_angle_at_machine_12colock": 10,
        "pole_angle_at_remote": 20,
        "time_": time.time(),
        "pic_box_colum1_pole_number": None,
        "pic_hand_grap_faild": None,
        "pic_file": None,
        "action_apraise_recorder": 5,
    }
    data_d_n = data_d.items()
    data_fram = pandas.DataFrame(data_d_n, columns=["key", "value"])
    data_fram = data_fram.set_index("key")

    data_fram.loc["order_name", "alias"] = "命令名称"
    data_fram.loc["order_parameter", "alias"] = "命令参数"
    data_fram.loc["current_push_pull_gear", "alias"] = "当前推拉档位"
    data_fram.loc["current_push_pull_gear_coordinate", "alias"] = "当前推拉坐标"
    data_fram.loc["current_drill_gear", "alias"] = "当前旋转档位"
    data_fram.loc["current_drill_gear_coordinate", "alias"] = "当前旋转坐标"
    data_fram.loc["push_pull_coordinate_begin", "alias"] = "当前推拉坐标开始"
    data_fram.loc["push_pull_coordinate_stop", "alias"] = "当前推拉坐标终点"
    data_fram.loc["tigger_head_move_coordinate", "alias"] = "整个虎牙头部移动坐标"
    data_fram.loc["tigger_head_move_coordinate_middle", "alias"] = "整个虎牙头部中间点坐标"
    data_fram.loc["tigger_outer_coordinate", "alias"] = "外虎牙开合坐标"
    data_fram.loc["tigger_outer_full_open_coordinate", "alias"] = "外虎牙完全开坐标"
    data_fram.loc["tigger_outer_full_grap_coordinate", "alias"] = "外虎牙完全抓坐标"
    data_fram.loc["tigger_inner_coordinate", "alias"] = "内虎牙开合坐标"
    data_fram.loc["tigger_inner_grap_coordinate", "alias"] = "内虎牙完全抓坐标"
    data_fram.loc["tigger_inner_relax_coordinate", "alias"] = "内虎牙完全开坐标"
    data_fram.loc["tigger_inner_drill_relax", "alias"] = "内虎牙完全松"
    data_fram.loc["current_pole_number_in_hole", "alias"] = "当前完全入坑钻杆"
    data_fram.loc["current_pole_distance_not_in_hole", "alias"] = "当前虎牙到没有入坑钻杆长度"
    data_fram.loc["messure_push_pull", "alias"] = "钻杆推拉压力"
    data_fram.loc["messure_drill", "alias"] = "钻杆旋转压力"
    data_fram.loc["messure_water", "alias"] = "钻杆内水压力"
    data_fram.loc["water_deep", "alias"] = "剩余水量"
    data_fram.loc["oil_deep", "alias"] = "剩余油量"
    data_fram.loc["beam_coordinate", "alias"] = "大梁动力头坐标"
    data_fram.loc["hand_coordinate", "alias"] = "钻箱抓手坐标"
    data_fram.loc["hand_get_pole_at_beam_coordinate", "alias"] = "抓手到达大梁可以抓钻杆坐标"
    data_fram.loc["hand_box_unstop_beam_driving_coordinate", "alias"] = "抓手到达不影响大梁前后运行坐标"
    data_fram.loc["hand_box_cloumns_1_coordinate", "alias"] = "钻箱内一栏钻杆位置坐标"
    data_fram.loc["hand_box_cloumns_3_coordinate", "alias"] = "钻箱内三栏钻杆位置坐标"
    data_fram.loc["beam_head_coordinate", "alias"] = "大梁前部最大值"
    data_fram.loc["beam_tail_coordinate", "alias"] = "大梁尾部最大值"
    data_fram.loc["box_up_coordinate", "alias"] = "钻箱上升到最高"
    data_fram.loc["box_half_up_coordinate", "alias"] = "钻箱下降到可以取钻杆位置"
    data_fram.loc["box_hand_relax_grap", "alias"] = "钻箱抓手放松"
    data_fram.loc["machine_angle_H", "alias"] = "机器水平角度"
    data_fram.loc["machine_angle_V", "alias"] = "机器垂直角度"
    data_fram.loc["pole_angle_at_machine", "alias"] = "机器侧钻杆角度"
    data_fram.loc["pole_angle_at_machine_12colock", "alias"] = "机器侧钻杆12点时读取的角度"
    data_fram.loc["pole_angle_at_remote", "alias"] = "远端钻杆角度"
    data_fram.loc["time_", "alias"] = "备份时间"
    data_fram.loc["pic_box_colum1_pole_number", "alias"] = "钻箱第一栏目钻杆数"
    data_fram.loc["pic_hand_grap_faild", "alias"] = "钻箱抓手抓取失败"
    data_fram.loc["pic_file", "alias"] = "以上图机器照片"
    data_fram.loc["action_apraise_recorder", "alias"] = "操作评分"
    data_fram.loc[:, "class_name"] = "every_order"


    print(data_fram)
    print(len(data_fram))
    data_fram.to_csv("D:\machine\机器端\machine_run_recorder2.csv", encoding="gbk")
    return data_fram
data_fram = creat_new_data()
data_split = data_fram.loc[:, "value"].str.split(".", expand=False)
def egg_s(data):
    try:
        print(data[-1])
    except Exception:
        print(None)
data_split.apply(egg_s)
print("*******************************************************************")

import pickle
with open("parameter_backup_data.tex", "rb") as parameter:
    old_data = pickle.load(parameter)

data2 = pandas.DataFrame(old_data.items(), columns=["key", "values"])
data2 = data2.set_index("key")
print(data2)
print(type(data2))
# Equepment_pole_push_pull                                           TextLabel         NaN                                             NaN
data2.loc["box_grap_hand_tight_strong", ["class_name", "file_path"]] = ["drill_box_", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["tiger_tight_time_", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["tiger_loose_time_", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["polethread_out_circle_number", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_taile_mother_thread_out_circle_numeber", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["tiger_dirll_pole_pole_tight_max_pressure", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["tiger_dirll_pole_pole_tight_max_pressure_level", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_loose_need_mini_circle_drill_level", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_loose_need_mini_circle", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_taile_mother_thread_out_pressure", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_in_middle_tiger_tooth", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_in_middle_tiger_tooth_tiggerback", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_in_middle_tiger_tooth_to_taile", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_in_middle_tiger_tooth_to_taile_tofaward", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["beam_taile_5cm", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["pole_pull_back_can_out_box_hand_to_grap", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["main_beam_last_pole_up_down_expangd_hole", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["man_give_pole_place", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["man_give_pole_place_back_last_point", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["the_new_point_man_can_let_pole_out_beam", ["class_name", "file_path"]] = ["main_beam", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["box_updown_column_up", ["class_name", "file_path"]] = ["drill_box_", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["box_updown_bottom", ["class_name", "file_path"]] = ["drill_box_", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["box_updown_column_can_grap", ["class_name", "file_path"]] = ["drill_box_", "D:\machine\机器端\machine_high_lever_equepment.py"]
data2.loc["point1", ["class_name", "file_path"]] = ["drill_box", "D:\machine\机器端\sensor.py"]
data2.loc["point2", ["class_name", "file_path"]] = ["drill_box", "D:\machine\机器端\sensor.py"]
data2.loc["point3", ["class_name", "file_path"]] = ["drill_box", "D:\machine\机器端\sensor.py"]
data2.loc["point_beam_grap", ["class_name", "file_path"]] = ["drill_box", "D:\machine\机器端\sensor.py"]
data2.loc["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate", ["class_name", "file_path"]] = ["drill_box", "D:\machine\机器端\sensor.py"]
data2.loc["point_unstop_beam_coordinate", ["class_name", "file_path"]] = ["drill_box", "D:\machine\机器端\sensor.py"]
data2.loc["_drill_box_grap_hand_tight_slight", ["class_name", "file_path"]] = ["drill_box_", "D:\machine\机器端\machine_high_lever_equepment.py"]

# print(data2)
print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
print(numpy.random.randint(-1, 11))
