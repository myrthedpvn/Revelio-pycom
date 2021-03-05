import wifi
import sonar
import lora
import time
import wifiadafruit

lora.connect()
sonar.read_uart()

#Zet degene die je niet gebruikt in comments
while True:
    sonar.read_uart()
    distance = sonar.get_distance()
    lora.send(distance)
    print(distance)
    time.sleep(10)

#wifi.connect()
#sonar.read_uart()

#while True:
    #sonar.read_uart()
    #distance = sonar.get_distance()
    #wifiadafruit.sendDataWifi(distance)
    #print(distance)
    #time.sleep(10)
