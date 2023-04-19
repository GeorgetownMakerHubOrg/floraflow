# GNU General Public License <https://www.gnu.org/licenses>
#
# Copyright (c) 2021 F. Pascal Girard
#
# Tool tests the PWM module on the base station.
# 
# Uses the following modules:
# bme280 - https://github.com/robert-hh/BME280
# 
# Implemented on a Lolin ESP32S2 Mini module
#
from machine import Pin, I2C, SoftI2C 
import sensors.bme280_float as bme280
from time import sleep

INTERVAL = 60 * 1000   # once a minute

i2c2 = SoftI2C(scl=Pin(35), sda=Pin(33))

# Pin assignments 
sensor = bme280.BME280(i2c=i2c2, address=118)

def Fahrenheit(x) : 
    return (x * 9/5) + 32

print("Start BME280 test code.")

while (True):
    # In all cases, read sensors, calculate PID
    temperature, pressure, humidity = sensor.read_compensated_data()
    print('T: ', Fahrenheit(temperature), 'P: ', pressure, 'H: ', humidity)
    sleep(1)

