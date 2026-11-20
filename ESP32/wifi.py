"""Connect the ESP32 to a Wi-Fi network."""

import network
import time


def connect(ssid, password):
    """Connect to Wi-Fi and return the ESP32's IP address."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait until the Wi-Fi connection is established
    while not wlan.isconnected():
        time.sleep(1)

    return wlan.ifconfig()[0] 