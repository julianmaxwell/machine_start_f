import queue
import socket
import wmi
import struct
import pickle

from threading import Thread, Lock, Event
from multiprocessing import Process, Lock, Event, Queue

from_console = queue.Queue()
from_self = queue.Queue()
host_data = "192.168.1.188"
port_send = 7000
port_recve = 7500
ipdata_send = (host_data, port_send)
ipdata_reve = (host_data, port_recve)
buffer = 1024
first_recev_data_buffer = 4

class machin_run:
    def __init__(self):
        self.authenticate = False
        self.recve_que = queue.Queue()
        self.send_que = queue.Queue()
        self.thread_send_to_console = Thread(target=self.send)
        self.thread_send_to_console.setDaemon(True)
        self.thread_recve_from_console = Thread(target=self.recve)
        self.thread_recve_from_console.setDaemon(True)

    def get_run_py(self):
        selfmachine_cilent = open("machin_cilent.py", "r")
        data = ""
        for every_line in selfmachine_cilent:
            data = data + every_line
        data = pickle.dumps(data)

        return data

    def get_bios_cpu_number(self):
        data = wmi.WMI()
        for cpu in data.Win32_Processor():
            cup_id = cpu.ProcessorId.strip()
        for bios in data.Win32_BaseBoard():
            bios_id = bios.SerialNumber
        return cup_id, bios_id

    def send(self):
        while True:
            data = self.send_que.get()
            self.send_data_to_console_station_(data)

    def recve(self):
        while True:
            data = self.recve_data_from_console_station()
            self.recve_que.put(data)

    def send_data_to_console_station_(self, data, send_slice_lenth=buffer):
        while True:
            self.send_data_toconsole = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.send_data_toconsole.connect(ipdata_send)
            if type(data) == bytes:
                l_ = len(data)
                l_s = struct.pack("i", l_)
            else:
                data = pickle.dumps(data)
                l_ = len(data)
                l_s = struct.pack("i", l_)
            while True:
                try:
                    self.send_data_toconsole.send(l_s)
                    lr = self.send_data_toconsole.recv(l_)
                except Exception as e:
                    print(e)
                    break
                if lr != l_s:
                    continue
                else:
                    while True:
                        try:

                            b = data[:send_slice_lenth]
                            if len(b) == 0:
                                lr__ = self.send_data_toconsole.recv(l_)
                                if lr__ != l_:
                                    break
                                else:
                                    return True
                            for bb in b:
                                data.remove(bb)
                            self.send_data_toconsole.send(b)
                            print(len(data), list(data))
                        except Exception as e:
                            print(e)
                            break

    def recve_data_from_console_station(self):
        """
        the return data has pickle.unpack not bytes
        :return:
        """
        while True:
            self.getdata = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.getdata.connect(ipdata_reve)
            lr = 0
            lrb = None
            ddata = b""
            while True:
                if lr == 0:
                    try:
                        lr = self.getdata.recv(first_recev_data_buffer)
                        self.getdata.send(lr)
                    except Exception as e:
                        print(e)
                        break
                else:
                    if lrb == None:
                        lrb = struct.unpack("i", lr)
                    else:
                        if lrb > buffer:
                            data = self.getdata.recv(buffer)
                            lrb = lrb - buffer
                            ddata = ddata + data
                        else:
                            data = self.getdata.recv(lrb)
                            ddata = ddata + data
                            ddata = pickle.unpack(ddata)
                            return ddata

    def run(self):
        self.thread_recve_from_console.start()
        self.thread_send_to_console.start()
        while True:
            if self.authenticate == False:
                data = self.get_bios_cpu_number()
                cpu_bios_id = {"cpu_bios_id", data}
                program_code_ = self.get_run_py()
                program_code = {"program_code": program_code_}
                self.send_que.put(cpu_bios_id)
                self.send_que.put(program_code)
            order_name, value = self.recve_que.get()
            if order_name == "authenticate":
                if value is True:
                    self.authenticate = True
                    break
                else:
                    continue
        if self.authenticate is True:
            key, value = self.recve_que.get()
            if key == "runcode":
                exec(value)









test = machin_run()
test.get_run_py()
cup_id, bios_id = test.get_bios_cpu_number()
print(cup_id, bios_id)
test.run()
