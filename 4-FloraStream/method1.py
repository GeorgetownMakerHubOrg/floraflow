# For this stepper motor setup, I would recommend using the TMC2208 driver.	 I found a number of wiring diagrams that let me set up this board to the ESP32S3.	 There are two ways that we can implement the code:
# Using standard sleep_ms() - I don’t think we need super fast steppers action so this python code will rotate the shaft one full revolution:
from machine import Pin
from time import sleep, sleep_ms

upper = 1600
lower = 0
step = 1

dir_pin = Pin(35, Pin.OUT, value=0)		 # green lead
step_pin = Pin(37, Pin.OUT, value=0)		# blue lead

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
