from machine import Pin
import time

#Es lebt!

led_pin = 8  # Default on-board RGB LED GPIO08 does not work

led = Pin(led_pin, Pin.OUT)

for i in range(10):
  led.value(not led.value())
  time.sleep_ms(500)
  print("Blink ", i+1)
