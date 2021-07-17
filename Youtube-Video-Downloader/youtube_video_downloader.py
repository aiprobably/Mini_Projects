#Importing the Libraries
from tkinter import *
from pytube import YouTube
​
#Creating the main GUI window
root = Tk()
root.geometry('800x500')
root.resizable(1280,720)
root.title('Personal YouTube Video Downloader')
​
Label(root, bg = "#88cffa", text = 'Personal Youtube Video Downloader',
font ='Algerian 20 bold').pack()
link = StringVar()
​
Label(root, text = 'Paste the YouTube video link Here:', 
font = 'arial 15 bold').place(x= 260 , y = 160)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 200, y = 100)
​
#Defining the download function
def Video_Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 300 , y = 260)
​
#Creating a button to start the download event
Button(root,text = 'Click here to start Download', font = 'SansSerif 12 bold' ,
bg = 'orange', padx = 2, command = Video_Downloader).place(x=300 ,y = 220)
​
#Loop to rerun the above code
root.mainloop()
