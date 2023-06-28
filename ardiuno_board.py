import asyncio
import time
from multiprocessing import Process, Pipe
import inspect
import sys
import pandas
from PyMata import pymata
import abc
from threading import Lock, Event, Thread
from multiprocessing import Lock
import testk
import seting
from functools import partial
loop_index = pandas.Index(["next_run_time", "scan_time", "last_run_time", "delta_run_time"])

class Board_com(abc.ABC):
    def __init__(self, portparameter, pipeSendtoProcessStation, pipeGetFromProcessStationWilltoEquepment):

        self.pipeGetFromProcessStationWilltoEquepment = pipeGetFromProcessStationWilltoEquepment
        self.pipeSendtoProcessStation = pipeSendtoProcessStation
        self.portparameter = portparameter

    def gaze(self):
        pass


    def normal(self):
        pass

    # @abc.abstractmethod
    def setting_point(self, pin_id=None, com=None, pin_number=None, pin_mode="INPUT", pin_type='DIGITAL'):
        pass


    def write_data(self, data):
        pass


class ardiuno2560(Board_com):
    def __init__(self, portparameter, pipeSendtoProcessStation, pipeGetFromProcessStationWilltoEquepment):
        super(ardiuno2560, self).__init__(portparameter, pipeSendtoProcessStation, pipeGetFromProcessStationWilltoEquepment)
        # print("this is the board obj  use it write data, and the com = {} ".format(com_set))
        com_set = portparameter["board_ports"]
        try:
            self.obj = pymata.PyMata(com_set)
        except Exception as e3:
            print("some thing is happened")
            print(e3)
        self.ardiuno_lock = Lock()
        self.port = com_set
        self.pin_ids = pin_ids = self.get_arduino_pin()
        self.setting_point(pin_ids=pin_ids)
        self.pins_read_data = {}
        self.ardiuno_event = Event()
        self.read_data()
        self.loop_write_to_equepment_pipe_data()


    def read_data_(self, lock_):
        # print(
        # f"im in {type(self).__name__} function name is {inspect.currentframe().f_code.co_name}, my linenb is {inspect.currentframe().f_lineno}")
        pin_ids = self.pin_ids
        time_ = time.time
        digital_read = self.obj.digital_read
        analog_read = self.obj.analog_read
        ardiuno_lock_acquire = lock_.acquire
        ardiuno_lock_release = lock_.release
        pipeSendtoProcessStation = self.pipeSendtoProcessStation
        while True:
            try:
                for pin_id in pin_ids:
                    if pin_id[3] == 'INPUT':
                                # print(
                                #     f"im in {type(self).__name__} function name is {inspect.currentframe().f_code.co_name}, my linenb is {inspect.currentframe().f_lineno}")
                                ardiuno_lock_acquire()
                                read_begin_time = time_()
                                if pin_id[2] == "DIGITAL":
                                    pin_read_value = digital_read(pin_id[1])

                                    # return pin_read_value
                                elif pin_id[2] == "ANALOG":
                                    pin_read_value = analog_read(pin_id[1])
                                else:
                                    pin_read_value = None
                                ardiuno_lock_release()
                                send_value = {read_begin_time: {pin_id: pin_read_value}}
                                pipeSendtoProcessStation.send(send_value)
                                # return pin_read_value
            except Exception as ff:
                print(ff)

    def read_data(self):
        Process_read = Thread(target=self.read_data_, args=(self.ardiuno_lock,))
        Process_read.setDaemon(True)
        Process_read.start()

    def write_data(self, data):
                # print("i'm in read in board ..................")
                function_name, _pin, value = data
                pin_com, pin, pin_ad_, pin_io, pin_class = _pin
                self.ardiuno_lock.acquire()
                if pin_ad_ == "DIGITAL":
                    if value != None:
                        self.obj.digital_write(pin, value)
                if pin_ad_ == "ANALOG":
                    self.obj.analog_write(pin, value)
                self.ardiuno_lock.release()

    def loop_write_to_equepment_pipe_data(self):
        pipeGetFromProcessStationWilltoEquepment = self.pipeGetFromProcessStationWilltoEquepment
        while True:
            # data format is function_name, pin_id, value
            func_name, pin_id, value = pipeGetFromProcessStationWilltoEquepment.recv()
            function_ = getattr(self, func_name)
            function_(pin_id, value)

    def setting_point(self, pin_ids=None, com_nuber=None, pin_number=None, pin_mode="INPUT", pin_type='DIGITAL'):
        try:
            for pin_id in pin_ids:
                # print("good-----------------------------------", pin_id, self.obj)
                if pin_id[3] == "INPUT":
                    mode = self.obj.INPUT
                if pin_id[3] == "OUTPUT":
                    mode = self.obj.OUTPUT
                if pin_id[2] == "DIGITAL":
                    tye = self.obj.DIGITAL
                if pin_id[2] == "ANALOG":
                    tye = self.obj.ANALOG
                self.obj.set_pin_mode(pin_id[1], mode, tye)
                # self.obj.set_pin_mode(19, "INPUT", "DIGITAL")
        except Exception as e:
            print("board 初始化设置错误", e)
            print(type(pin_id[1]), type(pin_id[3]), type(pin_id[2]))


            # pin, mode, pin_type,
    def get_arduino_pin(self):
        pinids = []
        for equepment_name in self.portparameter.keys():
            if equepment_name.startswith("Equepment_"):
                for may_pin in self.portparameter[equepment_name]:
                    if may_pin.endswith("_pin"):
                        pinids.append(self.portparameter[equepment_name][may_pin])
        return pinids

class ReadWrite():
    """
    here read write data format is  machine_id, function_code, target_machine_id, func_name, *args = data

    """
    def __init__(self, pipeGetFromProcessStationWilltoEquepment, pipeSendtoProcessStation, machine_name="machine_one"):
        self.pipeGetFromProcessStationWilltoEquepment = pipeGetFromProcessStationWilltoEquepment
        self.pipeSendtoProcessStation = pipeSendtoProcessStation
        self.machine_name = machine_name
        self.setting_board()
        print("board setting is over")
        self.write_data()

    def write_data(self):
        # get data format is (machine_id, function_code, target_machine_id, func_name, *args)
        # value format is (com_obj, pinid, ddd,
        #  ('modbus485__', ((4,), 11), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12')
        #  ('ardiuno2560__', 6, 'ANALOG', 'INPUT', 'ardiuno2560')
        pipeGetFromProcessStationWilltoEquepment = self.pipeGetFromProcessStationWilltoEquepment
        while True:
            data = pipeGetFromProcessStationWilltoEquepment.recv()
            for key, value in data.items():
                func_name_new, port_obj_name, pin, data_type, in_out_type, function_class = key
                pin_id = (port_obj_name, pin, data_type, in_out_type, function_class)
                self.board_objs_to_equepment_pipe[port_obj_name].send((func_name_new, pin_id, value))


    def setting_board(self):
        machine_data = getattr(seting, self.machine_name)
        del machine_data["virtual_equepment"]
        port_obj_names = machine_data.keys()
        self.board_objs = {}
        self.board_class_map_obj = {}
        self.board_objs_to_equepment_pipe = {}
        for port_obj_name in port_obj_names:
                com_name = machine_data[port_obj_name]["board_ports"]
                class_name = machine_data[port_obj_name]["port_option_class"]
                class__ = getattr(sys.modules[__name__], class_name)
                print(inspect.currentframe().f_lineno, __class__, __file__, "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
                print(f"class name is {class_name}, class is {class__}   com_name is {com_name}, mmmmmmmmmmmmmmmmmmmmmmmm")
                pipeGetFromProcessStationWilltoEquepment_inner, board_objs_to_equepment_pipes = Pipe()
                self.board_objs_to_equepment_pipe[port_obj_name] = board_objs_to_equepment_pipes
                obj = None
                # try:
                Process_obj = Process(target=class__, args=(
                             machine_data[port_obj_name],
                             self.pipeSendtoProcessStation,
                             pipeGetFromProcessStationWilltoEquepment_inner))
                Process_obj.start()
                # except Exception as ff:
                #     print(f"{port_obj_name} is not build, im at {inspect.currentframe().f_lineno}, my file is {__file__}")

                if obj is not None:

                    self.board_objs[port_obj_name] = obj
                    self.board_class_map_obj[class_name] = obj



class modbus485(Board_com):
    def __init__(self, portparameter, pipeSendtoProcessStation, pipeGetFromProcessStationWilltoEquepment):
        super(modbus485, self).__init__(portparameter, pipeSendtoProcessStation, pipeGetFromProcessStationWilltoEquepment)
        self.portparameter = data = portparameter
        PORT = data["board_ports"]
        baudrate = data["baudrate"]
        bytesize = data["bytesize"]
        parity = data["parity"]
        stopbits = data["stopbits"]
        xonxoff = data["xonxoff"]
        self.port_time_out = data["port_time_out"]
        self.child_equepment_name_obj = {}
        self.loop_name_timedelta_scan_time = pandas.DataFrame([], columns=loop_index)
        self._485_equepment_class_name_map_obj = {}

        try:
            self.port_obj = testk.get_master(PORT, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits,
                                           xonxoff=xonxoff, )
        except Exception as e:
            print(e)
        self.port485EqupmentNameMapClass = self.get_port_obj_child_equpment()
        self.port_obj_child_equpment_objs = self.creat_equepment()
        self.read_data()
        self.read_write_data()

    def get_port_obj_child_equpment(self):
        data = self.portparameter
        equepments = data.keys()
        equepment_name_map_class = {}
        for equepment in equepments:
            if equepment.startswith("Equepment_"):
                equepment_name_map_class[equepment] = getattr(sys.modules[__name__], data[equepment]["Equepment_class"])
        return equepment_name_map_class

    def creat_equepment(self):
        equepment_parameter_data = self.portparameter
        equepment_name_map_equep_class_obj = {}

        for every_equpment in self.port485EqupmentNameMapClass.keys():
            class_name = self.port485EqupmentNameMapClass[every_equpment]
            obj = class_name(equepment_parameter_data[every_equpment], self.port_obj)
            self._485_equepment_class_name_map_obj[class_name.__name__] = obj
            equepment_name_map_equep_class_obj[class_name] = obj
            self.child_equepment_name_obj[every_equpment] = obj
            self.loop_name_timedelta_scan_time.loc[every_equpment, "last_run_time"] = time.time()
            self.loop_name_timedelta_scan_time.loc[every_equpment, "next_run_time"] = obj.scan_time + self.loop_name_timedelta_scan_time.loc[every_equpment, "last_run_time"]
            try:
                self.loop_name_timedelta_scan_time.loc[every_equpment, "scan_time"] = obj.scan_time
            except Exception:
                self.loop_name_timedelta_scan_time.loc[every_equpment, "scan_time"] = self.port_time_out
            self.loop_name_timedelta_scan_time.loc[every_equpment, "last_run_time"] = time.time()
            self.loop_name_timedelta_scan_time.loc[every_equpment, "delta_run_time"] = self.loop_name_timedelta_scan_time.loc[every_equpment, "next_run_time"] - time.time()
        return equepment_name_map_equep_class_obj

    def read_data_(self):
        loop_name_timedelta_scan_time = self.loop_name_timedelta_scan_time

        time_ = time.time
        child_equepment_name_obj = self.child_equepment_name_obj
        pipeGetFromProcessStationWilltoEquepment = self.pipeGetFromProcessStationWilltoEquepment
        _485_equepment_class_name_map_obj = self._485_equepment_class_name_map_obj

        while True:
            # print(inspect.currentframe().f_lineno, __class__, __file__)
            current_time = time_()
            loop_name_timedelta_scan_time.loc[:, "delta_run_time"] = loop_name_timedelta_scan_time.loc[:, "next_run_time"] - current_time
            loop_name_timedelta_scan_time.loc[:, "delta_run_time"] = loop_name_timedelta_scan_time.loc[:,
                                                                     "delta_run_time"].astype('float64')
            _485_machine_equepment_name = loop_name_timedelta_scan_time.loc[:, "delta_run_time"].idxmin(axis=0)
            current_equepment_obj = child_equepment_name_obj[_485_machine_equepment_name]
            data = current_equepment_obj.read_data()

            slave_id = current_equepment_obj.slave_id
            single_io_type = current_equepment_obj.single_io_type
            single_dig_type = current_equepment_obj.single_dig_type
            port_obj_name = current_equepment_obj.port_obj_name
            if type(slave_id) is tuple:
                slave_id = slave_id[0]
            obj_class = current_equepment_obj.Equepment_class
            current_time2 = time_()
            virtual_pins = current_equepment_obj.virtual_pin
            if data is None:
                for every_ping_ in virtual_pins.keys():
                    ping__ = virtual_pins[every_ping_][1]
                    send_data_ = {current_time2: {
                        (port_obj_name, ping__, single_dig_type, single_io_type, obj_class): None} }
                    self.pipeSendtoProcessStation.send(send_data_)
            else:
                for index in data.keys():
                    send_data_ = {current_time2: {(port_obj_name, (slave_id, index), single_dig_type, single_io_type, obj_class): data[index]}}
                    # virtual_pins[(_485_machine_equepment_name, (slave_id, index), 'ANALOG', 'INPUT', obj_class)] = data[index]
                    self.pipeSendtoProcessStation.send(send_data_)
            loop_name_timedelta_scan_time.loc[_485_machine_equepment_name, "last_run_time"] = current_time2
            loop_name_timedelta_scan_time.loc[_485_machine_equepment_name, "next_run_time"] = current_time2 + loop_name_timedelta_scan_time.loc[_485_machine_equepment_name, "scan_time"]
            if pipeGetFromProcessStationWilltoEquepment.poll():
                data = pipeGetFromProcessStationWilltoEquepment.recv()
                value, ping_ = data
                port_obj_name, port_id, data_type, iotype, equpment_class = ping_
                slave_id, ping_id = port_id
                _485_equepment_class_name_map_obj[equpment_class].write_data(ping_id, value)

    def read_data(self):
        m485_read_process = Thread(target=self.read_data_)
        m485_read_process.start()

    def read_write_data(self, ):
        pipeGetFromProcessStationWilltoEquepment = self.pipeGetFromProcessStationWilltoEquepment
        child_equepment_name_obj = self.child_equepment_name_obj
        while True:
            func_name, pin_id, value = pipeGetFromProcessStationWilltoEquepment.recv()
            equepment_name, pind, data_type, io_Type, class_name = pin_id
            pin_0, pin_ = pind
            obj = child_equepment_name_obj[equepment_name]
            function_ = getattr(obj, func_name)
            function_(pin_, value)

class modbus_rtu_485Beam4mRopeEncodeXiYuWeiYiSensor():
    def __init__(self, equepment_parameter_data, port_obj):
        self.equepment_parameter_data = equepment_parameter_data
        self.port_obj = port_obj
        Read_code = equepment_parameter_data["Read_code"]
        self.shebei_name = equepment_parameter_data["shebei_name"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]

        first_addr_id = equepment_parameter_data["first_addr_id"]
        start_addr = equepment_parameter_data["start_addr"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        date_len = equepment_parameter_data["date_len"]
        operation_code = equepment_parameter_data["operation_code"]
        explain_function = getattr(testk, equepment_parameter_data["explain_function"])
        baudrate = equepment_parameter_data["baudrate"]
        bytesize = equepment_parameter_data["bytesize"]
        parity = equepment_parameter_data["parity"]
        stopbits = equepment_parameter_data["stopbits"]
        xonxoff = equepment_parameter_data["xonxoff"]
        manager_port_number = equepment_parameter_data["manager_port_number"]
        product_name = equepment_parameter_data["product_name"]

        self.scan_time = equepment_parameter_data["scan_time"]
        self.read_function = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len,
                                     operation_code=operation_code, master=self.port_obj,
                                     explain_function=explain_function)

    def setting_point(self, data):
        #function_name, pin_id, value = data
        pass
        # self.master.execute(slave_id, operation_code, start_addr, data_len)

    def write_data(self, data):
        #function_name, pin_id, value = data
        pass

    def read_data(self):
        data = self.read_function()
        return data

    def loop_read_data_regest(self):
        self.port_obj.child_equepment_name_obj[self.shebei_name] = self
        self.port_obj.add_loop(asyncio.wait_for(self.read_data, timeout=self.scan_time))


class modbus_rtu_485_xiAnZz12():
    def __init__(self, equepment_parameter_data, port_obj):
        data = equepment_parameter_data
        self.port_obj = port_obj
        # Read_code = data["Read_code"]
        self.shebei_name = data["shebei_name"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]
        first_addr_id = data["first_addr_id"]
        start_addr = data["start_addr"]
        date_len = data["date_len"]
        operation_code = data["operation_code"]
        explain_function = getattr(testk, data["explain_function"])
        baudrate = data["baudrate"]
        bytesize = data["bytesize"]
        parity = data["parity"]
        stopbits = data["stopbits"]
        xonxoff = data["xonxoff"]
        manager_port_number = data["manager_port_number"]
        product_name = data["product_name"]
        self.scan_time = data["scan_time"]
        self.read_function = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len,
                                     operation_code=operation_code, master=self.port_obj,
                                     explain_function=explain_function)
        self.pipeout = self.scan_time

    def setting_point(self, data):
        pass
        # self.master.execute(slave_id, operation_code, start_addr, data_len)

    def write_data(self, data):
        pass

    def read_data(self):
        data = self.read_function()
        return data


class modbus_rtu_485_xiAnZz8():
    def __init__(self, equepment_parameter_data, port_obj):
        self.port_obj = port_obj
        Read_code = equepment_parameter_data["Read_code"]
        self.shebei_name = equepment_parameter_data["shebei_name"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]
        start_addr = equepment_parameter_data["start_addr"]
        date_len = equepment_parameter_data["date_len"]
        operation_code = equepment_parameter_data["operation_code"]
        first_addr_id = equepment_parameter_data["first_addr_id"]
        baudrate = equepment_parameter_data["baudrate"]
        bytesize = equepment_parameter_data["bytesize"]
        parity = equepment_parameter_data["parity"]
        stopbits = equepment_parameter_data["stopbits"]
        xonxoff = equepment_parameter_data["xonxoff"]
        manager_port_number = equepment_parameter_data["manager_port_number"]
        product_name = equepment_parameter_data["product_name"]
        explain_function = getattr(testk, equepment_parameter_data["explain_function"])
        self.scan_time = equepment_parameter_data["scan_time"]
        self.read_function = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len,
                                     operation_code=operation_code, master=self.port_obj,
                                     explain_function=explain_function)

    def setting_point(self, data):
        pass
        # self.master.execute(slave_id, operation_code, start_addr, data_len)

    def write_data(self, data):
        pass

    def read_data(self):
        data = self.read_function()
        return data


class modbus_rtu_485_WeiTeAngleSensor():
    def __init__(self, equepment_parameter_data, port_obj):
        self.port_obj = port_obj
        Read_code = equepment_parameter_data["Read_code"]
        self.shebei_name = equepment_parameter_data["shebei_name"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]
        first_addr_id = equepment_parameter_data["first_addr_id"]
        start_addr = equepment_parameter_data["start_addr"]
        date_len = equepment_parameter_data["date_len"]
        operation_code = equepment_parameter_data["operation_code"]
        baudrate = equepment_parameter_data["baudrate"]
        bytesize = equepment_parameter_data["bytesize"]
        parity = equepment_parameter_data["parity"]
        stopbits = equepment_parameter_data["stopbits"]
        xonxoff = equepment_parameter_data["xonxoff"]
        manager_port_number = equepment_parameter_data["manager_port_number"]
        # translate_function = equepment_parameter_data["translate_function"]
        product_name = equepment_parameter_data["product_name"]
        explain_function = getattr(testk, equepment_parameter_data["explain_function"])
        self.scan_time = equepment_parameter_data["scan_time"]
        self.read_function = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len,
                                     operation_code=operation_code, master=self.port_obj,
                                     explain_function=explain_function)

    def setting_point(self, data):
        pass
        # self.master.execute(slave_id, operation_code, start_addr, data_len)

    def write_data(self, data):
        pass

    def read_data(self):
        data = self.read_function()
        return data


class modbus_rtu_485_DrillBoxHandOperatioOuMuLong8():
    def __init__(self, equepment_parameter_data, port_obj):
        self.port_obj = port_obj
        Read_code = equepment_parameter_data["Read_code"]
        self.shebei_name = equepment_parameter_data["shebei_name"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]
        first_addr_id = equepment_parameter_data["first_addr_id"]
        start_addr = equepment_parameter_data["start_addr"]
        date_len = equepment_parameter_data["date_len"]
        operation_code = equepment_parameter_data["operation_code"]
        baudrate = equepment_parameter_data["baudrate"]
        bytesize = equepment_parameter_data["bytesize"]
        parity = equepment_parameter_data["parity"]
        stopbits = equepment_parameter_data["stopbits"]
        xonxoff = equepment_parameter_data["xonxoff"]
        manager_port_number = equepment_parameter_data["manager_port_number"]
        # translate_function = equepment_parameter_data["translate_function"]
        product_name = equepment_parameter_data["product_name"]
        # explain_function = getattr(testk, equepment_parameter_data["explain_function"])
        self.scan_time = equepment_parameter_data["scan_time"]
        # self.write_data_ = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len, operation_code=testk.cst.WRITE_SINGLE_COIL,
        #                   master=testk.master1_nomale, output_value=0x0000)
        self.write_data_ = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len, operation_code=testk.cst.WRITE_SINGLE_COIL,
                          master=self.port_obj)


    def setting_point(self, data):
        pass


    def write_data(self, data):
        # position_code = 0x0001 0x0002 ....0x0007
        # value = 0xFF00  0x0000  the 0FF00 is on  and  0x0000 is off
        # ('modbus485__', ((4,), 11), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz12')
        function_name, pin_, output_value_ = data

        if output_value_ is True:
            output_value = 255
        else:
            output_value = 0
        slaveid, start_addr = pin_[1]
        rdata = self.write_data_(start_addr=start_addr, output_value=output_value)
        return rdata

    def read_data(self):
        pass


class modbus_rtu_485_main_beam_4m_abs_encodeWuXiHaoBang64():
    def __init__(self, equepment_parameter_data, port_obj):
        self.port_obj = port_obj
        Read_code = equepment_parameter_data["Read_code"]
        self.shebei_name = equepment_parameter_data["shebei_name"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        first_addr_id = equepment_parameter_data["first_addr_id"]
        start_addr = equepment_parameter_data["start_addr"]
        date_len = equepment_parameter_data["date_len"]
        operation_code = equepment_parameter_data["operation_code"]
        baudrate = equepment_parameter_data["baudrate"]
        bytesize = equepment_parameter_data["bytesize"]
        parity = equepment_parameter_data["parity"]
        stopbits = equepment_parameter_data["stopbits"]
        xonxoff = equepment_parameter_data["xonxoff"]
        manager_port_number = equepment_parameter_data["manager_port_number"]
        # translate_function = equepment_parameter_data["translate_function"]
        product_name = equepment_parameter_data["product_name"]
        explain_function = getattr(testk, equepment_parameter_data["explain_function"])
        self.scan_time = equepment_parameter_data["scan_time"]
        self.read_function = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len,
                                     operation_code=operation_code, master=self.port_obj,
                                     explain_function=explain_function)


    def setting_point(self, data):
        pass

    def write_data(self,  data):

        pass

    def read_data(self):
        data = self.read_function()
        return data

#********************************************************************************************************************next com

class modbus485__2(modbus485):
    pass




class modbus485__2_MainBeam_4mRopeEncode():
    def __init__(self, equepment_parameter_data, port_obj):
        self.port_obj = port_obj
        Read_code = equepment_parameter_data["Read_code"]
        self.shebei_name = equepment_parameter_data["shebei_name"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        first_addr_id = equepment_parameter_data["first_addr_id"]
        start_addr = equepment_parameter_data["start_addr"]
        date_len = equepment_parameter_data["date_len"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]
        operation_code = equepment_parameter_data["operation_code"]
        baudrate = equepment_parameter_data["baudrate"]
        bytesize = equepment_parameter_data["bytesize"]
        parity = equepment_parameter_data["parity"]
        stopbits = equepment_parameter_data["stopbits"]
        xonxoff = equepment_parameter_data["xonxoff"]
        manager_port_number = equepment_parameter_data["manager_port_number"]
        translate_function = equepment_parameter_data["translate_function"]
        product_name = equepment_parameter_data["product_name"]
        explain_function = getattr(testk, equepment_parameter_data["explain_function"])
        self.scan_time = equepment_parameter_data["scan_time"]
        self.read_function = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len,
                                     operation_code=operation_code, master=self.port_obj,
                                     explain_function=explain_function)

    def setting_point(self, data):
        pass

    def write_data(self, data):
        pass

    def read_data(self):
        data = self.read_function()
        return data


class modbus485__2_BoxHand1mRopeEncode():
    def __init__(self, equepment_parameter_data, port_obj):
        self.port_obj = port_obj
        Read_code = equepment_parameter_data["Read_code"]
        self.shebei_name = equepment_parameter_data["shebei_name"]
        self.slave_id = slave_id = equepment_parameter_data["slave_id"]
        self.Equepment_class = equepment_parameter_data["Equepment_class"]
        self.port_obj_name = equepment_parameter_data["port_obj_name"]
        self.virtual_pin = equepment_parameter_data["virtual_pin"]
        self.single_io_type = equepment_parameter_data["single_io_type"]
        self.single_dig_type = equepment_parameter_data["single_dig_type"]
        first_addr_id = equepment_parameter_data["first_addr_id"]
        start_addr = equepment_parameter_data["start_addr"]
        date_len = equepment_parameter_data["date_len"]
        operation_code = equepment_parameter_data["operation_code"]
        baudrate = equepment_parameter_data["baudrate"]
        bytesize = equepment_parameter_data["bytesize"]
        parity = equepment_parameter_data["parity"]
        stopbits = equepment_parameter_data["stopbits"]
        xonxoff = equepment_parameter_data["xonxoff"]
        manager_port_number = equepment_parameter_data["manager_port_number"]
        # translate_function = equepment_parameter_data["translate_function"]
        product_name = equepment_parameter_data["product_name"]
        explain_function = getattr(testk, equepment_parameter_data["explain_function"])
        self.scan_time = equepment_parameter_data["scan_time"]
        self.read_function = partial(testk.modbus_getdate, slave_id=slave_id, start_addr=start_addr, date_len=date_len,
                                     operation_code=operation_code, master=self.port_obj,
                                     explain_function=explain_function)

    def setting_point(self, data):
        pass

    def write_data(self, data):
        pass

    def read_data(self):
        data = self.read_function()
        return data


class borad_wrong():
    def __init__(self, single):
        self.single = single

    def __str__(self):
        return self.single

    def getisetin_data(self):
       setting_data = seting.machine_one
       self.port_all_need_read_pin ={}
       temple = set()
       for key_board, value_board in setting_data.items():

           for key_equepment,value_equepument in value_board.items():
               try:
                   for key_equepment_part,value_equepument_part in value_equepument.items():
                       if "_pin" in key_equepment_part:
                           temple.add(value_equepument_part)

               except:
                   pass
       self.port_all_need_read_pin = list(temple)

def get_(pipe_read_from_machine_board):
    while True:
        DATA = pipe_read_from_machine_board.recv()
        print(DATA)
        # data format is {1643971608.0018759: {('modbus485__', (1, 6), 'ANALOG', 'OUTPUT', 'modbus_rtu_485_xiAnZz8'): None}}


if __name__ == "__main__":

    pipeGetFromProcessStationWilltoEquepment, pipe_write_write = Pipe()
    pipe_read_from_machine_board, pipeSendtoProcessStation = Pipe()

    pipe_write_back_read, pipe_write_back_write = Pipe()
    # _modbus485 = modbus485(seting.machine_one["modbus485__"], pipeSendtoProcessStation, pipe_write_back_read)
    # _modbus485 = modbus485(seting.machine_one["modbus485__2"], pipeSendtoProcessStation, pipe_write_back_read)
    Thread_P = Thread(target=get_, args=(pipe_read_from_machine_board, ))
    Thread_P.start()
    machine_port_obj = ReadWrite(pipeSendtoProcessStation, pipeGetFromProcessStationWilltoEquepment)
