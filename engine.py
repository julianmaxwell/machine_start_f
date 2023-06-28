## this module is used to read the real data of the ardiuno_board , result is the basic data.

import inspect
from multiprocessing import Process ,Manager, Queue, Pipe
from threading import Thread
import seting
import time
import ardiuno_board
import random
forward = 1
backward = 2
stop = 3

DATA = [1, 1, 1, 1, 1]
DATA2 = [0, 0, 0, 0, 0]
encode_push_pull_pole_obj = seting.setting_class.statistatics_encode_push_pull_equipment()

class board_basic_data_operation():
    # pipe_read_write, pipe_write_read, pipe_write_back_write
    def __init__(self,pipeGetFromProcessStationWilltoEquepment, pipeSendtoObservation):
        print(f"im class is {type(self).__name__}, im lines {inspect.currentframe().f_lineno} , my file_name is {__file__}")
        self.getisetin_data()
        self.pipeGetFromProcessStationWilltoEquepment = pipeGetFromProcessStationWilltoEquepment
        self.pipeSendtoObservation = pipeSendtoObservation
        self.equipment_obj_calcludes_dict = {}
        self.ReadWrite_obj = ardiuno_board.ReadWrite(pipeGetFromProcessStationWilltoEquepment, pipeSendtoObservation)
        print(
            f"im class is {type(self).__name__}, im lines {inspect.currentframe().f_lineno} , my file_name is {__file__}")

    def runing(self):

        self.ReadWrite_obj.write_data()



    def get_machine_port_obj_name(self):
        pass

    def getisetin_data(self):
       self.port_all_need_read_pin = seting.setting_class.getisetin_data()
       self.port_all_need_read_pin_2 = seting.setting_class. getisetin_modbus_485_child()
       self.port_all_need_read_pin.append(self.port_all_need_read_pin_2)


class dangger(Exception):
    def __init__(self, danger_new):
        super().__init__()
        self.danger = danger_new
    def __str__(self):
        return self.danger


class simulate:
    def __init__(self, port_all_need_read_pin):
         self.port_all_need_read_pin = port_all_need_read_pin
         self.example_dataset_read()
         self.example_dataset_write()

    def run(self):
        while True:
            time_ = time.time()
            # read_example = {time_:[( 20,False, 'DIGITAL'),( 21, True,'DIGITAL,')]}

    def example_dataset_read(self):
        self.pin_write = {}
        self.time_example_readdata = {}
        self.read_example ={}
        port_pin_example = {}
        for every_pin in self.port_all_need_read_pin:

                if every_pin[2] == "DIGITAL" and every_pin[3] == 'INPUT':
                    choise_data1 = [True,False]
                    pin_value = random.choice(choise_data1)
                    port_pin_example[every_pin] = pin_value
                if every_pin[2] == 'ANALOG' and every_pin[3] == 'INPUT':
                    choise_data = [x for x in range(0, 1000)]
                    pin_value = random.choice(choise_data)
                    port_pin_example[every_pin] = pin_value
        self.read_example.update(port_pin_example)
        time.sleep(0.001*random.choice([x for x in range(20)]))
        timekey = time.time()
        self.time_example_readdata[timekey] = port_pin_example
        return self.time_example_readdata

    def example_dataset_write(self):
        can_out_pin ={}
        self.example_write_data = {}
        self.time_example_write_data = {}

        for pin_data in self.port_all_need_read_pin:
                if pin_data[2] == 'DIGITAL' and pin_data[3] == 'OUTPUT':
                    pin_number = pin_data[1]
                    pin_value = random.choice([True,False])
                    can_out_pin.update({pin_data:pin_value})
                if pin_data[2] == 'ANALOG' and  pin_data[3] == 'OUTPUT':
                    pin_number = pin_data[1]
                    pin_value = random.choice([x for x in range(0,1000)])
                    can_out_pin.update({pin_data:pin_value})
        self.example_write_data.update(can_out_pin)

        time.sleep(0.003*random.choice([0,1,2,3,4,5,6]))
        ctime_ = time.time()
        self.time_example_write_data[ctime_] = self.example_write_data

        return self.time_example_write_data
    def check_write_data(self,data):
        if type(data) != dict:
            print("data_type_errols")
        for time_,data_ in data.items():
            if type(data_) == dict:
                right = {}
                wrong = {}
                for port_,port_data in data_.items():
                    checkpoint = self.check_point(port_)
                    if type(port_data) == list:
                        right_ = set()
                        wrong_ = set()
                        for pin_data in port_data:
                            if type(pin_data) is not tuple:
                               pass
                            else:
                                point_data_check = (pin_data[0],pin_data[2],'OUTPUT')
                                if point_data_check in checkpoint :
                                    # check( 20, 'DIGITAL','OUTPUT'))
                                    #  pin_data (pin_number, pin_value, pin_data[0]) ==> pin_data[0] == 'DIGITAL'
                                    right_.add(pin_data)
                                else:
                                    wrong_.add(pin_data)
                        right[port_] = right_
                        wrong[port_] = wrong_
                if len(wrong) == 0:
                     return True
                else:
                    print("wrong===========>", wrong)
                print("right==========>",right)
    def check_point(self,port_):
        pass
        return True

class CalcludeRockerArm:
    direction = {
        (1, 0): forward,   #"clock_wise"
        (0, 1): backward   # "anti_cloc wise"
    }

    def __init__(self, A_pin, B_pin,Forward_pin, Backward_pin, recve_pin, equipment_obj_name):
        self.equipment_obj_name = equipment_obj_name
        self.A_pin_addr = A_pin
        self.B_pin_addr = B_pin
        self.Forward_pin = Forward_pin
        self.Backward_pin = Backward_pin
        if recve_pin != None:
            self.recve_pin_addr = recve_pin
        self.direction = "stop"
        self.count_begin = 0
        self.time_begin = 0
        self.anolog_data_avel = 0
        self.anolog_data = []
        self.operation_a_list = []
        self.avel_i = 0

    # temporary_data[push_pull_equipment_obj.A_pin], temporary_data[push_pull_equipment_obj.B_pin]

    def encode_decode(self, temporary_data, order):  ###this function an usede by distance and direct

        if order != None:
            if self.Forward_pin in order.keys():
                if (order[self.Forward_pin], order[self.Backward_pin]) == (0, 1):
                    self.direction = "forward"
                elif(order[self.Forward_pin], order[self.Backward_pin]) == (1, 0):
                    self.direction = "backward"
                elif (order[self.Forward_pin], order[self.Backward_pin]) == (1, 1):
                    self.direction = "stop"

        if hasattr(self, "recve_pin_addr"):
            if self.avel_i < 6:
                self.anolog_data.append(temporary_data[self.recve_pin_addr])
                self.avel_i = self.avel_i + 1
            else:
                average_data_ = int(sum(self.anolog_data)/6)
                self.avel_i = 0
                self.anolog_data = []
                if self.recve_pin_addr[1] == 11:
                    print("i receive the annog data {} pin number is A{}".format(average_data_, self.recve_pin_addr[1]))
        if self.count_begin < 10001:
            if self.time_begin == 0:
                self.time_begin = time.time()
            self.count_begin = self.count_begin + 1
        else:
            time_delta = time.time() - self.time_begin
            # print("the count every s speed is {}".format(int(self.count_begin / time_delta)))
            self.count_begin = 0
            self.time_begin = time.time()

def run(ff_read, ff_write, ff_write_back):
    board_engine = board_basic_data_operation(ff_read, ff_write, ff_write_back)
    board_engine.runing()

if __name__  == '__main__':
    # pipe_read_write, pipe_write_read, pipe_write_back_write
    ff_read = Queue()
    ff_write = Queue()
    ff_write_back = Queue()
    pipe_write_read, pipe_write_write = Pipe()
    pipe_write_back_read, pipe_write_back_write = Pipe()
    pipe_read_read, pipe_read_write = Pipe()

    borard_process = Process(target=run, args=(pipe_read_write, pipe_write_read, pipe_write_back_write))
    borard_process.start()