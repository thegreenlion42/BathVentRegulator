from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin, SoftI2C
from bmp280 import *
import time
import ahtx0

#Update routine
def UpdateRoutine():
    firmware_url = "https://raw.githubusercontent.com/thegreenlion42/BathVentRegulator/main/"
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

    ota_updater.download_and_install_update_if_available()

#Sensor setup
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
bmp = BMP280(i2c)

sensor = ahtx0.AHT20(i2c)

bmp.use_case(BMP280_CASE_INDOOR)
bmp.oversample(BMP280_OS_HIGH)

bmp.temp_os = BMP280_TEMP_OS_8
bmp.press_os = BMP280_PRES_OS_4

#bmp.standby = BMP280_STANDBY_250
#bmp.iir = BMP280_IIR_FILTER_2

#bmp.spi3w = BMP280_SPI3W_ON
count = 0
while True:
    print(count)
    
    if count == 0:
        UpdateRoutine()
    elif count >= 10:
        UpdateRoutine()
    count += 1
                
    bmp.force_measure()

    #print(bmp.temperature)
    print(bmp.pressure)
    print("x2:", bmp.temperature, "y2:", bmp.pressure)
    print("x:", sensor.temperature, "y:", sensor.relative_humidity)
    time.sleep(1)
