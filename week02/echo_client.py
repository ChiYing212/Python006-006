#-*- coding: UTF-8 -*-
import socket,os,struct

HOST = 'localhost'
PORT = '10000'
FILE_PATH='./test.txt'

def echo_client():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    while True:
        
        if os.path.isfile(FILE_PATH):
            fileinfo_size=struct.calcsize('128sl') #定义打包规则
            #定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sl',os.path.basename(FILE_PATH),os.stat(FILE_PATH).st_size)
            s.send(fhead) 
            print 'client FILE_PATH: ',FILE_PATH
            fo = open(FILE_PATH,'rb')
            while True:
                filedata = fo.read(1024)
                if not filedata:
                    break
                s.send(filedata)
            fo.close()
        else:
            break
    print 'send over...'
    s.close()

if __name__ == "__main__":
    echo_client()

