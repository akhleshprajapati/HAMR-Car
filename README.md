# HAMR Car

## About the Project

HAMR is a robotic car built using an ESP32-C6 microcontroller. The project combines electronics, programming, wireless communication, and robotics.

The robot can operate in three modes: autonomous mode, mobile phone control, and laptop control. It uses two ultrasonic sensors for obstacle detection and two DC motors for movement.

The main aim of this project is to understand how a robot can receive commands, control its movement, detect obstacles, and operate in different modes.

## Features

- Autonomous movement and obstacle avoidance
- Manual control using a mobile phone
- Control using a laptop
- Wireless communication
- Obstacle detection using two ultrasonic sensors
- Forward, backward, left, right, and stop movements

## Project Structure

HAMR Car/
│
├── README.md
│
├── Auto_manual/
│   ├── main.py
│   └── README.md
│
├── ESP32/
│   ├── main.py
│   ├── server.py
│   ├── wifi.py
│   └── README.md
│
└── Laptop/
    ├── server.py
    ├── user.py
    └── README.md

Each folder contains the code and documentation for a different part of the HAMR project.

## File Setup and Upload Guide

This section explains where each Python file should be saved, which files need to be uploaded to the ESP32-C6, and which files should run on the laptop.

### 1. Auto_manual Mode

Folder: `Auto_manual/`

| File | Where to Save | Where to Run |
|---|---|---|
| `main.py` | ESP32-C6 | ESP32-C6 |

Upload `main.py` from the `Auto_manual` folder to the ESP32 using Thonny.

### 2. ESP32 Wireless Control

Folder: `ESP32/`

| File | Where to Save | Where to Run |
|---|---|---|
| `main.py` | ESP32-C6 | ESP32-C6 |
| `server.py` | ESP32-C6 | ESP32-C6 |
| `wifi.py` | ESP32-C6 | ESP32-C6 |

Upload all three files from the `ESP32` folder to the ESP32-C6 using Thonny.

### 3. Laptop Control

Folder: `Laptop/`

| File | Where to Save | Where to Run |
|---|---|---|
| `user.py` | Laptop | Laptop |
| `server.py` | Laptop | Laptop |

Keep both files inside the `Laptop` folder on your computer. Connect your laptop to the ESP32 Wi-Fi network and run `user.py` using Python.

### Uploading Files to ESP32 Using Thonny

1. Connect the ESP32-C6 to your laptop using USB.
2. Open Thonny.
3. Select the MicroPython interpreter for ESP32.
4. Open the required Python file from the project folder.
5. Save or upload the file to the ESP32 device.
6. Make sure the required files are present on the ESP32.
7. Run `main.py` to start the selected mode.

### Running Laptop Control

1. Install Python 3 on your laptop.
2. Connect your laptop to the ESP32 Wi-Fi network.
3. Open the `Laptop` folder in the terminal.
4. Run the following command:

   ```bash
   python user.py

## Hardware Components

| Component | Quantity | Purpose |
|---|---:|---|
| ESP32-C6 | 1 | Main microcontroller |
| L298N Motor Driver | 1 | Controls the DC motors |
| DC Motors | 2 | Robot movement |
| HC-SR04 Ultrasonic Sensors | 2 | Obstacle detection |
| 12V Battery | 1 | Recommended motor power supply |
| Robot Chassis and Wheels | 1 set | Robot body and movement |
| Jumper Wires | As required | Electrical connections |

## Hardware Connections

### ESP32-C6 to L298N

| ESP32-C6 GPIO | L298N Pin |
|---|---|
| GPIO 15 | IN1 |
| GPIO 18 | IN2 |
| GPIO 19 | IN3 |
| GPIO 20 | IN4 |

### L298N to Motors

| L298N Output | Motor |
|---|---|
| OUT1 and OUT2 | Left motor |
| OUT3 and OUT4 | Right motor |

The ENA and ENB jumpers are connected on the L298N motor driver.

### Ultrasonic Sensor Connections

#### Left Ultrasonic Sensor

| Sensor Pin | ESP32-C6 |
|---|---|
| TRIG | GPIO 8 |
| ECHO | GPIO 9 |

#### Right Ultrasonic Sensor

| Sensor Pin | ESP32-C6 |
|---|---|
| TRIG | GPIO 6 |
| ECHO | GPIO 7 |

## Power Supply

The HAMR car can use a 5V power source or a 12V battery for the motor driver, depending on the power supply and motor requirements.

### Recommended: 12V Battery

- Connect the 12V battery positive (+) to the L298N motor supply input (Vs).
- Connect the battery negative (-) to the L298N GND.
- The 12V battery supplies power to the motors through the L298N motor driver.
- The ESP32-C6 is powered separately through USB.
- The ESP32-C6, L298N, and sensors must share a common ground.

### Alternative: 5V Power Supply

- A suitable 5V power source can be used for the L298N motor supply if the motors support 5V operation.
- Ensure the power source can provide sufficient current for both motors.
- The ESP32 USB power supply is not recommended for powering the motors because the motors can draw more current than the board's power supply can safely provide.

### Sensor Power and Safety

- Supply the ultrasonic sensors according to their voltage requirements.
- If HC-SR04 sensors are powered at 5V, their ECHO signals must be reduced to a safe voltage before connecting to ESP32 GPIO pins.
- Never connect the 12V battery directly to the ESP32 or ultrasonic sensors.

## How HAMR Works

HAMR has three operating modes.

### 1. Autonomous Mode

In autonomous mode, the robot moves without continuous human control.

The two ultrasonic sensors measure the distance to nearby obstacles. The ESP32 processes the sensor readings and controls the motors through the L298N motor driver.

When an obstacle is detected, the robot responds according to the programmed obstacle-avoidance logic.

### 2. Mobile Phone Control

In this mode, a mobile phone is used to control the robot wirelessly.

The ESP32 creates a Wi-Fi network, and the phone connects to it. Commands from the mobile control application are received by the ESP32 and translated into motor movements.

### 3. Laptop Control

In laptop mode, a laptop sends movement commands to the robot through wireless communication.

The laptop program sends commands, while the ESP32 receives them and controls the motors.

## Software Requirements

- MicroPython
- Thonny IDE
- ESP32-C6
- Python 3 (for laptop control)
- Wi-Fi capable mobile phone
- RoboLink mobile application (for phone control)
- USB cable

## Getting Started

### Step 1: Assemble the Robot

Connect the ESP32-C6, L298N motor driver, two DC motors, and two ultrasonic sensors according to the hardware connections listed above.

Check all power and ground connections before switching on the robot.

### Step 2: Install MicroPython

Install MicroPython firmware on the ESP32-C6 and connect the board to Thonny.

### Step 3: Select a Mode

Choose the required mode and open its corresponding folder:

- `Auto_manual/` – Autonomous and manual control
- `ESP32/` – ESP32 wireless control programs
- `Laptop/` – Laptop control programs

### Step 4: Upload and Run the Code

Upload the required files to the ESP32 or run the laptop program, depending on the selected mode.

Follow the instructions inside the README file of the selected folder.

### Step 5: Test the Robot

Test the robot in an open and safe area.

Start with basic movement, check the motors and sensors, and then test the selected operating mode.

## Common Problems and Solutions

| Problem | Possible Solution |
|---|---|
| Robot does not move | Check the motor power supply, battery, wiring, and L298N connections. |
| Only one motor works | Check motor wires and corresponding output terminals. |
| Robot moves in the wrong direction | Check motor polarity and movement logic. |
| Ultrasonic sensors give incorrect readings | Check TRIG and ECHO wiring, power, ground, and sensor placement. |
| Robot does not detect obstacles | Check sensor readings and obstacle detection logic. |
| ESP32 Wi-Fi is not visible | Restart the ESP32 and check the Wi-Fi setup code. |
| Phone connects but robot does not respond | Check the application commands and ESP32 communication code. |
| Laptop commands do not work | Check Wi-Fi connection, IP address, port, and laptop program. |
| ESP32 restarts during movement | Check the motor power supply and ground connections. Motors should not be powered directly from the ESP32. |

## Safety

- Test the robot on a flat surface.
- Keep fingers away from moving wheels.
- Check wiring before connecting the power supply.
- Avoid short circuits.
- Never connect 12V directly to the ESP32 or ultrasonic sensors.
- Do not connect 5V ECHO signals directly to ESP32 GPIO pins.
- Test autonomous mode in an open space away from stairs and people.

## Future Improvements

- Better obstacle-avoidance logic
- Improved turning and movement accuracy
- More reliable wireless communication
- Speed control using PWM
- Additional autonomous navigation features

## Project Credits

This project was developed as part of Group Project 3 (GP3) at Azim Premji University.

The project combines electronics, programming, robotics, and teamwork to build and test a functional robotic car.

---

**HAMR – Hardware, Automation, Movement and Robotics**