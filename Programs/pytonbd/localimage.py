# to get local photo
from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.geometry("1900x2000")

image=Image.open("x.jpg")# to get jpg file
photo=ImageTk.PhotoImage(image)
#ima=photoImage(file="x.jpg") #this method support only png format
label1=Label(image=photo)
label1.pack()
window.mainloop()
     
