import server                                   
                                                
                                                
server_address=("10.186.9.75", 5000)            
                                                
                                                
while True:                                     
    command=input("Enter command: ").lower()    
    if command=="exit":                         
        server.send(server_address,"stop")      
        print("Controller closed")              
        break                                   
    response=server.send(server_address,command)
    print(response)                             