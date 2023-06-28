import copy

import pandas
import numpy
import time
import os
pandas.set_option("display.width", 500)
pandas.set_option("display.max_columns", 500)
pandas.set_option("display.max_rows", 5000)
order_name = "operator_top_forward_manual"
path_ = r"D:\machine\机器端\nnnnnn.csv"
__all__ = ["add_data_", "apply_veclocity_data_interface", "apply_acceleration_face", "creat_apply_v_apply_a", "machinRunData_V_A_Apply"]
class machinRunData_V_A_Apply:
    columns_ = ['order_name', 'order_parameter', 'current_push_pull_gear',
                'current_push_pull_gear_coordinate', 'current_drill_gear',
                'current_drill_gear_coordinate', 'push_pull_coordinate_begin',
                'push_pull_coordinate_stop', 'tigger_head_move_coordinate',
                'tigger_head_move_coordinate_middle', 'tigger_coordinate_outer',
                'tigger_outer_full_open_coordinate',
                'tigger_outer_full_grap_coordinate', 'tigger_inner_coordinate',
                'tigger_inner_grap_coordinate', 'tigger_inner_relax_coordinate',
                'tigger_inner_drill_relax', 'current_pole_number_in_hole',
                'current_pole_distance_not_in_hole', 'messure_push_pull',
                'messure_drill', 'messure_water', 'water_deep', 'oil_deep',
                'beam_coordinate', 'hand_coordinate',
                'hand_get_pole_at_beam_coordinate',
                'hand_box_unstop_beam_driving_coordinate',
                'hand_box_cloumns_1_coordinate', 'hand_box_cloumns_3_coordinate',
                'beam_head_coordinate', 'beam_tail_coordinate', 'box_up_coordinate',
                'box_half_up_coordinate', 'box_hand_relax_grap', 'machine_angle_H',
                'machine_angle_V', 'pole_angle_at_machine',
                'pole_angle_at_machine_12colock', 'pole_angle_at_remote', 'time_',
                'pic_box_colum1_pole_number', 'pic_hand_grap_faild', 'pic_file',
                'action_apraise_recorder', 'tigger_outer_coordinate', 'class_name',
                'veclocity', 'acceleration']
    def __init__(self, order_name=order_name, path_=path_, number=14000, write_=False ):
        self.order_name = order_name
        self.path_ = path_
        self.number = number
        self.write_ = write_

    def add_data_(self, current_push_pull_gearar=1, current_drill_gear=0):
        columns_ = self.columns_
        add_data_.columns = columns_
        if os.path.exists(self.path_):
            data_fram = pandas.read_csv(self.path_, encoding="gbk")
            columns_ = data_fram.columns
        else:
            columns_ = columns_

        all_timie = 280
        time__ = 0
        delta_tim = 0.02
        resample_number = all_timie / delta_tim

        start = 0
        end = 4600
        beam_distance = end - start
        delta_distance = beam_distance / resample_number

        pull_gear_all_distance = 100  # mm
        all_time_gear = 1
        delta_ = all_time_gear / pull_gear_all_distance
        tigger_head_move_coordinate = (8, 12)
        tigger_head_move_coordinate_middle = 10

        tigger_outer_full_open_coordinate = (0, 35)
        tigger_outer_full_grap_coordinate = (80, 120)

        hand_not_stop_beam = 650
        hand_box_innercolum1 = 450
        box_hand_coodinate = (hand_box_innercolum1, hand_not_stop_beam)
        hand_get_pole_at_beam_coordinate = 950
        hand_get_pole_at_beam_coordinate = (
        hand_get_pole_at_beam_coordinate - 10, hand_get_pole_at_beam_coordinate + 10)
        point1_coordinate = 40
        point2_coordinate = 28
        point3_coordinate = 15

        beam_begin = 0
        beam_end = 4800
        box_up_coordinate = 20
        box_half_up_coordinate = 40
        n = 0
        randint = numpy.random.randint
        choice = numpy.random.choice
        order_name = self.order_name
        data_fram_ = pandas.DataFrame([], columns=columns_)
        data_fram_add = pandas.Series([])

        while True:
            data_fram_add.loc["order_name"] = order_name
            data_fram_add.loc["order_parameter"] = None
            data_fram_add.loc["current_push_pull_gear"] = current_push_pull_gearar
            data_fram_add.loc["current_push_pull_gear_coordinate"] = 11  # 20
            data_fram_add.loc["current_drill_gear"] = current_drill_gear
            data_fram_add.loc["current_drill_gear_coordinate"] = "当前旋转坐标"
            data_fram_add.loc["push_pull_coordinate_begin"] = "当前推拉坐标开始"
            data_fram_add.loc["push_pull_coordinate_stop"] = "当前推拉坐标终点"
            data_fram_add.loc["tigger_head_move_coordinate"] = randint(*tigger_head_move_coordinate)
            data_fram_add.loc["tigger_head_move_coordinate_middle"] = tigger_head_move_coordinate_middle
            data_fram_add.loc["tigger_outer_coordinate"] = randint(*tigger_outer_full_open_coordinate)
            data_fram_add.loc["tigger_outer_full_open_coordinate"] = randint(
                *tigger_outer_full_open_coordinate)
            data_fram_add.loc["tigger_outer_full_grap_coordinate"] = randint(
                *tigger_outer_full_grap_coordinate)
            data_fram_add.loc["tigger_inner_coordinate"] = randint(*tigger_outer_full_open_coordinate)
            data_fram_add.loc["tigger_inner_grap_coordinate"] = randint(
                *tigger_outer_full_grap_coordinate)
            data_fram_add.loc["tigger_inner_relax_coordinate"] = randint(
                *tigger_outer_full_open_coordinate)
            data_fram_add.loc["tigger_inner_drill_relax"] = 0  # -30  30   0 is 水平
            data_fram_add.loc["current_pole_number_in_hole"] = 0
            data_fram_add.loc["current_pole_distance_not_in_hole"] = 2500
            data_fram_add.loc["messure_push_pull"] = randint(1)
            data_fram_add.loc["messure_drill"] = randint(1)
            data_fram_add.loc["messure_water"] = numpy.random.rand(1)[0]
            data_fram_add.loc["water_deep"] = randint(20, 100)
            data_fram_add.loc["oil_deep"] = randint(20, 100)
            start = start + delta_distance
            data_fram_add.loc["beam_coordinate"] = start
            data_fram_add.loc["hand_coordinate"] = randint(*box_hand_coodinate)
            data_fram_add.loc["hand_get_pole_at_beam_coordinate"] = randint(
                *hand_get_pole_at_beam_coordinate)
            data_fram_add.loc["hand_box_unstop_beam_driving_coordinate"] = randint(*box_hand_coodinate)
            data_fram_add.loc["hand_box_cloumns_1_coordinate"] = point1_coordinate
            data_fram_add.loc["hand_box_cloumns_2_coordinate"] = point2_coordinate
            data_fram_add.loc["hand_box_cloumns_3_coordinate"] = point3_coordinate
            data_fram_add.loc["beam_head_coordinate"] = beam_end
            data_fram_add.loc["beam_tail_coordinate"] = beam_begin
            data_fram_add.loc["box_up_coordinate"] = box_up_coordinate
            data_fram_add.loc["box_half_up_coordinate"] = box_half_up_coordinate
            data_fram_add.loc["box_hand_relax_grap"] = choice((True, False, None))
            data_fram_add.loc["machine_angle_H"] = 0
            data_fram_add.loc["machine_angle_V"] = randint(-3, 24)
            data_fram_add.loc["pole_angle_at_machine"] = randint(360)
            data_fram_add.loc["pole_angle_at_machine_12colock"] = randint(360)
            data_fram_add.loc["pole_angle_at_remote"] = randint(360)
            time__ += delta_tim
            data_fram_add.loc["time_"] = time__
            print(time__)
            data_fram_add.loc["pic_box_colum1_pole_number"] = randint(0, 11)
            data_fram_add.loc["pic_hand_grap_faild"] = None
            data_fram_add.loc["pic_file"] = None

            if point1_coordinate < data_fram_add.loc["hand_coordinate"] < hand_not_stop_beam:
                data_fram_add.loc["action_apraise_recorder"] = 65
            else:
                data_fram_add.loc["action_apraise_recorder"] = 0

            data_fram_ = data_fram_.append(data_fram_add, ignore_index=True)
            if n == self.number:
                break
            n = n + 1
            data_fram_add.loc["class_name"] = "every_order"

        if self.write_ is False:
            return data_fram_
        else:
            data_fram_.to_csv(self.path_, index=False, encoding="gbk")
            return data_fram_

    def __apply_veclocity_data__(self, data_frame):
        if hasattr(self, "last_data"):
            last_data = self.last_data
            delta_time = data_frame.loc["time_"] - last_data.loc["time_"]
            delta_distance_ = data_frame.loc["beam_coordinate"] - last_data.loc["beam_coordinate"]
            delta_hand_distance_ = data_frame.loc["hand_coordinate"] - last_data.loc["hand_coordinate"]
            v_ = delta_distance_/delta_time
            v_hand = delta_hand_distance_/delta_time
            self.last_data = copy.deepcopy(data_frame)
            return v_, v_hand
        else:
            self.last_data = copy.deepcopy(data_frame)
            return 0, 0

    def apply_veclocity_data_interface(self, write_=False):
        """
        this function apply the target data , and add the new data
        """
        data_frame3 = pandas.read_csv(self.path_, encoding="gbk")
        dd = data_frame3.apply(self.__apply_veclocity_data__, axis=1, result_type="expand")
        if hasattr(self, "last_data"):
            delattr(self, "last_data")
        data_frame3.loc[:, "velocity"] = dd.loc[:, 0]
        data_frame3.loc[:, "hand_velocity"] = dd.loc[:, 1]
        if write_:
            data_frame3.to_csv(self.path_, index=False, encoding="gbk")
            return data_frame3
        else:
            return data_frame3


    def __apply_acceleration__(self, data_v):
        if not hasattr(self, "last_v_data"):
            self.last_v_data = copy.deepcopy(data_v)
            a = 0
            a_hand = 0
        else:
            last_v_data = self.last_v_data
            delta_time = data_v.loc["time_"] - last_v_data.loc["time_"]
            a = (data_v.loc["velocity"] - last_v_data.loc["velocity"])/delta_time
            a_hand = (data_v.loc["hand_velocity"] - last_v_data.loc["hand_velocity"])/delta_time
            if a < 0.0001:
                a = 0
            if a_hand < 0.0001:
                a_hand = 0
            self.last_v_data = copy.deepcopy(data_v)
        return a, a_hand

    def apply_acceleration_face(self, write_=False):
        data_frame3 = pandas.read_csv(self.path_, encoding="gbk")
        ff = data_frame3.apply(self.__apply_acceleration__, axis=1, result_type="expand")
        data_frame3.loc[:, "beam_acceleration"] = ff.loc[:, 0]
        data_frame3.loc[:, "hand_acceleration"] = ff.loc[:, 1]
        if write_:
            data_frame3.to_csv(self.path_, encoding="gbk", index=False)
        return data_frame3

    def creat_apply_v_apply_a(self, number=14000):
        time__ = time.time()
        self.add_data_()
        self.apply_acceleration_face(write_=True)
        data = self.apply_acceleration_face(write_=True)
        delta_time = time.time() - time__
        return data, delta_time

columns_ = ['order_name', 'order_parameter', 'current_push_pull_gear',
       'current_push_pull_gear_coordinate', 'current_drill_gear',
       'current_drill_gear_coordinate', 'push_pull_coordinate_begin',
       'push_pull_coordinate_stop', 'tigger_head_move_coordinate',
       'tigger_head_move_coordinate_middle', 'tigger_coordinate_outer',
       'tigger_outer_full_open_coordinate',
       'tigger_outer_full_grap_coordinate', 'tigger_inner_coordinate',
       'tigger_inner_grap_coordinate', 'tigger_inner_relax_coordinate',
       'tigger_inner_drill_relax', 'current_pole_number_in_hole',
       'current_pole_distance_not_in_hole', 'messure_push_pull',
       'messure_drill', 'messure_water', 'water_deep', 'oil_deep',
       'beam_coordinate', 'hand_coordinate',
       'hand_get_pole_at_beam_coordinate',
       'hand_box_unstop_beam_driving_coordinate',
       'hand_box_cloumns_1_coordinate', 'hand_box_cloumns_3_coordinate',
       'beam_head_coordinate', 'beam_tail_coordinate', 'box_up_coordinate',
       'box_half_up_coordinate', 'box_hand_relax_grap', 'machine_angle_H',
       'machine_angle_V', 'pole_angle_at_machine',
       'pole_angle_at_machine_12colock', 'pole_angle_at_remote', 'time_',
       'pic_box_colum1_pole_number', 'pic_hand_grap_faild', 'pic_file',
       'action_apraise_recorder', 'tigger_outer_coordinate', 'class_name',
       'veclocity', 'acceleration']




def add_data_(order_name=None, number=14000, write_=False, file_path_=path_):
    global columns_
    add_data_.columns = columns_
    # push pull 1gear data
    if os.path.exists("path_"):
        data_fram = pandas.read_csv("D:\machine\机器端\machine_run_recorder2.csv", encoding="gbk")
        data_fram = data_fram.rename({"value": "orange"}, axis=1)
        data_fram.set_index("key", inplace=True)
        columns_ = data_fram.index
    else:
        columns_ = columns_

    all_timie = 280
    time__ = 0
    delta_tim = 0.02
    resample_number = all_timie/delta_tim

    start = 0
    end = 4600
    beam_distance = end - start
    delta_distance = beam_distance/resample_number


    pull_gear_all_distance = 100 #mm
    all_time_gear = 1
    delta_ = all_time_gear/pull_gear_all_distance
    tigger_head_move_coordinate = (8, 12)
    tigger_head_move_coordinate_middle = 10

    tigger_outer_full_open_coordinate = (0, 35)
    tigger_outer_full_grap_coordinate = (80, 120)

    hand_not_stop_beam = 650
    hand_box_innercolum1 = 450
    box_hand_coodinate = (hand_box_innercolum1, hand_not_stop_beam)
    hand_get_pole_at_beam_coordinate = 950
    hand_get_pole_at_beam_coordinate = (hand_get_pole_at_beam_coordinate-10, hand_get_pole_at_beam_coordinate+10)
    point1_coordinate = 40
    point2_coordinate = 28
    point3_coordinate = 15

    beam_begin = 0
    beam_end = 4800
    box_up_coordinate = 20
    box_half_up_coordinate = 40
    n = 0

    data_fram_ = pandas.DataFrame([], columns=columns_)
    data_fram_add = pandas.Series([])

    while True:
        data_fram_add.loc["order_name"] = "operator_top_forward_manual"
        data_fram_add.loc["order_parameter"] = None
        data_fram_add.loc["current_push_pull_gear"] = 1
        data_fram_add.loc["current_push_pull_gear_coordinate"] = 11   #20
        data_fram_add.loc["current_drill_gear"] = 0
        data_fram_add.loc["current_drill_gear_coordinate"] = "当前旋转坐标"
        data_fram_add.loc["push_pull_coordinate_begin"] = "当前推拉坐标开始"
        data_fram_add.loc["push_pull_coordinate_stop"] = "当前推拉坐标终点"
        data_fram_add.loc["tigger_head_move_coordinate"] = numpy.random.randint(*tigger_head_move_coordinate)
        data_fram_add.loc["tigger_head_move_coordinate_middle"] = tigger_head_move_coordinate_middle
        data_fram_add.loc["tigger_outer_coordinate"] = numpy.random.randint(*tigger_outer_full_open_coordinate)
        data_fram_add.loc["tigger_outer_full_open_coordinate"] = numpy.random.randint(*tigger_outer_full_open_coordinate)
        data_fram_add.loc["tigger_outer_full_grap_coordinate"] = numpy.random.randint(*tigger_outer_full_grap_coordinate)
        data_fram_add.loc["tigger_inner_coordinate"] = numpy.random.randint(*tigger_outer_full_open_coordinate)
        data_fram_add.loc["tigger_inner_grap_coordinate"] = numpy.random.randint(*tigger_outer_full_grap_coordinate)
        data_fram_add.loc["tigger_inner_relax_coordinate"] = numpy.random.randint(*tigger_outer_full_open_coordinate)
        data_fram_add.loc["tigger_inner_drill_relax"] = 0  # -30  30   0 is 水平
        data_fram_add.loc["current_pole_number_in_hole"] = 0
        data_fram_add.loc["current_pole_distance_not_in_hole"] = 2500
        data_fram_add.loc["messure_push_pull"] = numpy.random.randint(1)
        data_fram_add.loc["messure_drill"] = numpy.random.randint(1)
        data_fram_add.loc["messure_water"] = numpy.random.rand(1)[0]
        data_fram_add.loc["water_deep"] = numpy.random.randint(20, 100)
        data_fram_add.loc["oil_deep"] = numpy.random.randint(20, 100)
        start = start + delta_distance
        data_fram_add.loc["beam_coordinate"] = start
        data_fram_add.loc["hand_coordinate"] = numpy.random.randint(*box_hand_coodinate)
        data_fram_add.loc["hand_get_pole_at_beam_coordinate"] = numpy.random.randint(*hand_get_pole_at_beam_coordinate)
        data_fram_add.loc["hand_box_unstop_beam_driving_coordinate"] = numpy.random.randint(*box_hand_coodinate)
        data_fram_add.loc["hand_box_cloumns_1_coordinate"] = point1_coordinate
        data_fram_add.loc["hand_box_cloumns_3_coordinate"] = point3_coordinate
        data_fram_add.loc["beam_head_coordinate"] = beam_end
        data_fram_add.loc["beam_tail_coordinate"] = beam_begin
        data_fram_add.loc["box_up_coordinate"] = box_up_coordinate
        data_fram_add.loc["box_half_up_coordinate"] = box_half_up_coordinate
        data_fram_add.loc["box_hand_relax_grap"] = numpy.random.choice((True, False, None))
        data_fram_add.loc["machine_angle_H"] = 0
        data_fram_add.loc["machine_angle_V"] = numpy.random.randint(-3, 24)
        data_fram_add.loc["pole_angle_at_machine"] = numpy.random.randint(360)
        data_fram_add.loc["pole_angle_at_machine_12colock"] = numpy.random.randint(360)
        data_fram_add.loc["pole_angle_at_remote"] = numpy.random.randint(360)
        time__ += delta_tim
        data_fram_add.loc["time_"] = time__
        print(time__)
        data_fram_add.loc["pic_box_colum1_pole_number"] = numpy.random.randint(0, 11)
        data_fram_add.loc["pic_hand_grap_faild"] = None
        data_fram_add.loc["pic_file"] = None

        if point1_coordinate < data_fram_add.loc["hand_coordinate"] < hand_not_stop_beam:
            data_fram_add.loc["action_apraise_recorder"] = 65
        else:
            data_fram_add.loc["action_apraise_recorder"] = 0

        data_fram_ = data_fram_.append(data_fram_add, ignore_index=True)
        if n == number:
            break
        n = n + 1
        data_fram_add.loc["class_name"] = "every_order"

    if write_ is False:
        return data_fram_
    else:
        data_fram_.to_csv(r"D:\machine\机器端\nnnnnn.csv", index=False, encoding="gbk")
        return data_fram_

def apply_veclocity_data(data_frame, n=5):
    if hasattr(apply_veclocity_data, "last_data"):
        last_data = apply_veclocity_data.last_data
        delta_time = data_frame.loc["time_"] - last_data.loc["time_"]
        delta_distance_ = data_frame.loc["beam_coordinate"] - last_data.loc["beam_coordinate"]
        delta_hand_distance_ = data_frame.loc["hand_coordinate"] - last_data.loc["hand_coordinate"]
        print("***********************1")
        print(delta_time)
        print("***********************2")
        v_ = delta_distance_/delta_time
        v_hand = delta_hand_distance_/delta_time
        apply_veclocity_data.last_data = copy.deepcopy(data_frame)
        return v_, v_hand
    else:
        apply_veclocity_data.last_data = copy.deepcopy(data_frame)
        print(data_frame.loc["time_"])
        return 0, 0

def apply_veclocity_data_interface(write_ = False):
    """
    this function apply the target data , and add the new data
    """
    data_frame3 = pandas.read_csv(r"D:\machine\机器端\nnnnnn.csv", encoding="gbk")
    if "velocity" not in data_frame3.columns.values:
        dd = data_frame3.apply(apply_veclocity_data, args=(8,), axis=1, result_type="expand")
        dd.rename({0: "velocity", 1: "hand_velocity"}, inplace=True, axis=1)
        pandas.concat([data_frame3, dd], axis=1)
        if write_:
            data_frame3.to_csv(r"D:\machine\机器端\nnnnnn.csv", index=False, encoding="gbk")
            return data_frame3
        else:
            return data_frame3
    return data_frame3

def apply_acceleration(data_v):
    if not hasattr(apply_acceleration, "last_v_data"):
        apply_acceleration.last_v_data = copy.deepcopy(data_v)
        a = 0
    else:
        last_v_data = apply_acceleration.last_v_data
        delta_time = data_v.loc["time_"] - last_v_data.loc["time_"]
        a = (data_v.loc["veclocity"] - last_v_data.loc["veclocity"])/delta_time
        a_hand = (data_v.loc["hand_velocity"] - last_v_data.loc["hand_velocity"])/delta_time
        if a < 0.0001:
            a = 0
        if a_hand < 0.0001:
            a_hand = 0
        apply_acceleration.last_v_data = copy.deepcopy(data_v)
    return a, a_hand

def apply_acceleration_face(write_=False):
    data_frame3 = pandas.read_csv(r"D:\machine\机器端\nnnnnn.csv", encoding="gbk")
    if "acceleration" in data_frame3.columns.values:
        return data_frame3
    else:
        ff = data_frame3.apply(apply_acceleration, axis=1)
        data_frame3 = pandas.concat([data_frame3, ff])
        # data_frame3.loc[:, "acceleration"] = ff
        if write_:
            data_frame3.to_csv(r"D:\machine\机器端\nnnnnn.csv", encoding="gbk", index=False)
        return data_frame3

def creat_apply_v_apply_a(number=14000):
    time__ = time.time()
    add_data_(number=number, write_=True)
    apply_acceleration_face(write_=True)
    data = apply_acceleration_face(write_=True)
    delta_time = time.time() - time__
    return data, delta_time



mm = machinRunData_V_A_Apply(write_=True)
dd = mm.apply_acceleration_face(write_=True)
print(dd)
print(dd.columns)