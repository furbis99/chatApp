import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MessageWindow(tk.Canvas):
    def __init__(self,container,*args,**kwargs):
        super().__init__(container,*args,**kwargs,highlightthickness=0)

        # Frame that is contained in the canvas
        self.message_frame = ttk.Frame(container,style='Messages.TFrame')
        self.message_frame.columnconfigure(0,weight=1)

        # Config scrollable window
        self.scrollable_window = self.create_window((0,0),window=self.message_frame,anchor="nw")

        # Region to be scrollable
        def config_scrollable_region(event):
            self.configure(scrollregion=self.bbox("all"))

        #Scorllable window frame Size
        def config_window_size(event):
            self.itemconfig(self.scrollable_window,width = self.winfo_width())

        # Bind functions     
        self.bind('<Configure>',config_window_size)
        self.message_frame.bind('<Configure>',config_scrollable_region)
        self.bind_all('<MouseWheel>',self._on_mousewheels)

        # Scrollbar Widget
        scrollbar = ttk.Scrollbar(container,orient="vertical",command=self.yview)
        scrollbar.grid(row=0,column=1,sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def _on_mousewheels(self,event):
        self.yview_scroll(-int(event.delta/120),"units")


    
    def update_message_widget(self,messages,message_labels):
        # Load messages that have already been shown in the chat
        existing_labels = [
            (message["text"],time["text"]) for message,time in message_labels
            ]
        
        
        for message in messages: # loop through the global variable
            message_time = datetime.datetime.fromtimestamp(int(message["date"])).strftime("%d-%m-%Y %H:%M:%S")
            
            if (message["message"],message_time) not in existing_labels: # Evaluates if it is a new message
                
                # create message container function
                self._create_message_container(message["message"],message_time,message_labels)
    
    def _create_message_container(self,message_content,message_time,message_labels):
        # private function that will help us grid the container messages
        container = ttk.Frame(self.message_frame)
        container.columnconfigure(1,weight=1)
        container.grid(sticky="EW",padx=(10,50),pady=10)

        self._create_message_buble(container,message_content,message_time,message_labels)
        

    def _create_message_buble(self,container, message_content,message_time,message_labels):
        #  Image
        #TODO: resize the image label 
        #avatar_image = Image.open("./assets/user.png")
        #avatar_image.resize((5,5))
       # avatar_photo = ImageTk.PhotoImage(avatar_image)

        # Image Label 
        #avatar_label = tk.Label(container,image=avatar_photo,style='Avatar.TLabel')
        #avatar_label.grid(row=0,column=0,rowspan=2,sticky="NEW",padx=(0,10),pady=(5,0))
        
        # Labels message
        time_label = ttk.Label(container,text=message_time,style='Time.TLabel')
        time_label.grid(row=0,column=1,sticky="NEW")

        # if it is a new message create a label
        new_message = ttk.Label(
            container,
            text = message_content,
            anchor="w",
            justify="left",
            style='Message.TLabel'
        )

        new_message.grid(row=1,column=1,sticky="NSEW") # show label
        message_labels.append((new_message,time_label)) # add to the list