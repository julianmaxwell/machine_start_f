
    # if dict value is pin number ,it key must include "_pin"
    # if Equepment  dict   it ke must begin with  "Equepment_"
    #  key "ardiuno2560" and "raspberry"  is obj_name not class name
[board_obj]
    "ardiuno2560__": {
    "board_ports": "com4",
    "port_option_class": "ardiuno_pymata",

    "raspberry__": {
        "board_ports": "com2",
        "port_option_class": "ardiuno_pymata",

        }


[Equepment_obj]
    "Equepment_tigger_tooch_f": {
        "Equepment_class": "encode_push_pull",
        "A_pin": ('ardiuno2560__', 20, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "B_pin": ('ardiuno2560__', 21, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "Forward_pin": ('ardiuno2560__', 22, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "Backward_pin": ('ardiuno2560__', 23, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "puls": 16,
        "circumference_of_cycle": 9,
        "positive_point_end": 0,
        "stop_point": 100,
        "negative_point_end": 200,
        "encode_push_pull_stop_percent" : 0.65,
    },


    "Equepment_tigger_tooch_b": {
        "Equepment_class": "encode_push_pull",
        "A_pin": ('ardiuno2560__', 24, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "B_pin": ('ardiuno2560__', 25, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "Forward_pin": ('ardiuno2560__', 26, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "Backward_pin": ('ardiuno2560__', 27, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "pulse": 16,
        "circumference_of_cycle": 9,
        "positive_point": 0,
        "stop_point": 100,
        "negative_point": 200,
        "encode_push_pull_stop_percent" : 0.65,
        },


    "Equepment_tigger_drill": {
        "Equepment_class": "encode_push_pull",
        "A_pin": ('ardiuno2560__', 16, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "B_pin": ('ardiuno2560__', 17, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "Forward_pin": ('ardiuno2560__', 18, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "Backward_pin": ('ardiuno2560__', 19, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "pulse": 16,
        "circumference_of_cycle": 9,
        "positive_point_end": 0,
        "stop_point": 100,
        "negative_point_end": 200,
        "encode_push_pull_stop_percent": 0.65,
        },

    "Equepment_pole_push_pull": {
        "Equepment_class": "encode_push_pull",
        "A_pin": ('ardiuno2560__', 12, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "B_pin": ('ardiuno2560__', 13, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "Forward_pin": ('ardiuno2560__', 14, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "Backward_pin": ('ardiuno2560__', 15, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "pulse": 16,
        "circumference_of_cycle": 9,
        "positive_point_end": 0,
        "stop_point": 100,
        "negative_point_end": 200,
        "encode_push_pull_stop_percent": 0.65,
        },
    "Equepment_pole_dirll": {
        "Equepment_class": "encode_push_pull",
        "A_pin": ('ardiuno2560__', 47, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "B_pin": ('ardiuno2560__', 48, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "Forward_pin": ('ardiuno2560__', 49, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "Backward_pin": ('ardiuno2560__', 50, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "pulse": 16,
        "circumference_of_cycle": 9,
        "positive_point_end": 0,
        "stop_point": 100,
        "negative_point_end": 200,
        "encode_push_pull_stop_percent": 0.65,
        },
    "Equepment_warter_deep_measure": {
        "Equepment_class": "water_deep",

        "warter_deep_pin": ('ardiuno2560__', 0, 'ANALOG', 'INPUT', 'ardiuno2560')
        },
    "Equepment_line_distance_measure_4m_beam": {
        "Equepment_class": "line_distance",

        "recve_pin": ('ardiuno2560__', 1, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_distance": 4000,
        "_init_zero_data" : None,
        "max_distance_data" : None
        },
    "Equepment_line_distance_measure_1m_drill_box": {
        "Equepment_class": "line_distance",
        "recve_pin": ('ardiuno2560__', 2, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_distance": 1000,
        "_init_zero_data" : None,
        "max_distance_data" : None
        },
    "Equepment_line_distance_measure_beam_taile": {
        "Equepment_class": "line_distance",
        "recve_pin": ('ardiuno2560__', 3, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_distance": 200,
        "_init_zero_data": None,
        "max_distance_data" : None
        },
    "Equepment_line_distance_measure_beam_head": {
        "Equepment_class": "line_distance",
        "recve_pin": ('ardiuno2560__', 4, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_distance": 200,
        "_init_zero_data": None,
        "max_distance_data" : None

        },
    "Equepment_line_distance_measure_dirll_box_updown": {
        "Equepment_class": "line_distance",
        "recve_pin": ('ardiuno2560__', 5, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_distance": 200,
        "_init_mini_data": None,
        "max_distance_data" : None
        },
    "Equepment_pressure_warter": {
        "Equepment_class": "pressure_measure",
        "recve_pin": ('ardiuno2560__', 6, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_range":16
        },
    "Equepment_pressure_push_pull": {
        "Equepment_class": "pressure_measure",
        "recve_pin": ('ardiuno2560__', 7, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_range": 40

        },
    "Equepment_pressure_torque": {
        "Equepment_class": "pressure_measure",
        "recve_pin": ('ardiuno2560__', 8, 'ANALOG', 'INPUT', 'ardiuno2560'),
        "measure_range":40
        },
    "Equepment_angle_torque_to_pole": {
        "Equepment_class": "angle_torque",
        "recve_pin": ('ardiuno2560__', 9, 'ANALOG', 'INPUT', 'ardiuno2560')
        },

    "Equepment_main_beam_obj": {
        "Equepment_class": "main_beam_position",
        "main_beam_last_pole_up_down_expangd_hole": ('ardiuno2560__', 38, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "push_pull_quicken_pin": ('ardiuno2560__', 29, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "torque_quicken_pin": ('ardiuno2560__', 30, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "Equepment_main_beam_taile_5cm_pin": ('ardiuno2560__', 34, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "main_beam_box_can_back_pole_pin": ('ardiuno2560__', 35, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "main_beam_from_tiger_tooth_5cm_pin": ('ardiuno2560__', 36, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "main_beam_tiger_tooth_middle_pin": ('ardiuno2560__', 37, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_water_open_close_pin": ('ardiuno2560__', 7, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),


        },
    "Equepment_lamp_light":{
        "Equepment_class": "lamp_",
        "middle_lamp_pin": ('ardiuno2560__', 8, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "top_lamp_pin": ('ardiuno2560__', 11, 'DIGITAL', 'OUTPUT', 'ardiuno2560')
        },
    "Equepment_warning_light" :{
        "Equepment_class": "warning_lamp",
        "warning_sound_pin": ('ardiuno2560__', 28, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "yelow_ready_pin": ('ardiuno2560__', 31, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "_green_ok_pin": ('ardiuno2560__', 32, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "red_back_pin": ('ardiuno2560__', 33, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        },
    "Equepment_drill_box_digit_piont": {
        "Equepment_class": "drill_box",
        "pole_box_has_uped_pin":('ardiuno2560__', 42, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_has_down_pin":('ardiuno2560__', 43, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_has_down_can_grip_pin":('ardiuno2560__', 44, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_1_point_pin": ('ardiuno2560__', 39, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_2_point_pin": ('ardiuno2560__', 40, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_3_point_pin": ('ardiuno2560__', 41, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_arm_forward_pin":('ardiuno2560__', 1, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_arm_backward_pin": ('ardiuno2560__', 2, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_hand_grip_pin": ('ardiuno2560__', 3, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_hand_relax_pin": ('ardiuno2560__', 4, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "pole_box_down_pin": ('ardiuno2560__', 5, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "pole_box_up_pin": ('ardiuno2560__', 6, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        "beam_taile_hand_pin": ('ardiuno2560__', 45, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "beam_forward_hand_pin": ('ardiuno2560__', 46, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "box_point1_pin_new": ('ardiuno2560__', 9, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "box_point2_pin_new": ('ardiuno2560__', 10, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "box_point3_pin_new": ('ardiuno2560__', 51, 'DIGITAL', 'INPUT', 'ardiuno2560'),
        "point1_coordinate" : 120,
        "point2_coordinate" : 240,
        "point3_coordinate" : 360,
        "drill_box_unstoppable_coordinate": 410,
        "can_hold_beam_pole_coordinate": 920,
        },
        },

