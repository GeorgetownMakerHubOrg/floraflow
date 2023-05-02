# ESP microcontroller and related resources

## ESP32 board specs
ESP32 overview [link](https://docs.micropython.org/en/latest/esp32/quickref.html)

We're specifically using ESP32-S2 Mini: ESP32-S2FN4R2
- The ESP board is running [Tasmota open source firmware](https://tasmota.github.io/docs/) (?).
- See the schematic in the pdf in this folder.
- S2 mini board features & [pins](https://www.wemos.cc/en/latest/s2/s2_mini.html)
- S2 mini on [AliExpress](https://www.aliexpress.us/item/3256802958877264.html)


## ESP32 board usage
For more information, see my local cheat sheet (which I will upload here regularly).  Hoping that 

### Understanding WIFI
- Difference between station interface and access-point interface [Link](https://www.phind.com/search?cache=b09bc23a-eb5d-42ac-a63f-3a9eb64b3376)

### Micropython general usage
- See ReadTheDocs for micropython. [Link here](http://docs.micropython.org/en/latest/esp32/quickref.html)
- See Micropython GitHub issues for help when [resolving bugs](https://github.com/micropython/micropython/issues)
- [Learn to get started with MicroPython on S2](https://www.wemos.cc/en/latest/tutorials/s2/get_started_with_micropython_s2.html)

Refer to Gtown doorbell [script](https://github.com/GeorgetownMakerHubOrg/iot_doorbell/blob/master/doorbell.py) for how to update to dashboard as well as how to HTTP POST to a site (including the Sonoff/Tasmota pump switch).

### Adafruit Dashboard API
[Feed practice](https://io.adafruit.com/oinoinoin/feeds/luminance)

[Adafruit IO](https://io.adafruit.com/api/docs/?python#create-multiple-data-records)

[Example feed](https://io.adafruit.com/maiden/public)


## MQTT (Mosquitto) protocol or HTTP Requests
Managing the Sonoff S31 switch can done from the ESP32 MCU using either MQTT - [Official website](https://mqtt.org/) or vanilla HTTP requests (see MicroPython urequests for details).   HTTP access is configured under the "Configuration->Other" on the Sonoff/Tasmota switch.

MQTT explorer, available on MacOS, Linux, and M$FT) is useful for debugging MQTT publish/subscribe issues.

### Tasmota MQTT
Plug in the sonoff3 switch, then go to http://10.120.9.245/

## ESP Over-The-Air (OTA) updates
- Via [GitHub releases](https://github.com/rdehuyss/micropython-ota-updater)
	- A [Medium article on this](https://medium.com/@ronald.dehuysser/micropython-ota-updates-and-github-a-match-made-in-heaven-45fde670d4eb)

# ESP32 Web server tutorials
- [ESP32 web server tutorial](http://www.energiazero.org/arduino/esp32/electronicshub.org-a%20complete%20beginners%20tutorial%20on%20how%20to%20create%20esp32%20web%20server.pdf)
