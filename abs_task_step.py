__author__ = "boss"
__date__ = '2022/11/29 16:44'
import contextlib


class step_():
    def __init__(self):

        self.pause = False
        self.step = [
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
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2, False, "wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],


    @contextlib.contextmanager
    def in_run(self, N, coordinate, keep_distance_coordinat):
        self.step[N][2] = "begin"
        self.current_step = self.step[N]
        yield self.step[N][0](coordinate, keep_distance_coordinat)
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
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, True, True, True, True, False):
            with self.in_run(7) as T:
                if T == True:
                    self.step[7][1] = True
                    return  True
        if (self.step[1][1], self.step[2][1],  self.step[3][1],  self.step[4][1],  self.step[5][1],  self.step[6][1],  self.step[7][1]) == (True, True, True, True, True, True, True):
            with self.in_run(8) as T:
                if T == True:
                    self.step[8][1] = True
                    return  True
    def run_pause_stop(self):
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
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],

    def run_2(self):
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],

    def run_3(self):
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],

    def run_4(self):
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],
    def run_5(self):
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],
    def run_6(self):
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],

    def run_7(self):
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],
    def run_8(self):
        self.step[0] = [self.run_1, False, "wait_run"],
        self.step[1] = [self.run_2,False,"wait_run"],
        self.step[2] = [self.run_3, False, "wait_run"],
        self.step[3] = [self.run_4, False, "wait_run"],
        self.step[4] = [self.run_5, False, "wait_run"],
        self.step[5] = [self.run_6, False, "wait_run"],
        self.step[6] = [self.run_7, False, "wait_run"],
        self.step[7] = [self.run_8, False, "wait_run"],


class oldMachineProcess():
    # this class has be inherited new class name is oldMachineProcess and it loop function has be transfer to
    # the new loop sys at the order system  .the order get from there
    def set_parameter_obj(self, machine_obj, box_pole_obj):
        self.box_pole_obj = box_pole_obj
        self.machin_obj = machine_obj

        self.ProcessSendOrderToWindowPipe = machine_obj.ProcessSendOrderToWindowPipe
        self.remenber_parameter = {}
        self.authticate = None

    def set_zero_encodin_push_pull_equepment(self, new_parameter=None):
            if new_parameter == ("lock_operation", True):
                self.authticate = True
            if new_parameter == ("lock_operation", False):
                self.authticate = False
            self.reset_parameter(new_parameter)
            self.set_angle_zero_correcting_angle(new_parameter)
            self.set_hand_box_run_uncorecte_range(new_parameter)
            self.set_drill_box_up_down_uncorrect_range(new_parameter)
            self.set_beam_parameter(new_parameter)
            # use dict here to change the parameter

    def set_beam_parameter(self, parameter):
        if parameter[0] == "polethread_out_circle_number_intiger":
            self.remenber_parameter["polethread_out_circle_number_intiger"] =  parameter[1]

        if parameter[0] == "tiger_loose_time_":
            self.remenber_parameter["tiger_loose_time_"] = parameter[1]
            self.machin_obj.main_beam.tiger_loose_time_ = parameter[1]

        if parameter[0] == "tiger_tight_time_":
            self.remenber_parameter["tiger_tight_time_"] = parameter[1]
            self.machin_obj.main_beam.tiger_tight_time_ = parameter[1]
        if parameter[0] == "box_grap_hand_tight_strong":
            self.remenber_parameter["box_grap_hand_tight_strong"] = parameter[1]
            self.machin_obj.drill_box.box_grap_hand_tight_strong = parameter[1]
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.box_grap_hand_tight_strong  = parameter[1]

        if parameter[0] == "_drill_box_grap_hand_tight_slight":
            self.remenber_parameter["_drill_box_grap_hand_tight_slight"] = parameter[1]
            self.machin_obj.drill_box._drill_box_grap_hand_tight_slight = parameter[1]
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont._drill_box_grap_hand_tight_slight  = parameter[1]

        if parameter[0] == "drill_box_grap_hand_tight_greater_strong":
            self.remenber_parameter["drill_box_grap_hand_tight_greater_strong"] = parameter[1]
            self.machin_obj.drill_box.drill_box_grap_hand_tight_greater_strong = parameter[1]
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_grap_hand_tight_greater_strong = parameter[1]

        if parameter[0] == "drill_box_grap_hand_relax_full":
            self.remenber_parameter["drill_box_grap_hand_relax_full"] = parameter[1]
            self.machin_obj.drill_box.drill_box_grap_hand_relax_full = parameter[1]
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_grap_hand_relax_full = \
            parameter[1]

        if parameter[0] == "drill_box_grap_hand_relax_half":
            self.remenber_parameter["drill_box_grap_hand_relax_half"] = parameter[1]
            self.machin_obj.drill_box.drill_box_grap_hand_relax_half = parameter[1]
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_grap_hand_relax_half = \
            parameter[1]

        if parameter[0] == "drill_box_grap_hand_relax_greater_part":
            self.remenber_parameter["drill_box_grap_hand_relax_greater_part"] = parameter[1]
            self.machin_obj.drill_box.drill_box_grap_hand_relax_greater_part = parameter[1]
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_grap_hand_relax_greater_part = \
            parameter[1]

        if parameter[0] == "pole_taile_mother_thread_out_circle_numeber":
            self.remenber_parameter["pole_taile_mother_thread_out_circle_numeber"] = parameter[1]
            self.machin_obj.main_beam.pole_taile_mother_thread_out_circle_numeber = parameter[1]

        if parameter[0] == "pole_taile_mother_thread_out_pressure":
            self.remenber_parameter["pole_taile_mother_thread_out_pressure"] = parameter[1]
            self.machin_obj.main_beam.pole_taile_mother_thread_out_pressure = parameter[1]

        if parameter[0] == "tiger_dirll_pole_and_poletight_max_pressure":
            self.remenber_parameter["tiger_dirll_pole_and_poletight_max_pressure"] = parameter[1]
            self.machin_obj.main_beam.tiger_dirll_pole_and_poletight_max_pressure = parameter[1]

        if parameter[0] == "tiger_dirll_pole_pole_tight_max_pressure_level":
            self.remenber_parameter["tiger_dirll_pole_pole_tight_max_pressure_level"] = parameter[1]
            self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_max_pressure_level = parameter[1]

        if parameter[0] == "tiger_dirll_pole_pole_tight_push_max_pressure_level":
            self.remenber_parameter["tiger_dirll_pole_pole_tight_push_max_pressure_level"] = parameter[1]
            self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure_level = parameter[1]

        if parameter[0] == "tiger_dirll_pole_pole_tight_push_max_pressure":
            self.remenber_parameter["tiger_dirll_pole_pole_tight_push_max_pressure"] = parameter[1]
            self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure = parameter[1]

        if parameter[0] == "tiger_dirll_pole_pole_loose_max_pressure":
            self.remenber_parameter["tiger_dirll_pole_pole_loose_max_pressure"] = parameter[1]
            self.machin_obj.main_beam.tiger_dirll_pole_pole_loose_max_pressure = parameter[1]

        if parameter[0] == "pole_loose_need_mini_circle":
            self.remenber_parameter["pole_loose_need_mini_circle"] = parameter[1]
            self.machin_obj.main_beam.pole_loose_need_mini_circle = parameter[1]

        if parameter[0] == "set_pole_taile_mother_thread_out_circle_":
            self.remenber_parameter["set_pole_taile_mother_thread_out_circle_"] = parameter[1]
            self.machin_obj.main_beam.set_pole_taile_mother_thread_out_circle_ = parameter[1]

        if parameter[0] == "no_load_move_to_coordinnate_point_max_pressure":
            self.remenber_parameter["no_load_move_to_coordinnate_point_max_pressure"] = parameter[1]
            self.machin_obj.main_beam.no_load_move_to_coordinnate_point_max_pressure = parameter[1]

        if parameter[0] == "no_load_move_start_level":
            self.remenber_parameter["no_load_move_start_level"] = parameter[1]
            self.machin_obj.main_beam.no_load_move_start_level = parameter[1]

        if parameter[0] == "no_load_move_end_level":
            self.remenber_parameter["no_load_move_end_level"] = parameter[1]
            self.machin_obj.main_beam.no_load_move_end_level = parameter[1]

        if parameter[0] == "no_load_move_parameter_contrl_distance":
            self.remenber_parameter["no_load_move_parameter_contrl_distance"] = parameter[1]
            self.machin_obj.main_beam.no_load_move_parameter_contrl_distance = parameter[1]

        if parameter[0] == "tiger_touch_delta":
            self.remenber_parameter["tiger_touch_delta"] = parameter[1]
            self.machin_obj.main_beam.tiger_touch_delta = parameter[1]

        if parameter[0] == "beam_push_pull_in_tiger_step_distance":
            self.remenber_parameter["beam_push_pull_in_tiger_step_distance"] = parameter[1]
            self.machin_obj.main_beam.beam_push_pull_in_tiger_step_distance = parameter[1]

        if parameter[0] == "delta_contrast_beam_ruler_tiger_ruler":
            self.remenber_parameter["delta_contrast_beam_ruler_tiger_ruler"] = parameter[1]
            self.machin_obj.main_beam.delta_contrast_beam_ruler_tiger_ruler = parameter[1]

        if parameter[0] == "first_point_coordinate":
            self.remenber_parameter["first_point_coordinate"] = parameter[1]
            self.machin_obj.main_beam.first_point_coordinate = parameter[1]

        if parameter[0] == "first_point_coordinate_delta":
            self.remenber_parameter["first_point_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.first_point_coordinate_delta = parameter[1]

        if parameter[0] == "first_point_coordinate_map_tiger_ruler_range":
            self.remenber_parameter["first_point_coordinate_map_tiger_ruler_range"] = parameter[1]
            self.machin_obj.main_beam.first_point_coordinate_map_tiger_ruler_range = parameter[1]

        if parameter[0] == "first_point_characteristic_success_value":
            self.remenber_parameter["first_point_characteristic_success_value"] = parameter[1]
            self.machin_obj.main_beam.first_point_characteristic_success_value = parameter[1]

        if parameter[0] == "second_point_coordinate":
            self.remenber_parameter["second_point_coordinate"] = parameter[1]
            self.machin_obj.main_beam.second_point_coordinate = parameter[1]

        if parameter[0] == "second_point_coordinate_delta":
            self.remenber_parameter["second_point_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.second_point_coordinate_delta = parameter[1]

        if parameter[0] == "second_point_coordinate_map_tiger_ruler_range":
            self.remenber_parameter["second_point_coordinate_map_tiger_ruler_range"] = parameter[1]
            self.machin_obj.main_beam.second_point_coordinate_map_tiger_ruler_range = parameter[1]

        if parameter[0] == "taile_thread_is_ok_point_coordinate":
            self.remenber_parameter["taile_thread_is_ok_point_coordinate"] = parameter[1]
            self.machin_obj.main_beam.taile_thread_is_ok_point_coordinate = parameter[1]

        if parameter[0] == "taile_thread_is_ok_point_coordinate_delat":
            self.remenber_parameter["taile_thread_is_ok_point_coordinate_delat"] = parameter[1]
            self.machin_obj.main_beam.taile_thread_is_ok_point_coordinate_delat = parameter[1]

        if parameter[0] == "taile_thread_is_ok_point_coordinate_map_tiger_ruler_range":
            self.remenber_parameter["taile_thread_is_ok_point_coordinate_map_tiger_ruler_range"] = parameter[1]
            self.machin_obj.main_beam.taile_thread_is_ok_point_coordinate_map_tiger_ruler_range = parameter[1]

        if parameter[0] == "fourth_point_coordinate":
            self.remenber_parameter["fourth_point_coordinate"] = parameter[1]
            self.machin_obj.main_beam.fourth_point_coordinate = parameter[1]

        if parameter[0] == "fourth_point_coordinate_delta":
            self.remenber_parameter["fourth_point_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.fourth_point_coordinate_delta = parameter[1]

        if parameter[0] == "fourth_point_coordinate_map_tiger_ruler_range":
            self.remenber_parameter["fourth_point_coordinate_map_tiger_ruler_range"] = parameter[1]
            self.machin_obj.main_beam.fourth_point_coordinate_map_tiger_ruler_range = parameter[1]

        if parameter[0] == "Equepment_line_distance_measure_4m_beam_coordinate_delta":
            self.remenber_parameter["Equepment_line_distance_measure_4m_beam_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate_delta = parameter[1]

        if parameter[0] == "Equepment_line_distance_measure_beam_taile_coordinate_delta":
            self.remenber_parameter["Equepment_line_distance_measure_beam_taile_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate_delta = parameter[1]

        if parameter[0] == "Equepment_line_distance_measure_beam_head_coordinate_delta":
            self.remenber_parameter["Equepment_line_distance_measure_beam_head_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate_delta = parameter[1]

        if parameter[0] == "Equepment_line_distance_measure_dirll_box_updown_coordinate_delta":
            self.remenber_parameter["Equepment_line_distance_measure_dirll_box_updown_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.Equepment_line_distance_measure_dirll_box_updown.coordinate_delta = parameter[1]

        if parameter[0] == "drill_box.Equepment_drill_box_digit_piont.pole_point_delta":
            self.remenber_parameter["drill_box.Equepment_drill_box_digit_piont.pole_point_delta"] = parameter[1]
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.pole_point_delta = parameter[1]

        if parameter[0] == "third_point_coordinate":
            self.remenber_parameter["third_point_coordinate"] = parameter[1]
            self.machin_obj.main_beam.third_point_coordinate = parameter[1]

        if parameter[0] == "third_point_coordinate_delta":
            self.remenber_parameter["third_point_coordinate_delta"] = parameter[1]
            self.machin_obj.main_beam.third_point_coordinate_delta = parameter[1]

        if parameter[0] == "third_point_coordinate_map_tiger_ruler_range":
            self.remenber_parameter["third_point_coordinate_map_tiger_ruler_range"] = parameter[1]
            self.machin_obj.main_beam.third_point_coordinate_map_tiger_ruler_range = parameter[1]

    def reset_parameter(self, parameter):

        if  self.authticate == True:
            if parameter == ("set_stop_current_value", True):
                old_data = {}
                try:
                    with open("parameter_backup_data.tex", "rb") as parameterw:
                        old_data = pickle.load(parameterw)
                        if len(old_data) == 0:
                            old_data = {}

                except Exception:
                    pass
            print(parameter[0])
            if parameter[0] == ("Equepment_pole_push_pull_data_coordinate", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_start = value
                try:
                    self.remenber_parameter["Equepment_pole_push_pull_data_coordinate"][0] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_push_pull_data_coordinate"] = [value, 0, 0]
                    print("**********************************************************", inspect.currentframe().f_lineno, __class__)
                print("start data is ", self.remenber_parameter)

            if parameter[0] == ("Equepment_tigger_tooch_f_coordinate", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_start = value
                try:
                    self.remenber_parameter["Equepment_tigger_tooch_f_coordinate"][0] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_tooch_f_coordinate"] = [value, 0, 0]

            if parameter[0] == ("Equepment_tigger_tooch_b_coordinate", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_start = value
                try:
                    self.remenber_parameter["Equepment_tigger_tooch_b_coordinate"][0] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_tooch_b_coordinate"] = [value, 0, 0]

            if parameter[0] == ("Equepment_tigger_drill_coordinate", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_start = value
                try:
                    self.remenber_parameter["Equepment_tigger_drill_coordinate"][0] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_drill_coordinate"] = [value, 0, 0]


            if parameter[0] == ("Equepment_pole_push_pull_data_coordinate", "stop"):
                print("**********************************************************", inspect.currentframe().f_lineno, __class__)
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_stop = value
                try:
                    self.remenber_parameter["Equepment_pole_push_pull_data_coordinate"][1] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_push_pull_data_coordinate"] = [0, value, 0]

                    print("**********************************************************", inspect.currentframe().f_lineno, __class__)
                print("start data is ", self.remenber_parameter)

            if parameter[0] == ("Equepment_pole_dirll_coordinate", "stop"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_dirll.coordinate_stop = value
                try:
                    self.remenber_parameter["Equepment_pole_dirll_coordinate"][1] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_dirll_coordinate"] = [0, value, 0]

            if parameter[0] == ("Equepment_pole_dirll_coordinate", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_dirll.coordinate_stop = value
                try:
                    self.remenber_parameter["Equepment_pole_dirll_coordinate"][0] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_dirll_coordinate"] = [value, 0, 0]

            if parameter[0] == ("Equepment_pole_dirll_coordinate", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_dirll.coordinate_stop = value
                try:
                    self.remenber_parameter["Equepment_pole_dirll_coordinate"][2] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_dirll_coordinate"] = [0, 0, value]




            if parameter[0] == ("Equepment_tigger_tooch_f_coordinate", "stop"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_stop = value
                try:
                    self.remenber_parameter["Equepment_tigger_tooch_f_coordinate"][1] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_tooch_f_coordinate"] = [0, value, 0]



            if parameter[0] == ("Equepment_tigger_tooch_b_coordinate", "stop"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_stop = value
                try:
                    self.remenber_parameter["Equepment_tigger_tooch_b_coordinate"][1] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_tooch_b_coordinate"] = [0, value, 0]

            if parameter[0] == ("Equepment_tigger_drill_coordinate", "stop"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_stop = value
                try:
                    self.remenber_parameter["Equepment_tigger_drill_coordinate"][1] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_drill_coordinate"] = [0, value, 0]




            if parameter[0] == ("Equepment_pole_push_pull_data_coordinate", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_end = float(parameter[1])
                try:
                    self.remenber_parameter["Equepment_pole_push_pull_data_coordinate"][2] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_push_pull_data_coordinate"] = [0, 0, value]
                    print("**********************************************************", inspect.currentframe().f_lineno, __class__)
                print("start data is ", self.remenber_parameter)


            if parameter[0] == ("Equepment_tigger_tooch_f_coordinate", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_end = value
                try:
                    self.remenber_parameter["Equepment_tigger_tooch_f_coordinate"][2] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_tooch_f_coordinate"] = [0, 0, value]

            if parameter[0] == ("Equepment_tigger_tooch_b_coordinate", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_end = value
                try:
                    self.remenber_parameter["Equepment_tigger_tooch_b_coordinate"][2] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_tooch_b_coordinate"] = [0, 0, value]


            if parameter[0] == ("Equepment_tigger_drill_coordinate", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_end = value
                try:
                    self.remenber_parameter["Equepment_tigger_drill_coordinate"][2] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_tigger_drill_coordinate"]  = [0, 0, value]



            if parameter[0] == ("Equepment_pole_push_pull_data_cycle_number", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_push_pull.cycle_number_start = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_pole_push_pull_data_cycle_number"][0] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_pole_push_pull_data_cycle_number", [value, 0, 0])

            if parameter[0] == ("Equepment_pole_dirll_cycle_number", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_dirll.cycle_number_start = value
                try:
                    self.remenber_parameter["Equepment_pole_dirll_cycle_number"][0] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_dirll_cycle_number"] = [value, 0, 0]

            if parameter[0] == ("Equepment_tigger_tooch_f_cycle_number", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_start = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_tooch_f_cycle_number"][0] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_tooch_f_cycle_number", [value, 0, 0])


            if parameter[0] == ("Equepment_tigger_tooch_b_cycle_number", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_start = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_tooch_b_cycle_number"][0] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_tooch_b_cycle_number", [value, 0, 0])


            if parameter[0] == ("Equepment_tigger_drill_cycle_number", "start"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_start = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_drill_cycle_number"][0] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_drill_cycle_number", [value, 0, 0])


            if parameter[0] == ("Equepment_pole_push_pull_data_cycle_number", "stop"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_stop = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_pole_push_pull_data_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_pole_push_pull_data_cycle_number", [0, value, 0])


            if parameter[0] == ("Equepment_pole_dirll_cycle_number", "stop"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_dirll.cycle_number_stop = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_pole_dirll_cycle_number"][1] = value
                else:
                    self.remenber_parameter["Equepment_pole_dirll_cycle_number"] = [0, value, 0]

            if parameter[0] == ("Equepment_tigger_tooch_f_cycle_number", "stop"):
                value = float(parameter[1])
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_tooch_f_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_tooch_f_cycle_number", [0, value, 0])
                self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_stop = value

            if parameter[0] == ("Equepment_tigger_tooch_b_cycle_number", "stop"):
                value = float(parameter[1])
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_tooch_b_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_tooch_b_cycle_number", [0, value, 0])
                self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_stop = value

            if parameter[0] == ("Equepment_tigger_drill_cycle_number", "stop"):
                value = float(parameter[1])
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_drill_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_drill_cycle_number", [0, value, 0])

                self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_stop = value



            if parameter[0] == ("Equepment_pole_push_pull_data_cycle_number", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_end = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_pole_push_pull_data_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_pole_push_pull_data_cycle_number", [0, 0, value])

            if parameter[0] == ("Equepment_pole_dirll_cycle_number", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_pole_dirll.cycle_number_end = value
                try:
                    self.remenber_parameter["Equepment_pole_dirll_cycle_number"][1] = value
                except Exception as ff:
                    self.remenber_parameter["Equepment_pole_dirll_cycle_number"] = [0, 0, value]


            if parameter[0] == ("Equepment_tigger_tooch_f_cycle_number", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_end = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_tooch_f_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_tooch_f_cycle_number", [0, 0, value])

            if parameter[0] == ("Equepment_tigger_tooch_b_cycle_number", "end"):
                value = float(parameter[1])
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_tooch_b_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_tooch_b_cycle_number", [0, 0, value])
                self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_end = value

            if parameter[0] == ("Equepment_tigger_drill_cycle_number", "end"):
                value = float(parameter[1])
                self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_end = value
                if parameter[0][0] in self.remenber_parameter.keys():
                    self.remenber_parameter["Equepment_tigger_drill_cycle_number"][1] = value
                else:
                    self.remenber_parameter.setdefault("Equepment_tigger_drill_cycle_number", [0, 0, value])

            if parameter[0] == "pole_in_middle_tiger_tooth_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_cycle_number", value)

            if parameter[0] == "pole_in_middle_tiger_tooth_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_coordinate", value)



            if parameter[0] == "pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate":
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddddddddddddddddddddddd", inspect.currentframe().f_lineno)
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate", value)


            if parameter[0] == "pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number":
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddddddddddddddddddddddd", inspect.currentframe().f_lineno)
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number", value)

            if parameter[0] == "pole_in_middle_tiger_tooth_tiggerback_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_tiggerback_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_tiggerback_cycle_number", value)


            if parameter[0] == "pole_in_middle_tiger_tooth_to_taile_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_to_taile_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_to_taile_coordinate", value)

            if parameter[0] == "pole_in_middle_tiger_tooth_to_taile_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_to_taile_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_to_taile_cycle_number", value)

            if parameter[0] == "pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate", value)

                print(inspect.currentframe().f_lineno, __file__, "pole_in_middle_tiger_tooth_to_taile_coordinate  value", value)


            if parameter[0] == "pole_in_middle_tiger_tooth_tiggerback_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_tiggerback_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_tiggerback_cycle_number", value)

            if parameter[0] == "pole_in_middle_tiger_tooth_tiggerback_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_in_middle_tiger_tooth_tiggerback_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("pole_in_middle_tiger_tooth_tiggerback_coordinate", value)







            if parameter[0] == "beam_taile_5cm_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.beam_taile_5cm_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["beam_taile_5cm_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("beam_taile_5cm_coordinate", value)

            if parameter[0] == "beam_taile_5cm_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.beam_taile_5cm_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["beam_taile_5cm_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("beam_taile_5cm_cycle_number", value)

            if parameter[0] == "pole_pull_back_can_out_box_hand_to_grap_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_pull_back_can_out_box_hand_to_grap_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_pull_back_can_out_box_hand_to_grap_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("pole_pull_back_can_out_box_hand_to_grap_coordinate", value)

            if parameter[0] == "pole_pull_back_can_out_box_hand_to_grap_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.pole_pull_back_can_out_box_hand_to_grap_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["pole_pull_back_can_out_box_hand_to_grap_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("pole_pull_back_can_out_box_hand_to_grap_cycle_number", value)

            if parameter[0] == "main_beam_last_pole_up_down_expangd_hole_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.main_beam_last_pole_up_down_expangd_hole_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["main_beam_last_pole_up_down_expangd_hole_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("main_beam_last_pole_up_down_expangd_hole_coordinate", value)

            if parameter[0] == "main_beam_last_pole_up_down_expangd_hole_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.main_beam_last_pole_up_down_expangd_hole_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["main_beam_last_pole_up_down_expangd_hole_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("main_beam_last_pole_up_down_expangd_hole_cycle_number", value)

            if parameter[0] == "man_give_pole_place_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.man_give_pole_place_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["man_give_pole_place_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("man_give_pole_place_coordinate", value)

            if parameter[0] == "man_give_pole_place_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.man_give_pole_place_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["man_give_pole_place_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("man_give_pole_place_cycle_number", value)

            if parameter[0] == "man_give_pole_place_back_last_point_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.man_give_pole_place_back_last_point_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["man_give_pole_place_back_last_point_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("man_give_pole_place_back_last_point_coordinate", value)

            if parameter[0] == "man_give_pole_place_back_last_point_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.man_give_pole_place_back_last_point_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["man_give_pole_place_back_last_point_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("man_give_pole_place_back_last_point_cycle_number", value)

            if parameter[0] == "the_new_point_man_can_let_pole_out_beam_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.the_new_point_man_can_let_pole_out_beam_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["the_new_point_man_can_let_pole_out_beam_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("the_new_point_man_can_let_pole_out_beam_coordinate", value)

            if parameter[0] == "the_new_point_man_can_let_pole_out_beam_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.the_new_point_man_can_let_pole_out_beam_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["the_new_point_man_can_let_pole_out_beam_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("the_new_point_man_can_let_pole_out_beam_cycle_number", value)

            if parameter[0] == "box_updown_column_up":
                value = float(parameter[1])
                self.machin_obj.main_beam.box_updown_column_up = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["box_updown_column_up"] = value
                else:
                    self.remenber_parameter.setdefault("box_updown_column_up", value)
                print("box_updown_column_up", self.remenber_parameter["box_updown_column_up"])
            if parameter[0] == "box_updown_bottom":
                value = float(parameter[1])
                self.machin_obj.main_beam.box_updown_bottom = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["box_updown_bottom"] = value
                else:
                    self.remenber_parameter.setdefault("box_updown_bottom", value)

            if parameter[0] == "box_updown_column_can_grap_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.box_updown_column_can_grap_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["box_updown_column_can_grap_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("box_updown_column_can_grap_coordinate", value)

            if parameter[0] == "point1_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.point1_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point1_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("point1_coordinate", value)

            if parameter[0] == "point1_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.point1_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point1_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("point1_cycle_number", value)

            if parameter[0] == "point2_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.point2_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point2_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("point2_coordinate", value)

            if parameter[0] == "point2_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.point2_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point2_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("point2_cycle_number", value)

            if parameter[0] == "point3_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.point3_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point3_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("point3_coordinate", value)

            if parameter[0] == "point3_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.point3_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point3_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("point3_cycle_number", value)
            if parameter[0] == "point_beam_grap_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.point_beam_grap_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point_beam_grap_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("point_beam_grap_coordinate", value)

            if parameter[0] == "point_beam_grap_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.point_beam_grap_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point_beam_grap_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("point_beam_grap_cycle_number", value)

            if parameter[0] == "box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate", value)

            if parameter[0] == "box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number", value)
            if parameter[0] == "point_unstop_beam_coordinate":
                value = float(parameter[1])
                self.machin_obj.main_beam.point_unstop_beam_coordinate = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point_unstop_beam_coordinate"] = value
                else:
                    self.remenber_parameter.setdefault("point_unstop_beam_coordinate", value)

            if parameter[0] == "point_unstop_beam_cycle_number":
                value = float(parameter[1])
                self.machin_obj.main_beam.point_unstop_beam_cycle_number = value
                if parameter[0] in self.remenber_parameter.keys():
                    self.remenber_parameter["point_unstop_beam_cycle_number"] = value
                else:
                    self.remenber_parameter.setdefault("point_unstop_beam_cycle_number", value)

            if parameter == ("save",):
                old_data2 = pandas.read_csv(r"D:\machine\机器端\mmmmmmmmmmm.csv", index_col='Unnamed: 0')
                old_data2.apply(self.apply_save_data)

            if parameter == ("load_parameter",):
                load_data = seting.get_dict_parameter()
                self.load_encode_rock_arm_data(load_data)
                self.load_drill_box_data(load_data)
                self.reset_pole_box_1_2_3point_coordinate(load_data)
                self.load_mainbeam_parameter(load_data)

    def apply_save_data(self, data):
        _data = dict(data, **self.remenber_parameter)
        time.sleep(0.1)
        _data = pandas.Series(_data)
        _data.to_csv(r"D:\machine\机器端\mmmmmmmmmmm.csv")



    def reset_pole_box_1_2_3point_coordinate(self, parameter):

        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point1_coordinate = parameter.get("point1_coordinate", 0)
        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point2_coordinate = parameter.get("point2_coordinate", 0)
        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point3_coordinate = parameter.get("point3_coordinate", 0)

    def load_encode_rock_arm_data(self, load_data):
        # if self.authticate == True:
            Equepment_pole_push_pull_coordinate = load_data.get("Equepment_pole_push_pull_data_coordinate", [0, 0, 0])
            print(Equepment_pole_push_pull_coordinate)
            print(inspect.currentframe().f_lineno, __file__, __class__)
            self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_start = Equepment_pole_push_pull_coordinate[0]
            self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_stop = Equepment_pole_push_pull_coordinate[1]
            self.machin_obj.main_beam.Equepment_pole_push_pull.coordinate_end = Equepment_pole_push_pull_coordinate[2]

            Equepment_pole_push_pull_data_cycle_number = load_data.get("Equepment_pole_push_pull_data_cycle_number", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_pole_push_pull.cycle_number_start = Equepment_pole_push_pull_data_cycle_number[0]
            self.machin_obj.main_beam.Equepment_pole_push_pull.cycle_number_stop = Equepment_pole_push_pull_data_cycle_number[1]
            self.machin_obj.main_beam.Equepment_pole_push_pull.cycle_number_end = Equepment_pole_push_pull_data_cycle_number[2]


            Equepment_pole_dirll_coordinate = load_data.get("Equepment_pole_dirll_coordinate", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_pole_dirll.coordinate_start = Equepment_pole_dirll_coordinate[0]
            self.machin_obj.main_beam.Equepment_pole_dirll.coordinate_stop = Equepment_pole_dirll_coordinate[1]
            self.machin_obj.main_beam.Equepment_pole_dirll.coordinate_end = Equepment_pole_dirll_coordinate[2]

            Equepment_pole_dirll_cycle_number = load_data.get("Equepment_pole_dirll_cycle_number", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_pole_dirll.cycle_number_start = Equepment_pole_dirll_cycle_number[0]
            self.machin_obj.main_beam.Equepment_pole_dirll.cycle_number_stop = Equepment_pole_dirll_cycle_number[1]
            self.machin_obj.main_beam.Equepment_pole_dirll.cycle_number_end = Equepment_pole_dirll_cycle_number[2]



            Equepment_tigger_tooch_f_coordinate = load_data.get("Equepment_tigger_tooch_f_coordinate", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_start = Equepment_tigger_tooch_f_coordinate[0]
            self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_stop = Equepment_tigger_tooch_f_coordinate[1]
            self.machin_obj.main_beam.Equepment_tigger_tooch_f.coordinate_end = Equepment_tigger_tooch_f_coordinate[2]

            Equepment_tigger_tooch_f_cycle_number = load_data.get("Equepment_tigger_tooch_f_cycle_number", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_tigger_tooch_f.cycle_number_start = Equepment_tigger_tooch_f_cycle_number[0]
            self.machin_obj.main_beam.Equepment_tigger_tooch_f.cycle_number_stop = Equepment_tigger_tooch_f_cycle_number[1]
            self.machin_obj.main_beam.Equepment_tigger_tooch_f.cycle_number_end = Equepment_tigger_tooch_f_cycle_number[2]



            Equepment_tigger_tooch_b_coordinate = load_data.get("Equepment_tigger_tooch_b_coordinate", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_start = Equepment_tigger_tooch_b_coordinate[0]
            self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_stop = Equepment_tigger_tooch_b_coordinate[1]
            self.machin_obj.main_beam.Equepment_tigger_tooch_b.coordinate_end = Equepment_tigger_tooch_b_coordinate[2]

            Equepment_tigger_tooch_b_cycle_number = load_data.get("Equepment_tigger_tooch_b_cycle_number", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_tigger_tooch_b.cycle_number_start = Equepment_tigger_tooch_b_cycle_number[0]
            self.machin_obj.main_beam.Equepment_tigger_tooch_b.cycle_number_stop = Equepment_tigger_tooch_b_cycle_number[1]
            self.machin_obj.main_beam.Equepment_tigger_tooch_b.cycle_number_end = Equepment_tigger_tooch_b_cycle_number[2]

            Equepment_tigger_drill_coordinate = load_data.get("Equepment_tigger_drill_coordinate", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_start = Equepment_tigger_drill_coordinate[0]
            self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_stop = Equepment_tigger_drill_coordinate[1]
            self.machin_obj.main_beam.Equepment_tigger_drill.coordinate_end = Equepment_tigger_drill_coordinate[2]

            Equepment_tigger_drill_cycle_number = load_data.get("Equepment_tigger_drill_cycle_number", [0, 0, 0])
            self.machin_obj.main_beam.Equepment_tigger_drill.cycle_number_start = Equepment_tigger_drill_cycle_number[0]
            self.machin_obj.main_beam.Equepment_tigger_drill.cycle_number_stop = Equepment_tigger_drill_cycle_number[1]
            self.machin_obj.main_beam.Equepment_tigger_drill.cycle_number_end = Equepment_tigger_drill_cycle_number[2]


    def load_mainbeam_parameter(self, parameter):
        ProcessSendOrderToWindowPipe = self.ProcessSendOrderToWindowPipe

        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_coordinate = parameter.get(
            "pole_in_middle_tiger_tooth_coordinate", None)  # the middle_tooth
        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_cycle_number = parameter.get(
            "pole_in_middle_tiger_tooth_cycle_number", None)  # the middle_tooth



        if self.machin_obj.main_beam.pole_in_middle_tiger_tooth_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_5.setText", "请重新设置"))

        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback_coordinate = parameter.get("pole_in_middle_tiger_tooth_tiggerback_coordinate",None)  # 20 father thread can out
        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback_cycle_number = parameter.get("pole_in_middle_tiger_tooth_tiggerback_cycle_number",None)  # 20 father thread can out
        ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_5.setText", str(self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback_cycle_number)))
        ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_98.setText", str(self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback_cycle_number)))


        if self.machin_obj.main_beam.pole_in_middle_tiger_tooth_tiggerback == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_6.setText", "请重新设置"))
            # self.ui_window.lineEdit_6.setText("请重新设置")


        self.machin_obj.drill_box.box_updown_column_up = parameter.get(
            "box_updown_column_up", None)  # the middle_tooth

        if self.machin_obj.drill_box.box_updown_column_up == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_12.setText", "请重新设置"))

        self.machin_obj.drill_box.box_updown_bottom = parameter.get(
            "box_updown_bottom", None)  # the middle_tooth
        if self.machin_obj.drill_box.box_updown_bottom == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_13.setText", "请重新设置"))

        self.machin_obj.drill_box.box_updown_colbox_updown_column_can_grapumn_up = parameter.get(
            "box_updown_colbox_updown_column_can_grapumn_up", None)  # the middle_tooth
        if self.machin_obj.drill_box.box_updown_colbox_updown_column_can_grapumn_up == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_11.setText", "请重新设置"))


        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_coordinate = parameter.get(
            "pole_in_middle_tiger_tooth_to_taile_coordinate", None)  # 20 father thread can out
        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_cycle_number = parameter.get(
            "pole_in_middle_tiger_tooth_to_taile_cycle_number", None)  # 20 father thread can out

        if self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_14.setText", "请重新设置"))

        if self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_cycle_number == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_100.setText", "请重新设置"))



        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate = parameter.get(
            "pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate", None)  # 20 father thread can out
        self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number = parameter.get(
            "pole_in_middle_tiger_tooth_to_taile_tofaward_cycle_number", None)  # 20 father thread can out

        self.point_beam_grap = self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point_beam_grap_coordinate = parameter.get(
            "point_beam_grap_coordinate", None)
        self.point_beam_grap_cycle_number = self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point_beam_grap_cycle_number = parameter.get(
            "point_beam_grap_cycle_number", None)

        self.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number = \
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number= \
            parameter.get("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_cycle_number", None)

        self.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate = \
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate = \
            parameter.get("box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate", None)

        self.point_unstop_beam_coordinate = self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point_unstop_beam_coordinate = \
            parameter.get("point_unstop_beam_coordinate", None)

        self.point_unstop_beam_cycle_number = self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point_unstop_beam_cycle_number = \
            parameter.get("point_unstop_beam_cycle_number", None)

        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point1_coordinate = parameter.get(
            "point1_coordinate", None)  # 20 father thread can out
        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point1_cycle_number = parameter.get(
            "point1_cycle_number", None)  # 20 father thread can out
        if self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point1_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_27.setText", "请重新设置"))
        if self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point1_cycle_number == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_114.setText", "请重新设置"))

        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point2_coordinate = parameter.get(
            "point2_coordinate", None)  # 20 father thread can out
        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point2_cycle_number = parameter.get(
            "point2_cycle_number", None)  # 20 father thread can out
        if self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point2_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_27.setText", "请重新设置"))
        if self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point2_cycle_number == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_114.setText", "请重新设置"))

        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point3_coordinate = parameter.get(
            "point3_coordinate", None)  # 20 father thread can out
        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point3_cycle_number = parameter.get(
            "point3_cycle_number", None)  # 20 father thread can out
        if self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point3_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_27.setText", "请重新设置"))
        if self.machin_obj.drill_box.Equepment_drill_box_digit_piont.point3_cycle_number == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_114.setText", "请重新设置"))

        if self.machin_obj.main_beam.pole_in_middle_tiger_tooth_to_taile_tofaward_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_15.setText", "请重新设置"))
            # self.ui_window.lineEdit_15.setText("请重新设置")

        self.machin_obj.main_beam.beam_taile_5cm_coordinate = parameter.get(
            "beam_taile_5cm_coordinate", None)  # 20 father thread can out
        self.machin_obj.main_beam.beam_taile_5cm_cycle_number = parameter.get(
            "beam_taile_5cm_cycle_number", None)  # 20 father thread can out


        if self.machin_obj.main_beam.beam_taile_5cm_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_8.setText", "请重新设置"))

            # self.ui_window.lineEdit_8.setText("请重新设置")

        self.machin_obj.main_beam.pole_pull_back_can_out_box_hand_to_grap = parameter.get(
            "pole_pull_back_can_out_box_hand_to_grap", None)  # 20 father thread can out
        if self.machin_obj.main_beam.pole_pull_back_can_out_box_hand_to_grap == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_9.setText", "请重新设置"))

            # self.ui_window.lineEdit_9.setText("请重新设置")

        self.machin_obj.main_beam.main_beam_last_pole_up_down_expangd_hole_coordinate = parameter.get(
            "main_beam_last_pole_up_down_expangd_hole_coordinate", None)  # 20 father thread can out
        self.machin_obj.main_beam.main_beam_last_pole_up_down_expangd_hole_cycle_number = parameter.get(
            "main_beam_last_pole_up_down_expangd_hole_cycle_number", None)  # 20 father thread can out


        if self.machin_obj.main_beam.main_beam_last_pole_up_down_expangd_hole_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_10.setText", "请重新设置"))

            # self.ui_window.lineEdit_10.setText("请重新设置")

        self.machin_obj.main_beam.man_give_pole_place_coordinate = parameter.get(
            "man_give_pole_place_coordinate", None)  # 20 father thread can out
        self.machin_obj.main_beam.man_give_pole_place_cycle_number = parameter.get(
            "man_give_pole_place_cycle_number", None)  # 20 father thread can out

        if self.machin_obj.main_beam.man_give_pole_place_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_23.setText", "请重新设置"))

            # self.ui_window.lineEdit_23.setText("请重新设置")

        self.machin_obj.main_beam.man_give_pole_place_back_last_point_coordinate = parameter.get(
            "man_give_pole_place_back_last_point_coordinate", None)  # 20 father thread can out
        self.machin_obj.main_beam.man_give_pole_place_back_last_point_cycle_number = parameter.get(
            "man_give_pole_place_back_last_point_cycle_number", None)  # 20 father thread can out


        if self.machin_obj.main_beam.man_give_pole_place_back_last_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_31.setText", "请重新设置"))

            # self.ui_window.lineEdit_31.setText("请重新设置")

        self.machin_obj.main_beam.the_new_point_man_can_let_pole_out_beam_coordinate = parameter.get(
            "the_new_point_man_can_let_pole_out_beam_coordinate", None)  # 20 father thread can out
        self.machin_obj.main_beam.the_new_point_man_can_let_pole_out_beam_cycle_number = parameter.get(
            "the_new_point_man_can_let_pole_out_beam_cycle_number", None)  # 20 father thread can out


        if self.machin_obj.main_beam.the_new_point_man_can_let_pole_out_beam_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_28.setText", "请重新设置"))

            # self.ui_window.lineEdit_28.setText("请重新设置")

        self.machin_obj.main_beam.polethread_out_circle_number = parameter.get(
            "polethread_out_circle_number", None)  # 20 father thread can out
        if self.machin_obj.main_beam.polethread_out_circle_number == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_111.setText", "请重新设置"))

            # self.ui_window.pushButton_111.setText("请重新设置")

        self.machin_obj.main_beam.pole_taile_mother_thread_out_circle_numeber = parameter.get(
            "pole_taile_mother_thread_out_circle_numeber", None)  # 20 father thread can out
        if self.machin_obj.main_beam.pole_taile_mother_thread_out_circle_numeber == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_122.setText", "请重新设置"))

            # self.ui_window.pushButton_122.setText("请重新设置")

        self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_max_pressure = parameter.get(
            "tiger_dirll_pole_pole_tight_max_pressure", None)

        if self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_max_pressure == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_113.setText", "请重新设置"))

            # self.ui_window.pushButton_113.setText("请重新设置")

        self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_max_pressure_level = parameter.get(
            "tiger_dirll_pole_pole_tight_max_pressure_level", None)  # 20 father thread can out
        if self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_max_pressure_level == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_115.setText", "请重新设置"))

            # self.ui_window.pushButton_115.setText("请重新设置")

        self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure_level = parameter.get(
            "tiger_dirll_pole_pole_tight_push_max_pressure_level", None)  # 20 father thread can out
        if self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure_level == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_124.setText", "请重新设置"))

            # self.ui_window.pushButton_124.setText("请重新设置")

        self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure = parameter.get(
            "tiger_dirll_pole_pole_tight_push_max_pressure", None)  # 20 father thread can out
        if self.machin_obj.main_beam.tiger_dirll_pole_pole_tight_push_max_pressure == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_140.setText", "请重新设置"))

            # self.ui_window.pushButton_140.setText("请重新设置")
        self.machin_obj.main_beam.pole_taile_mother_thread_out_pressure = parameter.get(
            "pole_taile_mother_thread_out_pressure", None)  # 20 father thread can out
        if self.machin_obj.main_beam.pole_taile_mother_thread_out_pressure == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_123.setText", "请重新设置"))

            # self.ui_window.pushButton_123.setText("请重新设置")

        self.machin_obj.main_beam.pole_loose_need_mini_circle = parameter.get(
            "pole_loose_need_mini_circle", None)  # 20 father thread can out
        if self.machin_obj.main_beam.pole_loose_need_mini_circle == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_114.setText", "请重新设置"))

            # self.ui_window.pushButton_114.setText("请重新设置")

        self.machin_obj.main_beam.pole_loose_need_mini_circle_drill_level = parameter.get(
            "pole_loose_need_mini_circle_drill_level", None)  # 20 father thread can out
        if self.machin_obj.main_beam.pole_loose_need_mini_circle_drill_level == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_116.setText", "请重新设置"))

            # self.ui_window.pushButton_116.setText("请重新设置")

        self.machin_obj.main_beam.box_grap_hand_tight_strong = parameter.get(
            "box_grap_hand_tight_strong", None)  # 20 father thread can out
        if self.machin_obj.main_beam.box_grap_hand_tight_strong == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_117.setText", "请重新设置"))

            # self.ui_window.pushButton_117.setText("请重新设置")

        self.machin_obj.main_beam._drill_box_grap_hand_tight_slight = parameter.get(
            "_drill_box_grap_hand_tight_slight", None)  # 20 father thread can out
        if self.machin_obj.main_beam._drill_box_grap_hand_tight_slight == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_118.setText", "请重新设置"))

            # self.ui_window.pushButton_118.setText("请重新设置")

        self.machin_obj.main_beam.drill_box_grap_hand_tight_greater_strong = parameter.get(
            "drill_box_grap_hand_tight_greater_strong", None)  # 20 father thread can out
        if self.machin_obj.main_beam.drill_box_grap_hand_tight_greater_strong == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_325.setText", "请重新设置"))
            # self.ui_window.pushButton_325.setText("请重新设置")

        self.machin_obj.main_beam.drill_box_grap_hand_relax_full = parameter.get(
            "drill_box_grap_hand_relax_full", None)  # 20 father thread can out
        if self.machin_obj.main_beam.drill_box_grap_hand_relax_full == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_173.setText", "请重新设置"))

            # self.ui_window.pushButton_173.setText("请重新设置")

        self.machin_obj.main_beam.drill_box_grap_hand_relax_half = parameter.get(
            "drill_box_grap_hand_relax_half", None)  # 20 father thread can out
        if self.machin_obj.main_beam.drill_box_grap_hand_relax_half == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_174.setText", "请重新设置"))

            # self.ui_window.pushButton_174.setText("请重新设置")

        self.machin_obj.main_beam.drill_box_grap_hand_relax_greater_part = parameter.get(
            "drill_box_grap_hand_relax_greater_part", None)  # 20 father thread can out
        if self.machin_obj.main_beam.drill_box_grap_hand_relax_greater_part == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_324.setText", "请重新设置"))

            # self.ui_window.pushButton_324.setText("请重新设置")

        self.machin_obj.main_beam.tiger_loose_time_ = parameter.get(
            "tiger_loose_time_", None)  # 20 father thread can out
        if self.machin_obj.main_beam.tiger_loose_time_ == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_121.setText", "请重新设置"))

            # self.ui_window.pushButton_121.setText("请重新设置")

        self.machin_obj.main_beam.tiger_tight_time_ = parameter.get(
            "tiger_tight_time_", None)  # 20 father thread can out
        if self.machin_obj.main_beam.tiger_tight_time_ == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.pushButton_120.setText", "请重新设置"))

            # self.ui_window.pushButton_120.setText("请重新设置")

        self.machin_obj.main_beam.tiger_tight_time_ = parameter.get(
            "tiger_tight_time_", None)  # 20 father thread can out
        if self.machin_obj.main_beam.no_load_move_to_coordinnate_point_max_pressure == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_34.setText", "请重新设置"))

            # self.ui_window.lineEdit_34.setText("请重新设置")

        if self.machin_obj.main_beam.no_load_move_start_level == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_37.setText", "请重新设置"))
            # self.ui_window.lineEdit_37.setText("请重新设置")

        if self.machin_obj.main_beam.no_load_move_end_level == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_38.setText", "请重新设置"))

            # self.ui_window.lineEdit_38.setText("请重新设置")

        if self.machin_obj.main_beam.no_load_move_parameter_contrl_distance == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_76.setText", "请重新设置"))

            # self.ui_window.lineEdit_76.setText("请重新设置")

        if self.machin_obj.main_beam.tiger_touch_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_89.setText", "请重新设置"))

            # self.ui_window.lineEdit_89.setText("请重新设置")

        if self.machin_obj.main_beam.beam_push_pull_in_tiger_step_distance == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_90.setText", "请重新设置"))

            # self.ui_window.lineEdit_90.setText("请重新设置")

        if self.machin_obj.main_beam.delta_contrast_beam_ruler_tiger_ruler == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_91.setText", "请重新设置"))

            # self.ui_window.lineEdit_91.setText("请重新设置")

        if self.machin_obj.main_beam.first_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_75.setText", "请重新设置"))

            # self.ui_window.lineEdit_75.setText("请重新设置")
        if self.machin_obj.main_beam.first_point_coordinate_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_79.setText", "请重新设置"))

            # self.ui_window.lineEdit_79.setText("请重新设置")
        if self.machin_obj.main_beam.first_point_coordinate_map_tiger_ruler_range == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_82.setText", "请重新设置"))

            # self.ui_window.lineEdit_82.setText("请重新设置")
        if self.machin_obj.main_beam.first_point_characteristic_success_value == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_109.setText", "请重新设置"))

            # self.ui_window.lineEdit_109.setText("请重新设置")



        if self.machin_obj.main_beam.second_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_77.setText", "请重新设置"))

            # self.ui_window.lineEdit_77.setText("请重新设置")
        if self.machin_obj.main_beam.second_point_coordinate_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_80.setText", "请重新设置"))

            # self.ui_window.lineEdit_80.setText("请重新设置")
        if self.machin_obj.main_beam.second_point_coordinate_map_tiger_ruler_range == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_84.setText", "请重新设置"))

            # self.ui_window.lineEdit_84.setText("请重新设置")

        if self.machin_obj.main_beam.taile_thread_is_ok_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_92.setText", "请重新设置"))
            # self.ui_window.lineEdit_92.setText("请重新设置")

        if self.machin_obj.main_beam.taile_thread_is_ok_point_coordinate_delat == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_93.setText", "请重新设置"))

            # self.ui_window.lineEdit_93.setText("请重新设置")
        if self.machin_obj.main_beam.taile_thread_is_ok_point_coordinate_map_tiger_ruler_range == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_94.setText", "请重新设置"))

            # self.ui_window.lineEdit_94.setText("请重新设置")



        if self.machin_obj.main_beam.fourth_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_78.setText", "请重新设置"))

            # self.ui_window.lineEdit_78.setText("请重新设置")


        if self.machin_obj.main_beam.fourth_point_coordinate_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_81.setText", "请重新设置"))

            # self.ui_window.lineEdit_81.setText("请重新设置")
        if self.machin_obj.main_beam.fouoint_coordinate_map_tiger_rurth_pler_range == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_85.setText", "请重新设置"))

            # self.ui_window.lineEdit_85.setText("请重新设置")

        if self.machin_obj.main_beam.Equepment_line_distance_measure_4m_beam.coordinate_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_110.setText", "请重新设置"))

            # self.ui_window.lineEdit_110.setText("请重新设置")
        if self.machin_obj.main_beam.Equepment_line_distance_measure_beam_taile.coordinate_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_111.setText", "请重新设置"))

            # self.ui_window.lineEdit_111.setText("请重新设置")

        if self.machin_obj.main_beam.Equepment_line_distance_measure_beam_head.coordinate_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_135.setText", "请重新设置"))

            # self.ui_window.lineEdit_135.setText("请重新设置")

        if self.machin_obj.main_beam.Equepment_line_distance_measure_dirll_box_updown.coordinate_delta == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_136.setText", "请重新设置"))

            # self.ui_window.lineEdit_136.setText("请重新设置")

        if self.machin_obj.main_beam.third_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_86.setText", "请重新设置"))

            # self.ui_window.lineEdit_86.setText("请重新设置")

        if self.machin_obj.main_beam.third_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_87.setText", "请重新设置"))

            # self.ui_window.lineEdit_87.setText("请重新设置")
        if self.machin_obj.main_beam.third_point_coordinate == None:
            ProcessSendOrderToWindowPipe.send(("ui_window.lineEdit_88.setText", "请重新设置"))

            # self.ui_window.lineEdit_88.setText("请重新设置")

    def set_angle_zero_correcting_angle(self, parameter):
        if parameter == ("angle_0_corectting", "zero_angle"):
            self.machin_obj.main_beam.angle_0_corectting = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
            self.remenber_parameter["angle_0_corectting"] =  self.machin_obj.main_beam.angle_0_corectting

    def set_drill_box_every_pole_power_distance(self, parameter):
        if parameter == ("dirll_box_inner_column_1_distance", ):
            self.box_pole_obj.box_power_distance[(1,1)] = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_2_distance", ):
            self.box_pole_obj.box_power_distance[(1,2)] = self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_3_distance", ):
            self.box_pole_obj.box_power_distance[(1,3)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_4_distance", ):
            self.box_pole_obj.box_power_distance[(1,4)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_5_distance", ):
            self.box_pole_obj.box_power_distance[(1,5)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_6_distance", ):
            self.box_pole_obj.box_power_distance[(1,6)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_7_distance", ):
            self.box_pole_obj.box_power_distance[(1,7)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_8_distance", ):
            self.box_pole_obj.box_power_distance[(1,8)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_9_distance", ):
            self.box_pole_obj.box_power_distance[(1,9)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_inner_column_10_distance", ):
            self.box_pole_obj.box_power_distance[(1,10)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_1_distance", ):
            self.box_pole_obj.box_power_distance[(2,1)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_2_distance", ):
            self.box_pole_obj.box_power_distance[(2,2)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_3_distance", ):
            self.box_pole_obj.box_power_distance[(2,3)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_4_distance", ):
            self.box_pole_obj.box_power_distance[(2,4)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_5_distance", ):
            self.box_pole_obj.box_power_distance[(2,5)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_6_distance", ):
            self.box_pole_obj.box_power_distance[(2,6)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_7_distance", ):
            self.box_pole_obj.box_power_distance[(2,7)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_8_distance", ):
            self.box_pole_obj.box_power_distance[(2,8)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_9_distance", ):
            self.box_pole_obj.box_power_distance[(2,9)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_middle_column_10_distance", ):
            self.box_pole_obj.box_power_distance[(2,10)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_1_distance", ):
            self.box_pole_obj.box_power_distance[(3,1)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_2_distance", ):
            self.box_pole_obj.box_power_distance[(3,2)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_3_distance", ):
            self.box_pole_obj.box_power_distance[(3,3)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_4_distance", ):
            self.box_pole_obj.box_power_distance[(3,4)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_5_distance", ):
            self.box_pole_obj.box_power_distance[(3,5)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_6_distance", ):
            self.box_pole_obj.box_power_distance[(3,6)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_7_distance", ):
            self.box_pole_obj.box_power_distance[(3,7)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_8_distance", ):
            self.box_pole_obj.box_power_distance[(3,8)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_9_distance", ):
            self.box_pole_obj.box_power_distance[(3,9)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle
        if parameter == ("dirll_box_outter_column_10_distance", ):
            self.box_pole_obj.box_power_distance[(3,10)]= self.machin_obj.main_beam.Equepment_angle_torque_to_pole.angle

    def set_hand_box_run_uncorecte_range(self, parameter, ProcessSendOrderToWindowPipe=None):
        ProcessSendOrderToWindowPipe = self.ProcessSendOrderToWindowPipe
        if parameter[0] == "hand_box_run_uncoreccte_rangge"  :
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.pole_point_delta  = parameter[1]
            # self.ui_window.ui_form_dirll_box_every_pole_distance.pushButton_118.setText("抓手位移误差" + str(parameter[1]))
            ProcessSendOrderToWindowPipe.send(("ui_form_dirll_box_every_pole_distance.pushButton_118.setText",
                                 "抓手位移误差" + str(parameter[1])))

            self.remenber_parameter["hand_box_run_uncoreccte_rangge"] = parameter[1]

    def set_drill_box_up_down_uncorrect_range(self, parameter, ProcessSendOrderToWindowPipe=None):
        ProcessSendOrderToWindowPipe = self.ProcessSendOrderToWindowPipe
        if parameter[0] == "drill_box_up_down_uncorecte_range":
            self.machin_obj.drill_box.Equepment_drill_box_digit_piont.pole_point_delta = parameter[1]

            # self.ui_window.ui_form_dirll_box_every_pole_distance.pushButton_119.setText(
            #         "钻箱上下误差" + str(parameter[1]))
            ProcessSendOrderToWindowPipe.send(("ui_window.ui_form_dirll_box_every_pole_distance.pushButton_119.setText",
                                 "钻箱上下误差" + str(parameter[1])))
            self.remenber_parameter["drill_box_up_down_uncorecte_range"] = parameter[1]

            # ("hand_box_run_uncoreccte_rangge", value)

            # ("hand_box_run_uncoreccte_rangge", value)

    def load_drill_box_data(self, load_data):
        ProcessSendOrderToWindowPipe = self.ProcessSendOrderToWindowPipe
        self.machin_obj.drill_box.Equepment_line_distance_measure_dirll_box_updown.coordinate_delta = load_data.get("drill_box_up_down_uncorecte_range",0)
        ProcessSendOrderToWindowPipe.send(("ui_window.ui_form_dirll_box_every_pole_distance.pushButton_119.setText",
                             "设置已经成功" + str(load_data.get("drill_box_up_down_uncorecte_range",0))))
        # self.ui_window.ui_form_dirll_box_every_pole_distance.pushButton_119.setText(
        #     "设置已经成功" + str(load_data.get("drill_box_up_down_uncorecte_range",0)))
        # self.ui_window.ui_form_dirll_box_every_pole_distance.horizontalSlider_2.setValue(
        #     load_data.get("hand_box_run_uncoreccte_rangge", 0))
        ProcessSendOrderToWindowPipe.send(("ui_window.ui_form_dirll_box_every_pole_distance.horizontalSlider_2",
                             "设置已经成功" + str(load_data.get("hand_box_run_uncoreccte_rangge", 0))))

        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.pole_point_delta = load_data.get("hand_box_run_uncoreccte_rangge", 0)
        # self.ui_window.ui_form_dirll_box_every_pole_distance.pushButton_118.setText("设置已经成功" + str(load_data.get("hand_box_run_uncoreccte_rangge", 0)))
        ProcessSendOrderToWindowPipe.send(("ui_window.ui_form_dirll_box_every_pole_distance.pushButton_118.setText",
                             "设置已经成功" + str(load_data.get("hand_box_run_uncoreccte_rangge", 0))))
        # self.ui_window.ui_form_dirll_box_every_pole_distance.horizontalSlider.setValue(load_data.get("hand_box_run_uncoreccte_rangge", 0))
        ProcessSendOrderToWindowPipe.send(("ui_window.ui_form_dirll_box_every_pole_distance.horizontalSlider",
                             "设置已经成功" + str(load_data.get("hand_box_run_uncoreccte_rangge", 0))))

        self.machin_obj.drill_box.Equepment_drill_box_digit_piont.drill_box_unstoppable_coordinate = load_data.get("point_unstop_beam", 0)