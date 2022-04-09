# This is for the server

######################################### For Control #########################################
#!/usr/bin/env python
# Server.py of 'Remote Desktop'
# import socket # For network connections
# import tkinter as tk # To create a graphical user interface
# from tkinter.messagebox import showinfo # To give alerts
# from random import randint # To pick a random number

# def type_box():
#     tp_fr = tk.Tk()
#     tp_fr.title('Python Remote Keyboard')
#     bx_txt = tk.Entry(tp_fr, width=100)
#     bx_txt.pack()
#     send_but =tk.Button(tp_fr, text="Type Text", command=lambda:conn.send(('cde:'+bx_txt.get()).encode()))
#     del_but =tk.Button(tp_fr, text="Delete", command=lambda:conn.send(('del'.encode())))
#     nl_but =tk.Button(tp_fr, text="Enter", command=lambda:conn.send(('nl'.encode())))
#     del_but.pack()
#     send_but.pack()
#     nl_but.pack()
#     tp_fr.mainloop()

# def motion(event):
#     x, y = event.x, event.y
#     data = conn.recv(1024).decode()
#     data = str(x*2)+' '+str(y*2)
#     conn.send(data.encode())

# port = randint(1000, 10000)
# k = tk.Tk()
# showinfo('Control Data','Host = '+socket.gethostbyname(socket.gethostname())+'\nPort = '+str(port))
# k.destroy()
# root = tk.Tk()
# root.title('Python Remote Trackpad')
# root.geometry('960x540')
# global x, y, data
# host = socket.gethostname()

# server_socket = socket.socket()
# server_socket.bind((host, port))
# server_socket.listen(2)
# conn, address = server_socket.accept()
# print("Connection from: " + str(address))


# def a(o):
#     conn.send('c'.encode())
#     print("Click button pressed")
# def r(o):
#     conn.send('r'.encode())
#     print("Right Click Pressed")
# def d(o):
#     conn.send('d'.encode())


# def screen_control():
#     #This is the main code starting from here    
#     x = 10
#     y = 10

#     root.bind('<Motion>', motion)
#     print(10)
#     cde = ''
    
#     root.bind('<Control-l>', a)
#     root.bind('<Control-r>', r)
#     root.bind('<Control-d>', d)
#     menubar = tk.Menu(root)
#     menubar.add_command(label="Type", command=type_box)
#     root.config(menu = menubar)

#     root.mainloop()
        

######################################### For Control #########################################

from click import command
from flask import request
from vidstream import *
import tkinter as tk
import socket 
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())

############################ Functionality ########################

server = StreamingServer(local_ip_address,9999)
receiver = AudioReceiver(local_ip_address,8888)


def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'),7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'),7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'),6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

############################ Functionality ########################

# server = StreamingServer('192.168.0.207',9999)

############################# GUI PART #############################
window = tk.Tk()
window.title("Server Part")
window.geometry('300x200')

# adding elements to window
label_target_ip = tk.Label(window,text="Server IP Address:")
label_target_ip.pack()

text_target_ip = tk.Label(window,text=local_ip_address)
text_target_ip.pack()

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

############################# GUI PART #############################
