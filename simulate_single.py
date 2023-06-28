import numpy
import pandas
import time
import copy
import os
import asyncio
import seting
pandas.set_option("display.width", 500)
pandas.set_option("display.max_columns", 500)
pandas.set_option("display.max_rows", 5000)
order_name = "operator_top_forward_manual"
path_ = r"D:\machine\机器端\nnnnnn.csv"
__all__ = [ "machinRunData_V_A_Apply"]

class machinRunData_V_A_Apply:
    columns_ = ['action_apraise_recorder', 'beam_coordinate',
      'beam_head_coordinate', 'beam_tail_coordinate',
      'box_half_up_coordinate', 'box_hand_relax_grap',
      'box_up_coordinate', 'class_name',
      'current_drill_gear', 'current_drill_gear_coordinate',
      'current_pole_distance_not_in_hole', 'current_pole_number_in_hole',
      'current_push_pull_gear', 'current_push_pull_gear_coordinate',
      'hand_box_cloumns_1_coordinate', 'hand_box_cloumns_3_coordinate',
      'hand_box_unstop_beam_driving_coordinate', 'hand_coordinate',
       'hand_get_pole_at_beam_coordinate', 'hand_velocity', 'machine_angle_H',
      'machine_angle_V', 'messure_drill', 'messure_push_pull', 'messure_water',
      'oil_deep', 'order_name', 'order_parameter', 'pic_box_colum1_pole_number', 'pic_file',
      'pic_hand_grap_faild', 'pole_angle_at_machine', 'pole_angle_at_machine_12colock',
      'pole_angle_at_remote', 'push_pull_coordinate_begin', 'push_pull_coordinate_stop',
      'tigger_coordinate_outer', 'tigger_head_move_coordinate',
       'tigger_head_move_coordinate_middle', 'tigger_inner_coordinate', 'tigger_inner_drill_relax',
      'tigger_inner_grap_coordinate', 'tigger_inner_relax_coordinate', 'tigger_outer_coordinate',
      'tigger_outer_full_grap_coordinate', 'tigger_outer_full_open_coordinate', 'time_', 'velocity',
      'water_deep', 'beam_acceleration', 'hand_acceleration', 'hand_box_cloumns_2_coordinate']

    def __init__(self, order_name=order_name, path_=path_, number=14000, write_=False ):
        self.order_name = order_name
        self.path_ = path_
        self.number = number
        self.write_ = write_
        self.old_parameter_load_data = seting.parameter_load_data
        self.MAX_PUSH_PRESSURE = self.old_parameter_load_data["MAX_PUSH_PRESSURE"]
        self.MAX_PUSH_QUICK_PRESSURE = self.old_parameter_load_data["MAX_PUSH_QUICK_PRESSURE"]
        self.MAX_PUSH_SLOW_PRESSURE = self.old_parameter_load_data["MAX_PUSH_SLOW_PRESSURE"]
        self.MAX_DRILL_QUICK_PRESSURE = self.old_parameter_load_data["MAX_DRILL_QUICK_PRESSURE"]
        self.MAX_DRILL_SLOW_PRESSURE = self.old_parameter_load_data["MAX_DRILL_SLOW_PRESSURE"]
        self.MINI_ANGLE_SPEED = self.old_parameter_load_data["MINI_ANGLE_SPEED"]

        # self.interface_operator_obj = interface_operator_obj

        self.MAX_PUSH_QUICK_PRESSURE = self.old_parameter_load_data["MAX_PUSH_QUICK_PRESSURE"]
        self.MAX_PUSH_SLOW_PRESSURE = self.old_parameter_load_data["MAX_PUSH_SLOW_PRESSURE"]
        self.MAX_PULL_PRESSURE = self.old_parameter_load_data["MAX_PULL_PRESSURE"]
        self.MAX_PULL_QUICK_PRESSURE = self.old_parameter_load_data["MAX_PULL_QUICK_PRESSURE"]
        self.MINI_ANGLE_SPEED = self.old_parameter_load_data["MINI_ANGLE_SPEED"]

    def parse_pull_push_level(self):
        PUSH_LEVEL = []
        old_parameter_load_data = self.old_parameter_load_data
        new_obj_name = self
        stop_coordinate = old_parameter_load_data["Equepment_pole_push_pull_coordinate"][1]
        start_coordinate = old_parameter_load_data["Equepment_pole_push_pull_coordinate"][0]
        end_coordinate = old_parameter_load_data["Equepment_pole_push_pull_coordinate"][2]
        self.stop_gera_delta_coordinate = old_parameter_load_data["Equepment_pole_push_pull_coordinate"][3]

        every_step = (stop_coordinate - start_coordinate) / 6

        PUSH_LEVEL[6] = start_coordinate
        PUSH_LEVEL[5] = every_step + start_coordinate
        PUSH_LEVEL[4] = every_step * 2 + start_coordinate
        PUSH_LEVEL[3] = every_step * 3 + start_coordinate
        PUSH_LEVEL[2] = every_step * 4 + start_coordinate
        PUSH_LEVEL[1] = every_step * 5 + start_coordinate
        PUSH_LEVEL[0] = every_step * 6 + start_coordinate
        PULL_LEVEL = []
        every_step_pull = (end_coordinate - stop_coordinate) / 6
        PULL_LEVEL[1] = every_step_pull + stop_coordinate
        PULL_LEVEL[2] = every_step_pull * 2 + stop_coordinate
        PULL_LEVEL[3] = every_step_pull * 3 + stop_coordinate
        PULL_LEVEL[4] = every_step_pull * 4 + stop_coordinate
        PULL_LEVEL[5] = every_step_pull * 5 + stop_coordinate
        PULL_LEVEL[6] = every_step_pull * 6 + stop_coordinate

        self.gear_list = [
            PUSH_LEVEL[6],
            PUSH_LEVEL[5],
            PUSH_LEVEL[4],
            PUSH_LEVEL[3],
            PUSH_LEVEL[2],
            PUSH_LEVEL[1],
            PUSH_LEVEL[0],
            PULL_LEVEL[1],
            PULL_LEVEL[2],
            PULL_LEVEL[3],
            PULL_LEVEL[4],
            PULL_LEVEL[5],
            PULL_LEVEL[6],
        ]


    def coordinateToGear(self, coordinate):
        if hasattr(self, "gear_list"):
            pass
        else:
            self.parse_pull_push_level()
        new_list = [*map(lambda x: abs(x - coordinate), self.gear_list)]
        gear_number = new_list.index(min(new_list))
        if gear_number == 0:
            delta_ds = coordinate - self.gear_list[6]
            if abs(delta_ds) > self.stop_gera_delta_coordinate:
                if delta_ds > 0:
                    gear_number = 5
                else:
                    gear_number = 7
            else:
                gear_number = 6
        # data range is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12], 6 is the stop gear
        return gear_number

    def add_data_(self, current_push_pull_gearar=1, current_drill_gear=0):
        self.__init__data = False
        if os.path.exists(self.path_):
            data_fram = pandas.read_csv(self.path_, encoding="gbk")
            columns_ = data_fram.columns
        else:
            columns_ = self.columns_
        try:
            pieces = data_fram.loc[:, "pieces"].max() + 1
        except Exception:
            pieces = 0
        all_timie = 48        #order will used time
        time__ = 0
        delta_tim = 0.02
        resample_number = all_timie / delta_tim
        old_parameter_load_data = self.old_parameter_load_data
        # start = self.interface_operator_obj.main_beam.beam_begin
        # end = self.interface_operator_obj.main_beam.beam_end
        start = old_parameter_load_data["beam_head_coordinate"]
        end = old_parameter_load_data["beam_tail_coordinate"]


        beam_distance = end - start
        delta_distance = beam_distance / resample_number
        pull_gear_begin_coordinate = old_parameter_load_data[('Equepment_pole_push_pull', 'start')][0]
        pull_gear_end_coordinate = old_parameter_load_data[('Equepment_pole_push_pull', 'end')][2]
        pull_gear_all_distance = abs(pull_gear_begin_coordinate - pull_gear_end_coordinate)
        all_time_gear = 6       #gear data is [0, 1, 2, 3 ,4, 5, 6, 7, 8, 9, 10, 11, 12]   stop gear is 6
        delta_ = all_time_gear / pull_gear_all_distance

        tiger_backward_move_max_coordinate = old_parameter_load_data["tiger_backward_move_max_coordinate"]
        tiger_forward_move_max_coordinate = old_parameter_load_data["tiger_forward_move_max_coordinate"]
        if tiger_forward_move_max_coordinate < tiger_backward_move_max_coordinate:
            tigger_head_move_coordinate = (tiger_forward_move_max_coordinate , tiger_backward_move_max_coordinate)
        else:
            tigger_head_move_coordinate = (tiger_backward_move_max_coordinate, tiger_forward_move_max_coordinate)

        tigger_head_move_coordinate_middle = old_parameter_load_data["tiger_self_middle_zero_coordinate_"]

        tiger_inner_rule_relax = old_parameter_load_data["tiger_inner_rule_relax"]
        tiger_inner_rule_grap = old_parameter_load_data["tiger_inner_rule_grap"]

        tigger_outer_full_open_coordinate = old_parameter_load_data["tiger_outer_rule_relax"]
        tigger_outer_full_grap_coordinate = old_parameter_load_data["tiger_outer_rule_grap"]
        # hand_not_stop_beam = self.interface_operator_obj.drill_box.point_unstop_beam_coordinate
        # point1_coordinate = self.interface_operator_obj.drill_box.point1_coordinate
        # point2_coordinate = self.interface_operator_obj.drill_box.point2_coordinate
        # point3_coordinate = self.interface_operator_obj.drill_box.point3_coordinate
        # hand_not_stop_beam = self.interface_operator_obj.drill_box.point_unstop_beam_coordinate
        hand_not_stop_beam = old_parameter_load_data["point_unstop_beam_coordinate"]
        point1_coordinate = old_parameter_load_data["point1_coordinate"]
        point2_coordinate = old_parameter_load_data["point2_coordinate"]
        point3_coordinate = old_parameter_load_data["point3_coordinate"]


        box_hand_coodinate = (point1_coordinate, hand_not_stop_beam)
        # hand_get_pole_at_beam_coordinate1 = self.interface_operator_obj.drill_box.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate
        hand_get_pole_at_beam_coordinate1 = old_parameter_load_data["point_beam_grap_coordinate"]
        hand_get_pole_at_beam_coordinate = (hand_get_pole_at_beam_coordinate1 - 10, hand_get_pole_at_beam_coordinate1 + 10)



        # beam_begin = self.interface_operator_obj.main_beam.beam_begin
        # beam_end = self.interface_operator_obj.main_beam.beam_end
        # box_up_coordinate = self.interface_operator_obj.drill_box.box_updown_column_up
        # box_half_up_coordinate = self.interface_operator_obj.drill_box.box_updown_column_can_grap
        beam_begin = self.old_parameter_load_data["beam_head_coordinate"]
        beam_end = self.old_parameter_load_data["beam_tail_coordinate"]
        box_up_coordinate = self.old_parameter_load_data["box_updown_column_up"]
        box_half_up_coordinate = self.old_parameter_load_data["box_updown_column_can_grap"]
        box_updown_bottom = self.old_parameter_load_data["box_updown_bottom"]

        n = 0
        randint = numpy.random.randint
        choice = numpy.random.choice
        order_name = self.order_name
        data_fram_ = pandas.DataFrame([], columns=columns_)
        data_fram_add = pandas.Series([])
        self.add_last_data = None
        while True:
            if self.__init__data is False:
                self.__init__data = True
                data_fram_add.loc["order_name"] = order_name
                data_fram_add.loc["pieces"] = pieces
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
                # data_fram_add.loc["current_pole_number_in_hole"] = self.interface_operator_obj.main_beam.current_pole_number_in_hole
                # data_fram_add.loc["current_pole_distance_not_in_hole"] = self.interface_operator_obj.main_beam.current_pole_distance_not_in_hole
                data_fram_add.loc["current_pole_number_in_hole"] = 0
                data_fram_add.loc["current_pole_distance_not_in_hole"] = 2800
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
                self.add_last_data = copy.deepcopy(data_fram_add)

            else:
                data_fram_add.loc["order_name"] = order_name
                data_fram_add.loc["pieces"] = pieces
                data_fram_add.loc["order_parameter"] = None
                # data_fram_add.loc["current_push_pull_gear"] = self.interface_operator_obj.main_beam.Equepment_pole_push_pull.get_current_gear
                # data_fram_add.loc["current_push_pull_gear_coordinate"] = self.interface_operator_obj.main_beam.Equepment_pole_push_pull.coordinate
                data_fram_add.loc["current_push_pull_gear"] = self.__current_push_pull_gear__()
                data_fram_add.loc["current_push_pull_gear_coordinate"] = self.__current_push_pull_gear_coordinate__()
                data_fram_add.loc["push_pull_coordinate_begin"] = 0
                data_fram_add.loc["push_pull_coordinate_stop"] = 50
                data_fram_add.loc["push_pull_coordinate_end"] = 100

                data_fram_add.loc["current_drill_gear"] = current_drill_gear
                data_fram_add.loc["current_drill_gear_coordinate"] = "当前旋转坐标"
                data_fram_add.loc["drill_coordinate_begin"] = 0
                data_fram_add.loc["drill_coordinate_stop"] = 50
                data_fram_add.loc["drill_coordinate_end"] = 100

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
                data_fram_add.loc[
                    "current_pole_number_in_hole"] = self.interface_operator_obj.main_beam.current_pole_number_in_hole
                data_fram_add.loc[
                    "current_pole_distance_not_in_hole"] = self.interface_operator_obj.main_beam.current_pole_distance_not_in_hole
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



    def __simulage_manul_forward__(self, last_data, gear_order):
        level_data = pandas.read_csv("D:\machine\机器端\operate_arm_gear_pressure_velocity_map_table.csv")
        level_data.set_index(["gear", "pressure"])
        current_data = pandas.DataFrame([])
        hand_not_stop_beam = 64
        point1_coordinate = 70

        box_hand_coodinate = (point1_coordinate, hand_not_stop_beam)
        if last_data is None:
            ast_messure_drill = 0
            last_messure_push_pull = 0
            last_drill_gear = 6
            current_push_pull_gear = 0
            push_pull_coordinate_begin = 0
            push_pull_coordinate_stop = 50
            push_pull_coordinate_end = 100
            last_current_push_pull_gear_coordinate = 50
            current_drill_gear_coordinate = 50
            beam_coordinate = numpy.random.randint(100, 3000)
            last_beam_delta_distance_ = 0
            last_pole_angle_at_machine = numpy.random.randint(0, 360)
            delta_pole_angle_at_machine = 0.3
            hand_box_unstop_beam_driving_coordinate = numpy.random.randint(*box_hand_coodinate)
        else:
            last_messure_drill = last_data.loc["messure_drill"] = 0
            last_messure_push_pull = last_data.loc["messure_push_pull"]
            last_drill_gear = last_data.loc["current_drill_gear"]
            last_gear_ = last_data.loc["current_drill_gear"]
            current_push_pull_gear = last_data.loc["current_push_pull_gear"]
            push_pull_coordinate_begin = last_data.loc["push_pull_coordinate_begin"]
            push_pull_coordinate_stop = last_data.loc["push_pull_coordinate_stop"]
            push_pull_coordinate_end = last_data.loc["push_pull_coordinate_end"]
            last_current_push_pull_gear_coordinate = last_data.loc["current_push_pull_gear_coordinate"]
            current_drill_gear_coordinate = last_data.loc["current_drill_gear_coordinate"]
            beam_coordinate = last_data.loc["beam_coordinate"]
            last_beam_delta_distance_ = last_data.loc["delta_distance_"]
            last_pole_angle_at_machine = last_data.loc["pole_angle_at_machine"]
            delta_pole_angle_at_machine = last_data.loc["delta_pole_angle_at_machine"]
            hand_box_unstop_beam_driving_coordinate = last_data.loc["hand_box_unstop_beam_driving_coordinate"]

        will_delta = gear_order - last_drill_gear
        will_pressure = 1 + numpy.random.randn()/30
        delta_angle = 1

        delta_beam_coordinate = self.old_parameter_load_data["Equepment_line_distance_measure_4m_beam_coordinate_delta"]

        delta_drill_box_hand_run_coordinate = self.old_parameter_load_data["delta_drill_box_hand_run_coordinate"]
        current_messure_drill = 30
        current_messure_pushpull = 40
        delta_messure_push_pull = 40
        delta_pole_angle_at_machine = 40

        box_half_up_coordinate = 0

        delta_time = self.__get_delta_time__()

        current_data.loc["delta_time"] = delta_time
        current_data.loc["current_push_pull_gear"] = self.coordinateToGear(delta_beam_coordinate)
        current_data.loc["velocity"] = level_data.loc[(1, 2), "velocity"]
        current_data.loc["current_push_pull_gear_coordinate"] = self.__get_delta_pushpull_coordinate(delta_time, will_delta) + last_current_push_pull_gear_coordinate
        current_data.loc["current_drill_gear_coordinate"] = self.__get_delta_pushpull_coordinate(delta_time, will_delta) + current_drill_gear_coordinate


        if gear_order > last_drill_gear:
            pass


    def __get_delta_time__(self):
        x = 0.02
        xn = numpy.random.randn()
        delta_time = x + xn / 1000
        return delta_time

    def __get_delta_pushpull_coordinate(self, delta_time, will_delta, range_delta=2):
        v = 100 / 1.5
        v = v + numpy.random.rand() * 0.1
        if will_delta < 0:
            v = -v
        delta_coordinate = v * delta_time
        if will_delta < range_delta:
            return 0
        return delta_coordinate

    def coordinateTogear(self, coordinate):
        pass


    def __current_push_pull_gear__(self):
        pass

    def __current_push_pull_gear_coordinate__(self):
        pass

    def __delta_angle_calclude__(self, angle_current, angle_last):
            thread_control_angle_counterclockwise = - 100
            thread_control_angle_clockwise = 200
            delta_angle1 = angle_current - angle_last
            if delta_angle1 > thread_control_angle_clockwise:
                angle_delta_r = (360-angle_last) + angle_current
                return angle_delta_r
            elif delta_angle1 < thread_control_angle_counterclockwise:
                angle_delta_r = -angle_last + angle_current-360
                return angle_delta_r
            else:
                angle_delta_r = delta_angle1
                return angle_delta_r

    def __apply_veclocity_data__(self, data_frame):
        if hasattr(self, "last_data"):
            last_data = self.last_data
            delta_time = data_frame.loc["time_"] - last_data.loc["time_"]
            delta_distance_ = data_frame.loc["beam_coordinate"] - last_data.loc["beam_coordinate"]
            delta_hand_distance_ = data_frame.loc["hand_coordinate"] - last_data.loc["hand_coordinate"]
            v_ = delta_distance_/delta_time
            v_hand = delta_hand_distance_/delta_time
            current_push_pull_gear_coordinate = data_frame.loc["current_push_pull_gear_coordinate"] - last_data.loc["current_push_pull_gear_coordinate"]
            current_drill_gear_coordinate = data_frame.loc["current_drill_gear_coordinate"] - last_data.loc["current_drill_gear_coordinate"]
            delta_messure_push_pull = data_frame.loc["messure_push_pull"] - last_data.loc["messure_push_pull"]
            delta_messure_drill = data_frame.loc["messure_drill"] - last_data.loc["messure_drill"]
            delta_angle = self.__delta_angle_calclude__(data_frame.loc["pole_angle_at_machine"], last_data.loc["pole_angle_at_machine"])
            self.last_data = copy.deepcopy(data_frame)
            return v_, \
                   v_hand,\
                   delta_time, \
                   delta_distance_,\
                   delta_hand_distance_,\
                   current_push_pull_gear_coordinate,\
                   current_drill_gear_coordinate,\
                   delta_messure_push_pull,\
                   delta_messure_drill, \
                   delta_angle
        else:
            self.last_data = copy.deepcopy(data_frame)
            return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

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
        data_frame3.loc[:, "delta_time"] = dd.loc[:, 2]
        data_frame3.loc[:, "delta_distance_"] = dd.loc[:, 3]
        data_frame3.loc[:, "delta_hand_distance_"] = dd.loc[:, 4]
        data_frame3.loc[:, "current_push_pull_gear_coordinate"] = dd.loc[:, 5]
        data_frame3.loc[:, "current_drill_gear_coordinate"] = dd.loc[:, 6]
        data_frame3.loc[:, "delta_messure_push_pull"] = dd.loc[:, 7]
        data_frame3.loc[:, "delta_messure_drill"] = dd.loc[:, 8]
        data_frame3.loc[:, "delta_pole_angle_at_machine"] = dd.loc[:, 9]
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
            delta_time = data_v.loc["delta_time"]
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


class equepmentSingleManager:
    def __init__(self, interface_operator_obj):
        self.loop_list = [] # list all data must read
        self.all_order_name = []
        self.interface_operator_obj = interface_operator_obj
        self.load_data2 = seting.parameter_load_data

    def __get_push_pull_messure__(self):
        # if
        pass

    def __get_drill_messure__(self):
        gear_begin = self.load_data2["Equepment_pole_dirll_coordinate"][0]
        gear_end = self.load_data2["Equepment_pole_dirll_coordinate"][2]
        if gear_end > gear_begin:
            gear_begin_end = (gear_begin, gear_end)
        else:
            gear_begin_end = (gear_end, gear_begin)
        current_drill_gear_stop_coordinate = self.load_data2["Equepment_pole_dirll_coordinate"][3]
        pole_len = 28000

        # current_pole_number, soil statue, push_pull_pressure, push_pull_distance_delta, push_pull_gear_coordinate_delta,
        #_init_data.
        current_drill_gear_coordinate = numpy.random.randint(*gear_begin_end)  # if current_drill_gear_coordinate is None,
        # beam_coordinate = numpy.random.randint(*beam_coordinate_begin_end)  # if beam_coordinate is None,

        push_pull_coordinate_begin = current_drill_gear_stop_coordinate

        # if push_pull simulate input
        messure_push_pull = 0
        messure_drill = 0
        drill_delta = 22
        pass

    def push_pull_operate_simulate(self, gear_number, interface_operator_obj):
        if gear_number == 0:
            pass

    def __get__drill_angle_velocity(self, data_n, beam_coordinate):
        delta_time = data_n.loc["time_"]
        soil_level = 2
        pressure_k = 0.00058621875
        current_pole_number_in_hole = data_n["current_pole_number_in_hole"]
        current_pole_distance_not_in_hole = data_n["current_pole_distance_not_in_hole"]

        current_beam_coordinate_distance = 3000 - beam_coordinate - self.load_data2["pole_in_middle_tiger_tooth_coordinate"]
        delta = numpy.random.randn() / 100
        angle__set_delta = (soil_level * (
                    current_pole_number_in_hole * 3000 + current_beam_coordinate_distance) * pressure_k + delta)/delta_time  + delta
        data_n["angle__set_delta"] = angle__set_delta
        return angle__set_delta

    def __get__drill__angle__set_delta(self, data_n, beam_coordinate):
        """
        this function is the sample function only used at the simulation environment , real data must the pieces
        of data , delta time must last 10 seconds, it's difficult at the remote pole angle collection, current equepment
        don't support computer collected it, now only man read and input, this method will, only used the pillow read
        """
        soil_level = 2
        pressure_k = 0.00058621875
        current_pole_number_in_hole = data_n["current_pole_number_in_hole"]
        current_pole_distance_not_in_hole = data_n["current_pole_distance_not_in_hole"]

        current_beam_coordinate_distance = 3000 - beam_coordinate - self.load_data2["pole_in_middle_tiger_tooth_coordinate"]
        delta = numpy.random.randn() / 100
        delta_angle = soil_level * (
                    current_pole_number_in_hole * 3000 + current_beam_coordinate_distance) * pressure_k + delta
        data_n["angle__set_delta"] = delta_angle
        return delta_angle

    def __get__pushpull_distance_delta(self, data_n, beam_coordinate):
        """
        this function is the sample function only used at the simulation environment , real data must the pieces
        of data , delta time must last 10 seconds
        """
        soil_level = 2
        pressure_k = 0.00004625
        pole_lenth = 3000
        current_pole_number_in_hole = data_n["current_pole_number_in_hole"]
        current_pole_distance_not_in_hole = data_n["current_pole_distance_not_in_hole"]

        current_beam_coordinate_distance = pole_lenth - beam_coordinate - self.load_data2["pole_in_middle_tiger_tooth_coordinate"]
        delta = numpy.random.randn()/100
        puss_pressure = soil_level*(current_pole_number_in_hole*3000 + current_beam_coordinate_distance)*pressure_k + delta
        data_n["messure_push_pull"] = puss_pressure


    def __get_drill_pressure__(self, data_n, beam_coordinate):
        soil_level = 2
        pressure_k = 0.00004625
        current_pole_number_in_hole = data_n["current_pole_number_in_hole"]
        current_pole_distance_not_in_hole = data_n["current_pole_distance_not_in_hole"]

        current_beam_coordinate_distance = beam_coordinate - self.load_data2["pole_in_middle_tiger_tooth_coordinate"]
        delta = numpy.random.randn() / 100
        messure_drill = soil_level * (
                    current_pole_number_in_hole * 3000 + current_beam_coordinate_distance) * pressure_k + delta
        data_n["messure_drill"] = messure_drill

    def __get__water_messure__(self):
        data = 5 + numpy.random.randn()/10
        return data

    def __get_delta_time__(self):
        k = 0.02
        delta_time = numpy.random.randn()/50 + k
        return delta_time


    def run(self):
        # run method function map the observation method.
        pass

    def add_single(self, name):
        pass

    def run_observation_data(self):
        #observation data is map the run method
        pass

    async def beamcoordinate(self, interface_operator_obj, simulation=False):
        self.beam_velocity = 1
        data_n = pandas.read_csv(r"nnnnnn.csv")

        data_n.set_index(["current_push_pull_gear", "current_drill_gear", ])
        beam_4m_change = interface_operator_obj.machine_obj.main_beam.Equepment_line_distance_measure_4m_beam
        drill_box_1m_change = interface_operator_obj.machine_obj.drill_box_.Equepment_line_distance_measure_1m_drill_box
        while True:
            for every_d in data_n.itertuples():
                delta_distance = data_n.loc[every_d.Index, "delta_distance_"]
                beam_coordinate = data_n.loc[every_d.Index, "beam_coordinate"]
                hand_coordinate = data_n.loc[every_d.Index, "hand_coordinate"]
                delta_time = data_n.loc[:, "delta_time"]
                current_drill_gear = data_n.loc[every_d.Index, "current_drill_gear"]
                messure_drill = data_n.loc[every_d.Index, "messure_drill"]
                messure_push_pull = data_n.loc[every_d.Index, "messure_push_pull"]
                new_index = pandas.MultiIndex((delta_distance, current_drill_gear, messure_drill, messure_push_pull))
                beam_4m_change.simulation = True
                beam_4m_change.coordinate = beam_coordinate
                drill_box_1m_change.simulation = True
                drill_box_1m_change = hand_coordinate
                await asyncio.sleep(delta_time)

        pass

    async def hand_arm_coordinate(self):
        await asyncio.sleep(0.01)
        pass

    async def samulate_over(self):
        pass


