from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
import time
import pickle


def tcpConnection():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 4000
    serverSocket.bind(('', serverPort))
    serverSocket.listen(40)

    while True:
        print('Ready to server...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(
                1024)
            msg = pickle.loads(message)
            
            print("Name: " +msg['NAME'])
            print("IP: " +msg['IP'])
            print("UDP PORT: " +str(msg['UDP_PORT']))
            print("Time: " +str(msg['TIME']))

            
            message_to_client = {'STATUS': "Success",'ID': 0,'INTERVAL': 5, 'TCP_PORT': 4000 }
            msg_to_client = pickle.dumps(message_to_client)
            connectionSocket.send(msg_to_client)

            while True:
                info = connectionSocket.recv(1024)
                inf = pickle.loads(info)
                print(inf)
        except:
            connectionSocket.close()


def udpConnection():
    serverPort = 4000
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    socket.bind(('', serverPort))
    socket.listen(40)
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    # control = 'TCP_PORT 4000\nINTERVAL 1\n'
    # udpSocket.sendto(control.encode(), ('localhost', 4001))
def udpChangeParameter(interval, tcp_port):
    udpConnection()
    connectionSocket, addr = socket.accept()
    message_to_client = {'STATUS': "Success",'ID': 0,'INTERVAL': 5, 'TCP_PORT': 4000 }
    msg_to_client = pickle.dumps(message_to_client)
    connectionSocket.send(msg_to_client)
    


threads = []

newThread = Thread(target=tcpConnection, args=())
newThread.start()
threads.append(newThread)

for i in range(5):
    print(i)
    time.sleep(3)
udpSocket = socket(AF_INET, SOCK_DGRAM)
control = 'TCP_PORT 4000\nINTERVAL 1\n'
udpSocket.sendto(control.encode(), ('localhost', 4001))
print('send udp success 1')

time.sleep(15)

control = 'TCP_PORT 4000\nINTERVAL 5\n'
udpSocket.sendto(control.encode(), ('localhost', 4001))
print('send udp success 2')