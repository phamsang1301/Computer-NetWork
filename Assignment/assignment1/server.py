from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
import time


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
                1024).decode()
            print(message)
            clientUdpPort = message.split()[5]
            connectionSocket.send(
                'SUCCESS\nID 1\nINTERVAL 5\nTCP_PORT 4000'.encode())
            while True:
                info = connectionSocket.recv(
                    1024).decode()
                print(info)

        except:
            connectionSocket.close()


def udpConnection():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    control = 'TCP_PORT 4000\nINTERVAL 1\n'
    udpSocket.sendto(control.encode(), ('localhost', 4001))


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