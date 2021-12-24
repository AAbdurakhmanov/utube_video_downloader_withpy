"""
    This is facebook, youtube, instagram videos downloader app

"""
import tkinter as tk
from pytube import YouTube

dock = tk.Tk()
dock.geometry('800x400')
dock.resizable(0, 0)
dock.title("Youtube video downloader")
tk.Label(dock, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = tk.StringVar()

tk.Label(dock,
         text="Paste Link Here: ",
         font="arial 20 bold") \
    .place(x=160, y=60)

link_error = tk.Entry(dock,
                      width=70,
                      textvariable=link) \
    .place(x=32, y=90)


# Function to download the video
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(dock,
             text="Successfully Downloaded",
             font="arial 15") \
        .place(x=180, y=200)


# Download Button
tk.Button(dock,
          text="DOWNLOAD",
          font="Verdana 15 bold",
          bg="orange", padx=2,
          command=Downloader) \
    .place(x=180, y=150)

dock.mainloop()
