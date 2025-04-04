# 这个类是背板模块信息的类
class BackplaneModuleInformation:
    length = 0
    functionCode = 0x00
    moduleLength = 0
    # 表示每个模块的类型编码的字节流
    moduleCodeList = None
    # 产品型号, 产品描述, 输入字节, 输出字节
    moduleCodeMapping = {
        0x00: ('TTOS-214-00A', '数字量输入模块, 16输入,支持PNP/NPN输入', 2, 0),
        0x01: ('TTOS-215-00A', '数字量输入模块, 32输入,支持PNP/NPN输入', 4, 0),
        0x02: ('TTOS-224-00A', '数字量输出模块, 16输出,PNP输出', 0, 2),
        0x03: ('TTOS-224-01A', '数字量输出模块, 16输出,继电器输出', 0, 2),
        0x04: ('TTOS-225-00A', '数字量输出模块, 32输出,PNP输出', 0, 4),
        0x05: ('TTOS-234-00A', '数字量输入/输出模块, 8输入/8输出,PNP输出', 1, 1),
        0x06: ('TTOS-234-01A', '数字量输入/输出模块, 8输入/8输出,继电器输出', 1, 1),
        0x07: ('TTOS-234-01A', '数字量输入/输出模块, 16输入/16输出,PNP输出', 2, 2),
        0x08: ('TTOS-312-03A', '模拟量输入模块, 4 输入,16位精度，电压/电流输入', 8, 1),
        0x09: ('TTOS-313-03A', '模拟量输入模块,8 输入,16位精度，电压/电流输入', 16, 1),
        0x0A: ('TTOS-314-02A', '模拟量输入模块,16 输入,16位精度，电压输入', 32, 1),
        0x0B: ('TTOS-314-01A', '模拟量输入模块,16 输入,16位精度，电流输入', 32, 1),
        0x0C: ('TTOS-322-03A', '模拟量输出模块, 4 输出,16位精度，电压/电流输出', 0, 8),
        0x0D: ('TTOS-323-01A', '模拟量输出模块, 8 输出,16位精度，电流输出0~20mA', 0, 16),
        0x0E: ('TTOS-312-0TA', '热电偶测量模块, 4 输入,通道隔离，J、K等输入（XML文件配置），支持外部NTC补偿', 8, 1),
        0x0F: ('TTOS-313-0TA', '热电偶测量模块, 8 输入,通道隔离，J、K 等输入（XML 文件配置），支持外部NTC 补偿', 16, 1),
        0x10: ('TTOS-312-0RA', '热电阻测量模块, 4 输入,通道隔离，PT100、PT1000 等', 8, 1),
        0x11: ('TTOS-313-0RA', '热电阻测量模块, 8 输入,通道隔离，PT100、PT1000 等', 16, 1),
        0x12: ('TTOS-412-1CA',
               '2 通道高速计数模块，24V 单端输入/5V 差分，最大频率200KHZ/1MHZ，支持A,B 正交脉冲计数和脉冲+方向计数', 28,
               20),
        0x13: ('TTOS-412-0CA', '2 组同步串行（D+,D-,CI+,CI-）接口，最大通信速率1MHZ，支持多圈和单圈SSI 编码器', 16, 11),
        0x14: ('TTOS-402-3NA', '两个COM，Modbus 主/从站模式；每个串口拥有128 个字节（输入、输出）数据。', 128, 128),
        0x15: ('TTOS-402-3NA', '两个COM，自由口模式；每个串口拥有128 个字节（输入、输出）数据。', 128, 128)
    }

    def __init__(self, length: int, functionCode: bytes, moduleLength: int, moduleCodeList: bytes):
        self.length = length
        self.functionCode = functionCode
        self.moduleLength = moduleLength
        self.moduleCodeList = moduleCodeList
