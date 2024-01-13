from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("SingUp")
window.geometry('925x500+300+200')
window.config(bg='#fff')
window.resizable(False,False)

def sign_Up():
    Username = user.get()
    Password = user1.get()
    Comform_Password = user2.get()

    if Password == Comform_Password:
        try:
            file = open('data.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={Username:Password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('data.txt','w')
            w = file.write(str(r))

            messagebox.showinfo('Signup','Sucessfully Sign Up.')

        except:
            file=open('data.txt','w')
            pp=str({'Username': 'Password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalied','Both Password should match')

def sign_In():
    window.destroy()

img = PhotoImage(file='login3.png')
Label(window,image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window,width=350,height=350,bg='white')
frame.place(x=480,y=50)

heading = Label(frame,text='Sign Up', fg='#000',bg='#fff', font=('Microsoft Yahei UI Light', 23,'bold'))
heading.place(x=100,y=5)

# #############------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get() == '':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

# #############------------------------------
def on_enter(e):
    user1.delete(0,'end')
def on_leave(e):
    if user.get() == '':
        user1.insert(0,'Password')

user1 = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft Yahei UI Light', 11))
user1.place(x=30,y=150)
user1.insert(0,'Password')
user1.bind("<FocusIn>",on_enter)
user1.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

# #############------------------------------
def on_enter(e):
    user2.delete(0,'end')
def on_leave(e):
    if user2.get() == '':
        user2.insert(0,'Comform Password')

user2 = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft Yahei UI Light', 11))
user2.place(x=30,y=220)
user2.insert(0,'Comform Password')
user2.bind("<FocusIn>",on_enter)
user2.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

# ###############---------------------------------------

Button(frame,width=39,pady=7,text='Sign Up',bg='#000',fg="White",border=0,command=sign_Up).place(x=35,y=280)
lable = Label(frame,text='I have an account', fg='black',bg='white',font=('Microsoft Yahei UI Light', 9))
lable.place(x=90,y=320)

signin = Button(frame,width=6,text='Sign In',border=0, cursor='hand2',fg='black',command=sign_In)
signin.place(x=200,y=320)




window.mainloop()

#elif username != 'admin' and password != '1234':
#tkinter.messagebox.showinfo("Invalied", "invalied Username and Password.")

#elif password != '1234':
#tkinter.messagebox.showinfo("Invalied", "invalied Password.")

#elif username != 'admin':
#tkinter.messagebox.showinfo("Invalied", "invalied Username.")

#else:
#tkinter.messagebox.showerror('Invalied', 'invalied Username or Password.')
