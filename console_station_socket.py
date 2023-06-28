import queue
from multiprocessing import Queue as PQue
import socket
import struct
import pickle
import selectors
import gc

from threading import Thread, Lock, Event


start_port = 6500
end_port = 8000
from_console = queue.Queue()
from_self = queue.Queue()
host_data = "127.0.0.1"
dispath_port = start_port



buffer = 1024
first_recev_data_buffer = 4


class SeverRun:
    """
    here just finish the function : 1 receive the client program code , 2 send server data, 3 give a interface ,let the
    machine obj register in self.machine_obj.
    this class only distribute tasks use the machine obj dictionary , do nothing others.
    """
    def __init__(self, cilent_machine_recive_que, cilent_machine_send_que):
        self.authenticate = False
        self.cilent_machine_recive_que = cilent_machine_recive_que
        self.cilent_machine_send_que = cilent_machine_send_que
        self.distrbute_que = PQue()
        self.authenticate_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.console_station_ = selectors.DefaultSelector()
        self.machine_obj = {}   # key is (machine_bios_id, machine_cpu_id) , value is the program_code's has data
        self.consel_out_ip = self.get_console_ip_add()
        print(self.consel_out_ip)

    def run(self):

        send_thread = Thread(target=self.send)
        send_thread.start()
        print("okok"*20)
        self.authenticate_socket.bind((host_data, dispath_port))
        self.authenticate_socket.listen(2)
        self.console_station_.register(self.authenticate_socket, selectors.EVENT_READ, self.access_machine)

        self.console_station_.select()

    def access_machine(self, socket, mask):
        """
        here receive the machine request , and authenticate and machine operator the machine. if true create the
        machine obj
        :return:
        """
        cnn, addr = socket.accept()
        cnn.setblocking(False)
        cnn.ipaddr = addr
        self.console_station_.register(cnn, selectors.EVENT_READ, self.receive_and_distribute_ip_create_port)


    def receive_and_distribute_ip_create_port(self, sockecnn, mask):
        """
        here send the ip addr in ip pool and creat the machine obj operator connect
        :param cnn:
        :param mask:
        :dddata is the machine coming data , use it  can  create new machine obj , it's format is :
        {machin_cpu_id:12345678, machine_bios_id: 12345678, pwd, machine_program_code: "xxxxxxxxxx"}
        """
        ipaddr = sockecnn.ipaddr
        lrb = None
        ddata = b""
        while True:

            lr = self.sockecnn.recv(first_recev_data_buffer)
            if lr:
                self.sockecnn.send(lr)
            else:
                self.console_station_.unregister(self.sockecnn)
                self.prepair_socket(ipaddr)
                break
            if lrb == None:
                lrb = struct.unpack("i", lr)
            else:
                if lrb > buffer:
                    data = self.sockecnn.recv(buffer)
                    if data:
                        lrb = lrb - buffer
                        ddata = ddata + data
                    else:
                        self.console_station_.unregister(self.sockecnn)
                        self.prepair_socket(ipaddr)
                        ddata = b""
                        break
                else:
                    data = self.sockecnn.recv(lrb)
                    if data:
                        ddata = ddata + data
                        ddata = pickle.loads(ddata)
                        self.distrbute_que.put(ddata)    # here put the receive order to the que
                        self.sockecnn.close()
                        self.prepair_socket(ipaddr)
                    else:
                        self.console_station_.unregister(self.sockecnn)
                        self.prepair_socket(ipaddr)

                        ddata = b""
                        break


    def prepair_socket(self, ipaddr):
        self.sockecnn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockecnn.bind(ipaddr)
        self.sockecnn.listen(ipaddr)
        self.console_station_.register(self.sockecnn, selectors.EVENT_READ, self.access_machine)

    def send(self):
        while True:
            data = self.cilent_machine_recive_que.get()
            self.send_data(data)

    def recve(self):
        while True:
            data = self.recve_data_from_machine()
            self.cilent_machine_recive_que.put(data)

    def send_data(self, cnn, mask):
        while True:
            self.send_data_toconsole = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.send_data_toconsole.bind(ipdata_send)
            self.send_data_toconsole.listen(10)
            conn, addr = self.send_data_toconsole.accept()
            if type(data) == bytes:
                l_ = len(data)
                l_s = struct.pack("i", l_)
            else:
                data = pickle.dumps(data)
                l_ = len(data)
                l_s = struct.pack("i", l_)
            while True:
                try:
                    conn.send(l_s)
                    lr = conn.recv(l_)
                except:
                    conn.close()
                    break
                if lr != l_s or (lr is None):
                    conn.close()
                else:
                    while True:
                        try:
                            b = data[:send_slice_lenth]
                            if len(b) == 0:
                                lr__ = conn.recv(l_)
                                if lr__ != l_:
                                    conn.close()
                                    break
                                else:
                                    conn.close()
                                    return True
                            for bb in b:
                                data.remove(bb)
                            conn.send(b)
                            print(len(data), list(data))
                        except Exception as e:
                            print(e)
                            try:
                                conn.close()
                            except:
                                pass
                            break

    def recve_data(self, sockecnn, mask):
        # while True:
        #     self.sockecnn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     self.sockecnn.connect(ipdata_reve)
            ipaddr = sockecnn.ipaddr

            while True:

                    lr = self.sockecnn.recv(first_recev_data_buffer)
                    if lr:
                        self.sockecnn.send(lr)
                    else:
                        self.sockecnn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.sockecnn.connect(ipaddr)
                        self.console_station_.register(self.sockecnn, selectors.EVENT_READ, self.access_machine)
                    if lrb == None:
                        lrb = struct.unpack("i", lr)
                    else:
                        if lrb > buffer:
                            data = self.sockecnn.recv(buffer)
                            lrb = lrb - buffer
                            ddata = ddata + data
                        else:
                            data = self.sockecnn.recv(lrb)
                            ddata = ddata + data
                            ddata = pickle.unpack(ddata)
                            return ddata

    def get_distribute_port_pool(self):
        pass

    def getsysused_port(self):
        import re
        import subprocess
        x = subprocess.Popen("netstat -ano", shell=True, stdout=subprocess.PIPE)
        dd, ee = x.communicate()
        ffind = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)"
        zz = dd.decode(encoding="gbk")
        ff = re.findall(ffind, zz)
        fff = map(int, ff)
        data = sorted(list(set(fff)))
        return data

    def get_socket_ip(self, start_ip=5000, end_ip=15000):

        used_ip = set(self.getsysused_port())
        if not used_ip:
            start_ip = end_ip
            end_ip = end_ip + 10000
            used_ip = set(self.getsysused_port())
        all_ip = set(range(start_ip, end_ip))
        new_ip = all_ip - used_ip
        new_ip = list(new_ip)
        new_ip.sort()
        return new_ip[0:4]

    def get_console_ip_add(self):
        import subprocess
        import re
        X = subprocess.Popen(r"ipconfig", shell=True, stdout=subprocess.PIPE)
        out_, error = X.communicate()
        out_ = out_.decode(encoding="gbk")
        print(out_)
        # ip_addr = re.findall(r"(IPv4 地址[\.,\s]+) :(\d+\.\d+\.\d+\.\d+)\s", out_)
        # ip_addr = re.findall(r"IPv4 地址 . . . . . . . . . . . . : (.+)\s", out_)
        ip_addr = re.findall(r"IPv4 地址 (\. )+: (.+)\s", out_)
        ip_addr_outer, ip_addr_inner = ip_addr[0][1], ip_addr[1][1]
        return ip_addr_outer.strip(),  ip_addr_inner.strip()

class ServerMachine:
    """
    here the obj create as the machine receive the machine cpu id and the bios id for find the machine obj name. and
    create the machine obj.  economise the memory and computational power , not create all machine obj begin .
    """
    def __init__(self):
        self.dictionary = {}

    def get_every_machine_parameter(self):
        pass

    def create_and_register_machine_obj(self):
        pass

    def destroy_machine_obj(self, obj):
        del obj
        gc.collect()

if __name__ == "__main__":
    test = SeverRun(2, 3)
    data = test.getsysused_port()
    data_ip = test.get_socket_ip()
    print(len(data), data)
    print(data_ip)
    print(test.get_console_ip_add())

