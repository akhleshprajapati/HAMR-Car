"""Control HAMR remotely from a laptop using Wi-Fi and UDP."""

import time
import server
import wifi
from machine import Pin

# Motor control pins
left1 = Pin(15, Pin.OUT)
left2 = Pin(18, Pin.OUT)
right1 = Pin(19, Pin.OUT)
right2 = Pin(20, Pin.OUT)


def move(a, b, c, d):
    """Control the motors to move or turn the robot."""
    left1.value(a)
    left2.value(b)
    right1.value(c)
    right2.value(d)


def handle(command):
    """Receive a command and perform the corresponding movement."""

    if command == "forward":
        move(1, 0, 1, 0)
        return "Moving forward"

    elif command == "backward":
        move(0, 1, 0, 1)
        return "Moving backward"

    elif command == "left":
        move(0, 0, 1, 0)
        return "Turning left"

    elif command == "right":
        move(1, 0, 0, 0)
        return "Turning right"

    elif command == "stop":
        move(0, 0, 0, 0)
        return "Stopped"

    elif command == "status":
        return "HAMR is ready"

    return "Unknown command"


# Stop the motors when the program starts
move(0, 0, 0, 0)

# Connect the ESP32 to Wi-Fi
ip = wifi.connect("Motorola", "22222222")
print("ESP32 IP:", ip)

# Start the UDP server if Wi-Fi is connected
if ip:
    server.start(5000)
    print("Server started")

    # Receive commands and send responses
    while True:
        messages = server.receive()

        for client_address, command in messages:
            response = handle(command)
            server.reply(client_address, response)

        time.sleep_ms(10)