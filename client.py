############ For control ###############
#!/usr/bin/env python
# Client.py of 'Remote Desktop'

import pyautogui as pg
import socket

from click import command
from flask import request
from vidstream import *
import tkinter as tk
import socket 
import threading

#Lets implement console part in GUI
window = tk.Tk()
window.title("Client Part")
window.geometry('300x200')

# adding elements to window

#########To get the ip address
label_target_ip = tk.Label(window,text="Enter the Server IP Address here to start the connection:")
label_target_ip.pack()

text_target_ip = tk.Text(window,height=1)
text_target_ip.pack()

host = text_target_ip

#########To get the ip address

#########To get the port number
label_target_port = tk.Label(window,text="Enter the Port number here to start the connection:")
label_target_port.pack()

text_target_port = tk.Text(window,height=1)
text_target_port.pack()

port = text_target_port
#########To get the port number

# host = input('Host: ')  # as both code is running on same pc
# port = int(input('Port: '))  # socket server port number

#Lets implement console part in GUI

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server


message = 'done'

# This is for the client
local_ip_address = socket.gethostbyname(socket.gethostname())

############################ Functionality ########################

server = StreamingServer(local_ip_address,7777)
receiver = AudioReceiver(local_ip_address,6666)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'),9999)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'),9999)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'),8888)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

def chal_aakhri_chal():
    btn_listen = tk.Button(window,text="Start Listening",width=50,command=start_listening)
    btn_listen.pack(anchor=tk.CENTER,expand=True)

    btn_camera = tk.Button(window,text="Start Camera Stream",width=50,command=start_camera_stream)
    btn_camera.pack(anchor=tk.CENTER,expand=True)

    btn_screen = tk.Button(window,text="Start Screen Sharing",width=50,command=start_screen_sharing)
    btn_screen.pack(anchor=tk.CENTER,expand=True)

    btn_audio = tk.Button(window,text="Start Audio Stream",width=50,command=start_audio_stream)
    btn_audio.pack(anchor=tk.CENTER,expand=True)

    # btn_control = tk.Button(window,text="Start Screen Control",width=50,command=screen_control)
    # btn_control.pack(anchor=tk.CENTER,expand=True)

    window.mainloop() 

while True:
    try:
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response
            if data == 'c':
                pg.click(x, y)
            elif data == 'del':
                pg.typewrite(['backspace'])
            elif data.startswith('cde:'):
                pg.write(data.replace('cde:', ''))
            elif data=='r':
                pg.click(button='right')
            elif data=='d':
                pg.click(clicks=2)
            elif data=='nl':
                pg.typewrite(['enter'])
            elif data == 'exit':
                chal_aakhri_chal()
                print("Chal raha hai chal raha hai aakhri")
            else:
                x = int(data.split(' ')[0])
                y = int(data.split(' ')[1])
                pg.moveTo(x, y)  # show in terminal
            message = 'done' # again take input

        client_socket.close()  # close the connection
    except:
        pass

def screen_control():
    pass

############ For control ###############


############################ Functionality ########################

# server = StreamingServer('192.168.0.207',9999)

############################# GUI PART #############################




    ############################# GUI PART #############################
