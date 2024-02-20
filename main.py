from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin
import time

#Update routine
firmware_url = "https://raw.githubusercontent.com/thegreenlion42/BathVentRegulator/main/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

#Es lebt!

led_pin = 8  # Default on-board RGB LED GPIO08 does not work

led = Pin(led_pin, Pin.OUT)

for i in range(10):
  led.value(not led.value())
  time.sleep_ms(500)
  print("Blink ", i+1)
