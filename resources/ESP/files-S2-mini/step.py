# a simple test for moving a stepper motor one full rotation in both directions.
from machine import Pin
from time import sleep, sleep_ms

upper = 1600
lower = 0
step = 1

dir_pin = Pin(35, Pin.OUT, value=0)     # green lead
step_pin = Pin(37, Pin.OUT, value=0)    # blue lead

while True:
  dir_pin.on()
  print('Rotate CW')
  for cycle in range(lower,upper, step):
    step_pin.on()
    sleep_ms(1)
    step_pin.off()
    sleep_ms(1)
  sleep(1)
  dir_pin.off()
  print('Rotate CCW')
  for cycle in range(upper, lower, -step):
    step_pin.on()
    sleep_ms(1)
    step_pin.off()
    sleep_ms(1)
  sleep(1)

