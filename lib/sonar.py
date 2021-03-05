import pycom
import time
from machine import UART

uart = UART(1)

def read_uart():
    uart.init(9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3', 'P4'))

def get_distance():
        header_bytes = uart.read(1)
        while(header_bytes != b'\xff'):
            header_bytes=uart.read(1)
        data_high = int(uart.read(1)[0])
        data_low = int(uart.read(1)[0])
        data_sum = int(uart.read(1)[0])
        sum = data_high + data_low
        if (sum == data_sum + 1):
            distance = (data_high*256 + data_low)/10
            return distance
