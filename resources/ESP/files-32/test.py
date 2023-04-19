from machine import Pin, Signal
import uasyncio
led_pin = Pin(15, Pin.OUT)
led = Signal(led_pin, invert=False)

async def blink(led, period_ms):
    while True:
        led.on()
        await uasyncio.sleep_ms(5)
        led.off()
        await uasyncio.sleep_ms(period_ms)

async def main(led1):
    uasyncio.create_task(blink(led1, 700))
    await uasyncio.sleep_ms(10_000)

# Running on a generic board
uasyncio.run(main(led))
