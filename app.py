import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title("Y&F&I video downloader")


tk.Label(root,
         text='Youtube Video Downloader',
         anchor="center",
         font="arial 20 bold"
         ).pack(fill='both')

link = tk.StringVar()

tk.Label(root,
         text="Paste Link Here: ",
         anchor='w',
         font="arial 18 italic"
         ).pack(fill="both")

link_error = tk.Entry(root,
                      width=50,
                      textvariable=link) \
    .place(x=32, y=90)




# Function to download the video
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(root,
             text="Successfully Downloaded",
             font="arial 15"
             ).place(x=180, y=200)

# Download Button
tk.Button(root,
          text="DOWNLOAD",
          font="Verdana 15 bold",
          bg="orange", padx=2,
          command=Downloader
          ).place(x=120, y=120)

root.mainloop()
