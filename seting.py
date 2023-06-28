import pickle
import struct
import pandas
baudrate_485 = 9600
bytesize = 8
parity = 'N'
stopbits = 1
xonxoff = 0
port_time_out = 0.01
listen_port = ("127.0.0.1", 7500)
local_host = "127.0.0.1"
send_defalut_target_port = ("127.0.0.50", 9000)
first_recev_data_buffer = 4
normal_buffer = 1024
modbus_rtu_485_xiAnZz8SlaveId = 1
modbus_rtu_485_xiAnZz12SlaveId = 4
modbus_rtu_485_WeiTeAngleSensorSlaveId = 80
modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId = 5
modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64SlaveId = 6
modbus485__2_MainBeam_4mRopeEncodeSlaveId = 2
modbus485__2_BoxHand1mRopeEncodeSlaveId = 3
modbus485__2board_ports = "com4"
modbus485__board_ports = "com5"
ardiuno2560__board_ports = "com3"
parameter_load_path = "parameter_backup_data.tex"


parameter_load_data = {}
parameter_load_data1 = pandas.read_csv("D:\machine\机器端\mmmmmmmmmmm.csv")
data_frame3 = pandas.read_csv(r"D:\machine\机器端\nnnnnn.csv", encoding="gbk")
data_machine_empty_recorde_pandas = pandas.DataFrame([], columns=data_frame3.columns)

def evelv_type(data):
    try:
        data = eval(data)
        # print(data, type(data))
    except Exception:
        data = data
    return data

def get_dict_parameter():
    parameter_load_data1 = pandas.read_csv("D:\machine\机器端\mmmmmmmmmmm.csv")
    parameter_load_data1.loc[:, 'Unnamed: 0'] = parameter_load_data1.loc[:, 'Unnamed: 0'].apply(evelv_type)
    parameter_load_data1.loc[:, '0'] = parameter_load_data1.loc[:, '0'].apply(evelv_type)
    # print(parameter_load_data1.loc[:, 'Unnamed: 0'])
    # print(parameter_load_data1.loc[:, '0'])
    new_ = pandas.Series(parameter_load_data1.loc[:, "0"].values,
                         index=parameter_load_data1.loc[:, 'Unnamed: 0'].values)
    parameter_load_data = new_.to_dict()
    return parameter_load_data

parameter_load_data = get_dict_parameter()
parameter_load_data_Series = pandas.Series(parameter_load_data)

machine_recorde_data = pandas.read_csv("D:\machine\机器端\mmmmmmmmmmm.csv")
machine_recorde_data_index = machine_recorde_data.index
del machine_recorde_data

# print(parameter_load_data)
# print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm  ", type(new_))
"""
format is "machine_one" : {
                            port1_obj  __ "ardiuno2560__":{


machine_one is the port name_obj,   
        "board_ports": "com3",
        "port_option_class": "ardiuno_pymata",
        "timed_out": 0.001,
        up is the  port default attr
        
         Equepment_tigger_tooch_f is the child equepment  map every class has time_out attr , if hasnt, time_out = port.timed_out
        
"""

"""""# if dict value is pin number ,it key must include "_pin"
  # if Equepment  dict   it ke must begin with  "Equepment_"
  #  key "ardiuno2560" and "raspberry"  is obj_name not class name"""""
# every port map a obj and a class to run .

# coordinate_start = parameter_load_data[('Equepment_tigger_tooch_f', 'start')]

machine_one = {
    "ardiuno2560__": {
        "board_class": "ardiuno2560",
        "board_class_file": "ardiuno_board.py",
        "board_ports": ardiuno2560__board_ports,
        "port_option_class": "ardiuno2560",
        "port_obj_name": "ardiuno2560__",
        "timed_out": 0.001,
        "Equepment_tigger_tooch_f": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_tigger_tooch_f",
            "Forward_pin": ('ardiuno2560__', 22, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 23, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 14, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "stop_point": parameter_load_data[('Equepment_tigger_tooch_f', 'stop')],
            "coordinate_start": parameter_load_data[('Equepment_tigger_tooch_f', 'start')],

            "coordinate_end": parameter_load_data[('Equepment_tigger_tooch_f', 'end')],
        },
        "Equepment_tigger_tooch_b": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_tigger_tooch_b",
            "Forward_pin": ('ardiuno2560__', 26, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 27, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 13, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "coordinate_start": parameter_load_data[('Equepment_tigger_tooch_b', 'start')],
            "stop_point": parameter_load_data[('Equepment_tigger_tooch_b', 'stop')],
            "coordinate_end": parameter_load_data[('Equepment_tigger_tooch_b', 'end')],

        },
        "Equepment_tigger_drill": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_tigger_drill",
            "Forward_pin": ('ardiuno2560__', 18, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 19, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 10, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "coordinate_start": parameter_load_data[('Equepment_tigger_drill', 'start')],
            "stop_point": parameter_load_data[('Equepment_tigger_drill', 'stop')],
            "coordinate_end": parameter_load_data[('Equepment_tigger_drill', 'end')],

        },
        "Equepment_pole_push_pull": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_pole_push_pull",
            "Forward_pin": ('ardiuno2560__', 14, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 15, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 12, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "coordinate_start": parameter_load_data[('Equepment_pole_push_pull', 'start')],
            "stop_point": parameter_load_data[('Equepment_pole_push_pull', 'stop')],
            "coordinate_end": parameter_load_data[('Equepment_pole_push_pull', 'end')],
        },
        "Equepment_pole_dirll": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_pole_dirll",
            "Forward_pin": ('ardiuno2560__', 49, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 50, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 11, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "coordinate_start": parameter_load_data[('Equepment_pole_dirll', 'start')],
            "stop_point": parameter_load_data[('Equepment_pole_dirll', 'stop')],
            "coordinate_end": parameter_load_data[('Equepment_pole_dirll', 'end')],
        },
        "Equepment_warter_deep_measure": {
            "Equepment_class": "water_deep",
            "shebei_name": "Equepment_warter_deep_measure",
            "warter_deep_pin": ('ardiuno2560__', 0, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "warter_deep_safe": 13
        },
        "Equepment_line_distance_measure_4m_beam": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_4m_beam",
            "recve_pin": ('ardiuno2560__', 1, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_distance": 4000,
            "_init_zero_data": 0,
            "max_distance_data": 0.001
        },
        "Equepment_line_distance_measure_1m_drill_box": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_1m_drill_box",
            "recve_pin": ('ardiuno2560__', 2, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_distance": 1000,
            "_init_zero_data": 0,
            "max_distance_data": 0.001
        },
        "Equepment_line_distance_measure_beam_taile": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_beam_taile",
            "recve_pin": ('ardiuno2560__', 3, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_distance": 200,
            "_init_zero_data": 0,
            "max_distance_data": 0.001
        },
        "Equepment_line_distance_measure_beam_head": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_beam_head",
            "recve_pin": ('ardiuno2560__', 4, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_distance": 200,
            "_init_zero_data": 0,
            "max_distance_data" : 0.001

        },
        "Equepment_line_distance_measure_dirll_box_updown": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_dirll_box_updown",
            "recve_pin": ('ardiuno2560__', 5, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_distance": 200,
            "_init_zero_data": 0,
            "max_distance_data": 0.001
        },
        "Equepment_pressure_warter": {
            "Equepment_class": "pressure_measure",
            "shebei_name": "Equepment_pressure_warter",
            "recve_pin": ('ardiuno2560__', 6, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_range":16
        },
        "Equepment_pressure_push_pull": {
            "Equepment_class": "pressure_measure",
            "shebei_name": "Equepment_pressure_push_pull",

            "recve_pin": ('ardiuno2560__', 7, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_range": 40

        },
        "Equepment_pressure_torque": {
            "Equepment_class": "pressure_measure",
            "shebei_name": "Equepment_pressure_torque",
            "recve_pin": ('ardiuno2560__', 8, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_range":40
        },
        "Equepment_angle_torque_to_pole": {
            "Equepment_class": "angle_torque",
            "shebei_name": "Equepment_angle_torque_to_pole",
            "recve_pin": ('ardiuno2560__', 9, 'ANALOG', 'INPUT', 'ardiuno2560')
        },

        "Equepment_main_beam_obj": {
            "Equepment_class": "main_beam_position",
            "shebei_name": "Equepment_main_beam_obj",
            "main_beam_last_pole_up_down_expangd_hole": ('ardiuno2560__', 38, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "push_pull_quicken_pin": ('ardiuno2560__', 29, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "torque_quicken_pin": ('ardiuno2560__', 30, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "Equepment_main_beam_taile_5cm_pin": ('ardiuno2560__', 34, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "main_beam_box_can_back_pole_pin": ('ardiuno2560__', 35, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "main_beam_from_tiger_tooth_5cm_pin": ('ardiuno2560__', 36, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "main_beam_tiger_tooth_middle_pin": ('ardiuno2560__', 37, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_water_open_close_pin": ('ardiuno2560__', 7, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),


        },
        "Equepment_lamp_light": {
            "Equepment_class": "lamp_",
            "shebei_name": "Equepment_lamp_light",
            "middle_lamp_pin": ('ardiuno2560__', 8, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "top_lamp_pin": ('ardiuno2560__', 11, 'DIGITAL', 'OUTPUT', 'ardiuno2560')
        },
        "Equepment_warning_light": {
                "Equepment_class": "warning_lamp",
                "shebei_name": "Equepment_warning_light",
                "warning_sound_pin": ('ardiuno2560__', 28, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
                "yelow_ready_pin": ('ardiuno2560__', 31, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
                "_green_ok_pin": ('ardiuno2560__', 32, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
                "red_back_pin": ('ardiuno2560__', 33, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        },
        "Equepment_drill_box_digit_piont": {
                    "Equepment_class": "drill_box",
                    "shebei_name": "Equepment_drill_box_digit_piont",
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
                    "box_point1_pin": ('ardiuno2560__', 9, 'DIGITAL', 'INPUT', 'ardiuno2560'),
                    "box_point2_pin": ('ardiuno2560__', 10, 'DIGITAL', 'INPUT', 'ardiuno2560'),
                    "box_point3_pin": ('ardiuno2560__', 51, 'DIGITAL', 'INPUT', 'ardiuno2560'),
                    "point1_coordinate": 120,
                    "point2_coordinate": 240,
                    "point3_coordinate": 360,
                    "drill_box_unstoppable_coordinate": 410,
                    "box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole": 760,
                    "can_hold_beam_pole_coordinate": 920,

                },
    },

    "modbus485__": {

        # the "_pin" in the obj of Equipment name is must  program use it to distinguish the read equipment every circle
        "board_ports": modbus485__board_ports,
        "board_class": "get_master",  # is a function  return a class_obj  modbus485
        "board_class_file": "testk.py",
        "port_option_class": "modbus485",
        "port_obj_name": "modbus485__",
        "class_file_name": "ardiuno_board.py",
        "port_time_out": 0.01,
        "baudrate": baudrate_485,
        "bytesize": bytesize,
        "parity": parity,
        "stopbits": stopbits,
        "xonxoff": 0,
        "Equepment_modbus_expand_part12_anolog_chanel_": {
            # note:  西安舟正 equipment must set its slave id use it"s self soft
                    "Equepment_class": "modbus_rtu_485_xiAnZz12",
                    "port_obj_name": "modbus485__",
                    "single_io_type": 'OUTPUT',
                    "single_dig_type": 'ANALOG',
                    "shebei_name": "Equepment_modbus_expand_part12_anolog_chanel_",
                    "Write_code": None,
                    "Read_code": "04040000000C",
        # slave_id 01   operation_code 04, start_addr HIGH  00  start_addr LOW 00, route_number High 00, route_number Low  0C.
                    "set_code": None,
                    "slave_id": modbus_rtu_485_xiAnZz12SlaveId,
                    "first_addr_id": 0,
                    "start_addr": 0,
                    "date_len": 12,
                    "operation_code": 4,

                    "baudrate": baudrate_485,
                    "bytesize": bytesize,
                    "parity": parity,
                    "stopbits": stopbits,
                    "xonxoff": xonxoff,
                    "manager_port_number": 12,
                    "product_name": "西安舟正12anolog_12bit",
                    "explain_function": "calclude_anlog_12_8_read",
                    "explain_function_path": "textk.py",
                    "virtual_pin": {
                    "modbus_rtu_485_xiAnZz12_0_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 0), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_1_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 1), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_2_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 2), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_3_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 3), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_4_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 4), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_5_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 5), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_6_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 6), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_7_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 7), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_8_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 8), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_9_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 9), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_10_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 10), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    "modbus_rtu_485_xiAnZz12_11_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 11), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
                    },
                    "scan_time": 0.01,

                },
        "Equepment_modbus_expand_part8_anolog_chanel_": {
        # note:  西安舟正 equipment must set its slave id use it"s self soft
                    "Equepment_class": "modbus_rtu_485_xiAnZz8",
                    "port_obj_name": "modbus485__",
                    "single_io_type": 'OUTPUT',
                    "single_dig_type": 'ANALOG',
                    "shebei_name": "Equepment_modbus_expand_part8_anolog_chanel_",
                    "Equepment_class_path": "ardiuno_board.py",
                    "Write_code": None,
        # slave_id 01   operation_code 04, start_addr HIGH  00  start_addr LOW 00, route_number High 00, route_number Low  0C.
                    "Read_code": "010400000008",
                    "set_code": None,

        # slave_id 02   operation_code 10, start_addr HIGH  00  start_addr LOW 14, register_number High 00, register_number Low  01.
                    # will write bytes number 02, DATA will write content is 0001      it"s means slave id from 2 change to 1
                    "slave_id": modbus_rtu_485_xiAnZz8SlaveId,
                    "first_addr_id": "0000",
                    "start_addr": 0,
                    "date_len": 8,
                    "operation_code": 4,
                    "baudrate": baudrate_485,
                    "bytesize": bytesize,
                    "parity": parity,
                    "stopbits": stopbits,
                    "xonxoff": xonxoff,
                    "manager_port_number": 8,
                    "product_name": "西安舟正8anolog_16bit",
                    "explain_function": "calclude_anlog_12_8_read",
                    "explain_function_path": "textk.py",
                    "scan_time": 0.01,
                    "virtual_pin": {
                        "modbus_rtu_485_xiAnZz8_0_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 0), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                        "modbus_rtu_485_xiAnZz8_1_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 1), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                        "modbus_rtu_485_xiAnZz8_2_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 2), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                        "modbus_rtu_485_xiAnZz8_3_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 3), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                        "modbus_rtu_485_xiAnZz8_4_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 4), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                        "modbus_rtu_485_xiAnZz8_5_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 5), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                        "modbus_rtu_485_xiAnZz8_6_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 6), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                        "modbus_rtu_485_xiAnZz8_7_pin": (
                            'modbus485__', (modbus_rtu_485_xiAnZz8SlaveId, 7), 'ANALOG', 'OUTPUT',
                            'modbus_rtu_485_xiAnZz8'),
                    },


                },

        "Equepment_modbus_expand_part_Beam_ganle_check": {
            # note: 模块的 modbus 通信地址默认为 0x50，可以通过软件更改。
            "Equepment_class": "modbus_rtu_485_WeiTeAngleSensor",
            "port_obj_name": "modbus485__",
            "shebei_name": "Equepment_modbus_expand_part_Beam_ganle_check",
            "single_io_type": 'OUTPUT',
            "single_dig_type": 'ANALOG',
            "Write_code": None,
            "Read_code": "5003003d0003",
            "set_code": None,
            "slave_id": modbus_rtu_485_WeiTeAngleSensorSlaveId,  # int is 80
            "first_addr_id": "003d",
            "start_addr": 0,
            "date_len": 3,
            "operation_code": 3,
            "manager_port_number": 1,
            "baudrate": baudrate_485,
            "bytesize": bytesize,
            "parity": parity,
            "stopbits": stopbits,
            "xonxoff": xonxoff,
            "product_name": "维特智能 SINDT 倾角传感器",
            "explain_function": "calclude_angle",
            "explain_function_path": "testk.py",
            "scan_time": 0.01,
            "virtual_pin": {
                "modbus_rtu_485_WeiTeAngleSensor_pin": (
                    'modbus485__', (modbus_rtu_485_WeiTeAngleSensorSlaveId, 0), 'ANALOG', 'OUTPUT',
                    'modbus_rtu_485_WeiTeAngleSensor'),
            },


        },
        "Equepment_modbus_expand_part_drill_box_hand_operation": {
            # note: 模块的 modbus 通信地址set by the bottom on the equipment reset。
            "Equepment_class": "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8",
            "port_obj_name": "modbus485__",
            "shebei_name": "Equepment_modbus_expand_part_drill_box_hand_operation",
            "single_io_type": 'INPUT',
            "single_dig_type": 'DIGITAL',
            "Write_code": "0505000001",  # value tail must add the content you want to write
            "Read_code": None,
            "set_code": None,
            "slave_id": modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId,
            "first_addr_id": "0000",
            "start_addr": 0,
            "date_len": 1,
            "operation_code": 5,
            "manager_port_number": 1,
            "baudrate": baudrate_485,
            "bytesize": bytesize,
            "parity": parity,
            "stopbits": stopbits,
            "xonxoff": xonxoff,
            "product_name": "欧姆龙8路485数字开关",
            "explain_function": None,
            "scan_time": 0.01,
            "virtual_pin": {
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_0_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 0), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_1_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 1), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_2_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 2), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_3_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 3), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_4_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 4), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_5_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 5), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_6_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 6), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),
                "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_7_pin": (
                'modbus485__', (modbus_rtu_485_DrillBoxHandOperatioOuMuLong8SlaveId, 7), 'DIGITAL', 'INPUT',
                    'modbus_rtu_485_DrillBoxHandOperatioOuMuLong8'),

            },


        },
        "Equepment_modbus_expand_part_main_beam_4m_abs_encode": {
            # note: 模块的 modbus 通信地址set by the bottom on the equipment reset。
            # here not use it temporary. here use it only for backups.
            "Equepment_class": "modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64",
            "port_obj_name": "modbus485__",
            "single_io_type": 'OUTPUT',
            "single_dig_type": 'ANALOG',
            "shebei_name": "Equepment_modbus_expand_part_main_beam_4m_abs_encode",

            "Write_code": None,
            # "the "Write_code" must see the description for detail. must use the yellow line or red line on equipment.
            "Read_code": "060300030002",
            # know the "read_code" struct must see the description for details
            "set_code": "010600010006",
            # slave_id from 0001 change to 0006
            # be careful the default translate speed is 19200, not 9600  must set it before use .
            # the set code is : 01060000 0004   set 9600
            "slave_id": modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64SlaveId,  # this is not use
            "first_addr_id": "0003",
            "start_addr": 3,
            "date_len": 2,
            "operation_code": 3,
            "manager_port_number": 1,
            "baudrate": baudrate_485,
            "bytesize": bytesize,
            "parity": parity,
            "stopbits": stopbits,
            "xonxoff": xonxoff,
            "product_name": "无锡邦赫多圈绝对值旋转编码器64圈",
            "explain_function": "calcludej_back_encode_test",
            "explain_function_path": "testk.py",
            "scan_time": 0.01,
            "virtual_pin": {
                "modbus_rtu_485MainBeam4mAbsEncode_pin": (
                    'modbus485__', (modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64SlaveId, 0), 'ANALOG', 'OUTPUT',
                    'modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64'),
            },

        },
    },

    "modbus485__2": {
        # the "_pin" in the obj of Equipment name is must  program use it to distinguish the read equipment every circle
        "board_ports": modbus485__2board_ports,
        "board_class": "get_master",  # a function  return a class_obj  it used  in port_option_class, here only a note
        "board_class_file": "testk.py",
        "port_option_class": "modbus485",
        "port_obj_name": "modbus485__2",
        "class_file_name": "ardiuno_board.py",
        "baudrate": baudrate_485,
        "bytesize": bytesize,
        "parity": parity,
        "stopbits": stopbits,
        "xonxoff": xonxoff,
        "port_time_out": port_time_out,


        "Equepment_modbus_expand_part_Beam4m_rope_encode": {
            "Equepment_class": "modbus_rtu_485Beam4mRopeEncodeXiYuWeiYiSensor",
            "port_obj_name": "modbus485__2",
            "single_io_type": 'OUTPUT',
            "single_dig_type": 'ANALOG',
            "Write_code": None,
            # slave_id 01   operation_code 04, start_addr HIGH  00  start_addr LOW 00,
            # route_number High 00, route_number Low  0C.
            "Read_code": "0204000C0002",
            "set_code": "021000140001020001",
            # slave_id 02   operation_code 10, start_addr HIGH  00  start_addr LOW 14, register_number High 00, register_number Low  01.
            # will write bytes number 02, DATA will write content is 0001      it"s means slave id from 2 change to 1
            "slave_id": modbus485__2_MainBeam_4mRopeEncodeSlaveId,
            "first_addr_id": "000C",
            "start_addr": 8,
            "shebei_name": "Equepment_modbus_expand_part_Beam4m_rope_encode",

            "date_len": 2,
            "operation_code": 3,
            "baudrate": baudrate_485,
            "bytesize": bytesize,
            "parity": parity,
            "stopbits": stopbits,
            "xonxoff": xonxoff,
            "manager_port_number": 1,
            "product_name": "西域位移传感器WPS-M-5000-AS",
            "explain_function": "calclude_encode_distance",
            "explain_function_path": "testk.py",
            "scan_time": 0.001,
            "virtual_pin": {
                "modbus485__2_MainBeam_4mRopeEncode_pin": (
                    'modbus485__2', (modbus485__2_MainBeam_4mRopeEncodeSlaveId, 0), 'ANALOG', 'OUTPUT',
                    'modbus_rtu_485Beam4mRopeEncodeXiYuWeiYiSensor'),

            },



        },
        "Equepment_modbus_expand_part_box_hand1m_rope_encode": {
            "Equepment_class": "modbus485__2_BoxHand1mRopeEncode",
            "port_obj_name": "modbus485__2",
            "single_io_type": 'OUTPUT',
            "single_dig_type": 'ANALOG',
            "shebei_name": "Equepment_modbus_expand_part_box_hand1m_rope_encode",
            "Write_code": None,
            # slave_id 01   operation_code 04, start_addr HIGH  00  start_addr LOW 00,
            # route_number High 00, route_number Low  0C.
            "Read_code": "0304000C0002",
            "set_code": "031000140001020001",
            # slave_id 03   operation_code 10, start_addr HIGH  00  start_addr LOW 14,
            # register_number High 00, register_number Low  01.
            # will write bytes number 02, DATA will write content is 0001      it"s means slave id from 03 change to 1
            "slave_id": modbus485__2_BoxHand1mRopeEncodeSlaveId,
            "first_addr_id": "000C",
            "start_addr": 8,
            "date_len": 2,
            "operation_code": 3,
            "baudrate": baudrate_485,
            "bytesize": bytesize,
            "parity": parity,
            "stopbits": stopbits,
            "xonxoff": xonxoff,
            "manager_port_number": 1,
            "product_name": "西域位移传感器WPS-M-1000-AS",
            "explain_function": "calclude_encode_distance",
            "explain_function_path": "testk.py",
            "scan_time": 0.01,
            "virtual_pin": {
                "modbus485__2_BoxHand1mRopeEncode_pin": (
                    'modbus485__2', (modbus485__2_BoxHand1mRopeEncodeSlaveId, 0), 'ANALOG', 'OUTPUT',
                    'modbus485__2_BoxHand1mRopeEncode'),
            },


        },

    },

    "virtual_equepment": {
        "Equepment_tigger_tooch_f": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_tigger_tooch_f",
            "Forward_pin": ('ardiuno2560__', 22, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 23, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 14, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus_rtu_485_xiAnZz12_0_pin": ('modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 0), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
            "coordinate_start": parameter_load_data[("Equepment_tigger_tooch_f", "start")][2],
            "coordinate_stop": parameter_load_data[("Equepment_tigger_tooch_f", "stop")][2],
            "coordinate_end": parameter_load_data[("Equepment_tigger_tooch_f", "end")][2],
        },
        "Equepment_tigger_tooch_b": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_tigger_tooch_b",
            "Forward_pin": ('ardiuno2560__', 26, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 27, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 13, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus_rtu_485_xiAnZz12_0_pin": (
                    'modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 1), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
            "coordinate_start": parameter_load_data[("Equepment_tigger_tooch_b", "start")][2],
            "coordinate_stop": parameter_load_data[("Equepment_tigger_tooch_b", "stop")][2],
            "coordinate_end": parameter_load_data[("Equepment_tigger_tooch_b", "end")][2],
        },
        "Equepment_tigger_drill": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_tigger_drill",
            "Forward_pin": ('ardiuno2560__', 18, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 19, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 10, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus_rtu_485_xiAnZz12_0_pin": (
                    'modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 2), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
            "coordinate_start": parameter_load_data[("Equepment_tigger_drill", "start")][2],
            "coordinate_stop": parameter_load_data[("Equepment_tigger_drill", "stop")][2],
            "coordinate_end": parameter_load_data[("Equepment_tigger_drill", "end")][2],
        },
        "Equepment_pole_push_pull": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_pole_push_pull",
            "Forward_pin": ('ardiuno2560__', 14, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 15, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 12, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus_rtu_485_xiAnZz12_0_pin": (
                'modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 3), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
# coordinate_stop = old_parameter_load_data[(equepment_obj_name, "stop")][2]
            "coordinate_start": parameter_load_data[("Equepment_pole_push_pull", "start")][2],
            "coordinate_stop": parameter_load_data[("Equepment_pole_push_pull", "stop")][2],
            "coordinate_end": parameter_load_data[("Equepment_pole_push_pull", "end")][2],

        },
        "Equepment_pole_dirll": {
            "Equepment_class": "push_pull_rocker_arm",
            "shebei_name": "Equepment_pole_dirll",
            "Forward_pin": ('ardiuno2560__', 49, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "Backward_pin": ('ardiuno2560__', 50, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "recve_pin": ('ardiuno2560__', 11, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus_rtu_485_xiAnZz12_0_pin": (
                'modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 4), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
            "coordinate_start": parameter_load_data[("Equepment_pole_dirll", "start")][2],
            "coordinate_stop": parameter_load_data[("Equepment_pole_dirll", "stop")][2],
            "coordinate_end": parameter_load_data[("Equepment_pole_dirll", "end")][2],
        },
        "Equepment_warter_deep_measure": {
            "Equepment_class": "water_deep",
            "shebei_name": "Equepment_warter_deep_measure",
            "warter_deep_pin": ('ardiuno2560__', 0, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "warter_deep_safe": parameter_load_data["warter_deep_safe"],
        },
        "Equepment_line_distance_measure_4m_beam": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_4m_beam",
            "recve_pin": ('ardiuno2560__', 1, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus485__2_MainBeam_4mRopeEncode_pin": (
                'modbus485__2', (modbus485__2_MainBeam_4mRopeEncodeSlaveId, 0), 'ANALOG', 'OUTPUT',
                'modbus_rtu_485Beam4mRopeEncodeXiYuWeiYiSensor'),

        "modbus_rtu_485_DrillBoxHandOperatioOuMuLong8S_pin": (
                    'modbus485__', (modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64SlaveId, 0), 'ANALOG', 'OUTPUT',
                    'modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64'),
            "beam_begin": parameter_load_data["beam_head_coordinate"],
            "beam_end": parameter_load_data["beam_tail_coordinate"],
            "max_distance_data": 0.001
        },
        "Equepment_line_distance_measure_1m_drill_box": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_1m_drill_box",
            "recve_pin": ('ardiuno2560__', 2, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus485__2_BoxHand1mRopeEncode_pin": (
                    'modbus485__2', (modbus485__2_BoxHand1mRopeEncodeSlaveId, 0), 'ANALOG', 'OUTPUT',
                    'modbus485__2_BoxHand1mRopeEncode'),
            "hand_box_unstop_beam_driving_coordinate": parameter_load_data["hand_box_unstop_beam_driving_coordinate"],

            "measure_distance": 1000,
            "_init_zero_data": 0,
            "max_distance_data": 0.001
        },
        "Equepment_line_distance_measure_beam_taile": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_beam_taile",
            "recve_pin": ('ardiuno2560__', 3, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus_rtu_485_xiAnZz12_0_pin": (
                'modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 5), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
            "measure_distance": 200,
            "_init_zero_data": 0,
            "max_distance_data": 0.001
        },
        "Equepment_line_distance_measure_beam_head": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_beam_head",
            "recve_pin": ('ardiuno2560__', 4, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "modbus_rtu_485_xiAnZz12_0_pin": (
                'modbus485__', (modbus_rtu_485_xiAnZz12SlaveId, 6), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12'),
            "measure_distance": 200,
            "_init_zero_data": 0,
            "max_distance_data": 0.001

        },
        "Equepment_line_distance_measure_dirll_box_updown": {
            "Equepment_class": "line_distance",
            "shebei_name": "Equepment_line_distance_measure_dirll_box_updown",
            "recve_pin": ('ardiuno2560__', 5, 'ANALOG', 'INPUT', 'ardiuno2560'),

            "measure_distance": 200,
            "_init_zero_data": 0,
            "max_distance_data": 0.001
        },
        "Equepment_pressure_warter": {
            "Equepment_class": "pressure_measure",
            "shebei_name": "Equepment_pressure_warter",
            "recve_pin": ('ardiuno2560__', 6, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_range": 16
        },
        "Equepment_pressure_push_pull": {
            "Equepment_class": "pressure_measure",
            "shebei_name": "Equepment_pressure_push_pull",

            "recve_pin": ('ardiuno2560__', 7, 'ANALOG', 'INPUT', 'ardiuno2560'),

            "measure_range": 40

        },
        "Equepment_pressure_torque": {
            "Equepment_class": "pressure_measure",
            "shebei_name": "Equepment_pressure_torque",
            "recve_pin": ('ardiuno2560__', 8, 'ANALOG', 'INPUT', 'ardiuno2560'),
            "measure_range": 40
        },
        "Equepment_angle_torque_to_pole": {
            "Equepment_class": "angle_torque",
            "shebei_name": "Equepment_angle_torque_to_pole",
            "recve_pin": ('ardiuno2560__', 9, 'ANALOG', 'INPUT', 'ardiuno2560')
        },

        "Equepment_main_beam_obj": {
            "Equepment_class": "main_beam_position",
            "shebei_name": "Equepment_main_beam_obj",
            "main_beam_last_pole_up_down_expangd_hole": ('ardiuno2560__', 38, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "push_pull_quicken_pin": ('ardiuno2560__', 29, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "torque_quicken_pin": ('ardiuno2560__', 30, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "Equepment_main_beam_taile_5cm_pin": ('ardiuno2560__', 34, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "main_beam_box_can_back_pole_pin": ('ardiuno2560__', 35, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "main_beam_from_tiger_tooth_5cm_pin": ('ardiuno2560__', 36, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "main_beam_tiger_tooth_middle_pin": ('ardiuno2560__', 37, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_water_open_close_pin": ('ardiuno2560__', 7, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "modbus485__2_MainBeam_4mRopeEncode_pin": (
                'modbus485__', (modbus485__2_MainBeam_4mRopeEncodeSlaveId, 0), 'ANALOG', 'OUTPUT',
                'modbus_rtu_485Beam4mRopeEncodeXiYuWeiYiSensor'),
            "modbus_rtu_485MainBeam4mAbsEncode_pin": (
                    'modbus485__', (modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64SlaveId, 0), 'ANALOG', 'OUTPUT',
                    'modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64'),
            "parameter_file": r"mmmmmmmmmmm.csv"

        },
        "Equepment_lamp_light": {
            "Equepment_class": "lamp_",
            "shebei_name": "Equepment_lamp_light",
            "middle_lamp_pin": ('ardiuno2560__', 8, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "top_lamp_pin": ('ardiuno2560__', 11, 'DIGITAL', 'OUTPUT', 'ardiuno2560')
        },
        "Equepment_warning_light": {
            "Equepment_class": "warning_lamp",
            "shebei_name": "Equepment_warning_light",
            "warning_sound_pin": ('ardiuno2560__', 28, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "yelow_ready_pin": ('ardiuno2560__', 31, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "_green_ok_pin": ('ardiuno2560__', 32, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
            "red_back_pin": ('ardiuno2560__', 33, 'DIGITAL', 'OUTPUT', 'ardiuno2560'),
        },
        "Equepment_drill_box_digit_piont": {
            "Equepment_class": "drill_box",
            "shebei_name": "Equepment_drill_box_digit_piont",
            "pole_box_has_uped_pin": ('ardiuno2560__', 42, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_box_has_down_pin": ('ardiuno2560__', 43, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_box_has_down_can_grip_pin": ('ardiuno2560__', 44, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_box_1_point_pin": ('ardiuno2560__', 39, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_box_2_point_pin": ('ardiuno2560__', 40, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_box_3_point_pin": ('ardiuno2560__', 41, 'DIGITAL', 'INPUT', 'ardiuno2560'),
            "pole_box_arm_forward_pin": ('ardiuno2560__', 1, 'DIGITAL', 'INPUT', 'ardiuno2560'),
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

            "parameter_file": r"mmmmmmmmmmm.csv",
            "point1_coordinate": parameter_load_data["point1_coordinate"],
            "point2_coordinate": parameter_load_data["point2_coordinate"],
            "point3_coordinate": parameter_load_data["point3_coordinate"],

            "box_updown_column_up": parameter_load_data["box_updown_column_up"],
            "box_updown_bottom": parameter_load_data["box_updown_bottom"],
            "box_updown_column_can_grap": parameter_load_data["box_updown_column_can_grap"],

            "drill_box_unstoppable_coordinate": parameter_load_data["point_unstop_beam_coordinate"],
            "box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole": parameter_load_data["box_grap_to_beam_the_relax_hand_point_and_next_to_holed_pole_coordinate"],
            "can_hold_beam_pole_coordinate": parameter_load_data["point_beam_grap_coordinate"],
        },








    }
}
machine_two = {

}

xxyy = dir()
xx_locale = locals()

class setting_class:
    port_all_need_read_pin = {}

    def getmachine_obj():
        data_key = xxyy[9:]
        back_dict = {}
        for every_machin_key in data_key:
            back_dict[every_machin_key] = xx_locale[every_machin_key]
        print(len(back_dict), back_dict)
        return back_dict

    def all_board_obj_comnb_class():
        setting_data = machine_one
        temple = set()
        for key_board, value_board in setting_data.items():
            data = (key_board, value_board["port_option_class"], value_board["board_ports"])
            if data[2] is not None:
                temple.add(data)
        return temple

    def getisetin_data ():
       setting_data =machine_one
       temple = set()

       for key_board, value_board in list(setting_data.items()):
           for key_equepment,value_equepument in list(value_board.items()):
               try:
                   for key_equepment_part, value_equepument_part in list(value_equepument.items()):
                       if "_pin" in key_equepment_part:
                           temple.add(value_equepument_part)
               except:
                   pass
       return list(temple)

    def getsetin_data2():
        temple = set()
        for key_com, value in list(machine_one.items()):
            if key_com != "virtual_equepment":
                for key_equepment_name, equepment_parameter_value in value.items():
                    if type(equepment_parameter_value) is dict:
                        try:
                            for key_pin_name, pin_value in equepment_parameter_value.items():
                                if type(pin_value) is dict:
                                    for modbus_pin_name, modbus_pinvalue in pin_value.items():
                                        temple.add((modbus_pinvalue))
                                else:
                                    if key_pin_name.endswith("_pin"):
                                        temple.add((pin_value))
                        except Exception:
                            pass
        return list(temple)
    def getisetin_modbus_485_child():
        setting_data = machine_one
        temple = set()
        for key_, key_obj_value in setting_data.items():
            for ke_name in key_obj_value.keys():
                try:
                    if "modbus_expand_part" in ke_name:
                        dd = tuple(key_obj_value[ke_name].items())
                        data = (ke_name, tuple(key_obj_value[ke_name].items()))

                        data2 = (machine_one[key_]["port_option_class"], (dd[1][1], dd[2][1], dd[3][1], dd[4][1], dd[13][1]), key_)      # if oml_ dd[1][1]
                        temple.add(data2)
                except Exception as ee:
                    print("fffffffffffffffffffff", ke_name, ee)
        return list(temple)

    def get_modbus_485_com_class_obj():
        setting_data = machine_one
        temple = set()
        for key_, key_obj_value in setting_data.items():
            for ke_name in key_obj_value.keys():
                try:
                    if "modbus_expand_part" in ke_name:
                        dd = tuple(key_obj_value[ke_name].items())
                        data = (ke_name, tuple(key_obj_value[ke_name].items()))
                        data2 = (machine_one[key_]["board_ports"], machine_one[key_]["port_option_class"], key_)      # if oml_ dd[1][1]
                        temple.add(data2)
                except Exception as ee:
                    print("fffffffffffffffffffff", ke_name, ee)
        # for x in temple:
        #     print(x)
        return list(temple)

    def get_everyequepment_pinname_map_pingparameter_dict():
        everyequepment_pin_name_dict = {}
        setting_data = machine_one
        for equepment_name, pings in setting_data["virtual_equepment"].items():
            everyequepment_pin_name_dict[equepment_name] = {}
            for pin_name in pings.keys():
                if "_pin" in pin_name:
                    everyequepment_pin_name_dict[equepment_name][pin_name] = pings[pin_name]

        return everyequepment_pin_name_dict

    def getEquepment_other_paramete_exculde_pin():   #has Equepment calss  and other paramete
        Equepment_other_paramete_exculde_pin = {}
        setting_data = machine_one
        for board, board_value in setting_data.items():
                    for key, value in board_value.items():
                        try:
                            if "Equepment_" in key:
                                pin_name_ping_parameter = {}
                                for pin_name in value.keys():
                                    if "_pin" not in pin_name:
                                        pin_name_ping_parameter[pin_name] = value[pin_name]
                                        # print("every :"+key+":  ",pin_name_ping_parameter)
                                        Equepment_other_paramete_exculde_pin[key] = pin_name_ping_parameter
                        except:
                            pass

        return  Equepment_other_paramete_exculde_pin    # key = equepment_obj   value include equepment_class ,and other parameter

    def statistatics_encode_push_pull_equipment():
        bb_data = setting_class.get_everyequepment_pinname_map_pingparameter_dict()
        # print(bb_data)
        aa_data = setting_class.getEquepment_obj_getEquepment_class()
        # print(aa_data)
        statistatics_encode_push_pull_equipment_all = {}
        for every_equipment in aa_data.keys():
            # if aa_data[every_equipment] == 'encode_push_pull':
            if aa_data[every_equipment].startswith('push_pull') :
                pin_data = bb_data[every_equipment]
                # del pin_data['Forward_pin']
                # del pin_data['Backward_pin']
                statistatics_encode_push_pull_equipment_all[every_equipment] = pin_data

        return statistatics_encode_push_pull_equipment_all

    def getEquepment_obj_getEquepment_class():
            equepment_obj_map_class = {}
            Equepment_exculde_pin_name_data = setting_class.getEquepment_other_paramete_exculde_pin()
            for Equepment_obj,obj_paramete in Equepment_exculde_pin_name_data.items():
                equepment_obj_map_class[Equepment_obj] =obj_paramete['Equepment_class']
            return equepment_obj_map_class
    def equepmentj_other_parameter_without_class_and_pin():
            equepment_obj_map_pin_without_class = {}
            Equepment_exculde_pin_name_data = setting_class.getEquepment_other_paramete_exculde_pin()
            for equepment,value in Equepment_exculde_pin_name_data.items():
                  del value['Equepment_class']
                  equepment_obj_map_pin_without_class[equepment] = value
            return equepment_obj_map_pin_without_class

    def getEquepmentobj_other_parameter_without_class_and_pinparameter():
            # result only key = ping__name  value = ping_parameter in it  no class and other parameters
            Equepmentobj_other_parameter_without_class_and_pinparameter = {}
            Equepment_exculde_pin_name_data = setting_class.getEquepment_other_paramete_exculde_pin()
            for equepment,value in Equepment_exculde_pin_name_data.items():
                      del value['Equepment_class']
                      Equepmentobj_other_parameter_without_class_and_pinparameter[equepment] = value
            return Equepmentobj_other_parameter_without_class_and_pinparameter
    def getEquepment_obj_readpin_number(Equepment_obj_name):
        equepment_pin = setting_class.get_everyequepment_pinname_map_pingparameter_dict()
        allequepment_pinnumbrs = {}
        for equepmen_obj in equepment_pin:
            readpin_number = 0
            for every_pin, pinparameter in equepment_pin[equepmen_obj].items():

                if pinparameter[3] == "INPUT":

                    readpin_number = readpin_number+1

            allequepment_pinnumbrs[equepmen_obj] = readpin_number

        return allequepment_pinnumbrs[Equepment_obj_name]

    def get_pin_equepment_name():
        new_pin_data = {}
        for every_pin in setting_class.getisetin_data():


            for every_equepment,values in setting_class.get_everyequepment_pinname_map_pingparameter_dict().items():

                if every_pin in values.values():

                    equepment_name = every_equepment
                    new_pin_data[every_pin] = equepment_name
        return new_pin_data

    def get_port_class_and_obj_and_port_number():   #this function has been instead with  function all_board_obj_comnb_class

        setting_data = machine_one
        temple = set()
        for key_, key_obj_value in setting_data.items():
            print("port_obj_name is {}".format(key_))
            class_name = key_obj_value["port_option_class"]
            if key_obj_value["board_ports"] != None:
                port_data = key_obj_value["board_ports"]
                temple.add((key_, class_name, port_data))
        temple = tuple(temple)
        return temple

    def get_arduino_pin():

        portparameter = machine_one["ardiuno2560__"]
        pinids = []
        for equepment_name in portparameter.keys():
            if equepment_name.startswith("Equepment_"):
                for may_pin in portparameter[equepment_name]:
                    if may_pin.endswith("_pin"):
                        pinids.append(portparameter[equepment_name][may_pin])
        return pinids


try:
    import sys
    sys.path.append(r"D:\comunication_ui_")
    import communication_setting
    function_code8001 = str(struct.pack("i", 8001))
    function_code8002 = str(struct.pack("i", 8002))
    function_code8003 = str(struct.pack("i", 8003))
    function_code8004 = str(struct.pack("i", 8004))
    function_code8005 = str(struct.pack("i", 8005))

except Exception:
    pass

