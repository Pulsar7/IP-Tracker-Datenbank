#
# By Pulsar
# Github: https://github.com/Woodnet 
# Website: https://quantaphysics.000webhostapp.com
# Python-Version: Python 3.8.2
# C L I E N T
#
import os,socket 
from cryptography.fernet import Fernet 

os.system("cls")

key = input("Key> ")
f = Fernet(key.encode())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect(("localhost",1337))
packet = s.recv(2048)
message = f.decrypt(packet)
print("[SERVER] %s"%(message.decode()))
while True:
    ip = input("IP> ")
    packet = f.encrypt(ip.encode())
    s.send(packet)
    print("Gesendet")
    packet = s.recv(2048)
    message = f.decrypt(packet)
    print("[SERVER] %s"%(message.decode()))
    packet = s.recv(2048)
    complete_info = f.decrypt(packet)
    try:
        complete_info.decode().find(':')
        #print(complete_info.decode())
        informations = complete_info.decode().split(':')
        ip = informations[0]
        hostname = informations[1]
        country = informations[2]
        state = informations[3]
        city = informations[4]
        found = True
    except:
        found = False
    
    if (found == True):
        print("\n [IP] %s"%(informations[0]))
        print(" [Hostname] %s"%(informations[1]))
        print(" [Country] %s"%(informations[2]))
        print(" [State] %s"%(informations[3]))
        print(" [City] %s \n"%(informations[4]))
    else:
        print(" [SERVER] %s"%(complete_info.decode()))
    
