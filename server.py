from flask import request
from vidstream import *
import tkinter as tk
import socket 
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())

# server = StreamingServer('192.168.0.207',9999)

############################# GUI PART #############################
window = tk.Tk()
window.title("Client/Server Meeting Software")
window.geometry('300x200')

# adding elements to window
label_target_ip = tk.Label(window,text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window,height=1)
text_target_ip.pack()

btn_listen = tk.Button(window,text="Start Listening",width=50)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_camera = tk.Button(window,text="Start Camera Stream",width=50)
btn_camera.pack(anchor=tk.CENTER,expand=True)

btn_screen = tk.Button(window,text="Start Screen Sharing",width=50)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio = tk.Button(window,text="Start Audio Stream",width=50)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop() 

############################# GUI PART #############################
