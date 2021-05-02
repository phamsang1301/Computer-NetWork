import socket
import threading
import time
from tkinter import *
 
 
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT = 'END'
TIME = time.strftime('%H:%M:%S')
HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (HOST, PORT)
 
server = socket.socket()
server.bind(ADDR)
 
root = Tk()
lb1 = Listbox(root)
 
 
def client_handler(connection, address):
    print('[NEW CONNECTION] ' + address)
    connected = True
    while connected:
        msg_length = connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            message = connection.recv(msg_length).decode(FORMAT)
            if message == 'END':
                connection.send('See you later.'.encode())
                connected = False
            elif message == 'TIME':
                connection.send(TIME.encode())
 
            print(address + ': ' + message)
            connection.send('Message received.'.encode(FORMAT))
    connection.close()
 
 
def start_server():
    server.listen()
    print('SERVER: waiting...')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handler, args=(conn, addr))
        thread.start()
 
 
root.mainloop()
 
 
print('[START] Server started...')
start_server()