from machine import Pin,time_pulse_us
import time
import network
import socket

threshold=15
threshold2=5
current_mode=0
previous_mode=0

left1=Pin(15,Pin.OUT)
left2=Pin(18,Pin.OUT)
right1=Pin(19,Pin.OUT)
right2=Pin(20,Pin.OUT)

left_trig=Pin(8,Pin.OUT)
left_echo=Pin(9,Pin.IN)
right_trig=Pin(6,Pin.OUT)
right_echo=Pin(7,Pin.IN)

def move(a,b,c,d):
    left1.value(a)
    left2.value(b)
    right1.value(c)
    right2.value(d)

def distance(trig,echo):
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    duration=time_pulse_us(echo,1,30000)
    if duration<0:
        return -1
    return duration*0.0343/2

move(0,0,0,0)

wifi=network.WLAN(network.WLAN.IF_AP)
wifi.active(True)
wifi.config(ssid="HAMR")
time.sleep(2)

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",4210))
sock.setblocking(False)

while True:
    try:
        message=sock.recvfrom(200)[0].decode()
        if "mode:1" in message:
            if previous_mode==0:
                current_mode=1-current_mode
            previous_mode=1
        else:
            previous_mode=0

        if current_mode==0:
            if "nav_up:1" in message:
                move(1,0,1,0)
                
            elif "nav_down:1" in message:
                move(0,1,0,1)

            elif "nav_left:1" in message:
                move(0,0,1,0)

            elif "nav_right:1" in message:
                move(1,0,0,0)

            else:
                move(0,0,0,0)

        elif current_mode==1:
            left_distance=distance(left_trig,left_echo)
            time.sleep_ms(60)
            right_distance=distance(right_trig,right_echo)
            
            if left_distance<0 or right_distance<0:
                move(0,0,0,0)
                
            elif left_distance<threshold2 and right_distance<threshold2:
                move(0,1,0,1)
                time.sleep_ms(200)

            elif left_distance<threshold and right_distance<threshold:
                move(1,0,0,0)

            elif left_distance<threshold:
                move(0,0,1,0)

            elif right_distance<threshold:
                move(1,0,0,0)

            else:
                move(1,0,1,0)

    except OSError:
        pass

    time.sleep_ms(20)