# -*- coding: utf-8 -*-
# import subprocess

# for ping in range(1,10):
#    address = "192.168.1." + str(ping)
#    res = subprocess.call(['ping', '-c', '1', address])
#    if res == 0:
#        print( "ping to", address, "OK")
#    elif res == 2:
#        print("no response from", address)
#    else:
#        print("ping to", address, "failed!")

data = []

import socket
# print(socket.gethostbyaddr("8.8.8.8"))
# 95.85.72.0	95.85.72.255
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for AAA in range(95,255+1):
    for BBB in range(85,255+1):
        for CCC in range(72,255+1):
            for DDD in range(1,255+1):
                IPaddr = str(AAA)+"."+str(BBB)+"."+str(CCC)+"."+str(DDD)
                try:
                    print(IPaddr)
                    # s.connect((IPaddr, 80))
                    current = socket.gethostbyaddr(IPaddr)
                    print(current)
                    data.append(current)
                    
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst.args)     # arguments stored in .args
                    print(inst)


