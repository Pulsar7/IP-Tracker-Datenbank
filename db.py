#
# By Pulsar
# Github: https://github.com/Woodnet 
# Website: https://quantaphysics.000webhostapp.com
# Python-Version: Python 3.8.2
#
import socket,os,sys,time
from threading import Thread
from cryptography.fernet import Fernet
import requests

def encryption(message):
    packet = f.encrypt(message.encode())
    return packet 

def error_message(e):
    print(" [#] Error: %s"%(e))

def decryption(packet):
    message = f.decrypt(packet)
    return (message.decode())

def fatal_error(e):
    print(" [!]")
    print(" [!] Critical Failure: %s"%(e))
    quit()

def fatal_error_with_cl(e,client):
    print(" [!]")
    print(" [!] Critical Failure: %s"%(e))
    client.close()
    del clients[client]
    print(" [INFO] Die Verbindung wird zu %s geschlossen!"%(client))
    quit()

def incoming_connections():
    while True:
        client,client_address = db.accept()
        print(" [INFO] Connection from %s"%(client))
        clients[client] = client_address
        Thread(target=ip_database, args=(client,)).start()

def get_ip_info(IP):
    url = "https://tools.keycdn.com/geo.json?host=%s"%(IP)
    r = requests.get(url)
    r_dict = r.json()
    country = r_dict['data']['geo']['country_name']
    state = r_dict['data']['geo']['region_name']
    city = r_dict['data']['geo']['city']
    host = r_dict['data']['geo']['host']
    ip = r_dict['data']['geo']['ip']
    ips = open("ips.db","a")
    ips.write("\n%s:%s:%s:%s:%s"%(ip,host,country,state,city))
    ips.close()

def ip_database(client):
        print(" [INFO] Started new Thread")
        print(" [INFO] Sending response to client..")
        packet = encryption("Now you can send me the IP-address!")
        try:
            client.send(packet)
        except Exception as e:
            error_message(e)
        print(" [INFO] Message length> %s"%(len(packet)))
        while True:
            print(" [INFO] Receiving an IP..")
            try:
                s_IP = decryption(client.recv(2048))
            except socket.error as e:
                fatal_error_with_cl(e,client)
            print(" [INFO] Received> %s" % (s_IP))
            print(" [INFO] Searching in Database..")
            print(" [INFO] Sending response to client..")
            try:
                client.send(encryption("Searching in Database.."))
            except Exception as e:
                error_message(e)
            try:
                ip_file = open(all_files[0],"r")
                IPs = ip_file.readlines()
                f = 0
                #print("S_IP: %s"%(s_IP))
                for ip in IPs:
                    #print("IP-DB: %s"%(ip.strip()))
                    if (s_IP in ip.strip()):
                        print(" [+] Found!")
                        print(" [INFO] Complete information about %s : %s"%(s_IP,ip.strip()))
                        message = ip.strip()
                        break 
                    else:
                        f += 1
                        if (f == len(IPs)):
                            print(" [#] Not in the Database available! Adding IP to Database..")
                            message = "Not in the Database! Adding IP-Informations to Database.."
                            get_ip_info(s_IP)
                        else:
                            pass
            except Exception as e:
                error_message(e)
            ip_file.close()
            print(" [INFO] Sending response to client..")
            try:
                client.send(encryption(message))
            except socket.error as e:
                fatal_error_with_cl(e,client)
            
            



generated = Fernet.generate_key()
f = Fernet(generated)
print(" [INFO] Generated Encryption-Key> %s"%(generated.decode()))
all_files = [
    "ips.db"
]

clients = {}
addresses = {}

if __name__ == '__main__':
    db = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP 
    db_addr = ("localhost",1337)
    sys.stdout.write("\r  [INFO] Binding Address..")
    sys.stdout.flush()
    try:
        db.bind(db_addr)
        print("+")
    except socket.error as e:
        fatal_error(e)
    print(" [INFO] Waiting for incoming connections")
    db.listen(10)
    accept_thread = Thread(target=incoming_connections)
    accept_thread.start()
    accept_thread.join()
    db.close()

    
