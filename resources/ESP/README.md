# ESP microcontroller and related resources

## ESP32 board specs
ESP32 overview [link](https://docs.micropython.org/en/latest/esp32/quickref.html)

We're specifically using ESP32-S2 Mini: ESP32-S2FN4R2
- The ESP board is running [Tasmota open source firmware](https://tasmota.github.io/docs/) (?).
- See the schematic in the pdf in this folder.
- S2 mini board features & [pins](https://www.wemos.cc/en/latest/s2/s2_mini.html)
- S2 mini on [AliExpress](https://www.aliexpress.us/item/3256802958877264.html)


## ESP32 board usage
For more information, see my local cheat sheet (which I will upload here regularly).

### Understanding WIFI
- Difference between station interface and access-point interface [Link](https://www.phind.com/search?cache=b09bc23a-eb5d-42ac-a63f-3a9eb64b3376)

### Micropython general usage
- See ReadTheDocs for micropython. [Link here](http://docs.micropython.org/en/latest/esp32/quickref.html)
- [Learn to get started with MicroPython on S2](https://www.wemos.cc/en/latest/tutorials/s2/get_started_with_micropython_s2.html)

Refer to Gtown doorbell [script](https://github.com/GeorgetownMakerHubOrg/iot_doorbell/blob/master/doorbell.py) for how to update to dashboard.

### Adafruit Dashboard API
[Feed practice](https://io.adafruit.com/oinoinoin/feeds/luminance)

[Adafruit IO](https://io.adafruit.com/api/docs/?python#create-multiple-data-records)

[Example feed](https://io.adafruit.com/maiden/public)

## MQTT (Mosquitto) protocol
[Official website](https://mqtt.org/)

MQTT explorer (application) is useful

### Tasmota MQTT
Plug in the sonoff3 switch, then go to http://10.120.9.245/

## ESP Over-The-Air (OTA) updates
- Via [GitHub releases](https://github.com/rdehuyss/micropython-ota-updater)
	- A [Medium article on this](https://medium.com/@ronald.dehuysser/micropython-ota-updates-and-github-a-match-made-in-heaven-45fde670d4eb)
