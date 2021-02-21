from network import WLAN
import machine
import pycom
import time
wlan = WLAN(mode=WLAN.STA)

pycom.heartbeat(False)

wlan.connect(ssid='WiFi-2.4-AE1C', auth=(WLAN.WPA2, 'w72yxbfkbj5k9'))
while not wlan.isconnected():
    time.sleep(2)
    pycom.rgbled(0xFF0000)
print("WiFi connected succesfully")
pycom.rgbled(0x00FF00)
time.sleep(2)
print(wlan.ifconfig())
