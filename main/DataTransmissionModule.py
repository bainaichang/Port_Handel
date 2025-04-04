'''
该文件封装了CPU,MCU等模块之间通信的函数
'''
import struct

from serial import Serial
from main.DataObj.BackplaneFirmwareInformation import BackplaneFirmwareInformation
from main.DataObj.BackplaneModuleInformation import BackplaneModuleInformation
from main.DataObj.DiagnosisInfo import DiagnosisInfo
from main.DataObj.RX_PDO_DATA import RX_PDO_DATA


# ARM CPU发送 读背板固件信息 Read backplane firmware information

def sendBackplaneFirmwareInformation():
    return bytes([0x55, 0x55, 0x05, 0x01, 0x16])


# ARM CPU接收MUC的读背板固件信息
# 参数信息 ser: 串口连接对象
# 返回值为一个数据类, 如果为空表示数据读取失败
# read返回的是bytes字节数组, 但是对数组取值[0]会把二进制转成10进制数, 使用截取[0:0]得到的是字节数组
def receiveBackplaneFirmwareInformation(ser: Serial):
    tmp = ser.read(2)
    # 校验数据头是否正确
    if tmp[0] != 0x55 or tmp[1] != 0x55:
        print('背板固件信息错误 数据头不是0x55 0x55!')
        return None
    length = ser.read(1)[0]
    functionCode = ser.read(1)[0]
    versionStr = ser.read(4).decode('utf-8')
    RXTX_Len = ser.read(1)[0]
    reserved = ser.read(31)
    if ser.read(1)[0] != 0x16:
        print('ARM CPU接收MUC的读背板固件信息错误! 数据尾不对')
        return None
    info = BackplaneFirmwareInformation(length, functionCode, versionStr, bytes([0x1]), reserved)
    return info


# ARM CPU发送读模块信息函数
def sendBackplaneModuleInformation() -> bytes:
    return bytes([0x55, 0x55, 0x05, 0x12, 0x16])


# MCU 应答读模块信息
# 参数: ser: 串口连接对象
# 返回值: 背板模块信息封装对象
def receiveBackplaneModuleInformation(ser: Serial):
    data = ser.read(3)
    if data[0] != 0x55 or data[1] != 0x55:
        print('MCU读模块信息错误 头不对')
        return None
    if data[2] == 0x05:
        print('背板没准备好!')
        return None
    length = data[2]
    data = ser.read(length - 3)
    if data[-1] != 0x16:
        print('度模块信息错误 尾不对')
    functionCode = data[0:0]
    moduleLength = data[1]
    moduleCodeList = data[2:-1]
    return BackplaneModuleInformation(length, functionCode, moduleLength, moduleCodeList)


# ARM CPU写TX PDO数据
# 参数: PDO_Data: PDO数据 ,info: 接收的模块信息封装对象
# 返回值: 返回封装好的字节流
def send_TX_PDO_Data(PDO_Data: bytes, info: BackplaneModuleInformation):
    data = bytes([0x55, 0x55])  # 帧头
    moduleLength = 0
    # 统计模块的字节总长度
    for e in info.moduleCodeList:
        moduleLength += info.moduleCodeMapping[e][3]
    length = moduleLength + 6
    data += struct.pack('<H', length)  # 将 length 转换为小端模式的无符号 2 字节字节流
    data += bytes([0x34])
    data += PDO_Data
    data += bytes([0x16])
    return data


# ARM CPU 读RX PDO数据
# 返回读RX PDO 指令的字节流
def send_read_RX_RDO_Data():
    return bytes([0x55, 0x55, 0x05, 0x56, 0x16])


# 接收MCU向ARM CPU 应答RX PDO 的数据
# 返回值: PX PDO封装对象

def receive_RX_PDO(ser: Serial, info: BackplaneModuleInformation):
    data = ser.read(2)
    if data[0] != 0x55 or data[1] != 0x55:
        print('RX_PDO信息错误 头不对')
        return None
    length = ser.read(2)
    length = struct.unpack('<H', length)[0]  # 将字节流转换为小端模式的无符号整数
    functionCode = ser.read(1)
    if functionCode[0] != 0x16:
        print('RX PDO功能码不对', functionCode[0])
        return None
    PDO_module_index = 0
    PDO_Data_mapping = dict()
    for e in info.moduleCodeList:
        # e表示每个模块的编码
        # info.moduleCodeMapping[e][3]表示e这个模块的长度
        PDO_Data_mapping[PDO_module_index] = ser.read(info.moduleCodeMapping[e][3])
        PDO_module_index += 1
    end = ser.read(1)
    if end[0] != 0x16:
        print('RX PDO结束码不正确', end[0])
    return RX_PDO_DATA(length, PDO_Data_mapping)


# ARM CPU 读背板诊断信息
# 返回值: ARM CPU 读背板诊断信息指令的字节流
def send_read_diagnosis_info():
    return bytes([0x55, 0x55, 0x05, 0x78, 0x16])


# MUC 返回诊断信息
# 参数: ser: 串口连接对象
# 返回值: 返回诊断信息封装对象
def receive_diagnosis_info(ser: Serial):
    data = ser.read(2)
    if data[0] != 0x55 or data[1] != 0x55:
        print('MCU 返回诊断信息信息错误: 头不对')
        return None
    length = ser.read(1)[0]
    functionCode = ser.read(1)
    if functionCode[0] != 0x70:
        print("MCU 返回诊断信息信息错误: 功能码错误")
        return None
    module_bus_info = ser.read(4)
    module_power_info = ser.read(4)
    module_soft_version_info = ser.read(32)
    if ser.read(1)[0] != 0x16:
        print("MCU 返回诊断信息信息错误: 尾错误")
        return None
    return DiagnosisInfo(length, module_bus_info, module_power_info, module_soft_version_info)
