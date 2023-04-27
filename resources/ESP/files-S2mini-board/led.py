from machine import Pin, PWM
from time import sleep

frequency = 10000
led = PWM(Pin(5), freq=frequency)
upper = 1023
lower = 0
step = 1

while True:
  for cycle in range(lower,upper, step):
    led.duty(cycle)
    print('Duty cycle is: ',cycle)
    sleep(.01)
  sleep(5)
  for cycle in range(upper, lower, -step):
    led.duty(cycle)
    print('duty cycle is: ',cycle)
    sleep(.01)
  led.duty(0)
  sleep(5)

