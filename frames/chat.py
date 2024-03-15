
#! DEL IMPORT THAT NOT USE !!!!!
# import datetime
import tkinter as tk
import requests 

from tkinter import ttk
#from PIL import Image,ImageTk 

# Frames
from frames.message_window import MessageWindow


messages = [{"message":"hello world","date":"15498487"}]
message_labels = [] # ttk labels 

class Chat(ttk.Frame):
    def __init__(self,container,*args,**kwargs):
        super().__init__(container,*args,**kwargs)

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        self.messages_frame = MessageWindow(self)
        self.messages_frame.grid(row=0,column=0,sticky="NSEW",pady=5)

        input_frame = ttk.Frame(self,padding=10)
        input_frame.grid(row=1,column=0,sticky="EW")

        message_fetch = ttk.Button(input_frame,text="Fetch",command=self.get_messages)
        message_fetch.pack()

        self.messages_frame.update_message_widget(messages,message_labels)
        

    
    def get_messages(self):
        global messages  # declarte a global variable
        messages = requests.get("http://167.99.63.70/messages").json() # reponse json data
        self.messages_frame.update_message_widget(messages,message_labels) # call the function 
        self.after(150,lambda : self.messages_frame.yview_moveto(1.0))
    