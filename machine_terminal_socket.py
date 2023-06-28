import inspect
import traceback
from functools import partial
import selectors
import socket
import struct
import pickle
from threading import Thread, Lock
from queue import Queue as Tque
from multiprocessing import Pipe
import seting as setting
from inspect import currentframe, isfunction, iscoroutine
import asyncio
import time
import setting as process_computer
import pandas

lisen_number = 5
threading_pool_number = 38
process_pool_number = 3
first_recev_data_buffer = setting.first_recev_data_buffer
normal_buffer = setting.normal_buffer
bchange_code = struct.pack("b", 0) + struct.pack("b", 3)
b_struct_code_0 = struct.pack("b", 0)
function_code4 = str(struct.pack("i", 4))  # generator, will back data
function_code5 = str(struct.pack("i", 5))    #generator back function
function_code6 = str(struct.pack("i", 6))    # machine_ task  can run it will in add_task function
function_code7 = str(struct.pack("i", 7))    # if function_code7 , main_control_class will let the data to the communication pipe, and do nothing.
function_code8 = str(struct.pack("i", 8))    # if function_code8 , main_control_class will let the data to the communication pipe, and do nothing, the communication
function_code9 = str(struct.pack("i", 9))    # if function_code9 , only run in the communication module




function_code99 = str(struct.pack("i", 99))  # only run in the task_loop

"""
data format is machine_id inner_function_code target_function args .....
"""



class Client_socket:
    def __init__(self,
                 orderSendToMachineProcessPipe,
                 port_data=None,
                 data=None,
                 keep=False,
                 socket_=None,
                 selctor_obj=None,
                 client_attr="lisent"):
        self.current_function_code_s = 0
        self.orderSendToMachineProcessPipe = orderSendToMachineProcessPipe
        self.client_attr = client_attr      # value  "lisent_port" or  "send_port"
        self.master_slave = "None"
        self.loop_lock = Lock()
        self.selctor_obj = selctor_obj
        self.data = data
        self.keep = keep
        self.port_data = port_data
        self.regester_event_s = None
        self.regester_event_r = selectors.EVENT_READ
        self.re_set_socke_s_times = 0
        self.len_send = 0
        self.data_r_statue = 0
        self.re_set_socke_begeintime = None
        self.loop_appllay = False
        if port_data is None:
            # self.conenct_port = setting.communication_dict["listen_manager_sever_ip"][0]
            self.conenct_port = setting.listen_port
        else:
            self.conenct_port = port_data
        if socket_ is None:
            self.connect_socket = socket.socket()
            if self.conenct_port == setting.local_host:
                self.connect_socket.bind(self.conenct_port)
                self.connect_socket.listen(5)
                self.connect_socket.setblocking(False)
        else:
            self.connect_socket = socket_
        self.data = b''


    def get_new_target_socket(self):
        return setting.send_defalut_target_port

    def re_set_socke_s(self, function_code):
        if self.client_attr == "send_port":
            self.loop_lock.acquire()
            if self.re_set_socke_s_times == 0:
                statues = 0
                statues_dict = {}
                target_addr = self.get_new_target_socket()
                self.selctor_obj.selector_.unregister(self.connect_socket)
                self.connect_socket.close()
                self.re_set_socke_s_times = 1
                self.re_set_socke_begeintime = time.time()
            if self.re_set_socke_s_times == 1:
                    self.connect_socket = socket.socket()
                    self.connect_socket.setblocking(False)
                    try:
                        self.connect_socket.connect(target_addr)
                        self.selctor_obj.selector_.register(self.connect_socket, selectors.EVENT_WRITE, self.re_set_socke_s)
                        self.re_set_socke_s_times = 2
                        self.step0 = 0
                    except Exception:
                        self.step0 = 0
                        self.re_set_socke_s_times = 1
                        raise Exception
            if self.re_set_socke_s_times == 2:
                self.step0 = self.step0 + 1
                if self.step0 == 2:
                    if statues_dict.get(function_code, None) is None:
                        statues_dict[statues] = struct.pack("i", statues)
                    try:
                        self.connect_socket.send(setting.b_machine_id_len + statues_dict[statues] + setting.bmachine_id)
                        self.re_set_socke_s_times = 4
                        self.selctor_obj.selector_.modify(self.connect_socket, selectors.EVENT_READ, self.re_set_socke_s)
                        self.step0 = 0
                    except Exception:
                        self.step0 = 0
                        self.re_set_socke_s_times = 1
                        raise Exception

            if self.re_set_socke_s_times == 4:
                self.step0 = self.step0 + 1
                if self.step0 == 2:
                        try:
                            machine_len = self.connect_socket.recv(4)
                            if machine_len == setting.b_machine_id_len:
                                self.re_set_socke_s_times = 5
                                self.step0 = 0
                            else:
                                self.re_set_socke_s_times = 0
                                self.step0 = 0
                                raise Exception
                        except Exception:
                            self.step0 = 0
                            self.re_set_socke_s_times = 0
                            raise Exception


# next is the re connext work is over, the handle change to the  do_send.
            if self.re_set_socke_s_times == 5:
                        self.selctor_obj.clients[self.connect_socket] = self
                        self.selctor_obj.port_map_obj[target_addr] = self
                        self.selctor_obj.selector_.modify(self.connect_socket, self.regester_event_s, self.selctor_obj.do_send)
                        self.re_set_socke_s_times = 0
                        self.step0 = 0
                        return True
        # return True means loop will be stop , responds will be process only by do_send
            self.loop_lock.release()

    async def sendData(self, data, key, mask):
        sock = key.fileobj
        data_send = pickle.dumps(data)
        data_len = len(data_send)
        data_len_b = struct.pack("i", data_len)
        buffer_b_size = struct.pack("i", 1024)
        current_function_code_s = self.current_function_code_s
        sleep = asyncio.sleep
        while True:
            # innit data
            if self.len_send == 0:
                # send data len
                try:
                    current_function_code_s = 0
                    self.regester_event_s = selectors.EVENT_WRITE
                    self.selctor_obj.selector_.unregister(self.selctor_obj.fileobj)
                    sock.send(data_len_b)
                    self.selctor_obj.selector_.register(sock, selectors.EVENT_WRITE, self.sendData)
                    self.regester_event_s = selectors.EVENT_WRITE
                    self.len_send = 1
                    await sleep(0)
                except:
                    current_function_code_s = 0

# judge data send step
            if self.len_send == 1:
                if len(data_send) > setting.normal_buffer:
                    self.len_send = 2
                    function_code = struct.pack("b", 0) + struct.pack("b", 1)
                elif len(data_send) == setting.normal_buffer:
                    function_code = struct.pack("b", 0) + struct.pack("b", 2)
                else:
                    self.len_send = 10
# send 0--n*1024 data
            if self.len_send == 2:
                data_send_s = data_send[0:, setting.normal_buffer]
                del data_send[0:, setting.normal_buffer]
                self.len_send = 4
            if self.len_send == 4:
                try:
                            a = self.make_code()
                            sock.send(a)
                            sock.send(buffer_b_size)
                            sock.send(data_send_s)
                            self.len_send = 5
                            self.regester_event_s = selectors.EVENT_READ
                            self.selctor_obj.selector_.unregister(self.selctor_obj.fileobj)
                            self.selctor_obj.selector_.register(sock, selectors.EVENT_WRITE, self.sendData)
                            await sleep(0)
                except Exception as e:
                    traceback.print_exc()
                    self.selctor_obj.add_task(self.re_set_socke_s(self.len_send))
            if self.len_send == 5:
                self.selctor_obj.selector_.modify(sock, selectors.EVENT_READ, self.sendData)
                self.len_send = 6
                await sleep(0)
            if self.len_send == 6:
                try:
                    back_dd = sock.recv(8)
                    if back_dd == b"" or len(back_dd) < 8:
                        raise Exception
                    back_ = back_dd[0:4]
                    # back_ = sock.recv(4)
                    back_code_ = struct.unpack("i", back_)
                    len_back = back_dd[4:]
                    # len_back = sock.recv(4)
                except Exception:
                    self.selctor_obj.add_task(self.re_set_socke_s(self.len_send))
                if back_code_ == 1:
                    if len_back == buffer_b_size:
                        if data_len > setting.normal_buffer: #### here decide to last or return top 0
                            self.len_send = 2
                        elif data_len == 0:
                            self.len_send = 2

                        else:
                            self.len_send = 10
                        self.selctor_obj.selector_.modify(sock, selectors.EVENT_WRITE, self.sendData)
                        self.regester_event_s = selectors.EVENT_WRITE
                        await sleep(0)

                    else:
                        raise Exception

                else:
                    self.len_send = back_code_



# send last <1024 data
            elif self.len_send == 10:
                    data_send_s = data_send
                    data_len = len(data_send_s)
                    data_send = b""
                    data_len_s = struct.pack("i", data_len)
                    self.len_send = 12
                    current_function_code_s = 12
            elif self.len_send == 12:
                    try:
                        b_code = struct.pack("i", current_function_code_s)
                        sock.send(b_code)
                        sock.send(data_len_s)
                        sock.send(data_send_s)
                        self.len_send = 13
                        self.selctor_obj.selector_.modify(sock, selectors.EVENT_READ, self.senddata)
                        self.regester_event_s = selectors.EVENT_READ
                        await sleep(0)
                    except Exception:
                        traceback.print_exc()

            elif self.len_send == 13:
                try:
                    back_dd_ = sock.recv(8)
                    if not back_dd_ or (len(back_dd_) < 8):
                        raise Exception
                    back_ = back_dd_[0:4]
                    back_code_ = struct.unpack("i", back_)
                    len_back = back_dd_[4:]
                    # len_back = sock.recv(4)
                    if back_ == b"":
                        raise Exception
                    if len_back == b"":
                        raise Exception
                    if back_code_ == 1:
                        if len_back == buffer_b_size:
                            self.selctor_obj.selector_.unregister(sock)
                            del self.selctor_obj.clients[sock]
                            del self.selctor_obj.machine_id_map_obj[setting.bmachine_id]
                            sock.close()
                            self.len_send = 0
                            len_back = 0
                            return True
                        else:
                            self.len_send = 12
                            raise Exception
                    else:
                        self.len_send = back_code_
                except Exception:
                    pass
            elif self.len_send == 14:
                self.selctor_obj.selector_.unregister(sock)
                del self.selctor_obj.clients[sock]
                del self.selctor_obj.machine_id_map_obj[setting.bmachine_id]
                sock.close()
                self.len_send = 0
                return True

    def end_and_close(self):
        self.selctor_obj.selector_.unregister(self.connect_socket)
        del self.selctor_obj.clients[self.connect_socket]
        del self.selctor_obj.machine_id_map_obj[setting.bmachine_id]
        self.connect_socket.close()
        self.len_send = 0
        return True

    def end_still_keep_socket(self):
        if self.master_slave == "slave":
            pass # slave must send back over data.

        self.selctor_obj.selector_.modify(self.connect_socket, selectors.EVENT_READ, self.recieveData)
        self.regester_event_s = selectors.EVENT_READ

    def make_code(self, function_code=None):
        if self.client_attr == "lisent_port":
            if self.master_slave == "master":
                a = struct.pack("b", 1) + struct.pack("b", 0)
            else:
                a = struct.pack("b", 0) + struct.pack("b", 1)
        elif self.client_attr == "send_port":
            if self.master_slave == "master":
                a = struct.pack("b", 0) + struct.pack("b", 1)
            else:
                a = struct.pack("b", 1) + struct.pack("b", 0)
        if function_code is None:
            function_code_ = struct.pack("b", 0) + struct.pack("b", 1)
            function_code = a + function_code_
            return function_code

    def function_code_process(self, function_code):
        if function_code[2:] == bchange_code:
            new_code12 = 12
            if self.master_slave == "master":
                self.master_slave = "slave"
            else:
                self.master_slave = "master"
        if self.master_slave == "slave":
            try:
                self.function_code_map_function[function_code[2:]]()
            except Exception:
                self.function_code_default_process()


    def function_code_default_process(self):
        return True



    def recieveData(self, key, mask):
        recieve_data = self.recieveData
        regester_event_r = self.regester_event_r
        data_r_statue = self.data_r_statue
        selctor_obj = self.selctor_obj

        sock = key.fileobj
        all_data = b''
        all_data_l = 0
        data_r_statue = 0
        recv_detect = 0
        buffer_b_size = struct.pack("i", 1024)
        data_taile = 0
        regester_event_r = selectors.EVENT_READ
        if mask & selectors.EVENT_READ:
            pass
        else:
            selctor_obj.selector_.modify(sock, selectors.EVENT_READ, recieve_data)
        while True:
#this is set the innit data
            if data_r_statue == 0:
                if mask & selectors.EVENT_READ:
                    pass
                else:
                    selctor_obj.selector_.modify(sock, selectors.EVENT_READ, recieve_data)

                data_r_statue = 1
#this is receive the will receive data's size.
            if data_r_statue == 1:
                try:
                    data_len_b = sock.recv(first_recev_data_buffer)
                    data_len = struct.unpack("i", data_len_b)[0]
                    data_r_statue = 2
                    selctor_obj.selector_.modify(sock, selectors.EVENT_WRITE, recieve_data)
                    regester_event_r = selectors.EVENT_WRITE
                except Exception:
                    selctor_obj.selector_.unregister(sock)
                    sock.close()

            if data_r_statue == 2:
                    try:
                        sock.send(data_len_b)
                        selctor_obj.selector_.modify(sock, selectors.EVENT_READ, recieve_data)
                        regester_event_r = selectors.EVENT_READ
                        data_r_statue = 3
                    except Exception:
                        selctor_obj.selector_.unregister(sock)
                        sock.close()

# next is receive the 0-n*1024 bit data,
            if data_r_statue == 3:
                if (data_len - all_data_l) > normal_buffer:
                    data_r_statue = 4
                else:
                    data_r_statue = 10
            if data_r_statue == 4:
                try:
                    data_len_b = sock.recv(first_recev_data_buffer)
                    if data_len_b == buffer_b_size:
                        data_r_statue = 6
                        selctor_obj.selector_.modify(sock, selectors.EVENT_READ, recieve_data)
                        regester_event_r = selectors.EVENT_READ

                    else:
                        selctor_obj.selector_.unregister(sock)
                        sock.close()
                except Exception:
                    selctor_obj.selector_.unregister(sock)
                    sock.close()

            if data_r_statue == 6:
                try:
                    data_ = sock.recv(first_recev_data_buffer)
                    if len(data_) == normal_buffer:
                        data_r_statue = 7
                        all_data = all_data + data_
                        selctor_obj.selector_.modify(sock, selectors.EVENT_WRITE, recieve_data)
                        regester_event_r = selectors.EVENT_WRITE
                    else:
                        selctor_obj.selector_.unregister(sock)
                        sock.close()
                except Exception:
                    selctor_obj.selector_.unregister(sock)
                    sock.close()
            if data_r_statue == 7:
                try:
                    sock.send(data_len_b)
                    selctor_obj.selector_.modify(sock, selectors.EVENT_READ, recieve_data)
                    if (data_len - all_data_l) > normal_buffer:
                        regester_event_r = selectors.EVENT_READ
                        data_r_statue = 3
                    else:
                        data_r_statue = 10
                except Exception:
                    selctor_obj.selector_.unregister(sock)
                    sock.close()
# next is receive last data
            if data_r_statue == 10:
                try:
                    data_ll = sock.recv(first_recev_data_buffer)
                    if len(data_ll) == 4:
                        data_r_statue = 12
                        selctor_obj.selector_.modify(sock, selectors.EVENT_READ, recieve_data)
                        data_ll2 = struct.unpack("i", data_ll)[0]
                except Exception:
                    selctor_obj.selector_.unregister(sock)
                    sock.close()

            if data_r_statue == 12:
                try:
                    data_ll__ = sock.recv(data_ll2)
                    if len(data_ll__) == data_ll2:
                        all_data = all_data + data_ll__
                        selctor_obj.selector_.modify(sock, selectors.EVENT_WRITE, recieve_data)
                        data = pickle.loads(all_data)

                        self.orderSendToMachineProcessPipe.send(data)
                        data_r_statue = 13
                    else:
                        selctor_obj.selector_.unregister(sock)
                        sock.close()
                except Exception:
                    selctor_obj.selector_.unregister(sock)
                    sock.close()
            if data_r_statue == 13:
                try:
                    sock.send(data_ll)
                    selctor_obj.selector_.unregister(sock)
                    return True
                except:
                    return False



class Listening_selector:
    """
    communicationGetFromProcessPipe, communicationToProcessCorePipe
    """
    def __init__(self, orderSendToMachineProcessPipe):
        self.orderSendToMachineProcessPipe = orderSendToMachineProcessPipe
        self.socket_driver_que = Tque()
        self.listen_manager_ = setting.listen_port
        self.selector_ = selectors.DefaultSelector()
        self.clients = {}
        self.port_map_obj = {}
        self.machine_id_map_obj = {}
        self.clients_ls_port_set = set()
        self.local_host = setting.local_host
        self.send_set = set()
        self.socket_map_yield = {}
        self.startListening()
        self.send_recve_function_code_map = {
            0: 0,
        }

    def startListening(self, client_port=None, data=None):
        clients_ls_port_set = self.clients_ls_port_set
        selector_ = self.selector_
        port_map_obj = self.port_map_obj
        clients = self.clients
        connected = self.connected
        orderSendToMachineProcessPipe =self.orderSendToMachineProcessPipe
        # add client,monitor socked wtite event
        if client_port == None:
            client_port = self.listen_manager_
        if client_port[0] == self.local_host:
            if client_port not in clients_ls_port_set:
                clients_ls_port_set.add(client_port)
                client = Client_socket(orderSendToMachineProcessPipe, port_data=client_port, data=data, selctor_obj=self)
                connect_socket = client.connect_socket
                client.master_slave = "master"
                # 注册socket写事件
                selector_.register(connect_socket, selectors.EVENT_READ, connected)

                clients[connect_socket] = client
                port_map_obj[client_port] = client
            else:
                if client_port in port_map_obj.keys():
                    sock = port_map_obj[client_port]
                    selector_.unregister(sock)
                    clients_ls_port_set.add(client_port)
                    client = Client_socket(orderSendToMachineProcessPipe, port_data=client_port, data=data, selctor_obj=self)
                    connect_socket = client.connect_socket
                    client.master_slave = "master"
                    # 注册socket写事件
                    selector_.register(connect_socket, selectors.EVENT_READ, connected)
                    clients[connect_socket] = client
                    port_map_obj[client_port] = client
        else:
            client = Client_socket(orderSendToMachineProcessPipe, port_data=client_port, data=data, selctor_obj=self, client_attr="client")
            client.master_slave = "slave"
            connect_socket = client.connect_socket
            send_data = partial(client.sendData, data,)
            selector_.register(connect_socket, selectors.EVENT_WRITE, send_data)
            port_map_obj[client_port] = client
            clients[connect_socket] = client

    def connected(self, sock_):
        cnn, addr = sock_.access()
        recve_ = cnn.recve
        close_ = cnn.close
        while_done = 0
        function_code = None
        machine_id_data_len_ = None
        machine_id_data_ = None
        unpack = struct.unpack
        if while_done == 0:
            try:
                machine_id_data_len = recve_(4)
                machine_id_data_len_ = unpack("i", machine_id_data_len)[0]
                function_code = unpack("i", recve_(4))[0]
                while_done = 1
            except Exception:
                close_()
                print(currentframe().f_lineno, " is wrong")

        if while_done == 1:
            try:
                machine_id_data_ = recve_(machine_id_data_len_)
                while_done = 2
            except Exception:
                close_()
                print(currentframe().f_lineno, " is wrong")
        if while_done == 2:
            try:
                function_code = unpack("i", recve_(4))   # get inner function code
                while_done = 3
            except Exception:
                close_()
                print(currentframe().f_lineno, " is wrong")
        if while_done == 3:
            if function_code == 1:
                #example : self.machine_id_map_obj[machine_id_data_].len_send = 2
                # add function code function here
                while_done = 4
        if while_done == 4:
            if machine_id_data_ is not None:
                cilent_obj = self.machine_id_map_obj.get(machine_id_data_, False)
                if isinstance(cilent_obj, Client_socket):
                    cilent_obj.connect_socket = cnn
                    self.clients[cnn] = cilent_obj
                else:
                    cilent_obj = Client_socket(self.orderSendToMachineProcessPipe,
                                                      socket_=cnn)
                    self.clients[cnn] = cilent_obj
                    self.machine_id_map_obj[machine_id_data_] = self.clients[cnn]
                self.selector_.register(cnn, self.machine_id_map_obj[machine_id_data_].regester_event_r,
                                        cilent_obj.recieveData)


#orderSendToMachineProcessPipe
class comunicationProcessCore:   # use this class  other not use

    def __init__(self, orderSendToMachineProcessPipe,
                 communicationGetFromProcessPipe, ):
        # self.machine_order_dict = basedata.machineIdMapOrderList       # used every machine_id map an list, has it can used order to protect server.
        self.pip_dict = {}
        self.function_code_map_function = {
            struct.pack("i", 0): self.sendData,
            struct.pack("i", 1): self.recieveData,
            struct.pack("i", 2): self.end_and_close,
            struct.pack("i", 3): self.function_code_process_03,
            struct.pack("i", 4): self.function_code_process_04,
            struct.pack("i", 5): self.function_code_process_05,
            struct.pack("i", 6): self.function_code_process_06,
            struct.pack("i", 7): self.function_code_process_07,
            struct.pack("i", 8): self.function_code_process_08,
            struct.pack("i", 9): self.function_code_process_09,
            struct.pack("i", 10): self.function_code_process_10,
        }
        self.function_code_map_function = {
                                            function_code7: self.functinon_code7_,
                                            function_code4: self.receive_order_and_distribute,
                                            function_code5: self.receive_order_and_distribute,
                                            function_code9: self.function_code9,
                                           }
        self.getFromProcess, self.sendTocommunicationProcess = Pipe()
        self.lisen_ = Listening_selector(orderSendToMachineProcessPipe)
        self.connected_set = {}    # key is the (ip, port), value is the client_obj
        self.communicationGetFromProcessPipe = communicationGetFromProcessPipe
        self.socket_map_yield = {}
        self.socket_map_cillent = {}
        self.target_id = [process_computer.communication_dict["_listen_operator_ip"],
                              process_computer.communication_dict["to_machine_sever_ip"]]

        self.loop = asyncio.new_event_loop()
        # self.communication_table = setting.communication_dict
        self.run_loop()

    async def end_and_close(self, data):
        socket_ = self.lisen_.machine_id_map_obj[data[0]]
        cillent_ = self.lisen_.clients[socket_]
        cillent_.end_and_close()

    def authentication(self, data):
        if data[1] in (0, 1, 2):
            return True

    async def getOrderAndRun(self, data):
        data2 = pickle.loads(data)
        machine_id, function_code, target_machine_id, function_name, *_ = data2
        function_ = self.function_code_map_function.get(function_code, self.functinon_code7_)
        try:
            if self.authentication(data):
                function_(data)
        except Exception as ff:
            return None

    def receive_order_and_distribute(self, data):
        """
                     every terminal send order format must obey this convention : [0ne, two,three, four, five,six  ....sendtime]
                   one is the terminal_id , two is the function code three is the will run function, four is the function args, five is the operator's name,
                   six is the operator's password, severn is log equepment addr. last is the sendtime.
                   every class will not creat at begin, it created only at the time of the manager thread recieve the request .
                        back_pipe.send(data_back)
                   """

        (machine_id, functon_code, target_machine_id, func_, *args) = data
        if hasattr(self, func_):
            func__ = getattr(self, func_)
            func__(data)

    def function_code9(self, data):

        machine_id, founction_code, target_machine_id, function_name, *args = data
        if hasattr(self, function_name):
            function_ = getattr(self, function_name)
            try:
                function_(data)
            except Exception as first_recev_data_buffer:
                pass

    def functinon_code7_(self, data):
        self.sendData(data)

    def startListening_port(self, data):
        machine_id, functionc_code, target_machine_id, function_name, arges = data
        port_ = arges[0]
        self.lisen_.startListening(client_port=port_)

    def recieveData(self, key, mask):
        socket_ = key.fileobj
        port_ = socket_.getpeername()
        obj_ = self.lisen_.port_map_obj.get(port_, None)
        if obj_ is None:
            self.lisen_.startListening(port_)
        else:
            obj_.end_and_close()
            self.lisen_.startListening(port_)
            return True

    def sendData(self, data):
        print("im in communication , i will send data is ", data)
        port_ = data[3]
        obj_ = self.lisen_.port_map_obj.get(port_, None)
        if obj_ is None:
            self.lisen_.startListening(port_, data)
        else:
            obj_.end_and_close()
            self.lisen_.startListening(port_, data)

    async def getFromProcessPipe(self):
        print(f"im in communication module getFromProcessPipe function im at 1  {inspect.currentframe().f_lineno}\n ")
        communicationGetFromProcessPipe = self.communicationGetFromProcessPipe
        poll_ = communicationGetFromProcessPipe.poll
        recv_ = communicationGetFromProcessPipe.recv
        getOrder = self.getOrderAndRun
        print(f"im in communication module getFromProcessPipe function im at {inspect.currentframe().f_lineno}\n ")
        machine_id = process_computer.bmachine_id
        target_ids = self.target_id
        while True:
            if poll_():
                data_ = recv_()
                function_name, function_args = data_
                print(f"im in communication module im at {inspect.currentframe().f_lineno}, i recive data is \n {data_}")



                try:
                    len_d = len(data_)
                except Exception as ff:
                    len_d = 0
                if len_d > 0:
                    await getOrder(data_)
            if poll_():
                continue
            else:
                await asyncio.sleep(0)

    def translator_to_send(self, data):

        pass

    async def run_select_loop(self):
        selct_run = self.lisen_.selector_.select
        time.sleep(5)
        print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmm， over url is https://cloud.tencent.com/developer/article/1540043")
        while True:
            events = selct_run(timeout=0.001)
            for key, mask in events:
                print(key, mask)
                callback = key.data
                if iscoroutine(callback):
                    await callback(key, mask)
                else:
                    callback(key, mask)  # key.fileobj is cnn
            await asyncio.sleep(0)

    def run_loop(self):
        tread = Thread(target=self.loop.run_forever)
        asyncio.run_coroutine_threadsafe(self.getFromProcessPipe(), self.loop)
        asyncio.run_coroutine_threadsafe(self.run_select_loop(), self.loop)
        tread.setDaemon(True)
        tread.start()

        print(f"communication recve pipe data is begin , lines is {inspect.currentframe().f_lineno}")
        tread.join()

    def __connect_to_machinesever__(self):  # this function expand later
        pass

    def __connect_to_operator__(self):  # this function expand later
        pass

    def __connect_to_control_console(self):  # this function expand later
        pass



    async def function_code_process_01(self, data):
        #communication not over,
        pass

    def function_code_process_02(self, data):
        #communication end , and closed socket
        pass

    def function_code_process_03(self, data):
        #change master
        pass
    def function_code_process_04(self, data):
        #send data back verification
        pass

    def function_code_process_05(self, data):
        #communication is over, don't close socket,and set lisen and client socket recv statue.
        pass

    def function_code_process_06(self, data):
        #interrupt current communication
        pass

    def function_code_process_07(self, data):
        #must responds recv data
        pass

    def function_code_process_08(self, data):
        #communication is failed, all data will be transport agin .
        pass

    def function_code_process_09(self, data):
        #check the socket  active. as delta time frequence.
        pass

    def function_code_process_10(self, data):
        #slaver communication step will be changed to N step .
        pass

if __name__ == "__main__":
    communicationGetFromProcessPipe, pipe_2s = Pipe()
    orderSendToMachineProcessPipe, pipe_3s = Pipe()

    comunicationProcessCore(orderSendToMachineProcessPipe,
                 communicationGetFromProcessPipe)