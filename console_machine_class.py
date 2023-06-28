"""
this machine class run in the console,
"""

from abc import abstractmethod, ABC
import queue
import wmi
import pickle
import pandas as pd
import numpy as np


class Machine(ABC):
    one = None
    def __init__(self, obj_name, cpu_bios_id):
        self.obj_name = obj_name
        self.cup_id, self.bios_id = cpu_bios_id
        self.obj_class = None
        self.come_from_machine = queue.Queue()
        self.come_from_operator = queue.Queue()
        self.tomachine = queue.Queue()
        self.to_operator = queue.Queue()

    def __new__(cls, *args, **kwargs):
        if Machine.one == None:
            obj = object.__new__(Machine)
            Machine.one = obj
            return obj
        else:
            return Machine.one


    @abstractmethod
    def get_machine_parameter(self):
        return "machine obj class relation map table"

    def receive_data(self, responds):
        """
        responds is the data come from server socket.  come from network , and the console_station_socket.py processed
        and distribute to the every machine .
        :return:
        """
        pass

    def send_data(self, request):
        pass

    def get_run_py_code(self):
            """
            :return: (hasmd5_data, programe_code)
            """
            selfmachine_cilent = open("machin_cilent.py", "r")
            data = ""
            for every_line in selfmachine_cilent:
                data = data + every_line
            data = pickle.dumps(data )
            return data

    def get_bios_cpu_number(self):
        data = wmi.WMI()

        for cpu in data.Win32_Processor():
            cup_id = cpu.ProcessorId.strip()

        for bios in data.Win32_BaseBoard():
            bios_id = bios.SerialNumber
        return cup_id, bios_id


class terminal_code(Machine):

    def get_machine_parameter(self):
        return "machine obj class relation map table"


tt = terminal_code(1, 2)
cc = tt.get_bios_cpu_number()
print(cc)