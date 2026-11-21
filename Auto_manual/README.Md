# Auto_manual

## About

This folder contains the code for the HAMR car's autonomous and manual operating modes.

The robot can move automatically using ultrasonic sensors to detect obstacles. It can also be controlled manually using programmed movement commands.

## Features

- Autonomous movement
- Obstacle detection using two ultrasonic sensors
- Manual movement control
- Forward and backward movement
- Left and right turning
- Stop control

## Hardware Used

- ESP32-C6
- L298N motor driver
- 2 DC motors
- 2 HC-SR04 ultrasonic sensors
- Power supply (recommended 12V battery)
- Jumper wires

## Pin Connections

### Motor Driver

| ESP32 GPIO | L298N |
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

### Autonomous Mode

The ultrasonic sensors measure the distance between the robot and nearby obstacles.

The ESP32 processes the sensor readings and controls the motors through the L298N motor driver. When an obstacle is detected, the robot follows its programmed logic to avoid it.

### Manual Mode

In manual mode, movement commands are used to control the robot's direction.

The robot can move forward, backward, turn left, turn right, or stop.

## Software Requirements

- MicroPython
- Thonny IDE
- ESP32-C6

## How to Run

1. Connect the ESP32-C6 to your laptop using a USB cable.
2. Open Thonny and select the ESP32-C6 interpreter.
3. Open `main.py` from this folder.
4. Upload the code to the ESP32.
5. Run the program.
6. Test the robot in a safe, open area.

## Common Problems and Solutions

| Problem | Solution |
|---|---|
| Robot does not move | Check motor power and L298N wiring. |
| Motor moves in the wrong direction | Check motor wiring and movement logic. |
| Obstacle is not detected | Check ultrasonic sensor connections and distance readings. |
| Sensor readings are incorrect | Check TRIG, ECHO, power, and common ground. |
| Robot behaves unexpectedly | Stop the robot and check the code and connections. |

## Safety

- Test on a flat surface.
- Keep hands away from moving wheels.
- Check connections before powering on.
- Never connect 12V directly to ESP32 GPIO pins.

## Project

This folder is part of the HAMR robotic car project developed for Group Project 3 (GP3) at Azim Premji University.