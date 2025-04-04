# 方式1：调用函数接口打开串口时传入配置参数
import serial
from serial.serialutil import PARITY_ODD

from main.DataObj.BackplaneModuleInformation import BackplaneModuleInformation

# port_name = 'COM1'
# ser = serial.Serial(port_name, 9600, parity=PARITY_ODD)
# data = ser.read(2)
# print(data[0]==0x10)
myMap = dict()
myMap['s'] = 1
