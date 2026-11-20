"""Send movement commands to HAMR from the laptop."""

import server

# ESP32 IP address and UDP port
server_address = ("10.186.9.75", 5000)

# Continuously accept commands from the user
while True:
    command = input("Enter command: ").lower()

    # Stop the robot and close the controller
    if command == "exit":
        server.send(server_address, "stop")
        print("Controller closed")
        break

    # Send the command and display the response
    response = server.send(server_address, command)
    print(response)