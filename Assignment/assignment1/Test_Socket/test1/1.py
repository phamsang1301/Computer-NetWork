from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
import time
import pickle
from tkinter import *

# def createServer(host,port):
#     Server = socket(AF_INET, SOCK_STREAM)
#     Server.bind((host,port))
#     Server.listen(40)
#     return Server


    
    
def swtich():
    
    return True
    

def create_TCP_connection():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverPort = 4000
    serverSocket.bind(('localhost', serverPort))
    serverSocket.listen(40)
    
    # print('Ready to server...')
    # listbox_responses.insert('Ready to server...')
    listbox_responses.pack()
    
    
    connectionSocket, addr = serverSocket.accept()    
    message = connectionSocket.recv(
                1024)
    msg = pickle.loads(message)        
    print("Name: " +msg['NAME'])        
    print("IP: " + msg['IP'])
    print("UDP PORT: " +str(msg['UDP_PORT']))        
    print("Time: " +str(msg['TIME']))                

    if True:      
        message_to_client = {'STATUS': "Success",'ID': 0,'INTERVAL': 5, 'TCP_PORT': 4000 }
        msg_to_client = pickle.dumps(message_to_client)
        connectionSocket.send(msg_to_client)

        while True:
                info = connectionSocket.recv(
                    1024)
                inf = pickle.loads(info)
                # print(inf)
                print("CPU: "+ str(inf['CPU']) + " Degree")
                print("------------------------------")
                print("Memory: ")
                print("\t Total: " + str(inf['MEMORY']['Total']))
                print("\t Used: " + str(inf['MEMORY']['USED']))
                print("\t Available: " + str(inf['MEMORY']['Avaiable']))
                print("\t Use Percent: " + str(inf['MEMORY']['USED_PERCENT']))
                print("-------------------------------")      
                print("Disk: ")
                print("\t Total:" + str(inf['DISK']['Total']))
                print("\t USED: " + str(inf['DISK']['USED']))
                print("\t Available: " + str(inf['DISK']['Avaiable']))
                print("\t Use Percent: " + str(inf['DISK']['USED_PERCENT']))
                print("-------------------------------------------------------------")
                
                # send_new_para_to_client(1,4000)
       
def open_udp_connection():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 4001))

def send_new_para_to_client(interval, tcp_port):
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    socket.bind(('', 4000))
    socket.listen(40)
    connectionSocket, addr = socket.accept()

    if (True): 
        message_to_client = {'INTERVAL': interval, 'TCP_PORT': tcp_port }
        msg_to_client = pickle.dumps(message_to_client)
        connectionSocket.send(msg_to_client)


root = Tk()
root.geometry("1000x700")
root.title("Resource Management")
label_client = Label(root, text = "List Client", font = ("Arial", 18))
label_client.pack()
            
            #create textbox to enter new Interval
newInterval = Entry(root, width = 10)
newInterval.pack()

def getText():
    text_newInterval = newInterval.get()
    return text_newInterval
            
getNewIntervalButton = Button(root, text = "Sent",command = getText())
getNewIntervalButton.pack()

quitButton = Button(root, text="Quit", command=root.quit)
quitButton.pack()




show_computer_info = Text(root,width = 10)


# listbox responses
listbox_responses = Listbox(root, width=45)
listbox_responses.pack()


startButton = Button(root, text="Start", command=create_TCP_connection())
startButton.pack()
root.mainloop()




# threads = []

# newThread = Thread(target=create_TCP_connection, args=())
# newThread.start()
# threads.append(newThread)

# newThread2 = Thread(target=udpConnection, args=())
# newThread2.start()
# threads.append(newThread2)

# if __name__ == "__main__":
#     Server = createServer('',4000)   
#     create_TCP_connection(Server)
     




# root = createForm()
# root.mainloop()
