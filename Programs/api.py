import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

root=tk.TK()
root.geometry('1900x2000')
URL="https://image.freepik.com/free-vector/realistic-new-year-2020-background-with-golden-gift-bow_23-2148396931.jpg"
u=urlopen(URL)
raw_data=u.read()
u.close()

imn = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(imn)

label = tk.Label(image=photo)
label.image = Photo
label.pack()

root.mainloop()
