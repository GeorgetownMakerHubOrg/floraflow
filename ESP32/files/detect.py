# Micropython code for detecting power

import os, network, json, ntptime
import utime as time
import urequests as requests
import uasyncio
from machine import Pin, Signal, Timer, enable_irq, disable_irq
import config

# Change these to match your unique identifiers

led_pin = Pin(15, Pin.OUT)
led = Signal(led_pin, invert=True)

# WiFi
SSID = config.SSID
password = config.PASSWORD

# io.adafruit.com 
user = config.USER
X_AIO_Key = config.X_AIO_KEY
feed = config.FEED

# IFTTT 
key = config.IFTTT_KEY
event = config.EVENT

# set NTP server
ntptime.host = config.NTP_SERVER

async def blink(led, period_ms):
    while True:
         led.on()
         await uasyncio.sleep_ms(5)
         led.off()
         print('...')
         await uasyncio.sleep_ms(period_ms)

def set_time():
   try:
         ntptime.settime()
   except OSError as e:
         print("Failed ntp request - Error: {0}".format(e))
   return time.mktime(time.localtime())        

def do_connect():
	wlan = network.WLAN(network.STA_IF) 
	wlan.active(True)
	if not wlan.isconnected():
		print('Connecting to Network...')
		wlan.connect(SSID, password)
		while not wlan.isconnected():
			pass
	print('Network Configuration (IP/GW/DNS1/DNS2): ', wlan.ifconfig())

def do_post(current_time):
   headers = {'X-AIO-Key': X_AIO_Key,'Content-Type': 'application/json'}
   url='https://io.adafruit.com/api/v2/'+user+'/feeds/'+feed+'/data.json'
   data = json.dumps({"value": current_time})
   # POST response
   response = requests.post(url, headers=headers, data=data)
   #if not response.ok:
   #   print ("Error Posting to Adafruit") # what should we do?
   response.close()

def ifttt_it(current_time):
   url= 'https://maker.ifttt.com/trigger/'+event+'/with/key/'+key
   headers = {'Content-Type': 'application/json'}
   data = json.dumps({"value1": current_time//60}) # in minutes not seconds
   # POST response
   response = requests.post(url, headers=headers, data=data)
   response.close()

async def main(led) :
   while True:
      # post and record current time
      print('....')
      current_time = time.mktime(time.localtime()) 
      f = open('clock', 'w')
      f.write(str(current_time))
      f.close()
      do_post(current_time)
      await time.sleep(config.INTERVAL)

# Timer for recalibrating NTP once a day
ntp_timer = Timer(0)
ntp_timer.init(period=1000*60*60*24, mode=Timer.PERIODIC, callback=set_time)

ap = network.WLAN(network.AP_IF) # let's make sure we don't boot as an Access Point
ap.active(False)

do_connect()

current_time = set_time()
 
try :
   f = open('clock', 'r')
   last_time = int(f.read())
   f.close()
except :
   f = open('clock', 'w')
   f.write(str(current_time))
   f.close()
   last_time = 0  # first time run

delta = current_time - last_time
print('Delta:', delta)
if delta > config.DELTA :
   print ('We have been down for while...')
   ifttt_it(delta)

# Running on a generic board
uasyncio.create_task(blink(led, 700))
uasyncio.run(main(led))

