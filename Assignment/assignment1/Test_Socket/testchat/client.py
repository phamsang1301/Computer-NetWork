from tkinter import *
import socket
 
# s = socket.socket()
# HOST = 'localhost'
# PORT = 12345
 
 
# def send_to_server():
#     name = var_entry.get()
#     option = var_radio.get()
#     if option == 1:
#         s.connect((HOST, PORT))
#         s.send(name.encode() + 'TIME'.encode())
#         data = s.recv(1024)
#         listbox_responses.insert(data)
#     elif option == 2:
#         s.send(name.encode() + 'END'.encode())
#         data = s.recv(1024)
#         listbox_responses.insert(data)
#         s.close()
 
 
root = Tk()
 
# variables
var_entry = StringVar()
var_radio = IntVar()
 
# canvas
c = Canvas(root, bg='yellow', height=150, width=300)
coord = 60, 60, 240, 210
arc = c.create_arc(coord, start=0, extent=180, fill='red')
c.pack()
 
# name label
label_name = Label(root, text='Name', relief=RAISED, bg='blue', fg='white', width=42)
label_name.pack()
 
# name entry
entry_name = Entry(root, textvariable=var_entry, width=49)
entry_name.pack()
 
# radiobuttons
radio_time = Radiobutton(root, text='Time', variable=var_radio, value=1)
radio_end = Radiobutton(root, text='End', variable=var_radio, value=2)
radio_time.pack(anchor=W)
radio_end.pack(anchor=W)
 
# button - send request to server
# button_send = Button(root, text='SEND REQUEST TO SERVER', bg='limegreen', width=40, command=send_to_server)
# button_send.pack()
 
# label server responses
label_responses = Label(root, text='Server responses')
label_responses.pack()
 
# listbox responses
listbox_responses = Listbox(root, width=45)
listbox_responses.pack()
 
 
root.mainloop()