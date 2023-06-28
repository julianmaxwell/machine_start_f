import inspect
from threading import Thread, Lock, Event, Timer
from multiprocessing import Process
import queue
import time
import serial

import serial.tools.list_ports
from functools import partial
import struct
import asyncio
import modbus_tk
from modbus_tk.hooks import call_hooks
from modbus_tk.exceptions import(
    ModbusError, ModbusFunctionNotSupportedError, DuplicatedKeyError, MissingKeyError, InvalidModbusBlockError,
    InvalidArgumentError, OverlapModbusBlockError, OutOfModbusBlockError, ModbusInvalidResponseError,
    ModbusInvalidRequestError)
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu, utils, defines, LOGGER
from modbus_tk.utils import get_log_buffer
from binascii import *
from crcmod import *
import pandas
ModbusInvalidResponseError = modbus_tk.modbus_rtu.ModbusInvalidResponseError


Lock_4m_1m_Lock = Lock()
Lock_COM2 = Lock()
R_all = 4.98
R_inner = 0.001
ruler_distance_range = 101.7
gaze_que = queue.Queue()
gaze_out_que = queue.Queue()

class Exclude(modbus_rtu.RtuMaster):
    @utils.threadsafe_function
    def execute(
            self, slave, function_code, starting_address, quantity_of_x=0, output_value=0, data_format="",
            expected_length=-1, write_starting_address_FC23=0):
        """
        Execute a modbus query and returns the data part of the answer as a tuple
        The returned tuple depends on the query function code. see modbus protocol
        specification for details
        data_format makes possible to extract the data like defined in the
        struct python module documentation
        """

        pdu = ""
        is_read_function = False
        nb_of_digits = 0

        # open the connection if it is not already done
        self.open()

        # Build the modbus pdu and the format of the expected data.
        # It depends of function code. see modbus specifications for details.
        if function_code == defines.READ_COILS or function_code == defines.READ_DISCRETE_INPUTS:
            is_read_function = True
            pdu = struct.pack(">BHH", function_code, starting_address, quantity_of_x)
            byte_count = quantity_of_x // 8
            if (quantity_of_x % 8) > 0:
                byte_count += 1
            nb_of_digits = quantity_of_x
            if not data_format:
                data_format = ">" + (byte_count * "B")
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode + crc1 + crc2
                expected_length = byte_count + 5

        elif function_code == defines.READ_INPUT_REGISTERS or function_code == defines.READ_HOLDING_REGISTERS:
            is_read_function = True

            pdu = struct.pack(">BHH", function_code, starting_address, quantity_of_x)

            if not data_format:
                data_format = ">" + (quantity_of_x * "H")
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode x 2 + crc1 + crc2
                expected_length = 2 * quantity_of_x + 5

        elif (function_code == defines.WRITE_SINGLE_COIL) or (function_code == defines.WRITE_SINGLE_REGISTER):
            if function_code == defines.WRITE_SINGLE_COIL:
                if output_value != 0:
                    output_value = output_value    # 0xff00
                fmt = ">BHH"
            else:
                fmt = ">BH" + ("H" if output_value >= 0 else "h")
            pdu = struct.pack(fmt, function_code, starting_address, output_value)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + value1+value2 + crc1 + crc2
                expected_length = 8
        elif function_code == defines.WRITE_MULTIPLE_COILS:
            byte_count = len(output_value) // 8
            if (len(output_value) % 8) > 0:
                byte_count += 1
            pdu = struct.pack(">BHHB", function_code, starting_address, len(output_value), byte_count)
            i, byte_value = 0, 0
            for j in output_value:
                if j > 0:
                    byte_value += pow(2, i)
                if i == 7:
                    pdu += struct.pack(">B", byte_value)
                    i, byte_value = 0, 0
                else:
                    i += 1
            if i > 0:
                pdu += struct.pack(">B", byte_value)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + outputQuant1 + outputQuant2 + crc1 + crc2
                expected_length = 8

        elif function_code == defines.WRITE_MULTIPLE_REGISTERS:

            if output_value and data_format:

                byte_count = struct.calcsize(data_format)
            else:

                byte_count = 2 * len(output_value)
                print(output_value, "kkkkkkkkkkkkkkkkkkkkkkkkk")
            pdu = struct.pack(">BHHBH", function_code, starting_address, 1, 2, 3)

            print("pdu pdu pdu {}".format(pdu))

        elif function_code == defines.READ_EXCEPTION_STATUS:
            pdu = struct.pack(">B", function_code)
            data_format = ">B"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                expected_length = 5

        elif function_code == defines.DIAGNOSTIC:
            # SubFuncCode  are in starting_address
            pdu = struct.pack(">BH", function_code, starting_address)
            if len(output_value) > 0:
                for j in output_value:
                    # copy data in pdu
                    pdu += struct.pack(">B", j)
                if not data_format:
                    data_format = ">" + (len(output_value) * "B")
                if expected_length < 0:
                    # No length was specified and calculated length can be used:
                    # slave + func + SubFunc1 + SubFunc2 + Data + crc1 + crc2
                    expected_length = len(output_value) + 6

        elif function_code == defines.READ_WRITE_MULTIPLE_REGISTERS:
            # print("pdu ...........{}")
            is_read_function = True
            byte_count = 2 * len(output_value)

            pdu = struct.pack(
                ">BHHHHB",
                function_code, starting_address, quantity_of_x, write_starting_address_FC23,
                len(output_value), byte_count
            )

            for j in output_value:
                fmt = "H" if j >= 0 else "h"
                # copy data in pdu
                pdu += struct.pack(">" + fmt, j)
            if not data_format:
                data_format = ">" + (quantity_of_x * "H")
            if expected_length < 0:
                # No lenght was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode x 2 + crc1 + crc2
                expected_length = 2 * quantity_of_x + 5

        # elif function_code == defines.MOD_SLAVE_ID:
        #     print("fffffffffffffffffffffffffffffffffffff")
        #     is_read_function = False
        #     pdu2 = struct.pack("BHHBH", function_code,  starting_address, quantity_of_x, quantity_of_x*2, output_value)
        #     print("write new pdu is {}".format(pdu2))
        else:
            raise ModbusFunctionNotSupportedError("The {0} function code is not supported. ".format(function_code))

        # instantiate a query which implements the MAC (TCP or RTU) part of the protocol
        query = self._make_query()

        # add the mac part of the protocol to the request

        if type(slave) is tuple:
            slave = slave[0]
        request = query.build_request(pdu, slave)

        # send the request to the slave
        retval = call_hooks("modbus.Master.before_send", (self, request))

        if retval is not None:
            request = retval
        if self._verbose:
            LOGGER.debug(get_log_buffer("-> ", request))

        self._send(request)

        call_hooks("modbus.Master.after_send", (self,))

        if slave != 0:
            # receive the data from the slave
            response = self._recv(expected_length)
            retval = call_hooks("modbus.Master.after_recv", (self, response))
            if retval is not None:
                response = retval
            if self._verbose:
                LOGGER.debug(get_log_buffer("<- ", response))

            # extract the pdu part of the response
            response_pdu = query.parse_response(response)

            # analyze the received data
            (return_code, byte_2) = struct.unpack(">BB", response_pdu[0:2])

            if return_code > 0x80:
                # the slave has returned an error
                exception_code = byte_2
                raise ModbusError(exception_code)
            else:
                if is_read_function:
                    # get the values returned by the reading function
                    byte_count = byte_2
                    data = response_pdu[2:]
                    if byte_count != len(data):
                        # the byte count in the pdu is invalid
                        raise ModbusInvalidResponseError(
                            "Byte count is {0} while actual number of bytes is {1}. ".format(byte_count, len(data))
                        )
                else:
                    # returns what is returned by the slave after a writing function
                    data = response_pdu[1:]

                # returns the data as a tuple according to the data_format
                # (calculated based on the function or user-defined)
                result = struct.unpack(data_format, data)

                if nb_of_digits > 0:
                    digits = []
                    for byte_val in result:
                        for i in range(8):
                            if len(digits) >= nb_of_digits:
                                break
                            digits.append(byte_val % 2)
                            byte_val = byte_val >> 1
                    result = tuple(digits)
                return result

def crc16Add(read):
    crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    read = list(read)
    # print(read, type(read[0]))
    if len(read) % 2 == 1:
        read.insert(2, "0")
    read = "".join(read)
    readcrcout = hex(crc16(unhexlify(read))).upper()
    str_list = list(readcrcout)
    if len(str_list) == 5:
        str_list.insert(2, '0')  # 位数不足补0
    crc_data = "".join(str_list)
    # print(crc_data)
    read = read.strip() + crc_data[4:] + crc_data[2:4]
    # print('CRC16校验:', crc_data[4:] + ' ' + crc_data[2:4])
    # print('增加Modbus CRC16校验：>>>', read)
    return read


def calcludej_back_encode_test(data, circle_dis=300, pulse_every_circle=1024):

    data = data[6:-4]
    l_data = data[0:4]
    l_data = int(l_data, 16)
    l_data = bin(l_data)
    l_data = l_data[2:]
    if len(l_data) < 16:
        l_data = "0" * (16 - len((l_data))) + l_data
    lpulse = l_data[6:]
    lcircle = l_data[:6]
    circls = int(lcircle, 2)
    puls = int(lpulse, 2)
    coordinate = round((circls + puls/pulse_every_circle) * circle_dis, 2)

    return circls, puls, coordinate

def calclude_anlog_12_8_read(data):
    data = data[6:-4]
    len_n = len(data)
    route_data = ["", ] * (int(len_n/4))
    for x in range(len_n):
        route_number = x // 4
        route_data[route_number] = route_data[route_number] + data[x]
    for every_route_number in range(int(len_n/4)):
        route_data[every_route_number] = int(route_data[every_route_number], 16)
    return route_data

def calclude_angle(data):

    slaveid = data[0:2]
    slaveid = "".join(slaveid)
    x_angle = data[6:10]
    x_angle = "".join(x_angle)
    x_angle = int(x_angle, 16)
    y_angle = data[10:14]
    y_angle = "".join(y_angle)
    y_angle = int(y_angle, 16)
    z_angle = data[14:18]
    z_angle = "".join(z_angle)
    z_angle = int(z_angle, 16)
    x_angle = x_angle / 32768 * 180
    y_angle = y_angle / 32768 * 180
    z_angle = z_angle/ 32768 * 180
    return x_angle, y_angle, z_angle

def calclude_encode_distance(data):
    slave_id = data[:2]
    # print(slave_id, ".....................")
    slave_id = "".join(slave_id)
    new_data = data[6:14]
    xx = int(new_data, 16)
    str_dataa = bin(xx)
    str_data = str_dataa[2:]
    while len(str_data) < 32:
        str_data = "0" + str_data
    data_step = int(str_data[1:9], 2)
    i = 0
    result = 0
    deceml_data = str_data[9:]
    while i < 23:
        da = int(deceml_data[i], 2)
        da_result = da * (2 ** (-i))
        result = result + da_result
        i = i + 1
    data = (1 + result / 2) * 2 ** (data_step - 127)
    data = round(data, 3)
    cc = "".join(list(reversed(new_data)))
    datee = int(cc, 16)
    xee = bin(datee)
    # print(xee)
    new_new = hexlify("".join(new_data).encode())
    # print(new_new)
    return slave_id, data

PORT = 'COM4'  # windows 端口是不一样Response address的 看你插的usb口是那个
PORT_usb = "COM5"

def HexToByte(hexStr):
    return bytes.fromhex(hexStr)


def str_to_hex(s):
    return ''.join([hex(ord(c)).replace('0x', '') for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


def modbus_getdate(slave_id, start_addr, date_len, operation_code, output_value=0,  master=None, explain_function=None):
    try:
        holding_date = master.execute(slave_id, operation_code, start_addr, date_len, output_value=output_value,)
        holding_data125 = []
        for i in range(len(holding_date)):
            holding_data125.append('%04x' % (holding_date)[i])  # append()在Tmp1列表末尾添加新的对象
        # all_holding_data = '%02x'%slave_id + '035a' + ''.join(holding_data125)
        all_holding_data = '0103' + '%02x' % (date_len * 2) + ''.join(holding_data125)
        all_holding_data = '%02x' %(slave_id) +"%02x" %(operation_code) + '%02x' % (date_len * 2) + ''.join(holding_data125)
        all_holding_data_crc16Add = crc16Add(all_holding_data)  # 增加Modbus CRC16校验值后的值
        # print("here {} port data is {}".format(slave_id, all_holding_data))
        if explain_function != None:
            return explain_function(str(all_holding_data_crc16Add))
        else:
            return str(all_holding_data_crc16Add)
        # write方法
    except ModbusInvalidResponseError as err:
        pass
        # print(err, __file__, inspect.currentframe().f_lineno)

# x = crc16Add(b'\x03\x00\x00\x00\x0c')
# print(x)

# t1 = time.time()

def get_master(port , baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0, time_out=0.01):
    try:

        master = Exclude(serial.Serial(port=port,
                                       baudrate=baudrate,
                                       bytesize=bytesize,
                                       parity=parity,
                                       stopbits=stopbits,
                                       xonxoff=xonxoff))
        # master 设置的不同参数也不同，要注意这里
        # logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")
        master.set_timeout(time_out)
        master.set_verbose(True)
        return master
    except Exception as e:
        print(e)
        print(__file__, inspect.currentframe().f_lineno)
        return None


# print("value is {}".format(master1_nomale))
try:
    master2_4m1m = get_master(PORT_usb)
except Exception as aa:
    print(PORT_usb, " is not over")
    print(aa)
    print(__file__, inspect.currentframe().f_lineno)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx111")
try:
    master1_nomale = get_master(PORT)
    print(PORT, " is over")
except Exception as bb:
    print(bb)
    print(__file__, inspect.currentframe().f_lineno)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx222")
# first1_time = time.time()
# first_time = time.time()

# data = modbus_getdate(slave_id=4, start_addr=0, date_len=12, operation_code=cst.READ_INPUT_REGISTERS, master=master1_nomale)
# time1 = time.time() - first_time
# first_time = time.time()
# dataa = modbus_getdate(slave_id=1, start_addr=0, date_len=8, operation_code=cst.READ_INPUT_REGISTERS, master=master1_nomale)
# time2 = time.time() - first_time
#
# print(calclude_anlog_12_8_read(data))

"""
西安舟正电子科技有限公司
①主机发送格式：【设备地址】【04】【寄存器地址高字节】【寄存器地址低字节】【寄存
器数高字节】【寄存器数低字节】【CRC 低字节】【CRC 高字节】；
②设备回应：【设备地址】【04】【字节数】【寄存器 1 值高字节】【寄存器 1 值低字节】…
【寄存器 N 值高字节】【寄存器 N 值低字节】【CRC 低字节】【CRC 高字节】
举例，在第 5 通道接 5V 电压输入，读取模块采集值：
主机发送（HEX）：01 04 00 00 00 0C F0 0F；
设备回应（HEX）：01 04 18 00 00 00 00 00 00 00 00 0F FF 00 00 00 00 00 00 00 00 00 00 00
00 00 00 78 3F 
 data is the 1e route equipment operation_code must = 4
 
"""

# data3 = modbus_getdate(slave_id=2, start_addr=8, date_len=2, operation_code=cst.READ_HOLDING_REGISTERS, master=master2_4m1m, explain_function=calclude_encode_distance)   # code = 3


line_test_4m_1m_4m_function = partial(modbus_getdate, slave_id=2, start_addr=8, date_len=2,
                                   operation_code=cst.READ_HOLDING_REGISTERS, master=master2_4m1m, explain_function=calclude_encode_distance)
#
line_test_4m_1m_1m_function = partial(modbus_getdate, slave_id=3, start_addr=8, date_len=2,
                                   operation_code=cst.READ_HOLDING_REGISTERS, master=master2_4m1m, explain_function=calclude_encode_distance)


zouzheng_8_chanel = partial(modbus_getdate, slave_id=1, start_addr=0, date_len=8, operation_code=cst.READ_INPUT_REGISTERS, master=master1_nomale, explain_function=calclude_anlog_12_8_read)
zouzheng_12_chanel = partial(modbus_getdate, slave_id=4, start_addr=0, date_len=12, operation_code=cst.READ_INPUT_REGISTERS, master=master1_nomale, explain_function=calclude_anlog_12_8_read)
data_encode_4m_ = partial(modbus_getdate, slave_id=6, start_addr=3, date_len=2, operation_code=cst.READ_HOLDING_REGISTERS, master=master1_nomale, explain_function=calcludej_back_encode_test)
x_angle_y_angle = partial(modbus_getdate, slave_id=80, start_addr=61, date_len=3, operation_code=cst.READ_HOLDING_REGISTERS, master=master1_nomale, explain_function=calclude_angle)
dataoml = partial(modbus_getdate, slave_id=5, start_addr=0, date_len=1, operation_code=cst.WRITE_SINGLE_COIL, master=master1_nomale, output_value=0x0000)

#
functions = {
    "line_test_4m_1m_4m_function": line_test_4m_1m_4m_function,
    "line_test_4m_1m_1m_function": line_test_4m_1m_1m_function,
    "zouzheng_8_chanel": zouzheng_8_chanel,
    "zouzheng_12_chanel": zouzheng_12_chanel,
    "data_encode_4m_": data_encode_4m_,
    "x_angle_y_angle": x_angle_y_angle,
    "dataoml": dataoml,

}

functions_com1 = ("line_test_4m_1m_4m_function", "line_test_4m_1m_1m_function")
functions_com2 = ("zouzheng_8_chanel", "zouzheng_12_chanel", "data_encode_4m_", "x_angle_y_angle", "dataoml")
delta_tame_gaze = 0.1
delta_time_gaze_com1 = 0.2
# def line_test_4m_1m_loop(que_in=None, que_out=gaze_out_que, timed_out=0):
#     all_count = 0
#     wrong_count = 0
#     while True:
#         time_first = time.time()
#         for every in functions_com1:
#             try:
#                     Lock_4m_1m_Lock.acquire()
#                     data = functions[every]()
#                     time_ = time.time()
#                     data_out = {time_: {every: data}}
#                     que_out.put(data_out)
#                     Lock_4m_1m_Lock.release()
#                     if line_test_4m_1m_EVENT.is_set():
#                         time.sleep(delta_time_gaze_com1)
#                     else:
#                         time.sleep(0.01)
#             except Exception as e:
#                 wrong_count = wrong_count + 1
#                 # print(e, every, "wrong")
#             all_count = all_count + 1

# order_name1 = None
# order_name_com1 = ("line_test_4m_1m_4m_function", "line_test_4m_1m_1m_function")
line_test_4m_1m_EVENT = Event()
#
# def line_test_4m_1m_gaze():
#     while True:
#         line_test_4m_1m_EVENT.wait()
#         if order_name1 in order_name_com1:
#             time_first = time.time()
#             try:
#                 Lock_4m_1m_Lock.acquire()
#                 data = functions[order_name1]()
#                 gaze_out_que.put((order_name1, data))
#                 Lock_4m_1m_Lock.release()
#                 print(order_name1, data, time.time()-time_first)
#
#             except Event as e:
#                 print(e, order_name1)
#                 pass
#
#
#         elif order_name1 == None:
#             line_test_4m_1m_EVENT.clear()

order_name = None

order_name2 = None
order_name_com2 = ("zouzheng_8_chanel", "zouzheng_12_chanel", "data_encode_4m_", "x_angle_y_angle", "dataoml",)
test_all_gaze_EVENT = Event()

def test_all_loop(pipeout=None, pipein=None):

    while True:
        time_first = time.time()
        wrong_count = 0
        for every in functions_com2:
            try:
                Lock_COM2.acquire()
                data = functions[every]()
                print(f"{every} data is {data}")
                gaze_out_que.put((every, data))
                if pipeout is not None:
                    pipeout.send((every, data))
                Lock_COM2.release()
                if test_all_gaze_EVENT.is_set():
                    time.sleep(delta_tame_gaze)
                else:
                    time.sleep(0.01)
            except Exception as e:
                wrong_count = wrong_count + 1
            print("test all wrongcount", wrong_count)

# this data will be read in the setting file. not write here direct
#
def test_all_gaze(pipein=None, pipout=None):
    while True:
        ti = time.time()
        test_all_gaze_EVENT.wait()
        # t2 = time.time() - ti
        # print("t2 is ", t2)
        if order_name2 in order_name_com2:
            try:
                Lock_COM2.acquire()
                data = functions[order_name2]()
                gaze_out_que.put((order_name2, data))
                if pipout is not None:
                    pipout.send((order_name2, data))
                Lock_COM2.release()
                print(data)
                t2 = time.time() - ti
                print("t2 is ", t2)
            except Exception as e:
                print(e, order_name2)
        elif order_name2 == None:
            test_all_gaze_EVENT.clear()
        t2 = time.time() - ti
        print("t2 is ", t2)

def input_data():
    global order_name1, order_name2
    while True:
        input_data_id = gaze_que.get()
        # input_data_id = input("please in put function id :")
        if input_data_id in functions_com1:
            order_name1 = input_data_id
            print("com1 will begin")
            line_test_4m_1m_EVENT.set()
        elif input_data_id in functions_com2:
            order_name2 = input_data_id
            test_all_gaze_EVENT.set()
        else:
            continue

# thread_4m_1m = Thread(target=line_test_4m_1m_loop)
# thread_4m_1m.start()
# thread_4m_4m = Thread(target=line_test_4m_1m_gaze)
# thread_4m_4m.start()
# thread_test_all = Thread(target=test_all_loop)
# thread_test_all.start()
# thread_test_all_gaze = Thread(target=test_all_gaze)
# thread_test_all_gaze.start()
# thread_input_data = Thread(target=input_data)
# thread_input_data.start()

# (x_angle, y_angle, z_angle) = calclude_angle(data2)
# print("x 角度是 {}， y 角度是{}， z 角度是{}".format(x_angle, y_angle, z_angle))
# (circls, pulse, coordinate) = calcludej_back_encode_test(data_encode_4m, 300, 1024)
# print(calclude_anlog_12_8_read(data))
# print(calclude_anlog_12_8_read(dataa))
# print("the circle is {}, and the pulse is {}, so  the coordinate is {} ".format(circls, pulse, coordinate),
#       "all sensor work is over")
# all_time = time.time() - first1_time
# print(all_time)
#
# print(time1, time2, time3, time4, time5, "<4m", time_ff, "<1m",  time6)
# print(int(1/0.07))
#
class Borad_Ssensor_loop:
    def __init__(self, pipein, pipeout):
        self.pipein = pipein
        self.pipout = pipeout
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx111")
        self.master1_nomale = get_master(PORT)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx222")
        self.master2_4m1m = get_master(PORT_usb)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx333")
        self.first1_time = time.time()
        self.first_time = time.time()
        self.line_test_4m_1m_4m_function = partial(modbus_getdate, slave_id=2, start_addr=8, date_len=2,
                                              operation_code=cst.READ_HOLDING_REGISTERS, master=self.master2_4m1m,
                                              explain_function=calclude_encode_distance)

        self.line_test_4m_1m_1m_function = partial(modbus_getdate, slave_id=3, start_addr=8, date_len=2,
                                              operation_code=cst.READ_HOLDING_REGISTERS, master=self.master2_4m1m,
                                              explain_function=calclude_encode_distance)

        self.zouzheng_8_chanel = partial(modbus_getdate, slave_id=1, start_addr=0, date_len=8,
                                    operation_code=cst.READ_INPUT_REGISTERS, master=master1_nomale,
                                    explain_function=calclude_anlog_12_8_read)
        self.zouzheng_12_chanel = partial(modbus_getdate, slave_id=4, start_addr=0, date_len=12,
                                     operation_code=cst.READ_INPUT_REGISTERS, master=master1_nomale,
                                     explain_function=calclude_anlog_12_8_read)
        self.data_encode_4m_ = partial(modbus_getdate, slave_id=6, start_addr=3, date_len=2,
                                  operation_code=cst.READ_HOLDING_REGISTERS, master=master1_nomale,
                                  explain_function=calcludej_back_encode_test)
        self.x_angle_y_angle = partial(modbus_getdate, slave_id=80, start_addr=61, date_len=3,
                                  operation_code=cst.READ_HOLDING_REGISTERS, master=master1_nomale,
                                  explain_function=calclude_angle)
        self.dataoml = partial(modbus_getdate, slave_id=5, start_addr=0, date_len=1, operation_code=cst.WRITE_SINGLE_COIL,
                          master=master1_nomale, output_value=0x0000)

        self.functions = {
            "line_test_4m_1m_4m_function": line_test_4m_1m_4m_function,
            "line_test_4m_1m_1m_function": line_test_4m_1m_1m_function,
            "zouzheng_8_chanel": zouzheng_8_chanel,
            "zouzheng_12_chanel": zouzheng_12_chanel,
            "data_encode_4m_": data_encode_4m_,
            "x_angle_y_angle": x_angle_y_angle,
            "dataoml": dataoml,

        }
        self.functions_com1 = ("line_test_4m_1m_4m_function", "line_test_4m_1m_1m_function")
        self.functions_com1_dict = dict(zip(self.functions_com1, [0.05, 0.01]))
        self.functions_com2 = ("zouzheng_8_chanel", "zouzheng_12_chanel", "data_encode_4m_", "x_angle_y_angle", "dataoml")
        self.delta_tame_gaze = 0.1
        self.delta_time_gaze_com1 = 0.2

        self.order_name1 = None
        self.order_name_com1 = ("line_test_4m_1m_4m_function", "line_test_4m_1m_1m_function")
        self.obersvation_event = Event()
        self.order_name = None
        self.order_name2 = None
        self.order_name_com2 = ("zouzheng_8_chanel", "zouzheng_12_chanel", "data_encode_4m_", "x_angle_y_angle", "dataoml",)
        self.test_all_gaze_EVENT = Event()

    def time_out(self, timed_out_=0):
        if timed_out_ != 0:
            Timer_ = Timer(timed_out_, self.time_out)
            timer_P = Process(target=Timer_.start)
        else:
            pass

    def loopRecveSendData(self, equepment_set, que_in=None, que_out=gaze_out_que, timed_out=0, Pipe_out=None):
        all_count = 0
        wrong_count = 0
        time__ = time.time
        Pipe_out_send = Pipe_out.send
        data_r = pandas.Series({"time_begin": None, "time_end": None, "delta_time": None, "order_name": None, "time_out":5})
        if self.pipein is not None:
            pipein = self.pipein
            pipeout = self.pipout
        else:
            pipein = None
            pipeout = None
        while True:
            for every in equepment_set:
                try:
                    Lock_4m_1m_Lock.acquire()
                    time_begin = time__()
                    data_observation_data = {"time_begin": time_begin, "time_end": None, "delta_time": None, "order_name": every, "time_out":5}
                    data_r.loc["time_begin"],  data_r.loc["order_name"] = time_begin, every
                    Pipe_out_send(data_observation_data)
                    data = functions[every]()
                    time_end = time__()
                    delta_time = time_end - time_begin
                    data_observation_data["time_end"] = time_end
                    data_observation_data["delta_time"] = delta_time
                    Pipe_out_send(data_observation_data)
                    data_out = {time_end: {every: data}}
                    if pipeout is not None:
                        pipeout.send(data_out)
                    else:
                        que_out.put(data_out)
                    Lock_4m_1m_Lock.release()
                    if line_test_4m_1m_EVENT.is_set():
                        time.sleep(delta_time_gaze_com1)
                    else:
                        time.sleep(0)
                except Exception as e:
                    wrong_count = wrong_count + 1
                    # print(e, every, "wrong")
                all_count = all_count + 1

    def write_data(self, value, Pipe_out_tosensor):

        time__ = time.time
        Pipe_out_tosensor = Pipe_out_tosensor.send
        data_r = pandas.Series(
            {"time_begin": None, "time_end": None, "delta_time": None, "order_name": None, "time_out": 5})

    def setting_point(self):
        pass

    def read_data(self, pin_id):
        pass

    def run_all_loop(self):
        thread_test_all = Thread(target=test_all_loop, args=(self.pipein, self.pipout))
        thread_test_all.start()
        thread_test_all_gaze = Thread(target=test_all_gaze, args=(self.pipein, self.pipout))
        thread_test_all_gaze.start()
        thread_input_data = Thread(target=input_data, args=(self.pipein, self.pipout))
        thread_input_data.start()

    def run_observation(self, pipefrom_sensor_loop, time_out=0.01):
        while True:
            if pipefrom_sensor_loop.poll(time_out):
                data = pipefrom_sensor_loop.recve()
                # data format is data["sensor_name", "", "time_out"] =

# if __name__ == "__main__":
#     import multiprocessing
#     piper, pipes = multiprocessing.Pipe()
#     Borad_Ssensor_loop(piper, pipes)