import tkinter as tk
import requests 


from tkinter import ttk

# Frames
from frames.message_window import MessageWindow
messages = [{"message":"hello world","date":"15498487"}]
message_labels = [] # ttk labels 

class Chat(ttk.Frame):
    def __init__(self,container,*args,**kwargs):
        super().__init__(container,*args,**kwargs)
        
        # Grid Config
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        # Window Messages Canvas
        self.message_window = MessageWindow(self)
        self.message_window.grid(row=0,column=0,sticky="NSEW",pady=5)

        # Frames
        input_frame = ttk.Frame(self,padding=10)
        input_frame.grid(row=1,column=0,sticky="EW")

        # Message Input
        self.message_input = tk.Text(input_frame,height=3)
        self.message_input.pack(expand=True,fill="both",side="left",padx=(0,10))

        # Send Button
        send_message = ttk.Button(input_frame,text="Send",command=self.post_messages)
        send_message.pack()
        
        # Fetch Button
        message_fetch = ttk.Button(input_frame,text="Fetch",command=self.get_messages)
        message_fetch.pack()

        self.message_window.update_message_widget(messages,message_labels)
        
    # Post message to the server 
    def post_messages(self):
        body = self.message_input.get("1.0","end").strip()
        requests.post("http://167.99.63.70/message",json={"message":body})
        self.message_input.delete("1.0","end")
        self.get_messages()

    # Get messages from the serverf     
    def get_messages(self):
        global messages  # declarte a global variable
        messages = requests.get("http://167.99.63.70/messages").json() # reponse json data
        self.message_window.update_message_widget(messages,message_labels) # call the function 
        self.after(150,lambda : self.message_window.yview_moveto(1.0))
    