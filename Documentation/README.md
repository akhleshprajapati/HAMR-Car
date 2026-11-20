# HAMR Car 🤖

HAMR is a robot car that I built and programmed and it is a group project 3 of my information science course. It started with autonomous and manual control, and later I added another way to control it remotely using a laptop.

The robot can move on its own, be controlled using a phone, or receive movement commands from a laptop.

## Features

### Autonomous Mode
In autonomous mode, the robot moves on its own. It uses ultrasonic sensors to detect obstacles and changes its direction to avoid hitting them.

### Manual Mode
I can control the robot using my phone through the RoboLink app. I can move it forward, backward, left, right, or stop.

### Laptop Remote Control
The robot can also be controlled using a laptop. A Python program sends movement commands to the ESP32 over Wi-Fi using UDP communication. The ESP32 receives the commands, controls the motors, and sends a response back.

## Components Used

- ESP32-C6
- Breadboard
- L298N motor driver
- DC motors
- HC-SR04 ultrasonic sensors
- Robot chassis and wheels
- Power supply
- Jumper wires

## Tools and Technologies

- Python
- MicroPython
- Wi-Fi
- UDP
- Kali Linux
- Thonny
- RoboLink

## Project Structure

HAMR Car/
├── Auto_manual/
│   └── main.py
│
└── HAMR_Remote/
    ├── ESP32/
    │   ├── main.py
    │   ├── server.py
    │   └── wifi.py
    │
    └── Laptop/
        ├── server.py
        └── client.py

## How to Use

### Autonomous and Manual Modes

1. Turn on the robot.
2. Connect your phone to the robot's Wi-Fi network (HAMR).
3. Open the RoboLink app.
4. Connect to the robot through the app an drive like game.
5. Use the mode selection to switch between Autonomous and Manual modes.

**Autonomous Mode:** The robot moves on its own, detects obstacles using ultrasonic sensors, and changes its direction to avoid them.

**Manual Mode:** Use the controls in RoboLink to move the robot forward, backward, left, right, or stop.

### Laptop Remote Control

1. Connect the ESP32 and laptop to the same Wi-Fi network.
2. Open the `HAMR_Remote/ESP32` folder in Thonny.
3. Enter the Wi-Fi name and password in `main.py`.
4. Run `main.py` on the ESP32.
5. Note the ESP32 IP address displayed in the Thonny Shell.
6. Open `HAMR_Remote/Laptop/client.py`.
7. Enter the ESP32 IP address in the client file.
8. Open a terminal inside the Laptop folder and run:

```bash
python3 client.py