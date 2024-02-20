from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
#Es lebt!
firmware_url = "https://github.com/thegreenlion42/BathVentRegulator/new/main/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()
