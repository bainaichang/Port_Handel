class RX_PDO_DATA:
    length = 0
    functionCode = 0x06
    # key: 第几个模块(从0开始) value: 该模块的字节流
    PDO_Data_mapping = {
        0: bytes([0x00])
    }
    def __init__(self,length:int,PDO_Data_mapping:dict):
        self.length = length
        self.PDO_Data_mapping = PDO_Data_mapping
