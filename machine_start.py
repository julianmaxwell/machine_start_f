__author__ = "boss"
__date__ = '2022/11/27 20:33'

from multiprocessing import Process
import machine_high_lever_equepment
import sensor
import order
import operation_interface
from machine_terminal_socket import *
import engine
import sys
sys.path.append(r"D:\comunication_ui_")
import communication_
import communication_setting

def run_borads( pipeGetFromProcessStationWilltoEquepment, pipeSendtoObservation,):
    print(f"im class is {inspect.currentframe().f_code.co_name}, im lines {inspect.currentframe().f_lineno}")
    board_engine = engine.board_basic_data_operation(pipeGetFromProcessStationWilltoEquepment, pipeSendtoObservation)
    print(f"im class is {inspect.currentframe().f_code.co_name}, im lines {inspect.currentframe().f_lineno}")
    board_engine.runing()




# def machine_control_station(processSendToCommunicationPipe,
#         machineProcessGetOrderPipe,
#         ProcessSendOrderToWindowPipe = None
# ):
#     all_equepment_updated_obj = sensor.all_equepment_updated()
#
#     oberservation_ = sensor.observation()
#     machine_obj = machine_high_lever_equepment.machine(
#         oberservation_, all_equepment_updated_obj, ProcessSendOrderToWindowPipe)

#     machin_thread = Thread(target=machine_obj.run)
#     machin_thread.setDaemon(True)
#     machin_thread.start()
#     board_process = Process(target=run_borads, args=(oberservation_.pipeGetFromProcessStationWilltoEquepment, oberservation_.pipeSendtoProcessStation,))
#
#     board_process.start()
#     machin_thread2 = Thread(target=machine_obj.colect_data_to_que)  # send machine_run statues data to the windows or communication
#     machin_thread2.setDaemon(True)
#     machin_thread2.start()
#
#     box_pole_obj = order.box_pole(machine_obj)
#     box_prepare_obj = order.box_prepare(box_pole_obj)
#     oldmachineprocess_ = order.oldMachineProcess()
#     oldmachineprocess_.set_parameter_obj(machine_obj, box_pole_obj)
#     interface_operator_obj = operation_interface.operator(box_prepare_obj, oldmachineprocess_, processSendToCommunicationPipe)
#     run_order_order_library = order.order_library(machineProcessGetOrderPipe, interface_operator_obj)
#     order_dict = order.all_interface_order_dict_collect(run_order_order_library)
#
#     run_order_thread = Thread(target=order_dict.interface_order_libary_dict.get_order_loop)
#     run_order_thread.start()
#
#
#     ordersystem = order.order_loop_(order_dict)
#     order_thread = Thread(target=ordersystem.run_loop)
#     order_thread.setDaemon(True)
#     order_thread.start()
#     communication_.create_communication_thread(ordersystem)

def engin_run():
    """
    machine obj start  every function connect it with socket  it setted at the file communication_setting.py

    """

    listen_port = communication_setting.locale_lisen_ip
    machine_obj = order.order_loop_()
    communication_.create_communication_thread(machine_obj, listen_port=listen_port)
    machine_obj.run_loop()

if __name__ == "__main__":
    engin_run()
