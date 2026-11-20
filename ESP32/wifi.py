import network                       
import time                          
                                     
                                     
def connect(ssid,password):          
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)                
    wlan.connect(ssid,password)      
                                     
    while not wlan.isconnected():    
        time.sleep(1)                
    return wlan.ifconfig()[0]        