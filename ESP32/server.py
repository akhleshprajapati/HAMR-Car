"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response
"""Handle UDP communication between the laptop and ESP32."""

import socket

# Create a UDP socket for communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def start(port):
    """Start the UDP server on the given port."""
    sock.bind(("0.0.0.0", port))
    sock.setblocking(False)


def receive():
    """Receive available messages from connected clients."""
    messages = []

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
        except OSError:
            break

        line = data.decode().strip()
        message = (client_address, line)
        messages.append(message)

    return messages


def reply(client_address, response_text):
    """Send a response back to the client."""
    data = (response_text + "\n").encode()
    sock.sendto(data, client_address)


def send(server_address, message):
    """Send a message and wait for a response from the server."""
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.settimeout(2)

    try:
        data = message.encode()
        client_sock.sendto(data, server_address)

        response_data, sender = client_sock.recvfrom(1024)
        response = response_data.decode().strip()

    except OSError:
        print("No response from", server_address[0], "port", server_address[1])
        response = None

    client_sock.close()
    return response