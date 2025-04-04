# 诊断信息类
class DiagnosisInfo:
    length = 0
    functionCode = 0x70
    # 共有32个模块

    # 每个Bit表示一个扩展模块的背板总线故障
    module_bus_info = bytes()
    # 每个Bit表示一个扩展模块的电源诊断故障
    module_power_info = bytes()
    # 依次表示扩展模块的软件版本号，如0x10，表示该模块的软件版本号是V1.0
    module_soft_version_info = bytes()
    def __init__(self,length:int,module_bus_info:bytes,module_power_info:bytes,module_soft_version_info:bytes):
        self.length = length
        self.module_bus_info = module_bus_info
        self.module_power_info = module_power_info
        self.module_soft_version_info = module_soft_version_info