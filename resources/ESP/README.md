# ESP microcontroller and related resources

## ESP32 board specs
ESP32 overview [link](https://docs.micropython.org/en/latest/esp32/quickref.html)

The ESP board is running [Tasmota open source firmware](https://tasmota.github.io/docs/) (?).

See the schematic in the pdf in this folder.

S2 mini board features & [pins](https://www.wemos.cc/en/latest/s2/s2_mini.html)

S2 mini on [AliExpress](https://www.aliexpress.us/item/3256802958877264.html)

## ESP32 board usage
For more information, see my local cheat sheet (which I will upload here regularly).  Hoping that 

### Micropython general usage
See ReadTheDocs for micropython. [Link here](http://docs.micropython.org/en/latest/esp32/quickref.html)

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
