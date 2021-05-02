import wmi
import psutil
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import datetime
import time
from threading import Thread

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType == u'Temperature':
        print(sensor.Name)
        print(sensor.Value)
print("-----------------")
print(psutil.virtual_memory())
print('Total = ' + str(psutil.virtual_memory().total / pow(2, 30)))
print('Used = ' + str(psutil.virtual_memory().used / pow(2, 30)))
print('Available = ' + str(psutil.virtual_memory().available / pow(2, 30)))
print('Used Percent = ' + str(psutil.virtual_memory().percent))
print("-----------------")
cDisk = psutil.disk_usage('/dev/sda1')
dDisk = psutil.disk_usage('/dev/sda3')
print(cDisk)
print(dDisk)
print('Total = ' + str((cDisk.total + dDisk.total) / pow(2, 30)))
print('Used = ' + str((cDisk.used + dDisk.used) / pow(2, 30)))
print('Available = ' + str((cDisk.free + dDisk.free) / pow(2, 30)))
print('Used Percent = ' + str((cDisk.used + dDisk.used) /
                              (cDisk.total + dDisk.total) * 100))

#####################################

serverName = 'localhost'
serverPort = 4000
interval = 0


def tcpConnection():
    global serverName, serverPort, interval
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    message = "NAME tinh\nIP 127.0.0.1\nUDP_PORT 4001\nTIME " + \
        str(datetime.datetime.now()) + "\n"
    clientSocket.send(message.encode())
    m2 = clientSocket.recv(1024).decode()
    interval = int(m2.split()[4])
    serverPort = int(m2.split()[6])

    while True:

        info = 'Total = ' + str(psutil.virtual_memory().total / pow(2, 30))
        clientSocket.send(info.encode())
        print("Sleep...")
        print('interval in tcp = ' + str(interval))
        time.sleep(interval)

    # clientSocket.close()


def udpConnection():
    global interval
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 4001))
    while True:
        control, serverAddr = udpSocket.recvfrom(1024)
        print('receive udp success')
        control = control.decode()
        serverPort = int(control.split()[1])
        interval = int(control.split()[3])
        print('receive udp success 2')
        print('interval in udp = ' + str(interval))


threads = []

newThread = Thread(target=tcpConnection, args=())
newThread.start()
threads.append(newThread)

newThread2 = Thread(target=udpConnection, args=())
newThread2.start()
threads.append(newThread2)
