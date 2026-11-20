import time                                      
import server                                    
import wifi                                      
from machine import Pin                          
                                                 
                                                 
left1=Pin(15,Pin.OUT)                            
left2=Pin(18,Pin.OUT)                            
right1=Pin(19,Pin.OUT)                           
right2=Pin(20,Pin.OUT)                           
                                                 
                                                 
def move(a,b,c,d):                               
    left1.value(a)                               
    left2.value(b)                               
    right1.value(c)                              
    right2.value(d)                              
                                                 
                                                 
def handle(command):                             
    if command=="forward":                       
        move(1,0,1,0)                            
        return "Moving forward"                  
                                                 
                                                 
    elif command=="backward":                    
        move(0,1,0,1)                            
        return "Moving backward"                 
                                                 
                                                 
    elif command=="left":                        
        move(0,0,1,0)                            
        return "Turning left"                    
                                                 
                                                 
    elif command=="right":                       
        move(1,0,0,0)                            
        return "Turning right"                   
                                                 
                                                 
    elif command=="stop":                        
        move(0,0,0,0)                            
        return "Stopped"                         
                                                 
                                                 
    elif command=="status":                      
        return "HAMR is ready"                   
                                                 
                                                 
    return "Unknown command"                     
                                                 
                                                 
move(0,0,0,0)                                    
                                                 
                                                 
ip=wifi.connect("Motorola","22222222")           
print("ESP32 IP:",ip)                            
                                                 
                                                 
if ip:                                           
    server.start(5000)                           
    print("Server started")                      
                                                 
                                                 
    while True:                                  
        messages=server.receive()                
        for client_address,command in messages:  
            response=handle(command)             
            server.reply(client_address,response)
                                                 
        time.sleep_ms(10)                        