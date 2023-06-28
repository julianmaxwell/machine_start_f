from binascii import *
import crcmod

#生成CRC16-MODBUS校验码
def crc16Add(read):
    # hexlify(data)
    # # Hexadecimal representation of binary data.
    # (unhexlify(hexstr)
    #  Binary data of hexadecimal representation.
    crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    data = read.replace(" ", "") #消除空格
    print("crc before : {}, type is {}".format(data, type(data)))
    print("change first : {}".format(unhexlify(data)))
    print("crc over {}, type is : ".format(crc16(unhexlify(data))), type(crc16(unhexlify(data))))
    print("turn over and next will do upper() {}, current type  is {}".format(hex(crc16(unhexlify(data))), type(hex(crc16(unhexlify(data))))))

    readcrcout = hex(crc16(unhexlify(data))).upper()
    print("oupper() is over ,new data is {}".format(readcrcout))
    str_list = list(readcrcout)
    print(str_list, len(str_list))
    if len(str_list) == 5:
        str_list.insert(2, '0')  # 位数不足补0，因为一般最少是5个
    crc_data = "".join(str_list) #用""把数组的每一位结合起来  组成新的字符串
    print(crc_data)
    read = read.strip() + ' ' + crc_data[4:] + ' ' + crc_data[2:4] #把源代码和crc校验码连接起来
    # print('CRC16校验:', crc_data[4:] + ' ' + crc_data[2:4])
    print(read)
    return read

if __name__ == '__main__':
    crc16Add("01 06 00 66 00 C8 00 00")