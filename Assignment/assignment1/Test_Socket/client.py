import psutil
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import datetime
import time
from threading import Thread
import pickle
#Get computer's infomation 
# w = wmi.WMI(namespace="root\OpenHardwareMonitor")
# temperature_infos = w.Sensor()
# for sensor in temperature_infos:
#     if sensor.SensorType == u'Temperature':
#         print(sensor.Name)
#         print(sensor.Value)
temperature_infos = psutil.sensors_temperatures();

# for sensor in temperature_infos:
#     print(sensor)

print(temperature_infos['dell_smm'][0])
print("-----------------")
print(psutil.virtual_memory())
mem_total = psutil.virtual_memory().total / pow(2, 30)
mem_used = psutil.virtual_memory().used / pow(2, 30)
mem_avail = psutil.virtual_memory().available / pow(2, 30)
mem_percent = psutil.virtual_memory().percent / pow(2, 30) 

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
total = (cDisk.total + dDisk.total) / pow(2, 30)
used = (cDisk.used + dDisk.used) / pow(2, 30)
available = (cDisk.free + dDisk.free) / pow(2, 30)
used_percent = (used / total) * 100

infos = {'CPU': temperature_infos, 'DISK': {'Total': total, 'USED': used,'Avaiable': available, 'USED_PERCENT': used_percent },'MEMORY':{'Total': mem_total, 'USED': mem_used,'Avaiable': mem_avail, 'USED_PERCENT': mem_percent } }

send_infos = pickle.dumps(infos)
####################################


serverName = 'localhost'
serverPort = 4000
interval = 0


def tcpConnection():
    global serverName, serverPort, interval
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    
    time1 =  str(datetime.datetime.now())
    msg = {'IP': "127.0.0.1", 'NAME': "Sang", 'UDP_PORT': 4001, 'TIME':time1  }

    message = pickle.dumps(msg)
    clientSocket.send(message)
    
    m2 = clientSocket.recv(1024)
    msg_recive_from_server =  pickle.loads(m2)

    interval = msg_recive_from_server['INTERVAL']
    serverPort = msg_recive_from_server['TCP_PORT']

    while True:

        # info = 'Total = ' + str(psutil.virtual_memory().total / pow(2, 30))
        clientSocket.send(send_infos)
        print("Sleep...")
        print('Interval: ' + str(interval))
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

# newThread2 = Thread(target=udpConnection, args=())
# newThread2.start()
# threads.append(newThread2)
