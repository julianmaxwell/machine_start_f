from threading import Thread
import sys
from abc import ABCMeta
from PyQt5 import QtWidgets
from 主表 import UUi_MainWindow

class order_library():

    def __init__(self,  windowGetOrderFromProcessPipe, orderSendToMachineProcessPipe, uui_main_window_obj, window_order_dict):

        self.uui_main_window_obj = uui_main_window_obj

        self.windowGetOrderFromProcessPipe = windowGetOrderFromProcessPipe
        self.orderSendToMachineProcessPipe = orderSendToMachineProcessPipe
        self.orders = window_order_dict



    def get_order(self, windowGetOrderFromProcessPipe):
        order_function = None
        while True:

            order_function = windowGetOrderFromProcessPipe.get()
            if "machine_equepment_instantaneous_read_data" not in order_function:
                print(order_function, "recve_order and to run at onece")
            try:
                self.orders[order_function[0]](order_function[1])
                if "machine_equepment_instantaneous_read_data" != order_function[0]:
                    print(order_function[0] + "  is run out ")
            except:
                print(order_function[0] +"  not run")


    def regester_all_orders_(self, order_name,order_obj):
        self.orders[order_name] = order_obj

    def run_order(self, order_name):
        return self.orders[order_name]
#orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe
class order_(metaclass=ABCMeta):
    def __init__(self, order_name,order_obj,order_library_obj, windowGetOrderFromProcessPipe, orderSendToMachineProcessPipe,):
        self.order_library_obj = order_library_obj
        self.order_name_ = order_name
        self.order_obj = order_obj
        self.windowGetOrderFromProcessPipe = windowGetOrderFromProcessPipe
        self.orderSendToMachineProcessPipe = orderSendToMachineProcessPipe
        self.regist()

    def regist(self):
        self.order_library_obj.regester_all_orders_(self.order_name_,self.order_obj)

    def run(self, *args, **kwargs):
        try:
            if self.order_obj( *args, **kwargs) is True:
                return True
        except:
            pass


class windows_operator():
    def __init__(self, windowGetOrderFromProcessPipe, orderSendToMachineProcessPipe, uui_main_window_obj):

        self.windowGetOrderFromProcessPipe = windowGetOrderFromProcessPipe
        self.orderSendToMachineProcessPipe = orderSendToMachineProcessPipe
        self.uui_main_window_obj = uui_main_window_obj
        self.set_order_que_touui_main_window_obj()
        self.window_order_dict = {
            "ui_window.lineEdit_5.setText": self.uui_main_window_obj.lineEdit_5.setText,
            "ui_window.lineEdit_6.setText": self.uui_main_window_obj.lineEdit_6.setText,
            "ui_window.lineEdit_14.setText": self.uui_main_window_obj.lineEdit_14.setText,
            "ui_window.lineEdit_15.setText": self.uui_main_window_obj.lineEdit_15.setText,
            "ui_window.lineEdit_8.setText": self.uui_main_window_obj.lineEdit_8.setText,
            "ui_window.lineEdit_9.setText": self.uui_main_window_obj.lineEdit_9.setText,
            "ui_window.lineEdit_10.setText": self.uui_main_window_obj.lineEdit_10.setText,
            "ui_window.lineEdit_23.setText": self.uui_main_window_obj.lineEdit_23.setText,
            "ui_window.lineEdit_31.setText": self.uui_main_window_obj.lineEdit_31.setText,
            "ui_window.lineEdit_28.setText": self.uui_main_window_obj.lineEdit_28.setText,
            "ui_window.pushButton_111.setText": self.uui_main_window_obj.pushButton_111.setText,
            "ui_window.pushButton_122.setText": self.uui_main_window_obj.pushButton_122.setText,
            "ui_window.pushButton_113.setText": self.uui_main_window_obj.pushButton_113.setText,
            "ui_window.pushButton_115.setText": self.uui_main_window_obj.pushButton_115.setText,
            "ui_window.pushButton_124.setText": self.uui_main_window_obj.pushButton_124.setText,
            "ui_window.pushButton_140.setText": self.uui_main_window_obj.pushButton_140.setText,
            "ui_window.pushButton_123.setText": self.uui_main_window_obj.pushButton_123.setText,
            "ui_window.pushButton_114.setText": self.uui_main_window_obj.pushButton_114.setText,
            "ui_window.pushButton_116.setText": self.uui_main_window_obj.pushButton_116.setText,
            "ui_window.pushButton_117.setText": self.uui_main_window_obj.pushButton_117.setText,
            "ui_window.pushButton_118.setText": self.uui_main_window_obj.pushButton_118.setText,
            "ui_window.pushButton_325.setText": self.uui_main_window_obj.pushButton_325.setText,
            "ui_window.pushButton_173.setText": self.uui_main_window_obj.pushButton_173.setText,
            "ui_window.pushButton_174.setText": self.uui_main_window_obj.pushButton_174.setText,
            "ui_window.pushButton_324.setText": self.uui_main_window_obj.pushButton_324.setText,
            "ui_window.pushButton_121.setText": self.uui_main_window_obj.pushButton_121.setText,
            "ui_window.pushButton_120.setText": self.uui_main_window_obj.pushButton_120.setText,
            "ui_window.lineEdit_34.setText": self.uui_main_window_obj.lineEdit_34.setText,
            "ui_window.lineEdit_37.setText": self.uui_main_window_obj.lineEdit_37.setText,
            "ui_window.lineEdit_38.setText": self.uui_main_window_obj.lineEdit_38.setText,
            "ui_window.lineEdit_76.setText": self.uui_main_window_obj.lineEdit_76.setText,
            "ui_window.lineEdit_89.setText": self.uui_main_window_obj.lineEdit_89.setText,
            "ui_window.lineEdit_90.setText": self.uui_main_window_obj.lineEdit_90.setText,
            "ui_window.lineEdit_91.setText": self.uui_main_window_obj.lineEdit_91.setText,
            "ui_window.lineEdit_75.setText": self.uui_main_window_obj.lineEdit_75.setText,
            "ui_window.lineEdit_79.setText": self.uui_main_window_obj.lineEdit_79.setText,
            "ui_window.lineEdit_82.setText": self.uui_main_window_obj.lineEdit_82.setText,
            "ui_window.lineEdit_109.setText": self.uui_main_window_obj.lineEdit_109.setText,
            "ui_window.lineEdit_77.setText": self.uui_main_window_obj.lineEdit_77.setText,
            "ui_window.lineEdit_80.setText": self.uui_main_window_obj.lineEdit_80.setText,
            "ui_window.lineEdit_84.setText": self.uui_main_window_obj.lineEdit_84.setText,
            "ui_window.lineEdit_92.setText": self.uui_main_window_obj.lineEdit_92.setText,
            "ui_window.lineEdit_93.setText": self.uui_main_window_obj.lineEdit_93.setText,
            "ui_window.lineEdit_94.setText": self.uui_main_window_obj.lineEdit_94.setText,
            "ui_window.lineEdit_78.setText": self.uui_main_window_obj.lineEdit_78.setText,
            "ui_window.lineEdit_81.setText": self.uui_main_window_obj.lineEdit_81.setText,
            "ui_window.lineEdit_85.setText": self.uui_main_window_obj.lineEdit_85.setText,
            "ui_window.lineEdit_110.setText": self.uui_main_window_obj.lineEdit_110.setText,
            "ui_window.lineEdit_111.setText": self.uui_main_window_obj.lineEdit_111.setText,
            "ui_window.lineEdit_135.setText": self.uui_main_window_obj.lineEdit_135.setText,
            "ui_window.lineEdit_136.setText": self.uui_main_window_obj.lineEdit_136.setText,
            "ui_window.lineEdit_86.setText": self.uui_main_window_obj.lineEdit_86.setText,
            "ui_window.lineEdit_87.setText": self.uui_main_window_obj.lineEdit_87.setText,
            "ui_window.lineEdit_88.setText": self.uui_main_window_obj.lineEdit_88.setText,
            # ui_form_dirll_box_every_pole_distance
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText":
                self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_38.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText":
                self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_34.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_41.setText":
               self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_41.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_42.setText":
                self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.pushButton_42.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_37.setText":
                self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_37.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_33.setText":
                self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_33.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_36.setText":
                self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_36.setText,
            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_35.setText":
                self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.lineEdit_35.setText,

            "uui_main_window_obj.ui_form_dirll_box_every_pole_distance.verticalSlider.setValue":
              self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.verticalSlider.setValue,

            "pushButton_184.setVisible(False))":self.uui_main_window_obj.pushButton_184.setVisible,
            "machine_obj.wrong_data": self.write_all_message_box_every_data,
            "machine_base_pin_instantaneous_read_data": self.window_show,
            "machine_equepment_instantaneous_read_data": self.window_show




        }
        self.order_laibarary_and_loop = order_library(windowGetOrderFromProcessPipe, orderSendToMachineProcessPipe, uui_main_window_obj, self.window_order_dict)

    def set_order_que_touui_main_window_obj(self):
        setattr(self.uui_main_window_obj, "orderSendToMachineProcessPipe", self.orderSendToMachineProcessPipe)
        setattr(self.uui_main_window_obj, "windowGetOrderFromProcessPipe", self.windowGetOrderFromProcessPipe)

    def window_show(self, data):
        """
        it send map file is D:\machine\机器端\machine_high_lever_equepment.py  machine class colect_data_to_que method
        """
        self.uui_main_window_obj.label_221.setText(str(data["main_beam_coordinate_single1"]))
        self.uui_main_window_obj.label_222.setText(str(data["main_beam_cycle_number_coordinate_single1"]))

        self.uui_main_window_obj.label_223.setText(str(data["hand_grap_coordinate_single2"]))
        self.uui_main_window_obj.label_226.setText(str(data["main_beam_taile_20cm_single3"]))
        self.uui_main_window_obj.label_297.setText(str(data["main_beam_head_20cm_single4"]))
        self.uui_main_window_obj.label_313.setText(str(data["main_beam_pulpush_rocer_arm_coordinate_single5"]))
        self.uui_main_window_obj.label_315.setText(str(data["drill_rocker_arm_coordinate_single6"]))
        self.uui_main_window_obj.label_319.setText(str(data["pole_angle_single7"]))
        self.uui_main_window_obj.label_321.setText(str(data["warter_deep_coordinate_single8"]))
        self.uui_main_window_obj.label_332.setText(str(data["outer_tiger_rocker_arm_coordinate_single9"]))
        self.uui_main_window_obj.label_334.setText(str(data["inner_tiger_rocker_arm_coordinate_single10"]))
        self.uui_main_window_obj.label_336.setText(str(data["loose_tiger_rocker_arm_coordinate_single11"]))
        self.uui_main_window_obj.label_338.setText(str(data["water_pressure_single12"]))
        self.uui_main_window_obj.label_356.setText(str(data["push_pull_pressure_single13"]))
        self.uui_main_window_obj.label_358.setText(str(data["drill_pressure_single14"]))
        self.uui_main_window_obj.label_582.setText(str(data["dirll_box_up_dow_point_single15"]))
        self.uui_main_window_obj.label_54.setText(str(data["angle_0_corectting"]))
        self.uui_main_window_obj.lineEdit_75.setText(str(data["first_point_coordinate"]))
        self.uui_main_window_obj.lineEdit_77.setText(str(data["second_point_coordinate"]))
        self.uui_main_window_obj.lineEdit_78.setText(str(data["fourth_point_coordinate"]))
        self.uui_main_window_obj.lineEdit_86.setText(str(data["third_point_coordinate"]))
        self.uui_main_window_obj.lineEdit_92.setText(str(data["taile_thread_is_ok_point_coordinate"]))
        self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.label_3.setText(str(data["hand_grap_coordinate_single2"]))
        self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.label_4.setText(str(data["hand_grap_coordinate_single2"]))
        self.uui_main_window_obj.ui_form_dirll_box_every_pole_distance.label_11.setText(str(data["hand_grap_coordinate_single2"]))


    def messge_box_wrongdata(self, uui, setdata, outdata=None):
        uui.setVisible(setdata)
        if outdata != None:
            uui.setText(str(outdata))

    def write_message_box_every_data(self, uui, setdata, outdata=(None, None, None, None, None)):
        list(map(self.messge_box_wrongdata, uui, setdata, outdata))

    def write_all_message_box_every_data(self, setdata, outdata=(None, None, None, None, None)):
        ui_index = 0
        for every_ in setdata:
            self.write_message_box_every_data( self.uui_main_window_obj.message_lable_menu[ui_index], every_, outdata)
            if ui_index == 5:
                break
            ui_index = ui_index + 1
        if len(setdata) < 6:
            index2 = len(setdata)
            while index2 < 6:
                self.write_message_box_every_data( self.uui_main_window_obj.message_lable_menu[index2], [False, False, False, False, False],
                                                  outdata)
                index2 = index2 + 1
                if index2 > 5:
                    break


    def machine_obj_wrong_data_(self, *args):
        data = args[0]
        wrong_data = data[1]


    # self.ui_form_dirll_box_every_pole_distance.lineEdit_6.setText(value)
    def every_window_order_frome_machine(self, *args, **kwargs):
        data = args[0]
        key = data[0]
        value = data[1]
        try:
            self.window_order_dict[key](value)
        except KeyError:
            print("wrong single  ", KeyError)

    def window_get_order_loop(self):
        import os
        import pandas
        windowGetOrderFromProcessPipe = self.windowGetOrderFromProcessPipe
        permit_file_name = os.path.join(os.getcwd(), "permit_file_name.csv")
        operator_function = pandas.DataFrame([], columns=["operator_id", "operator_name", "machine_id",
                                                          "permit_function_name", "registered_time"])
        operator_permit_function_name = operator_function.loc[:, "permit_function_name"]
        while True:
            order_list = windowGetOrderFromProcessPipe.recv()
            name_, args = order_list

            try:
                self.every_window_order_frome_machine(order_list)
            except:
                print(order_list[0],"isn't run")



def window_run(orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe):
    """
    no use

    """
    application = QtWidgets.QApplication(sys.argv)
    widget_main = QtWidgets.QMainWindow()
    ui_widget_main = UUi_MainWindow()
    ui_widget_main.setupUi(widget_main, orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe)
    new_ui = windows_operator(windowGetOrderFromProcessPipe, orderSendToMachineProcessPipe, ui_widget_main)
    new_ui_thread = Thread(target=new_ui.window_get_order_loop)
    new_ui_thread.start()
    widget_main.show()
    sys.exit(application.exec_())

def window_run_c():
    """
    operator machine use this function begin ui

    """
    sys.path.append("D:\comunication_ui_")
    import communication_
    import communication_setting
    winip = communication_setting.window_ip
    application = QtWidgets.QApplication(sys.argv)
    widget_main = QtWidgets.QMainWindow()
    ui_widget_main = UUi_MainWindow()
    ui_widget_main.setupUi(widget_main)
    communication_.create_communication_thread(ui_widget_main, listen_port=winip)
    widget_main.show()
    sys.exit(application.exec_())


# def window_run_with_communication(orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe):
#     """
#     operator machine use this function begin ui
#
#     """
#     application = QtWidgets.QApplication(sys.argv)
#     widget_main = QtWidgets.QMainWindow()
#     ui_widget_main = UUi_MainWindow()
#     ui_widget_main.setupUi(widget_main)
#
#     new_ui = windows_operator(windowGetOrderFromProcessPipe, orderSendToMachineProcessPipe, ui_widget_main)
#     new_ui_thread = Thread(target=new_ui.window_get_order_loop)
#     new_ui_thread.start()
#     widget_main.show()
#     sys.exit(application.exec_())