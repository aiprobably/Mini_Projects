# Importing the necessary libraries
from pygame import mixer
from tkinter import *
import os
​
# Create a basic window 
root=Tk()
root.title('Music Player')
root.geometry("1000x150")
​
mixer.init()
track = StringVar()
status = StringVar()
​
# Functions to play, pause, stop and resume a song
def play():
    current=playlist.get(ACTIVE)
    print(current)
    mixer.music.load(current)
    mixer.music.play()
    status.set("Playing")
    track.set(playlist.get(ACTIVE))
​
def pause():
    mixer.music.pause()
    status.set("Paused")
​
def stop():
    mixer.music.stop()
    status.set("Stopped")
​
def resume():
    mixer.music.unpause()  
    status.set("Playing")  
​
# Track Frame for Song label & status label
trackframe = LabelFrame(root,bg="#98FB98",fg="black",bd=5,relief=GROOVE)
trackframe.place(x=0,y=0,width=600,height=70)
songtrack = Label(trackframe,textvariable=track,width=20,font=("times new roman",15,"bold"),bg="#708090",fg="white").grid(row=0,column=0,padx=15,pady=15)
trackstatus = Label(trackframe,textvariable=status,font=("times new roman",13, "bold"),bg="#708090",fg="white").grid(row=0,column=1,padx=10,pady=5)
​
# Button Frame
buttonframe = LabelFrame(root,bg="#FFF0F5",fg="white",bd=5,relief=GROOVE)
buttonframe.place(x=0,y=70,width=600,height=80)
​
playbtn = Button(buttonframe,text="PLAY",command=play,width=10,height=1,font=("times new roman",15,"bold"),fg="navyblue",bg="#ADD8E6").grid(row=0,column=0,padx=15,pady=15)
pausebtn = Button(buttonframe,text="PAUSE",command=pause,width=8,height=1,font=("times new roman",15,"bold"),fg="navyblue",bg="#ADD8E6").grid(row=0,column=1,padx=10,pady=5)
resumebtn = Button(buttonframe,text="RESUME",command=resume,width=10,height=1,font=("times new roman",15,"bold"),fg="navyblue",bg="#ADD8E6").grid(row=0,column=2,padx=10,pady=5)
stopbtn = Button(buttonframe,text="STOP",command=stop,width=10,height=1,font=("times new roman",15,"bold"),fg="navyblue",bg="#ADD8E6").grid(row=0,column=3,padx=10,pady=5)
​
# Playlist Frame
songsframe = LabelFrame(root,bg="#696969",fg="white",bd=5,relief=GROOVE)
songsframe.place(x=600,y=0,width=400,height=150)
playlist = Listbox(songsframe,selectbackground="#808080",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="#E0FFFF",fg="navyblue",bd=5,relief=GROOVE)
playlist.pack(fill=BOTH)
​
# Changing the directory for fetching Songs
os.chdir(r'C:\Users\AAYUSHI R\OneDrive\Desktop\music player') 
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
​
# Root Window Looping
mainloop()
​
