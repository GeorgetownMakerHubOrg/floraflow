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
	sleep(5)
	dir_pin.off()
	print('Rotate CCW')
	for cycle in range(upper, lower, -step):
		step_pin.on()
		sleep_ms(1)
		step_pin.off()
		sleep_ms(1)
	sleep(2)

# Method 2: Using the ESP32 RMT features - this gets really complicated and very accurate but it’s overkill, imho.   Check out Espressif’s RMT documentation for more details.
import esp32
from machine import Pin
from time import sleep, sleep_ms

dir_pin = Pin(35, Pin.OUT, value=0)     # green lead
rmt = esp32.RMT(0, pin=Pin(37), clock_div=8)

dir_pin.on()
print('Rotate CW')
rmt.loop(True)
rmt.write_pulses((700, 700), 0)  # Send 0 for 700ns, 1 for 700ns

# In either case, we will need a reed switch to home the motor.  On startup, head home until the switch is opened.  I *don’t* think that these motors drift but if they do, we might have to have another switch that disables the motor on the other end?


