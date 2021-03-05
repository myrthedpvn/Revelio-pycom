from network import LoRa
import socket
import time
import ubinascii
import ustruct

def connect():
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    app_eui = ubinascii.unhexlify('70B3D57ED003E9CA')
    app_key = ubinascii.unhexlify('FEF8B5917C63BE0CA338AEF8191EF181')
    dev_eui = ubinascii.unhexlify('70B3D54999521900')
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')
    print('Joined')

def send(data):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    s.setblocking(False)
    packet = ustruct.pack('f',data)
    s.send(packet)
    s.setblocking(False)
