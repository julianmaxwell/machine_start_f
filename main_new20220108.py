from multiprocessing import Process
import 主表2
import engine
import machine_high_lever_equepment
import sensor
import order
import operation_interface
from machine_terminal_socket import *
import sys

HOST_addr_send = ("192.168.12.106", 7500)       #order_to_machin
HOST_addr_receive = ("192.168.12.106", 8100)    #order_to_window

# HOST_addr_send = ("192.168.12.110", 7500)       #order_to_machin
# HOST_addr_receive = ("192.168.12.110", 8100)    #order_to_window

def run_borads( pipeGetFromProcessStationWilltoEquepment, pipeSendtoObservation,):
    print(f"im class is {inspect.currentframe().f_code.co_name}, im lines {inspect.currentframe().f_lineno}")
    board_engine = engine.board_basic_data_operation(pipeGetFromProcessStationWilltoEquepment, pipeSendtoObservation)
    print(f"im class is {inspect.currentframe().f_code.co_name}, im lines {inspect.currentframe().f_lineno}")
    board_engine.runing()

def machine_control_station(processSendToCommunicationPipe,
        machineProcessGetOrderPipe,
        ProcessSendOrderToWindowPipe = None
):
    all_equepment_updated_obj = sensor.all_equepment_updated()
    pipeGetFromProcessStationWilltoEquepment, obersvationWillSendToMachineBoardWritePipe = Pipe()
    pipeGetFromMachineBoard, pipeSendtoProcessStation = Pipe()


    oberservation_ = sensor.observation(pipeGetFromMachineBoard, obersvationWillSendToMachineBoardWritePipe)
    machine_obj = machine_high_lever_equepment.machine(
        oberservation_, all_equepment_updated_obj, ProcessSendOrderToWindowPipe)

    machin_thread = Thread(target=machine_obj.run)
    machin_thread.setDaemon(True)
    machin_thread.start()
    board_process = Process(target=run_borads, args=(pipeGetFromProcessStationWilltoEquepment, pipeSendtoProcessStation,))

    board_process.start()
    machin_thread2 = Thread(target=machine_obj.colect_data_to_que)  # send machine_run statues data to the windows or communication
    machin_thread2.setDaemon(True)
    machin_thread2.start()

    box_pole_obj = order.box_pole(machine_obj)
    box_prepare_obj = order.box_prepare(box_pole_obj)
    oldmachineprocess_ = order.oldMachineProcess()
    oldmachineprocess_.set_parameter_obj(machine_obj, box_pole_obj)
    interface_operator_obj = operation_interface.operator(box_prepare_obj, oldmachineprocess_, processSendToCommunicationPipe)
    run_order_order_library = order.order_library(machineProcessGetOrderPipe, interface_operator_obj)
    order_dict = order.all_interface_order_dict_collect(run_order_order_library)

    run_order_thread = Thread(target=order_dict.interface_order_libary_dict.get_order_loop)
    run_order_thread.start()

    """
    # run_order_thread here order_to_machine recev order  and parse order and send it to the order_que ordersystem     
     recv anc run it  the order_que used only between order_dict and ordersystem
    """
    ordersystem = order.order_loop_(order_dict)
    order_thread = Thread(target=ordersystem.run_loop)
    order_thread.setDaemon(True)
    order_thread.start()



def run_win(orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe):
    # 主表.window_run(orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe)
    主表2.window_run(orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe)


    ############################################################
    raise Exception


def permitToMachineQue(data):
    pass
    return True

def communication_recv_data_process(data):
    """ this is the very important function, here all of the data will be changed as the communication format"""
    machine_id, function_id, target_machine_id, function_name, args = data
    permitToMachineQue(data)
    "here you can load operator ."
    return function_name, args

def data_send_to_Communication_out(orderque_SendToCommunicationPipe, orderque_):
    print("fwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww", orderque_SendToCommunicationPipe)
    """
    orderque_  communication module get data from machine will be send to other station.
    """
    while True:
        data = orderque_.get()
        orderque_SendToCommunicationPipe.send(data)

def getFromscketPipe_recv(translateGetFromSoccketPipe, order_to_machine):
    while True:
        data = translateGetFromSoccketPipe.recv()
        newdata = communication_recv_data_process(data)
        if permitToMachineQue(data):
            order_to_machine.put(newdata)

def communication_que_change_pipe(order_to_machine,
                                  translateGetFromSoccketPipe,
                                  ):
    """
    orderque_ only used send order to communication.  order_to_machine order used by machine must send to order_to_machine
    order send to the order_to_machine format is function_name, args
    order send to the orderque_ format must (machine_id, function_code, target_machine_id, function_name, args)
    """
    Threadtor = Thread(target=getFromscketPipe_recv, args=(translateGetFromSoccketPipe, order_to_machine))
    Threadtor.start()

def run_communication(orderSendToMachineProcessPipe, communicationGetFromProcessPipe):
    # translateGetFromSoccketPipe, communicationToProcessCorePipe = Pipe()
    communication_que_change_pipe(
        orderSendToMachineProcessPipe,
        communicationGetFromProcessPipe,
    )
    """
    orderque_ only used send order to communication.  order_to_machine order used by machine must send to order_to_machine
    order send to the order_to_machine format is function_name, args
    order send to the orderque_ format must (machine_id, function_code, target_machine_id, function_name, args)
    """
    ProcessN = Process(target=comunicationProcessCore, args=(orderSendToMachineProcessPipe, communicationGetFromProcessPipe))
    ProcessN.start()


def run_start():
    """
    orderque_ only used send order to communication.  order_to_machine order used by machine must send to order_to_machine
    order send to the order_to_machine format is function_name, args
    order send to the orderque_ format must (machine_id, function_code, target_machine_id, function_name, args)
    """
    if __name__ == '__main__':
        communicationGetFromProcessPipe, processSendToCommunicationPipe = Pipe()
        machineProcessGetOrderPipe, orderSendToMachineProcessPipe = Pipe()
        windowGetOrderFromProcessPipe, ProcessSendOrderToWindowPipe = Pipe()

        machine_control_station(processSendToCommunicationPipe, machineProcessGetOrderPipe, ProcessSendOrderToWindowPipe)
        run_communication(orderSendToMachineProcessPipe, communicationGetFromProcessPipe)
        run_win(orderSendToMachineProcessPipe, windowGetOrderFromProcessPipe)



if __name__ == '__main__':
    run_start()
