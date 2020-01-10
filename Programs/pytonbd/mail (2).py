from tkinter import *
window =Tk()
window.geometry('500x500')
window.title("gmail")

label_0 = Label(window,text="sender",font=("bolt",10))
label_0.place(x=40,y=60)

label_1 = Label(window,text="reciever",font=("bold", 10))
label_1.place(x=40,y=80)

label_2 = Label(window,text="password",font=("bold", 10))
label_2.place(x=40,y=100)

s_mail=Entry()
s_mail.place(x=180,y=60)

r_mail=Entry()
r_mail.place(x=180,y=80)

a_mail=Entry()
a_mail.place(x=180,y=100) 
def submit():
    port=465
    context = ssl.create_default_context() 
    with smtplib.SMTP_SSL("SMTP.gmail.com",port,context=context)as server:
                      sender_email=s_mail.get()
                      password=a.get()
                      server.login(sender_email,password)
                      receiver_email=r_mail.get()
                      message ="\subject:this is text mail from python."
                      server.sendmail(sender_email,server_email,message)
                      messagebox.showinfo('mail status','mail send successegefully')
                      s_mail.delete(0 ,'end')
                      r_mail.delete(0 ,'end')
                      a_delete(0 ,'end')
                      s_mail.focus()
button=Button(window,text='submit',font=("bolt",10),command=submit)
button.place(x=180,y=150)
window.mainloop()
