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
    camera_client = CameraClient(local_ip_address,7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(local_ip_address,7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(local_ip_address,6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

############################ Functionality ########################


# server = StreamingServer('192.168.0.207',9999)

############################# GUI PART #############################
window = tk.Tk()
window.title("Server Meeting Part of Software")
window.geometry('300x200')

# adding elements to window
label_target_ip = tk.Label(window,text="The Server IP Address is equal to :")
label_target_ip.pack()

text_target_ip = tk.Label(window,text=local_ip_address)
text_target_ip.pack()

btn_listen = tk.Button(window,text="Start Server Listening to Clients",width=50,command=start_listening)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_camera = tk.Button(window,text="Start Camera Stream From Server Side",width=50,command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER,expand=True)

btn_screen = tk.Button(window,text="Start Screen Sharing From Server Side",width=50,command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio = tk.Button(window,text="Start Audio Stream From Server Side",width=50,command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop() 

############################# GUI PART #############################