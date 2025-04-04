class BackplaneFirmwareInformation:
    # 这个类是ARM CPU发送读背板固件信息数据类的封装
    # 头应为 0x55 0x55
    length = 1              # 数据帧长
    functionCode = 0x00     # 功能码, 应该为0x11
    versionStr = []         # 4字节的版本号字符串
    RXTX_Len = 0x1          # True表示RXTX长2B, False表示长1B PDF中看起来恒定为0x1
    reserved = []           # 为31个字节的数据

    def __init__(self, length:int, functionCode:bytes, versionStr:str, RXTX_Len:bytes, reserved:bytes):
        self.length = length
        self.functionCode = functionCode
        self.versionStr = versionStr
        self.RXTX_Len = RXTX_Len
        self.reserved = reserved
