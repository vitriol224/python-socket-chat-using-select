#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("")
from socket import *
from select import *

	
'''this is an echo chat system using the select module 
the module will help broadcast messages across all
connected clients.....'''


##create a function to send message....

def send_across(sock,client,message):
   ##to make sure we don't send the message to the 
   ##master and the client who sent it....'''
   
   for each_socket in all_sockets:
       if each_socket != sock and each_socket != client:
          try:
              message= "\n"+message
              each_socket.send(message.encode())
          except:
              ##socket connection lost....
              each_socket.close()
              if each_socket in all_sockets:
                   all_sockets.remove(each_sock)




##host = input("HOST IP: ")
##port = int(input ("PORT: "))
#host=gethostname()
host="172.16.0.1"
port=5555
all_sockets=[] 
properties =(host,port)
sock=socket(AF_INET,SOCK_STREAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

print("server started on {0}:{1}".format(host,port))

sock.bind(properties)
sock.listen(10)

print("now listening.....")

all_sockets.append(sock)

###create a continuous while loop

while True:

    ##get the list of all sockets that can be read from...
    
    readable_sock,writable_sock,error_sock=select(all_sockets,[],[],0)

    for all_socks in readable_sock:
    ## a new connection is pending....

         if all_socks==sock:

            ##accept the connection...

            sockdd,addr = sock.accept()
            all_sockets.append(sockdd)

            ## the use name from above.... 

            print(addr," joined room")
            to_send=str("{} joined chat room".format(addr))
            send_across(sock,sockdd,to_send)
         else:
             ##if not a new connection,text had been sent...
             ##send it across...
             try:
                data=all_socks.recv(2048)
                if data:
                
                     send_across(sock,all_socks,str("{}:{}".format(addr,data)))
                else:
                     if all_socks in all_sockets:
                         all_sockets.remove(all_socks)
                     to_send2= str("{} is offline".format(addr))
                     send_across(sock,all_socks,to_send2)
                     print(addr," is offline")
        
             except:
                
                ## a broken connection 
                   to_send3= str("{} is offline".format(addr))
                   send_across(sock,all_socks,to_send3)
          
                   print(addr,"is offline\n")
          
                   continue
           
sock.close()
      
 
 
      
##### code ended..... by vitriol.....
