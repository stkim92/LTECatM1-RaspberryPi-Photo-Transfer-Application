import socket
from os.path import exists
import time,datetime
import os

HOST = '64:ff9b::de62:adcb'
# HOST = '222.98.163.203'

PORT = 7777

        
def getFileFromServer(filename):
    data_transferred = 0
    
    sock = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            sock = socket.socket(af, socktype, proto)
        except OSError as msg:
            sock = None
            continue
        try:
            sock.connect(sa)
        except OSError as msg:
            sock.close()
            sock = None
            continue
        break
    if sock is None:
        print('couldnt open socket')
        sys.exit(1)
    with sock:
        sock.sendall(filename.encode())
        filename_parsing = filename.split(',')
        filename = filename_parsing[0]
        if not exists(filename):
            print('file does not exist!')
            return
        print('[Start Sending]')
        cur_time = datetime.datetime.now()
        fUploadFile = open(filename,'rb')
        sRead = fUploadFile.read(4096)
        while sRead:
            data_transferred+= len(sRead)
            sock.send(sRead)
            sRead = fUploadFile.read(4096)
        
        cur_time1 = datetime.datetime.now()
    
    
    print('[File]: %s ,  [Size]: %d Bytes' %(filename, data_transferred))
    print('[send time] : ', str(cur_time))
    print('[send1 time] : ', str(cur_time1))
    print('[sending time] : ', str(cur_time1 - cur_time))
    print('[Complete]')
    


os.system("raspistill -o test.jpg -t 500 -q 5")

filename = input('Input File Name to Transfer:')
fileSize = os.path.getsize("test.jpg")
print("File size is : ", str(fileSize))
fileInfo = filename + ","+str(fileSize)
getFileFromServer(fileInfo)
