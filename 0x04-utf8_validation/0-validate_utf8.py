#!/usr/bin/python3
"""UTF-8 Validation"""


def get_bytes_count(num):
    tmp = num
    count = 0
    while tmp & 0b10000000:
        count += 1
        tmp <<= 1
    return count - 1


def validUTF8(data):
    i = 0
    while i < (len(data)):
        if data[i] > 127:
            print(bin(data[i]))
            num_bytes = get_bytes_count(data[i])
            print(num_bytes)
            if num_bytes == 0:
                return False
            for j in range(i + 1, i + num_bytes):
                if j >= len(data):
                    return False
                if data[j] & 0b11000000 != 0b10000000:
                    return False
            i = j
        i += 1
    return True
