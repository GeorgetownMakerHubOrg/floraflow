# This script continually reads from the sensors
from sensors.bh1750 import BH1750
from sensors.sht30 import SHT30
from time import sleep
from machine import Pin, SoftI2C
i2c = SoftI2C(scl=Pin(35), sda=Pin(33))
light = BH1750(i2c) # light sensor (lumens)
th = SHT30(i2c) # temperature & humidity sensor
while True: 
	i2c.scan()
	temperature, humidity = th.measure()
	print('luminance: ', light.luminance(BH1750.ONCE_HIRES_1))
	print('temperature: ', temperature)
	print('humidity: ', humidity)
	sleep(0.5)
