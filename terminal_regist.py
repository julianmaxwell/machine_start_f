from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import time

import console_station_socket as comiunication

from threading import Thread, Lock, Event
from multiprocessing import Manager, Process, Pool, Queue

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 400)



"""
send_que data format is ["send_machine_id", "send_port_data", "target_function", "function_args", "send_time"]
recieve data format is ["send_machine_id", "function_name", "function_args", .........."send_time"]
"""

class terminal_equepment_regist_base(ABC):
    """
      every terminal send order format must obey this convention : [0ne, two,three, four, five,six  ....sendtime]
    one is the terminal_id , two is the will run function, three is the function args, four is the operator's name,
    five is the operator's password, six is log equepment addr. last is the sendtime.
    every class will not creat at begin, it created only at the time of the manager thread recieve the request .
    the terminal's all thing do in here. can't do at  other place .
    every terminal has it self class . one obj map one class. all terminal class inerit this class.
    """
    one_limit_obj = None

    def __init__(self, manager_thread_control, terminal_id):
        # print(self.one_limit_obj,"kkkkkkkkkkkkkkkkkkkkk")
        self.regist_boss_apply_times = 0
        self.current_machin_obj = []
        self.current_mode = "observation"    # can choise  "operation", "observation", "boss"  the "boss" is not use now
        self.can_operating_machin_obj = self.get_equepment_data(terminal_id)
        self.opened_machine_list = []
        self.authenticate = False
        self.manager_thread_control = manager_thread_control
        self.order_list = {
            "change_machine" : lambda machine_id:self.change_machine(machine_id),  # value is the machine id  or machine name (machine_id,)
            "console_station_worker_mode": None,            # the mode as watcher,  instead, both,
            "terminal_operate_mode" : None,                 # the mode include boss, operator, wather every terminal can
            # has it self mode. only obey it's self rule , it self excute. nothing relevant about other machine or terminal
            "regist_terminal": None, # fmt is [machine_id, boss_name_, operator_name, pwd, send_time]
            "opend_machine":None
        }
        self.operators_of_boss = []

    @classmethod
    def obj_creat(cls, *args, **kwargs):
        if not cls.one_limit_obj:
            cls.one_limit_obj = cls( *args, **kwargs)
            return cls.one_limit_obj
        else:
            return cls.one_limit_obj

    def get_equepment_data(self):

        """
        this function can be inherit.or re finished
        :return: self.can_operating_machin_obj

        """

    @abstractmethod
    def terminal_authenticate(self, args):
        """
        this function only used to manager thread.
        step 1 first check the terminal.
        recve the terminal send authenticate code. if is right.  can step2  else close socket.
        step 2 dynamic check terminal's right
        send the function code . let the terminal run. and get the respond data . if is the right
        data . let the self.authenticate is True.  otherwise close the socket
       step3 analysis the order.
       analysis the order , if the order has the right send the distribute port to the terminal.
       else self.authenticate is Faulse.
        :return: Faulse or (ports_list)
        """

    @abstractmethod
    def regist_terminal(self, args):
        """

        args can choies at :  ("boss", password)  ("operator", password)
        if authenticate is True:
            ("operator", machine)  ("boss", operator) ("boss", machine)
        here every terminal must regist it server equepments obj. and it need
        ports, and if the terminal id not in boss it's server equepments list.
        the request will be drop in console station.
         logged the recorde in the  operator_operate_terminal_recorde.xls
        :return: {terminal_obj_name: termina_callback_function}
        """



    @abstractmethod
    def send_function(self):
        """
        this function is used for console to transelate it code to this terminal
        to dynamic check the terminal right. every terminal must has a function
        running. to get the check order. this function can copy other terminal
        code.or use it self code.

        :return: "send_code"
        """
    def change_machine(self, machine_id):
        """
                if self.authenticate is True
            change mode here
        this function used for manager thread. to change the terminal work mode
        can choise "observation", "operator"
         logged the recorde in the  operator_operate_terminal_recorde.xls
        :param machine_id:
        :return: machine_obj
        """

    def opened_machine(self, machine_id):
        """
        if self.authenticate is True
            change mode here
        this function used for manager thread.
        logged the recorde in the  operator_operate_terminal_recorde.xls
        :param machine_id:
        :return: ports need number.
        """

    @abstractmethod
    def reload(self, order=False):
        """
        here back up the important data, and if order = True,  take back the data from back data.
        :return:
        """

    @abstractmethod
    def daily_tasks(self):
        """
        the work like check the working machine balance . warning the baance not inough boss.and close the machine
        working, this work check work every three miniuts do it
        :return:
        """


class P0001(terminal_equepment_regist_base):
    def get_equepment_data(self, userterminal_id):
        operator_operate_terminal_recorde__ = pd.read_csv(r"E:\machine\backdata\operator_operate_terminal_recorde.csv", parse_dates =["operate_time"],)
        data_boss_terminal_machine = pd.read_csv(r"E:\machine\backdata\machine_regist.csv",
                           parse_dates =["regist_date"],encoding="gbk" ).drop_duplicates().dropna(axis=0, how="all")
        data_boss_id = pd.read_csv(r"E:\machine\backdata\boss_id_recorder.csv",
                           parse_dates =["regist_time"], encoding="gbk" ).drop_duplicates().dropna(axis=0, how="all")
        data_boss_id["boss_phone"] =data_boss_id["boss_phone"].astype(str)
        # netcoordination_work_list = pd.read_csv(r"E:\machine\backdata\netcoordination_worker.csv",
        #                    parse_dates =["regist_time"],encoding="gbk" ).drop_duplicates().dropna(axis=0, how="all")
        # operator_operate_terminal_recorde__dd = \
        #     (operator_operate_terminal_recorde__[operator_operate_terminal_recorde__["use_terminal_id"]==userterminal_id])
        # netcoordination_work_list["bios_id"] = int(netcoordination_work_list["bios_id"])

        # print(operator_operate_terminal_recorde__dd)
        # print(data_boss_terminal_machine)
        # print(data_boss_id)
        # print(netcoordination_work_list)

    def terminal_authenticate(self, args):
        """
        :arg format is     {machin_cpu_id:12345678, machine_bios_id: 12345678, pwd:"wwww",
        operator:operator_id, machine_program_code: "xxxxxxxxxx"}
        here if return true . machine or terminal can work
        :param args:
        :return: self.authenticate = True if .... else faulse.
        """
        data_boss_id = pd.read_csv(r"E:\machine\backdata\boss_id_recorder.csv",
                        parse_dates=["regist_time"], encoding="gbk").drop_duplicates().dropna(axis=0, how="all")
        data_boss_id["boss_phone"] = data_boss_id["boss_phone"].astype(str)
        data_boss_id["boss_id"] = data_boss_id["boss_id"].str.strip(" ")

        machine_ids = pd.read_csv(r"E:\machine\backdata\machine_regist.csv",
                        parse_dates=["regist_date"], encoding="gbk").drop_duplicates().dropna(axis=0, how="all")
        boss_balance_data = pd.read_csv(r"E:\machine\backdata\boss_balance_mange.csv",
           parse_dates=["fill_money_date", "consum_date"], encoding="gbk").drop_duplicates().dropna(axis=0, how="all")
        operators = pd.read_csv(r"E:\machine\backdata\operator_regist.csv",
                        parse_dates=["regist_time"], encoding="gbk").drop_duplicates().dropna(axis=0, how="all")
        data_boss_id.drop_duplicates(["boss_id"], inplace=True)
        data_boss_id.drop_duplicates(["boss_name", "boss_phone", ], inplace=True)
        data_boss_id.sort_values(by=["boss_id"], inplace=True)
        try:
            self.operator = args["operator"]
            boss_id = operators["boss_id"][operators["operate_id"]==self.operator]
            operators__ = operators["operate_id"][operators["boss_id"]==boss_id.values[0]]
            self.operators_of_boss = operators__
            self.boss_id_ = boss_id.values[0]
            boss_balance = boss_balance_data["remainder_expanse"][boss_balance_data["boss_id"] == self.boss_id_]
            self.balance = boss_balance[0]
            self.operator_phone = (operators["operator_phone"][operators["operate_id"]==self.operator]).values[0]
            self.boss_phone = (data_boss_id["boss_phone"][data_boss_id["boss_id"] == self.boss_id_]).values[0]
            # print(self.boss_id_, self.boss_phone, self.balance)
            # print(self.operator, self.operator_phone)

        except  Exception as e:

            self.operators_of_boss = operators__
            self.operator = None
            self.boss_id_ = None
            self.balance = None
            self.authenticate = False
            self.boss_phone = None
            self.operator_phone = None
            return False

    def regist_terminal(self, args):
        pass

    def send_function(self):
        pass

    def reload(self, order=False):
        pass




    def regist_boss(self, boss_name, boss_id, boss_pwd, boss_phone,time_str):
        """
        this function used to new boss appyl  write table
        :param boss_name:
        :param boss_id:
        :param boss_pwd:
        :param boss_phone:
        :param time_str:
        :return:
        """
        data_boss_id = pd.read_csv(r"E:\machine\backdata\boss_id_recorder.csv",
                              parse_dates=["regist_time"], encoding="gbk").drop_duplicates().dropna(axis=0,  how="all")
        data_boss_id_copy = data_boss_id.copy()
        data_boss_id["boss_phone"] = data_boss_id["boss_phone"].astype(str)
        time_date = pd.to_datetime(time_str,format="%Y/%m/%d")
        append_data = np.array([boss_name, boss_id, boss_pwd,  boss_phone, "applying", "applying", time_date])
        append_data = pd.Series(append_data, index=data_boss_id.columns)
        data_boss_id = data_boss_id.append(append_data, ignore_index=True)
        data_boss_id = data_boss_id.sort_values(by="boss_id", axis=0)
        data_boss_id = data_boss_id.drop_duplicates()
        xx = list(zip(data_boss_id_copy["boss_name"],data_boss_id_copy["boss_id"]))
        xxa = (append_data[0], append_data[1])
        if xxa not in xx:
            print(append_data , "will not be write")
            data_boss_id.to_csv(r"E:\machine\backdata\boss_id_recorder.csv",index=False, encoding="gbk")
        # self.add_boss_fill_money_table()
    def add_boss_fill_money_table(self):
        """
        write money  it finished later and now the table writed by man
        :return:
        """
        boss_tale = pd.read_csv(r"E:\machine\backdata\boss_id_recorder.csv",
                              parse_dates=["regist_time"], encoding="gbk").drop_duplicates().dropna(axis=0,  how="all")
        balance_table = pd.read_csv(r"E:\machine\backdata\boss_balance_mange.csv",
                              parse_dates=["refill_money_date"], encoding="gbk").drop_duplicates().dropna(axis=0,  how="all")

        # print("kkkkkkkkkkkkkkkkkkkkkkkk")
        # print(boss_tale)
        # print(balance_table)


    def boss_review(self, manager, boss_id, result):
        """
        here only write the apply data to the table . and send a single to review manager. in the order regulation
        time , the manager must finished it. and boss review not use this function.
        :param manager:
        :param boss_id:
        :param result:
        :return:
        """
        if result is True:
            boss_tale = pd.read_csv(r"E:\machine\backdata\boss_id_recorder.csv",
                          parse_dates=["regist_time"], encoding="gbk").drop_duplicates().dropna(axis=0, how="all")
            manager_tale = pd.read_csv(r"E:\machine\backdata\inner_staff_table.csv",
                          parse_dates=["regist_time"], encoding="gbk").drop_duplicates().dropna(axis=0, how="all")
            permission_department = pd.read_csv(r"E:\machine\backdata\review_permission.csv",
                           encoding="gbk").drop_duplicates().dropna(axis=0, how="all")
        if boss_id.startswith("bs") and (len(boss_id)==8):
            xx = manager_tale.loc[:, "id"]
            rmanager=manager_tale[xx==manager]
            print(rmanager)
            xm = boss_tale["boss_id"]
            print(boss_tale[xm==boss_id])
            print(rmanager["level"].values[0] )
            # print("bbbbbbbbbbbbbbbbbbbbbbbbb")
            if (rmanager["level"].values[0] < 3) and  result:
                print("okkkkkkkkkkkkk")



            # print(xxx)
            # print(boss_tale[xxx])
            # print(boss_tale.iloc[0], boss_id)
            # print(boss_tale.loc[:"boss_id"]==boss_id)
            # pass_boss["former_status"] = "valid"
            # pass_boss["former_status"] = "valid"
            # pass_boss["review_manager"] = manager




    def regist_machine(self):
        pass

    def regist_operator(self):
        pass

    def daily_tasks(self):
        """

        :return:
        """

def machine_process_send_decorator(function):
    def qurey_data_function(self, function_name, args):
        if function_name in self.qurey_function_:
            xx = function(args)
            next(xx)
            self.query_doing_function[function_name] = xx
    return qurey_data_function

def manager_process_send_decorator(function):
    def qurey_data_function(self, function_name, args):
        if function_name in self.qurey_function_:
            xx = function(self, function_name, args)
            next(xx)
            self.query_doing_function[function_name] = xx
    return qurey_data_function







class machine_process_body:
    """
    all data be receive  by the self.que_into_console_station and send by  self.que_out_from_console_station
    by the function
    """
    machine_obj_list = None
    def __init__(self, cilent_machine_send_que, distrbute_que, machine_process_send):
        self.to_manager_process_class = cilent_machine_send_que
        self.manager_distrubute_que = distrbute_que     # need the data format.
        self.machine_process_send = machine_process_send
        self.machine_group = pd.DataFrame([], columns=[
            "machine_id", "terminal_or_machine_id", "port_number"])
        self.child_process_task_statues_table = pd.DataFrame([], columns=[
            "child_process_id", "child_process_thread_id", "child_thread_task_id", "thread_id_task_max_time",
            "thread_id_task_average_time"])
        self.manager_machine_process_contact_function_list = ["distribute_task",
                                                              "query_back_function",
                                                              "send_machine_port_need_table",

        ]
        self.qurey_function_ = []    # query function must in this list.
        self.query_doing_function = {}

    def run(self):
        """
        distrubute_data format: [one, two, three, four,.......time] the one is data type. may return_value、distribute_data
        ........   two is the function name which will run. three is the args.   args format is : [machine_id terminal_id
        ,group_id, port_number]
        :return:
        """
        print("im in machine process")
        terminal_function_run_thread = Thread(target=self.get_the_distrubute_data)
        terminal_function_run_thread.start()




    def get_the_distrubute_data(self):
        """
        data receive format is : [function_name, args], args format rule is seted by the function which used the args.
        :return:
        """
        while True:
            order = self.manager_distrubute_que.get(block=True)
            print("im in all machine, get data")

            if order[0] in self.manager_machine_process_contact_function_list:
                    try:
                        exec(order[0](order))
                    except:
                        try:
                            self.query_doing_function[order[0]].send(order)
                        except StopIteration:
                            del self.query_doing_function[order[0]]
                            print("over")
                        except Exception as e:
                            print("thing is wrong", e)

    def terminal_or_machine_login_order(self):
        pass

    def distribute_task(self):
        pass

    def send_machine_port_need_table(self, class_name, port_table="port_table"):
        x = eval(class_name)
        if port_table == True:
            self.machine_process_send.put(x.port_table)

    def query_back_function(self, args):
        #args format is [function_name, function_args]
        self.query_doing_function[args[0]].send(args)

    def init_child_proccess(self, process_number=8):
        for serial_number in range(process_number):
            process_name = "process_name-" + str(serial_number)
            child_process = Process(target=lambda: self.creat_child_process(process_name), name=process_name)
            self.child_process_task_statues_table.loc[child_process, :] = [process_name, None, None, None, None]

    def creat_child_process(self, process_id):
        process_obj = child_process_(process_id)
        thread_proccess_manger = Thread(target=process_obj.get_and_run_up_process_order)
        thread_proccess_manger.start()

    def creat_machien_obj(cls, *args, **kwargs):
        if not cls.machine_obj_list:
            machine_obj_list = cls(*args, **kwargs)
            return machine_obj_list
        else:
            return cls.machine_obj_list



    def from_pad_que_(self, order_data):
        """
        {terminal_pad_id:data}   if terminal_running_model is "master":......
                                 if terminal_running_model is "slave".......
                                 if terminal_running_model is "waiting"......

        :param order_data:
        :return:
        """

    def from_machine_que_(self, data):
        """
        machine send status data. to here.
        :param data:
        :return:
        """


    def to_pad_terminal(self):
        """

        if not one pad, it will send data to the
        :return:
        """
        pass

    def to_tomachine(self):
        pass


class child_process_:
    def __init__(self, process_id):
        self.process_id = process_id
        self.child_up_que = Queue()
        self.child_reciv_que = Queue()
        self.child_thread_statues = pd.DataFrame([], columns=[
            "child_process_id",
            "thread_id",
            "child_thread_task_id",
            "thread_id_task_max_time",
            "thread_id_task_average_time"])

    def get_and_run_up_process_order(self):
        order = self.child_reciv_que.get()
        self.run_order(order)

    def run_order(self, order):
        pass





class manager_port:
    """
    thi class is the most importangt , only used for the manager_port. give the machine and pad terminal transelate
    chanel. do nothing for the machine and it's terminal.
    """
    def __init__(self, cilent_machine_send_que, distrbute_que, cilent_machine_recive_que, machine_process_send):
        self.cilent_machine_recive_que = cilent_machine_recive_que
        self.cilent_machine_send_que = cilent_machine_send_que

        self.distrbute_que = distrbute_que
        self.machine_process_send = machine_process_send

        self.comiunication_ = comiunication.SeverRun(self.cilent_machine_recive_que, self.cilent_machine_send_que)
        self.base_data = all_data_process()
        self.manager_machine_process_contact_function_list = [
        ]
        self.manager_machine_process_terminal_function_list = [
            "operator_authenticate",
        ]

        self.query_function = ["query_back_function",


        ]
        self.query_doing_function = {}

    def query_back_function(self, args):
        #args format is [function_name, function_args]
        self.query_doing_function[args[0]].send(args)

    def getorder(self):

        """
        :param data:
        :return:
      every terminal send order format must obey this convention : [0ne, two,three, four, five,six  ....sendtime]
    one is the terminal_id , two is the will run function, three is the function args, four is the operator's name,
    five is the operator's password, six is log equepment addr. last is the sendtime.
    every class will not creat at begin, it created only at the time of the manager thread recieve the request .
    the terminal's all thing do in here. can't do at  other place .
    every terminal has it self class . one obj map one class. all terminal class inerit this class.
        """
        comiunication_thread = Thread(target=self.comiunication_.run, name="manager_port_communication")
        receive_order_and_run_terminal = Thread(target=self.receive_terminal_and_process_order_terminal, name="manger_order_run_thread")
        contact_order_and_run = Thread(target=self.manager_process_contac_machine_process, name="distribute_Thread")
        comiunication_thread.start()
        receive_order_and_run_terminal.start()
        contact_order_and_run.start()



    def receive_terminal_and_process_order_terminal(self):
        """
        the order map function must in this class , it can use this class'obj parameter.
        order format [one, two], one is the functions, two is the args
        :return: None, all of data processed is put to self.comiunication_.cilent_machine_recive_que or
        self.comiunication_.distrbute_que by the order map function
        """
        while True:
            try:
                print("while will run")
                order_ = (self.comiunication_.cilent_machine_send_que).get(block=True)
            except Exception as e:
                order_ = None
                print("que is read, it's wrong", e)

            if order_ and (order_ in self.manager_machine_process_terminal_function_list):
                if self.permit_review(order_):
                    try:
                        self.reciev_and_emplementation_order(order_)
                    except:
                        print("receive order is not exist, please check it")
                else:
                    print("permit is not enough, please contact manager")


    def reciev_and_emplementation_order(self, data):
        self.log_equepment_id = data[0]
        function_name = data[1]
        function_arg = data[2]
        self.operator_name = data[3]
        self.operator_pwd = data[4]
        self.equepment_addr = data[5]
        self.log_time = data[-1]
        self.authticate = False
        self.machine_log = False
            # "machine_id",
            # "terminal_id",
            # "machine_send_port",
            # "machine_receive_port",
            # "terminal_send_port",
            # "terminal_receive_port",

        try:
            self.log_equepment_id_boss = \
                self.base_data.machine_regist["boss_id"][self.base_data.machine_regist["mahine_id_cpu"] == self.base_data.log_equepment_id].values[0]
        except:
            self.log_equepment_id_boss = None
        try:
            self.boss_has_equepment_id = self.base_data.machine_regist["mahine_id_cpu"][
                self.base_data.machine_regist["boss_id"] == self.base_data.log_equepment_id_boss].values
        except:
            self.boss_has_equepment_id = []

        try:
            exec(function_name(data))
        except Exception as e:
            print("order function or function_arg is wrong", e)
        self.log_equepment_id = None
        function_name = None
        function_arg = None
        self.operator_name = None
        self.operator_pwd = None
        self.equepment_addr = None
        self.log_time = None
        self.authticate = False
        self.machine_log = False
        self.log_equepment_id_boss = None
        self.boss_has_equepment_id = []

    def manager_process_contac_machine_process(self):
        """
        every function must in the self.manager_machine_process_contact_function_list, only for security.
        :return:
        """
        while True:
            order = self.machine_process_send.get()
            if hasattr(self, order[0]):
                try:
                    exec(order[0](order))
                except:
                    try:
                        self.query_doing_function[order[0]].send(order)
                    except StopIteration:
                        del self.query_doing_function[order[0]]
                        print("over")
                    except Exception as e:
                        print("thing is wrong", e)

    @manager_process_send_decorator
    def query_machine_port_need_table(self, function_name, args):
        """
        backdata format is [function_name, args] args format is ["machine_id",
                                                                 "terminal_id",
                                                                 "machine_send_port",
                                                                 "machine_receive_port",
                                                                 "terminal_send_port",
                                                                 "terminal_receive_port",
                                                                 ]
        :param function_name: str  function name is the function_dict's key. here the function_name
        :param args:
        :return:
        """
        self.distrbute_que.put([function_name, args])
        back_data = yield
        parameter = back_data[1]
        if parameter[0] is not None:
            self.base_data.machine_ports_map_table.iloc[:, "machine_id"] = back_data[1]
        elif parameter[1] is not None:
            self.base_data.machine_ports_map_table.iloc[:, "machine_id"] = back_data[1]


    def permit_review(self,data):
        """
        here check the order .
        :param order:
        :return: """
        self.base_data.permit_review(data)


    def operator_authenticate(self, data):
        operator = data[3]
        pwd = data[4]
        log_equepment_id = data[0]
        if operator not in self.base_data.operator_regist["operate_id"].values:
            print("username or password is wrong")
            return "username or password is wrong"
        else:

            if pwd == (self.base_data.operator_regist["pwd"][self.base_data.operator_regist["operate_id"] == operator].values[0]):
                new_l = {"operate_id": operator,
                         "log_time": pd.datetime.datetime.now(),
                         "failed_times": 0,
                         "log_machine_id": self.log_equepment_id,
                         "success_times": 1,
                         "log_status": True,
                         "log_equepment_id": log_equepment_id
                         }
                login_equepment_name = self.base_data.machine_regist["machine_name"][
                    self.base_data.machine_regist["mahine_id_cpu"] == self.log_equepment_id].values[0]
                if login_equepment_name.startswith("test_pad_"):

                    send_que, receive_que = self.base_data.get_socket_ip(2)
                    ars = [None, self.log_equepment_id, None, None, send_que, receive_que]
         #  args format is ["machine_id", "terminal_id", "machine_send_port", "machine_receive_port",  "terminal_send_port",
                        #  "terminal_receive_port", ]  this args not save

                    self.base_data.machine_ports_map_table[self.base_data.machine_ports_map_table["terminal_id"]== self.log_equepment_id] =ars
                    new_log_ = pd.Series(new_l, index=self.base_data.operator_log_record_memery_tale.columns, )
                    new_log_ = new_log_.to_frame().T
                    new_log_["failed_times"] = new_log_["failed_times"].fillna(0)
                    new_log_["success_times"] = new_log_["success_times"].fillna(0)
                    new_log_["log_status"] = new_log_["log_status"].fillna(False)
                    self.base_data.operator_log_record_memery_tale = pd.concat([self.base_data.operator_log_record_memery_tale, new_log_])
                    self.base_data.operator_log_record_memery_tale.drop_duplicates(subset=["log_machine_id"], keep="last")
                    new_log_.to_csv(r"E:\machine\backdata\operator_log_record.csv", index=False, mode="a+", encoding="gbk", header=False)
                    return True
                elif login_equepment_name.startswith("machine_"):
                    send_que, receive_que = self.base_data.get_socket_ip(2)
                    ars = [None, self.log_equepment_id, send_que, receive_que, None, None]
                    #  args format is ["machine_id", "terminal_id", "machine_send_port", "machine_receive_port",  "terminal_send_port",
                    #  "terminal_receive_port", ]  this args not save
                    if self.base_data.machine_ports_map_table.loc[:,
                       "terminal_id"] == self.log_equepment_id is True:
                        self.base_data.machine_ports_map_table[
                            self.base_data.machine_ports_map_table.loc[:,
                            "terminal_id"] == self.log_equepment_id] = ars
                    else:
                        self.base_data.machine_ports_map_table.loc[
                            len(self.base_data.machine_ports_map_table)] = ars

                    new_log_ = pd.Series(new_l, index=self.base_data.operator_log_record_memery_tale.columns, )
                    new_log_ = new_log_.to_frame().T
                    new_log_["failed_times"] = new_log_["failed_times"].fillna(0)
                    new_log_["success_times"] = new_log_["success_times"].fillna(0)
                    new_log_["log_status"] = new_log_["log_status"].fillna(False)
                    self.base_data.operator_log_record_memery_tale = pd.concat(
                        [self.base_data.operator_log_record_memery_tale, new_log_])
                    self.base_data.operator_log_record_memery_tale.drop_duplicates(subset=["log_machine_id"],
                                                                                   keep="last")
                    new_log_.to_csv(r"E:\machine\backdata\operator_log_record.csv", index=False, mode="a+",
                                    encoding="gbk", header=False)
                    return True

            else:
                DDtime = pd.datetime.datetime.now()
                new_l = {"operate_id": operator,
                         "log_time": DDtime,
                         "failed_times": 1,
                         "log_machine_id": log_equepment_id,
                         "success_times": 0,
                         "log_status": False
                         }
                new_log_ = pd.Series(new_l, index=self.base_data.operator_log_record_memery_tale.columns, )

                new_log_ = new_log_.to_frame()
                new_log_ = new_log_.T
                (self.base_data.operator_log_record_memery_tale.loc[self.base_data.operator_log_record_memery_tale["log_machine_id"] ==
                 log_equepment_id])["failed_times"] = (self.base_data.operator_log_record_memery_tale.loc[
                 self.base_data.operator_log_record_memery_tale["log_machine_id"] == log_equepment_id])["failed_times"] + 1
                (self.base_data.operator_log_record_memery_tale.loc[self.base_data.operator_log_record_memery_tale["log_machine_id"] ==
                 log_equepment_id])["failed_times"] = DDtime
                # self.base_data.operator_log_record_memery_tale = pd.concat([self.base_data.operator_log_record_memery_tale, new_log_])
                # self.base_data.operator_log_record_memery_tale.drop_duplicates(subset=["log_machine_id"], keep="last")
                print(self.base_data.operator_log_record_memery_tale)
                new_log_.to_csv(r"E:\machine\backdata\operator_log_record.csv", index=False, mode="a+", encoding="gbk", header=0)
                return "username or password is wrong"

    def set_department_(self, data):
        self.base_data.set_deparment_function(data)

class all_data_process:
    def __init__(self):

        self.log_equepment_id = None
        function_name = None
        function_arg = None
        self.operator_name = None
        self.operator_pwd = None
        self.equepment_addr = None
        self.log_time = None
        self.authticate = False
        self.machine_log = False
        self.get_table()
        self.old_date = pd.datetime.datetime.now()

        self.machine_ports_map_table = pd.DataFrame([], columns=['machine_id',
                                                                  'recieve_port',
                                                                  'send_port',
                                                                  'self_ip',
                                                                  'target_recieve',
                                                                  'target_ip',
                                                                 "target_machine_id"])




    def loard_tale_file(self, path_, column_format, parse_dates=None, encoding="gbk", header=0):
        try:
            data_tale = pd.read_csv(path_, header=header,
                                    parse_dates=parse_dates, encoding=encoding).drop_duplicates().dropna(axis=0,
                                                                                                         how="all")
            # print("boss_tale", data_tale)
            return data_tale.drop_duplicates().dropna(axis=0, how="all")
        except FileNotFoundError:
            # ["boss_name", "boss_id", "pwd", "boss_phone", "former_status",
            #  "current_status", "regist_time"]
            data_tale = pd.DataFrame([], columns=column_format)
            data_tale.to_csv(path_, mode="w", index=False)
            return data_tale.drop_duplicates().dropna(axis=0, how="all")

    def get_table(self):
        self.boss_tale = self.loard_tale_file(r"..\backdata\boss_id_recorder.csv", ['name', 'id',
                'pwd', 'boss_phone', 'former_status', 'current_status', 'regist_time'], parse_dates=["regist_time"])
        self.permission_department = self.loard_tale_file(r"..\backdata\review_permission.csv", ["permission_name",
        "permission_id", "use_department_or_staff", "function_name"])

        self.boss_balance_mange = self.loard_tale_file(r"..\backdata\boss_balance_mange.csv", ["boss_id",
        "remainder_expanse", "accorting_period", "possting", "refill_money", "fill_money_date", "fill_operator",
        "consum_machine_id", "consum_task_id", "consum_money", "consum_date", "machine_banlance_first", "voucher_number",
        "accounting_name", "voucher_scan_file", "note: machine_banlance_first defaut value is TRUE"],)

        self.inner_staff_table = self.loard_tale_file(r"..\backdata\inner_staff_table.csv", ["name",
            "id",  "level", "regist_time", "status", "pwd"], parse_dates=["regist_time"])


        self.machine_regist = self.loard_tale_file(r"..\backdata\machine_regist.csv", ["machine_name",
            "mahine_id_cpu", "mahine_id_bios", "work_area", "boss_name", "boss_id", "machine_status", "regist_date",
            "regist_class"], parse_dates=["regist_date"])


        # self.netcoordination_worker = self.loard_tale_file(r"..\backdata\netcoordination_worker.csv", ["boss_id",
        #     "cpu_id", "bios_id", "has_md5", "state", "regist_time"], parse_dates=["regist_time"])


        self.operator_operate_terminal_recorde = self.loard_tale_file(r"..\backdata\operator_operate_terminal_recorde.csv", ["operator_id",
            "order_name", "order_args", "use_terminal_id", "operate_time", "operate_status"], parse_dates=["operate_time"])


        self.operator_regist = self.loard_tale_file(r"..\backdata\operator_regist.csv", ["id",
        'operator_type', 'name', 'phone', 'pwd', 'approval', 'status', 'level',
        'regist_time', " note: approval_content only the function name in programe"], parse_dates=["regist_time"])
        #
        self.task_implementation_record = self.loard_tale_file(r"..\backdata\task_implementation_record.csv", [
            "task_id", "machine_id", "opetator", "permit_number", "permit_begin_time",
            "permit_over_time", "permit_statue", "area_data"], parse_dates=["permit_begin_time", "permit_over_time"])

        self.operator_log_record = self.loard_tale_file(r"..\backdata\operator_log_record.csv", [
            "operate_id", "log_time", "failed_times", "success_times", "log_status"], parse_dates=["log_time"])

        self.function_arg_table_data = self.loard_tale_file(r"..\backdata\function_arg_table.csv", [
            "function_id", "function_name", "function_type", "class_name", "obj_name", "regist_time",
            "log_equepment_id"], parse_dates=["regist_time"])

        self.operator_permit = self.get_operator_permit_data()

        self.operator_log_record_memery_tale = pd.DataFrame([], columns=self.operator_log_record.columns)
        self.machine_regist_memery_table = pd.DataFrame([], columns=self.machine_regist.columns)
        self.boss_balance_data_table = self.fill_money()

    def get_operator_permit_data(self):
        """
        get the permit_data_table need group many table
        table columns = ['operator_name', 'operator_id', 'operator_department', 'equepment_id', 'class_id', 'obj_id', 'function_id', 'function_name', 'function_args', 'add_time', 'tag_row']
        """
        self.operator_permit = pd.DataFrame([], columns=['name', 'operator_id',
                         'class_id', 'obj_id', 'function_id', 'function_name', 'function_args', 'add_time', 'tag_row'])

        operator_ = self.operator_regist.loc[:, ['id', 'name']][self.operator_regist.loc[:, 'status'] == "active"]
        inner_staff = self.inner_staff_table.loc[:, ['id', 'name']][self.inner_staff_table.loc[:, 'status'] == "active"]
        boss = self.boss_tale.loc[:, ['id', 'name']][self.boss_tale.loc[:, "current_status"] == "active"]
        all_worker = pd.concat([operator_, inner_staff, boss], axis=0).reset_index(drop=True)
        print(all_worker)


    """
    one operation will not be doing only by it self.   one is send/start  review. over.
    normal_right  operator only do it's self range.
    
    """

    def add_new_boss(self, data):
        pass
    def add_new_operator(self, data):
        pass
    def add_new_department(self, data):
        pass
    def add_new_staff(self, data):
        pass


    def stop_boss(self, data):
        pass
    def stop_operator(self, data):
        pass
    def stop_department(self, data):
        pass


    def modify_boss(self, data):
        pass
    def modify_operator(self, data):
        pass
    def modify_staff(self, data):
        pass


    def review_boss(self, data):
        pass
    def review_operator(self, data):
        pass
    def review_staff(self, data):
        pass






    def reciev_and_emplementation_order(self, data):
        self.log_equepment_id = data[0]
        function_name = data[1]
        function_arg = data[2]
        self.log_time = data[-1]
        self.authticate = False
        self.machine_log = False
        login_equepment_name =self.machine_regist["machine_name"][self.machine_regist["mahine_id_cpu"]==self.log_equepment_id]
        if login_equepment_name.startswith("test_pad_"):
            ars = [None, self.log_equepment_id, None, None, None]

            # "machine_id",
            # "terminal_id",
            # "machine_send_port",
            # "machine_receive_port",
            # "terminal_send_port",
            # "terminal_receive_port",

        try:
            self.log_equepment_id_boss = \
            self.machine_regist["boss_id"][self.machine_regist["mahine_id_cpu"] == self.log_equepment_id].values[0]
        except:
            self.log_equepment_id_boss = None
        try:
            self.boss_has_equepment_id = self.machine_regist["mahine_id_cpu"][
                self.machine_regist["boss_id"] == self.log_equepment_id_boss].values
        except:
            self.boss_has_equepment_id = []

        try:
            exec(function_name(function_arg))
        except Exception as e:
            print("order function or function_arg is wrong")
        self.log_equepment_id = None
        function_name = None
        function_arg = None
        self.operator_name = None


        self.log_time = None
        self.authticate = False
        self.machine_log = False
        self.log_equepment_id_boss = None
        self.boss_has_equepment_id = []

    def permit_review(self, data):
        """
        :param data:
        :return: Faulse or data
        """
        # if self.operator_regist.loc[:, "status"][self.operator_regist.loc[:, "operator_id"]==operator].values[0] != "active":    #staff statues is active
        #     return False
        # if self.operator_log_record_memery_tale.loc[:, "log_status"][
        #     self.operator_log_record_memery_tale.loc[:, "operate_id"] == operator].values[0] != "active":   # the operator log is authticated.
        #     return False

    def operater_manager_operate(self, data):
        data_ = self.permit_review(data)
        if data_ is False:
            return False
        else:
            pass



    def fill_money(self, boss_id=None, equepment_id=None, boss_fill_number=0, consum_money=0, voucher_scan_file=None):
        """
        this function used for fill money and get the gruop data. in innit.
        :param boss_id:
        :param money_number:
        :return: self.boss_money_group pandaform data.
        """
        if (boss_id != None) or (equepment_id != None):
            if boss_id == None:
               boss_id = self.machine_regist["boss_id"][self.machine_regist["mahine_id_cpu"]==equepment_id].values[0]


            _date = pd.datetime.datetime.now()
            new_dic = {"boss_id": boss_id,
                       "refill_money": boss_fill_number,
                       "fill_money_date": _date,
                       "consum_machine_id": equepment_id,
                       "consum_money": consum_money,
                       "consum_date": _date,
                       "voucher_scan_file": voucher_scan_file}
            self.boss_balance_mange =self.boss_balance_mange.append(
                new_dic, ignore_index=True
            )
            print(self.boss_balance_mange)
        temporaty = self.boss_balance_mange.groupby("boss_id").agg({
                                                    "refill_money": "sum",
                                                    "consum_money": "sum",})
        temporaty["remainder_expanse"] = temporaty["refill_money"] - temporaty["consum_money"]
        temporaty["boss_id"] = temporaty.index
        self.boss_balance_data_table = temporaty
        return self.boss_balance_data_table




    def set_deparment_function(self, data):
        operator = data[3]
        if self.operator_log_record_memery_tale["log_status"][self.operator_log_record_memery_tale["operate_id"] == operator].values[0] == "active":
            return False
        args = data[2]
        #
        # if (args[0] in self.set_department_tale.loc[:, "department_name"]):
        #     if (self.set_department_tale[self.set_department_tale.loc[:, "department_name"] == args[0]]["department_statu"]) != "active":
        #         self.set_department_tale.loc[:, args[0]] = args
        #         self.set_department_tale.loc[:, args[0]]["department_statu"] = "in_review"
        #         self.set_department_tale.loc[:, args[0]]["department_review_statues"] = "waiting_review"
        # else:
        #     APP = pd.Series(args, index=self.set_department_tale.columns)
        #     self.set_department_tale.append(APP)
        #     self.set_department_tale.loc[:, args[0]]["department_statu"] = "in_review"
        #     self.set_department_tale.loc[:, args[0]]["department_review_statues"] = "waiting_review"

    def boss_balance_query(self, boss_id):
        # self.boss_money_group
        return self.boss_balance_data_table["remainder_expanse"][self.boss_balance_data_table["boss_id"]==boss_id]

    def machine_login(self, data):
        pass

    def connect_machine(self, data):
        pass

    def operator_authenticate(self, data):
        operator = data[2][0]
        pwd = data[2][1]
        log_equepment_id = data[0]
        if operator not in self.operator_regist["operate_id"].values:
            print("username or password is wrong")
            return "username or password is wrong"
        else:
            if pwd == self.operator_regist["pwd"][self.operator_regist["operate_id"] == operator].values[0]:
                new_l = {"operate_id": operator,
                         "log_time": pd.datetime.datetime.now(),
                         "failed_times": 0,
                         "log_machine_id": self.log_equepment_id,
                         "success_times": 1,
                         "log_status": True,
                         "log_equepment_id": log_equepment_id

                         }
                new_log_ = pd.Series(new_l, index=self.operator_log_record_memery_tale.columns, )
                new_log_ = new_log_.to_frame().T
                new_log_["failed_times"] = new_log_["failed_times"].fillna(0)
                new_log_["success_times"] = new_log_["success_times"].fillna(0)
                new_log_["log_status"] = new_log_["log_status"].fillna(False)
                print(new_log_)
                # self.operator_log_record_memery_tale.append(new_log_, ignore_index=True)
                self.operator_log_record_memery_tale = pd.concat([self.operator_log_record_memery_tale, new_log_])
                print(self.operator_log_record_memery_tale)
                # new_log_.replace(" ", "", inplace=True, regex=True)
                new_log_.to_csv(r"..\backdata\operator_log_record.csv", index=False, mode="a+", encoding="gbk", header=0)

                return True
            else:
                new_l = {"operate_id": operator,
                         "log_time": pd.datetime.datetime.now(),
                         "failed_times": 1,
                         "log_machine_id": self.log_equepment_id,
                         "success_times": 0,
                         "log_status": False
                         }
                new_log_ = pd.Series(new_l, index=self.operator_log_record_memery_tale.columns, )

                new_log_ = new_log_.to_frame()
                new_log_ = new_log_.T
                print(new_log_)
                self.operator_log_record_memery_tale = pd.concat([self.operator_log_record_memery_tale, new_log_])
                print(self.operator_log_record_memery_tale)
                new_log_.to_csv(r"..\backdata\operator_log_record.csv", index=False, mode="a+", encoding="gbk", header=0)
                return "username or password is wrong"



    """
      every terminal send order format must obey this convention : [0ne, two,three, four, five,six  ....sendtime]
    one is the terminal_id , two is the will run function, three is the function args, four is the operator's name,
    five is the operator's password, six is log equepment addr. last is the sendtime.
    every class will not creat at begin, it created only at the time of the manager thread recieve the request .
    the terminal's all thing do in here. can't do at  other place .
    every terminal has it self class . one obj map one class. all terminal class inerit this class.
    """

    def daily_task_empty_table(self):
        """
        this is the daily task. prevent the memory used too large by the table. every day"s 12.00 at night. the data
        of the table will be drop empty.

        :param table_name:
        :return:
        """
        daily_task_talbe = [self.operator_log_record_memery_tale,
                            self.machine_regist_memery_table]
        current_time = pd.datetime.datetime.now().date()
        delta_time = current_time - self.old_date
        if delta_time.days >= 1:
            for table_name in daily_task_talbe:
                table_name.drop(
                    index=table_name.index, inplace=True)
            self.old_date = current_time

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

    def get_socket_ip(self, n, start_ip=5000, end_ip=15000):
        used_ip = set(self.getsysused_port())
        if not used_ip:
            start_ip = end_ip
            end_ip = end_ip + 10000
            used_ip = set(self.getsysused_port())
        all_ip = set(range(start_ip, end_ip))
        new_ip = all_ip - used_ip
        new_ip = list(new_ip)
        new_ip.sort()
        return new_ip[0:n]

    def machine_apply_creat_obj(self):
        """
        creat machine obj and  get the port data list. data list format is to
        :return:
        """
        pass

    def pad_apply_conect_machine_obj(self):
        if self.authticate == True:
            pass

    def get_console_ip_add(self):
        import subprocess
        import re
        X = subprocess.Popen(r"ipconfig", shell=True, stdout=subprocess.PIPE)
        out_, error = X.communicate()
        out_ = out_.decode(encoding="gbk")
        ip_addr = re.findall(r"IPv4 地址 (\. )+: (.+)\s", out_)
        ip_addr_outer, ip_addr_inner = ip_addr[0][1], ip_addr[1][1]
        return ip_addr_outer.strip(),  ip_addr_inner.strip()

class console_state_run_class:
    def __init__(self):
        self.cilent_machine_send_que = Queue()
        self.cilent_machine_recive_que = Queue()
        self.distrbute_que = Queue()
        self.machine_process_send = Queue()

    def setmanager_port_process(self, cilent_machine_send_que,
                                distrbute_que,
                                cilent_machine_recive_que,
                                machine_process_send):
        self.manger_prot_obj = manager_port(cilent_machine_send_que,
                                            distrbute_que,
                                            cilent_machine_recive_que,
                                            machine_process_send)
        self.manger_prot_obj.getorder()

    def set_machine_process(self):
        self.machine_process_body_ = machine_process_body(self.cilent_machine_send_que,
                                                          self.distrbute_que,
                                                          self.machine_process_send)
        self.machine_process_body_.run()

    def run_(self):
        process_manager = Process(target=self.setmanager_port_process,
                                  args=(self.cilent_machine_send_que, self.distrbute_que, self.cilent_machine_recive_que, self.machine_process_send),
                                  name="manager_port_process")
        process_machine = Process(target=self.set_machine_process,
                                  name="machine_process_")
        process_manager.start()
        process_machine.start()





if __name__ == "__main__":

    xx = all_data_process()
    xx.get_operator_permit_data()
    dataa = console_state_run_class()
    dataa.run_()


