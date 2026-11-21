# Laptop Control

## About

This folder contains the Python programs used to control the HAMR car using a laptop.

The laptop communicates wirelessly with the ESP32-C6 and sends movement commands. The ESP32 processes these commands and controls the motors through the L298N motor driver.

## Files

| File | Description |
|---|---|
| `server.py` | Handles communication for laptop control. |
| `user.py` | Sends user movement commands to the robot. |

## Hardware Used

- ESP32-C6
- L298N motor driver
- 2 DC motors
- 2 HC-SR04 ultrasonic sensors
- Power supply (recommended 12V battery)
- Laptop
- Wi-Fi connection

## Pin Connections

### Motor Driver

| ESP32 GPIO | L298N Pin |
|---|---|
| GPIO 15 | IN1 |
| GPIO 18 | IN2 |
| GPIO 19 | IN3 |
| GPIO 20 | IN4 |

### Ultrasonic Sensors

| Sensor | TRIG | ECHO |
|---|---|---|
| Left | GPIO 8 | GPIO 9 |
| Right | GPIO 6 | GPIO 7 |

## How It Works

1. The ESP32-C6 starts its Wi-Fi network.
2. The laptop connects to the ESP32 network.
3. The laptop program sends movement commands.
4. The ESP32 receives the commands.
5. The ESP32 controls the motors through the L298N motor driver.

## Software Requirements

- Python 3
- Laptop
- ESP32-C6 running MicroPython
- Wi-Fi connection

## How to Run

1. Power on the ESP32-C6.
2. Connect the laptop to the Wi-Fi network created by the ESP32.
3. Open this folder on the laptop.
4. Make sure Python 3 is installed.
5. Open a terminal inside the `Laptop` folder.
6. Run the laptop control program:

   ```bash
   python user.py