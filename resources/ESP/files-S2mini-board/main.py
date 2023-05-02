print('flag1')
def connect_to_wifi():
	import network
	station_interface = network.WLAN(network.STA_IF)
	if not station_interface.isconnected():
		print('Connecting to GuestNet...')
		station_interface.active(True)
		station_interface.connect('GuestNet', '')
		while not station_interface.isconnected():
			pass
	print('Current network (GuestNet) config:', station_interface.ifconfig())	

connect_to_wifi()

# Quality-of-life improvements
import os

def readf(file_to_read):
	file_pointer = open(file_to_read)
	content = file_pointer.read()
	file_pointer = file_pointer.close()
	print(content)
