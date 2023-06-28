import cv2
import numpy
import seting
import copy
from multiprocessing import Pipe
from testk import Borad_Ssensor_loop
parameter_load_data_Series = seting.parameter_load_data_Series
loop_read_outer_pipe, outer_send_loop_pipe = Pipe()
outer_read_pipe, loop_send_outer_pipe = Pipe()
outer_read_pipe.poll()
machine_sensors_obj = Borad_Ssensor_loop(loop_read_outer_pipe, loop_send_outer_pipe)
if __name__ == "__main__":
    machine_sensors_obj.run_all_loop()
    print([i for i in dir(cv2) if not i.startswith("_")])
cameras = 10
mm0 = cv2.VideoCapture(0)
mm = cv2.VideoCapture(1)
"""
data_out = {time_end: {every: data}}   sensor loop send out format
data format = (slave_id, real_data) 

"""


def get_result_innit_data():
    data_sig12 = numpy.zeros(5) + numpy.random.randn(5) * 0.01 + 0.15
    """
    ["beam_has_pole", "box_up_down_can_Load_pole", "box_up_down_hand_grap_can_back_with_pole", "box_up_down_at_bottom",
    "ahead_hand_grap_has_pole", "tail_hand_grap_has_pole", ]
    """

    data_relu12 = numpy.zeros(5) + numpy.random.randn(5) * 0.01 + 0.15
    """
    "tiger_plat_x": 0,
    "tiger_plat_y": 0,
    "box_up_down_half_coordinate_modify": 0,
    "box_up_down_coordinate": 0,
    "hand_grap_1m_coordinate": 0,
    """

    data_soft_max12 = numpy.zeros((5, 6)) + numpy.random.rand(5, 6) * 0.01 + 0.15
    """
    "beam_pole_thread_statue": 1,  # [0, 1, 2, 3, 4, 5]  丝扣质量等级
    "beam_has_walter": 0,  # [0, 1, 2, 3, 4, 5]  0 is no,  1 has walter, no pressure, 2 .....
    "connect_statue": "not_in",  # [None, "willchangexy", "not_in", "enter", "connected_relax", "connected_tight"]
    "grap_hand_relax": "relax",  # [0, 1, 2, 3, 4, 5]
    "box_hand_at_point": "inner_column",
        ["inner_column", "middle_column", "outer_column", "not_stop_beam", "beam_middle", "near_beam_middle_can_relax_grap"]
    """

    camara12 = {"relu": data_relu12, "sigmoid": data_sig12, "softmax": data_soft_max12}

    data_Relu_23 = numpy.zeros(5) + numpy.random.randn(5) * 0.01 + 0.15
    """
    "tiger_plat_x": 0,
    "tiger_plat_y": 0,
    "tiger_head_ruler_coordinate": 0,
    "tiger_back_ruler_coordinate": 0,
    "tiger_move_coordinate": 0,        

    """
    data_sig_23 = numpy.zeros(5) + numpy.random.randn(5) * 0.01 + 0.15
    """
    "beam_pole_into_Plat": True,  # [True, False ]
    "pole_cross_plat_into_tiger": True,
    """

    data_soft_max23_1 = numpy.zeros(2) + numpy.random.randn(2) * 0.01 + 0.15
    """
    "pole_between_middle_tiger": list(range(-5, 6)),
    "tiger_tail_tooth_not_correct_bite_pole": list(range(-5, 6)),
    """
    data_soft_max23_2 = numpy.zeros(2) + numpy.random.randn(2) * 0.01 + 0.15
    """
    "tiger_head_tooth_bite": False,  # [True, False, "relax_bite"]
    "tiger_tail_tooth_bite": False,  # [True, False, "relax_bite"]
    """
    data_soft_max23_3 = numpy.zeros(2) + numpy.random.randn(2) * 0.01 + 0.15
    """
    "tiger_move_distance": 0, #list(range(-20, 21)),
    "tiger_tail_tooth_drill_angle": 0,  # [-20, 21]
    """

    data_soft_max23_4 = numpy.zeros((2, 5)) + numpy.random.rand(2, 5) * 0.01 + 0.15
    """
    "beam_to_hole_pole_bent": 1,  # [1, 2, 3, 4, 5, 6]
    "pole_connect_statue": None,
    # [None, "willchangexy", "not_in", "enter", "connected_relax", "connected_tight"]
    """
    camara23 = {
        "relu": data_Relu_23,
        "sigmoid": data_sig_23,
        "soft_max": [data_soft_max23_1, data_soft_max23_2, data_soft_max23_3, data_soft_max23_4]
    }

    """
    "camera4": {
        "gauges_": {



                    },

                     },
    """
    data_sig4 = data_relu12 = numpy.zeros(3) + numpy.random.randn(3) * 0.01 + 0.15
    """
    "oil": True,
    "hydraulic_oil": True,
    "engin_failure": False,
    """
    data_relu_4 = numpy.zeros(6) + numpy.random.randn(6) * 0.01 + 0.15
    """
    "       diesel_fuel": 0.5,
            "diesel_engine_drill_speed": 2500,
            "voltmeter": 25.5,

            "pressure_push_pull": 2,
            "pressure_drill": 1,
            "pressure_walter": 1,
    """
    data_soft_max4 = numpy.zeros((5, 11)) + numpy.random.rand(5, 11) * 0.01 + 0.15
    """
    "push_pull_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "drill_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "tiger_ahead_tooth_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "tiger_bacd_tooth_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "tiger_bacd_tooth_drill_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    """
    camara4 = {
        "relu": data_relu_4,
        "sigmoid": data_sig4,
        "soft_max": [data_soft_max4]
    }

    camara5 = numpy.zeros(1) + numpy.random.randn(1) * 0.01 + 0.15
    """
        "camera5": {
            "walter_for_pole": 0.5,
                }

    """

    camara = [camara12, camara23, camara4, camara5]
    return camara

def get_camera_obj():
    cam_objs = []
    for camera in range(cameras):
        cam_obj = cv2.VideoCapture(camera)
        if cam_obj.grab():
            cam_objs.append(cam_obj)
        else:
            cam_obj.release()
            break
    return cam_objs

slave_id_map_name = {
    ("line_test_4m_1m_4m_function", 2): "bearm_4m",
    ("line_test_4m_1m_4m_function", 3): "hand_grap_1m",
    ("x_angle_y_angle", 80): "pole_angle",
    ("zouzheng_8_chanel", 1): "bearm_4m",
    ("zouzheng_8_chanel", 1): "bearm_4m",
    ("zouzheng_8_chanel", 1): "bearm_4m",


}

def get_machine_sensor_data(outer_read_pipe=outer_read_pipe, outer_send_loop_pipe=outer_send_loop_pipe):
    if outer_read_pipe.poll(None):
        data = outer_read_pipe.recv()
        time_, dict_data = data.items()
        every, _data = dict_data.items()
        slave_id, real_data = _data

        if (every, slave_id) == ("line_test_4m_1m_4m_function", 2):
            data_return = {
              "bearm_4m": (time_, real_data),
            }
        if (every, slave_id) == ("line_test_4m_1m_4m_function", 3):
            data_return = {
              "hand_grap_1m": (time_, real_data),
            }
        if (every, slave_id) == ("zouzheng_8_chanel", 1):
            data_return = {
              "box_up_down": (time_, real_data("zouzheng_8_chanel", 1)[0]),
              "tiger_head_ruler": (time_, real_data("zouzheng_8_chanel", 1)[1]),
              "tiger_back_ruler": (time_, real_data("zouzheng_8_chanel", 1)[2]),
              "tiger_move": (time_, real_data("zouzheng_8_chanel", 1)[3]),
            }
        return data_return

"""
format is bearm_4m=str(time_)+str(realdata) 
format is hand_grap_1m=str(time_)+str(realdata) 
format is pole_angle=str(time_)+str(realdata) 
format is box_up_down=str(time_)+str(realdata) 
format is tiger_head_ruler=str(time_)+str(realdata) 
format is tiger_back_ruler=str(time_)+str(realdata) 
format is tiger_move=str(time_)+str(realdata) 
result = "_".join([bearm_4m, hand_grap_1m, pole_angle, box_up_down, tiger_head_ruler, tiger_back_ruler,tiger_move]) 
"""

machine_statue_man_input = {
    "beam_has_pole": True,
    "beam_pole_thread_statue": 1, #[1, 2, 3, 4, 5]  丝扣质量等级
    "beam_has_walter": 0, #[0, 1, 2, 3, 4, 5]  0 is no,  1 has walter, no pressure, 2 .....
    "beam_driver_male_head_will_into_pole_head_statue": {
        "x": 0,
        "y": 0,
        "connect_statue": "not_in"  # [None, "willchangexy", "not_in", "enter", "connected_relax", "connected_tight"]
    },
    "beam_pole_into_tigger_statue": {
        "in_Plat": True,   #[True, False ]
        "x": 0,
        "y": 0,
        "pole_over_plat_in_tiger": True,
        "pole_between_middle_tiger": {"x": 0},
        "tiger_tail_tooth_not_correct_bite_pole": {"x": 0},
        "tiger_move_distance": 0,
        "tiger_head_tooth_bite": False, #[True, False, "relax_bite"]
        "tiger_tail_tooth_bite": False, #[True, False, "relax_bite"]
        "tiger_tail_tooth_drill_angle": 0, #[-15, 15]
        "pole_connect_statue": None  # [None, "willchangexy", "not_in", "enter", "connected_relax", "connected_tight"]
    },
    "box_ple": {
            "columns_inner": {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True,},  #[True, False, None]
            "columns_middle": {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True},  #[True, False, None]
            "columns_outer": {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True},   #[True, False, None]
        },
    "box_up_down": {"x": 0,
                    "can_Load_pole": False,
                    "up_hand_grap_can_back_with_pole": False,
                    "battom_at": True,

                    },
    "box_hand_grap": {
        "grap_hand_relax": True,  # ["half_relax", "relax", "tight"]
        "ahead_hand_grap_has_pole": False,
        "tail_hand_grap_has_pole": False,
        "box_hand_point": {
            "x": 0,
            "name": "inner_column", # ["inner_column", "middle_column", "outer_column", "not_stop_beam", "beam_middle", "near_beam_middle_can_relax_grap"]
        }
    },
    "beam_to_hole_pole_bent": 1, #[1, 2, 3, 4, 5]
    "bearm_4m_coordinate" : 0,
    "hand_grap_1m_coordinate" : 0,
    "local_pole_angle": 0,
    "gui_machine_pole_angle": 0,
    "box_up_down_coordinate": 0,
    "tiger_head_ruler_coordinate": 0,
    "tiger_back_ruler_coordinate": 0,
    "tiger_move_coordinate": 0,
    "walter_for_pole": 0.5,
    "gauges_": {
        "oil": True,
        "hydraulic_oil": True,
        "diesel_fuel": 0.5,
        "diesel_engine_drill_speed": 2500,
        "voltmeter": 25.5,
        "engin_failure": False,
        "pressure_push_pull": 2,
        "pressure_drill": 1,
        "pressure_walter": 1,
            },
    "push_pull_gear": 1, #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "drill_gear": 1, #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "tiger_ahead_tooth_gear": 1, #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "tiger_bacd_tooth_gear": 1, #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    "tiger_bacd_tooth_drill_gear": 1, #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    }



ai_data_forat = {
    "cameras12": {
                "beam_has_pole": True,
                "beam_pole_thread_statue": 1,  # [1, 2, 3, 4, 5]  丝扣质量等级
                "beam_has_walter": 0,  # [0, 1, 2, 3, 4, 5]  0 is no,  1 has walter, no pressure, 2 .....
                "beam_female_pole_x": 0,
                "beam_female_pole_y": 0,
                "connect_statue": "not_in", # [None, "willchangexy", "not_in", "enter", "connected_relax", "connected_tight"]

                "box_ple": {
                    "columns_inner": {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True,
                                      10: True, },  # [True, False, None]
                    "columns_middle": {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True,
                                       10: True},  # [True, False, None]
                    "columns_outer": {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True,
                                      10: True},  # [True, False, None]
                            },
                "box_up_down_half_coordinate_modify": 0,

                "box_up_down_can_Load_pole": False,
                "box_up_down_hand_grap_can_back_with_pole": False,
                "box_up_down_at_bottom": True,

                "box_up_down_coordinate": 0,
                "hand_grap_1m_coordinate": 0,


                "grap_hand_relax": "relax",  # ["half_relax", "relax", "tight"]
                "ahead_hand_grap_has_pole": False,
                "tail_hand_grap_has_pole": False,
                "box_hand_at_point": "inner_column",
                                    # ["inner_column", "middle_column", "outer_column", "not_stop_beam", "beam_middle", "near_beam_middle_can_relax_grap"]
                },

    "camera23": {

                "beam_pole_into_Plat": True,  # [True, False ]
                "tiger_plat_x": 0,
                "tiger_plat_y": 0,
                "pole_cross_plat_into_tiger": True,
                "pole_between_middle_tiger": list(range(-5, 6)),
                "tiger_tail_tooth_not_correct_bite_pole": list(range(-5, 6)),
                "tiger_move_distance": 0, #list(range(-20, 21)),
                "tiger_head_tooth_bite": False,  # [True, False, "relax_bite"]
                "tiger_tail_tooth_bite": False,  # [True, False, "relax_bite"]
                "tiger_tail_tooth_drill_angle": 0,  # [-15, 15]
                "pole_connect_statue": None,
                # [None, "willchangexy", "not_in", "enter", "connected_relax", "connected_tight"]
                "tiger_head_ruler_coordinate": 0,
                "tiger_back_ruler_coordinate": 0,
                "tiger_move_coordinate": 0,
                "beam_to_hole_pole_bent": 1,  # [1, 2, 3, 4, 5]
            },

    "camera4": {
        "gauges_": {
            "oil": True,
            "hydraulic_oil": True,
            "diesel_fuel": 0.5,
            "diesel_engine_drill_speed": 2500,
            "voltmeter": 25.5,
            "engin_failure": False,
            "pressure_push_pull": 2,
            "pressure_drill": 1,
            "pressure_walter": 1,
                    },
        "push_pull_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        "drill_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        "tiger_ahead_tooth_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        "tiger_bacd_tooth_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        "tiger_bacd_tooth_drill_gear": 1,  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
                 },
    "camera1234": {
                    "bearm_4m_coordinate": 0,
                },
    "camera5": {
        "walter_for_pole": 0.5,
            }
}

def get_one_hot_normal(one_hot_d, lable=range(5), value_index=0):
    x = numpy.eye(len(lable))
    return x



def one_hot_pole(pole_c=None):
    if pole_c is None:
        pole_c = ai_data_forat["cameras12"]["box_ple"]
    x = numpy.eye(3)
    new_a = []
    new_numpy_arrow_all = None
    for pole_1 in pole_c.values():
        for key, value in pole_1.items():
            if value is True:
                value = x[0]
            elif value is False:
                value = x[1]
            else:
                value = x[2]  #None
            new_a.append(numpy.array(value))
        new_numpy_arrow = numpy.array([new_a])
        new_a = []
        if new_numpy_arrow_all is None:
            new_numpy_arrow_all = new_numpy_arrow
        else:
            new_numpy_arrow_all = numpy.concatenate([new_numpy_arrow_all, new_numpy_arrow], axis=0)
    return new_numpy_arrow_all



def set_parameter(data_return):
    data_parameter = parameter_load_data_Series
    data_r = {}
    if data_return["bearm_4m"] > data_parameter.loc["beam_taile_5cm"]:
        data_r["beam_taile_5cm"] = True
    else:
        data_r["beam_taile_5cm"] = False



def read_pic_map_machine_parameter():
    data_return = {
        "bearm_4m_coordinate": None,
        "hand_grap_1m_coordinate": None,
        "local_pole_angle": None,
        "gui_machine_pole_angle":0,
        "box_up_down_coordinate": None,
        "tiger_head_ruler_coordinate": None,
        "tiger_back_ruler_coordinate": None,
        "tiger_move_coordinate": None,
    }

    while True:
        add_data = get_machine_sensor_data()
        data_return.update(add_data)
        bearm_4m = "_".join(map(str, data_return["bearm_4m"]))
        hand_grap_1m = "_".join(map(str, data_return["hand_grap_1m"]))
        pole_angle = "_".join(map(str, data_return["pole_angle"]))
        box_up_down = "_".join(map(str, data_return["box_up_down"]))
        tiger_head_ruler = "_".join(map(str, data_return["tiger_head_ruler"]))
        tiger_back_ruler = "_".join(map(str, data_return["tiger_back_ruler"]))
        tiger_move = "_".join(map(str, data_return["tiger_move"]))
        file_name_1 = "__".join([bearm_4m, hand_grap_1m, pole_angle, box_up_down, tiger_head_ruler, tiger_back_ruler, tiger_move])
        warter = 0.75
        oil = 0.45
        hydraulic_oil = 0.77
        diesel_fuel = 0.45
        diesel_engine_drill_speed = 2000
        voltmeter = 25.5
        engin_failure = False

        pressure_push_pull = 4
        pressure_drill = 7
        pressure_walter = 3
        box_hand_relax = True


        xx = mm0.read()[1]
        xx1 = mm.read()[1]
        cv2.resize(xx, (480, 640))
        cv2.imshow("test", xx)
        cv2.imshow("test2", xx1)
        cv2.waitKey(30)
        xx = cv2.resize(xx, (480, 640))
        print("*********************")
        print(xx.shape)
        xx = cv2.cvtColor(xx, cv2.COLOR_BGR2GRAY)
        print("xxxxxxxxxxxxxxxxxxx", xx.shape)
        xx2 = numpy.reshape(xx, (640, 480, 1))
        print(xx2.shape)
        print("mmmmmmmmmmmmmmmmmmmmmmmm")
        xx = numpy.expand_dims(xx, axis=2)
        print(xx.shape)
        if xx.shape != (480, 640):
            print("over")


if __name__ == "__main__":
    while True:
        xx = mm0.read()[1]
        xx1 = mm.read()[1]
        cv2.resize(xx,  (480, 640))
        cv2.imshow("test", xx)
        cv2.imshow("test2", xx1)
        cv2.waitKey(30)
        xx = cv2.resize(xx, (480, 640))
        print("*********************")
        print(xx.shape)
        xx = cv2.cvtColor(xx, cv2.COLOR_BGR2GRAY)
        print("xxxxxxxxxxxxxxxxxxx", xx.shape)
        xx2 = numpy.reshape(xx, (640, 480,1))
        print(xx2.shape)
        print("mmmmmmmmmmmmmmmmmmmmmmmm")
        xx = numpy.expand_dims(xx, axis=2)
        print(xx.shape)
        if xx.shape != (480, 640):
            print("over")
    cv2.destroyAllWindows()