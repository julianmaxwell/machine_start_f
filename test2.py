import numpy
import copy
import machine_video_rp as aipre

def creat_column_pole():
    data = list(range(11))
    data_d = {}
    for key in data:
        data_d[key] = True
    return data_d

box_pole = aipre.ai_data_forat
pole_c = box_pole["cameras12"]["box_ple"]
x = numpy.eye(3)
def get_result_innit_data():

    data_sig12 = numpy.zeros(5) + numpy.random.randn(5)*0.01 + 0.15
    """
    ["beam_has_pole", "box_up_down_can_Load_pole", "box_up_down_hand_grap_can_back_with_pole", "box_up_down_at_bottom",
    "ahead_hand_grap_has_pole", "tail_hand_grap_has_pole", ]
    """

    data_relu12 = numpy.zeros(5) + numpy.random.randn(5)*0.01 + 0.15
    """
    "tiger_plat_x": 0,
    "tiger_plat_y": 0,
    "box_up_down_half_coordinate_modify": 0,
    "box_up_down_coordinate": 0,
    "hand_grap_1m_coordinate": 0,
    """

    data_soft_max12 = numpy.zeros((5, 6)) + numpy.random.rand(5, 6)*0.01 + 0.15
    """
    "beam_pole_thread_statue": 1,  # [0, 1, 2, 3, 4, 5]  丝扣质量等级
    "beam_has_walter": 0,  # [0, 1, 2, 3, 4, 5]  0 is no,  1 has walter, no pressure, 2 .....
    "connect_statue": "not_in",  # [None, "willchangexy", "not_in", "enter", "connected_relax", "connected_tight"]
    "grap_hand_relax": "relax",  # [0, 1, 2, 3, 4, 5]
    "box_hand_at_point": "inner_column",
        ["inner_column", "middle_column", "outer_column", "not_stop_beam", "beam_middle", "near_beam_middle_can_relax_grap"]
    """

    camara12 = {"relu": data_relu12, "sigmoid": data_sig12, "softmax": data_soft_max12}


    data_Relu_23 = numpy.zeros(5) + numpy.random.randn(5)*0.01 + 0.15
    """
    "tiger_plat_x": 0,
    "tiger_plat_y": 0,
    "tiger_head_ruler_coordinate": 0,
    "tiger_back_ruler_coordinate": 0,
    "tiger_move_coordinate": 0,        
        
    """
    data_sig_23 = numpy.zeros(5) + numpy.random.randn(5)*0.01 + 0.15
    """
    "beam_pole_into_Plat": True,  # [True, False ]
    "pole_cross_plat_into_tiger": True,
    """

    data_soft_max23_1 = numpy.zeros(2) + numpy.random.randn(2)*0.01 + 0.15
    """
    "pole_between_middle_tiger": list(range(-5, 6)),
    "tiger_tail_tooth_not_correct_bite_pole": list(range(-5, 6)),
    """
    data_soft_max23_2 = numpy.zeros(2) + numpy.random.randn(2)*0.01 + 0.15
    """
    "tiger_head_tooth_bite": False,  # [True, False, "relax_bite"]
    "tiger_tail_tooth_bite": False,  # [True, False, "relax_bite"]
    """
    data_soft_max23_3 = numpy.zeros(2) + numpy.random.randn(2)*0.01 + 0.15
    """
    "tiger_move_distance": 0, #list(range(-20, 21)),
    "tiger_tail_tooth_drill_angle": 0,  # [-20, 21]
    """

    data_soft_max23_4 = numpy.zeros((2, 5)) + numpy.random.rand(2, 5)*0.01 + 0.15
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
    data_sig4 = data_relu12 = numpy.zeros(3)+ numpy.random.randn(3)*0.01 + 0.15
    """
    "oil": True,
    "hydraulic_oil": True,
    "engin_failure": False,
    """
    data_relu_4 = numpy.zeros(6)+ numpy.random.randn(6)*0.01 + 0.15
    """
    "       diesel_fuel": 0.5,
            "diesel_engine_drill_speed": 2500,
            "voltmeter": 25.5,
    
            "pressure_push_pull": 2,
            "pressure_drill": 1,
            "pressure_walter": 1,
    """
    data_soft_max4 = numpy.zeros((5, 11)) + numpy.random.rand(5, 11)*0.01 + 0.15
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

    camara5 = numpy.zeros(1) + numpy.random.randn(1)*0.01 + 0.15
    """
        "camera5": {
            "walter_for_pole": 0.5,
                }
    
    """

    camara = [camara12, camara23, camara4, camara5]
    return camara

def one_hot_pole(pole_c):
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

one_hot_d = box_pole["cameras12"]["beam_pole_thread_statue"]

def get_one_hot_normal(one_hot_d, lable=range(5), value_index=0):
    x = numpy.eye(len(lable))
    return x