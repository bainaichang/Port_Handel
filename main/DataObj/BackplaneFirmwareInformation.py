class BackplaneFirmwareInformation:
    # 这个类是ARM CPU发送读背板固件信息数据类的封装
    # 头应为 0x55 0x55
    length = 1              # 数据帧长
    functionCode = 0        # 功能码
    versionStr = []         # 4字节的版本号字符串
    RXTX_Len = 0x1          # 0x1表示RXTX长2B, 0x0表示长1B
    reserved = []           # 为31个字节的数据

    def __init__(self, length:int, functionCode:int, versionStr:str, RXTX_Len:bytes, reserved:bytes):
        self.length = length
        self.functionCode = functionCode
        self.versionStr = versionStr
        self.RXTX_Len = RXTX_Len
        self.reserved = reserved
