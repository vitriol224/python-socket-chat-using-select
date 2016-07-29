#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("")
''' our client program also using select....

'''

from socket import *
from select import *
import sys
import random 
##define the prompt box for typing....
##we use standard outout so that 
## we can get what the person typed from 
## the keyboard @ the server side.. 

def type_message():
     sys.stdout.write("\nTYPE>> ")
     sys.stdout.flush()



## begin the client here.....
## code block by vitriol.....
##host = input("HOST IP: ")
##port = int(input ("PORT: "))
##port= random.randint(5555,65535)
#host=gethostname()
host="172.16.0.1"
port = 5555
prop=(host,port)
sock= socket(AF_INET,SOCK_STREAM)
##sock.settimeout(6)

try:
     sock.connect(prop)
except:
     print("unable to establish connection")
     sys.exit()
print(" you have connected successfully ")
type_message()

## start your while loop here....
## we don't want it to ever end.....
while 3:
    all_sockets=[sys.stdin,sock]
    readable,writable,error_s=select(all_sockets,[],[])
    for each_sock in readable:
         if each_sock==sock:
             data=each_sock.recv(2048)
             if not data:
                 print("\ndisconnected...")
                 sys.exit() 
                 
             else:
                 sys.stdout.write(data.decode('utf-8'))
                 type_message()
         else:
              message = sys.stdin.readline()
              sock.send(message.rstrip('\n').encode())
              type_message()


