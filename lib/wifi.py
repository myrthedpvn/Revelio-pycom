from network import WLAN
import machine
import pycom
import time
import request

wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)

def connect():
    wlan.connect(ssid='IoT', auth=(WLAN.WPA2, 'KdGIoT92!'))
    while not wlan.isconnected():
        time.sleep(2)
        pycom.rgbled(0xFF0000)
    print("WiFi connected succesfully")
    pycom.rgbled(0x00FF00)
    time.sleep(2)
    print(wlan.ifconfig())
