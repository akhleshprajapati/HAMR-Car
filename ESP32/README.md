# ESP32

## About

This folder contains the ESP32-C6 programs used for wireless communication and robot control.

The ESP32 acts as the main controller. It creates a Wi-Fi network, receives commands from connected devices, and controls the motors through the L298N motor driver.

## Files

| File | Description |
|---|---|
| `main.py` | Main program that handles robot control. |
| `server.py` | Handles incoming commands and communication. |
| `wifi.py` | Configures and manages the ESP32 Wi-Fi connection. |

## Hardware Used

- ESP32-C6
- L298N motor driver
- 2 DC motors
- 2 HC-SR04 ultrasonic sensors
- Power supply (recommended 12V battery)
- Jumper wires

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

1. The ESP32-C6 starts and configures its Wi-Fi network.
2. A mobile phone or laptop connects to the ESP32 network.
3. The connected device sends movement commands.
4. The ESP32 receives and processes the commands.
5. The motor driver controls the DC motors according to the commands.

## Software Requirements

- MicroPython
- Thonny IDE
- ESP32-C6
- Wi-Fi capable device

## How to Run

1. Connect the ESP32-C6 to your laptop using USB.
2. Open Thonny and select the ESP32-C6 interpreter.
3. Upload `wifi.py`, `server.py`, and `main.py` to the ESP32.
4. Make sure the required files are present on the board.
5. Run `main.py`.
6. Connect your phone or laptop to the Wi-Fi network created by the ESP32.
7. Send movement commands and test the robot.

## Common Problems and Solutions

| Problem | Solution |
|---|---|
| Wi-Fi network is not visible | Restart the ESP32 and check the Wi-Fi setup in `wifi.py`. |
| Device connects but commands do not work | Check the server program and command format. |
| Robot does not move | Check motor driver wiring, power, and movement code. |
| ESP32 restarts | Check the power supply and wiring for short circuits. |
| Communication stops | Reconnect to the ESP32 Wi-Fi and restart the program. |

## Safety

- Check all wiring before powering the robot.
- Do not connect the 12V battery directly to ESP32 GPIO pins.
- Keep the robot on a safe, flat surface during testing.
- Keep hands away from moving motors and wheels.

## Project

This folder is part of the HAMR robotic car project developed for Group Project 3 (GP3) at Azim Premji University.