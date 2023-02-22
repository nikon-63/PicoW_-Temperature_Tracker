# Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import onewire, ds18x20, time
import network   
import urequests 

wlan = network.WLAN(network.STA_IF)
wlan.active(True)


ssid = 'ENTER SSID'
password = 'PASSWORD'
wlan.connect(ssid, password)

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)


SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
roms = sensor.scan()

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
time.sleep(1) 

display = SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.text("Booting",0,0)
display.show()

numUpload = 0
run = 1

while run == 1:
    sensor.convert_temp() 
    time.sleep(300)
    if button1.value() == 1:
        print("Press")
        display.fill(0)
        display.text("Stop",0,0)
        display.show()
        stopData = str(numUpload)
        display.text(stopData,0,12)
        display.show()
        run = 0
    elif button1.value() == 0:
        for rom in roms:
            numUpload = numUpload + 1
            print((sensor.read_temp(rom)),"°C")
            data = sensor.read_temp(rom)
            data = str(data)
            display.fill(0)
            display.text(data,0,0)
            display.text('Running',0,12)
            display.text(str(numUpload),0,24)
            display.show()
            r = urequests.get('http://ENTERURL/api/tempCheck.php?id='+str(numUpload)+'&temp='+data).text
        
 

