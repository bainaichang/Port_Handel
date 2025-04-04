def bcd_to_int(bcd_bytes: bytes) -> int:
    # 用于2个字节BCD码转int,高位在高地址(反过来)
    if len(bcd_bytes) != 2:
        raise ValueError("Input must be exactly 2 bytes")

    low_byte = bcd_bytes[0]
    high_byte = bcd_bytes[1]

    low_nibble_low = low_byte & 0x0F
    low_nibble_high = (low_byte & 0xF0) >> 4

    high_nibble_low = high_byte & 0x0F
    high_nibble_high = (high_byte & 0xF0) >> 4

    if (low_nibble_high > 9 or low_nibble_low > 9 or
            high_nibble_high > 9 or high_nibble_low > 9):
        raise ValueError("Invalid BCD byte")

    number = (high_nibble_high * 1000 +
              high_nibble_low * 100 +
              low_nibble_high * 10 +
              low_nibble_low)

    return number