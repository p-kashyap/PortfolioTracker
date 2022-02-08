from atexit import register
from tabnanny import check
from tkinter import messagebox
import mysql.connector as msq
from tkinter import *
# database
class data:
    def __init__(self):
        self.conn = msq.connect(host='localhost',database='portfolio',user='root',password='vasu1dev2')
        self.c=self.conn.cursor()
    def check(self,username,pin):
        self.c.execute("select * from users")
        flag=False
        for i in self.c:
            if username==i[0] and pin==i[1]:
                flag=True
                break
        return flag
    def register(self,username='',pin=0):
        t=(
        "INSERT INTO users"
        " VALUES (%s,%s)"
        )
        data=(f'{username}',pin)
        self.c.execute(t,data)
        self.conn.commit()
#Login window
class Login(data):
    def __init__(self):
        super().__init__()
        self.flag=False
        self.login=Tk()
        self.login.title('AlphaTracker')
        self.login.geometry('400x200')
        self.user_var=StringVar()
        self.pin_var=StringVar()
        # Add image file
        bg = PhotoImage(file = "/Users/priyannk/Desktop/PortfolioApp/labelimage.png")
        canvas = Canvas(self.login, width = 300, height = 300)      
        canvas.pack() 
# Create Canvas
        canvas.create_image(20,20, anchor=NW, image=bg)
# Display image
        self.e1=Entry(self.login,textvariable=self.user_var)
        self.e1.insert(INSERT,"Username")
        self.e2=Entry(self.login,textvariable=self.pin_var)
        self.e2.insert(INSERT,"Pin")
        self.e1.place(x=100,y=40)
        self.e2.place(x=100,y=70)
        self.e1.bind("<Button-1>", self.click1)
        self.e2.bind("<Button-1>", self.click2)
        self.b1=Button(self.login,text='Login',command=self.log).place(x=100,y=120)
        self.b2=Button(self.login,text='Register',command=self.regex).place(x=220,y=120)
    def click1(self,*args):
        self.e1.delete(0, 'end')
    def click2(self,*args):
        self.e2.delete(0, 'end')
  
    # call function when we leave entry box
    def run(self):
        self.login.mainloop()
    def check(self,username,pin):
        return super().check(username,pin)
    def log(self):
        user=self.user_var.get().strip()
        pin=int(self.pin_var.get().strip())
        if not self.check(user,pin):
            messagebox.showerror('unknown user','Wrong username or password')
        else:
            self.login.destroy()
            self.flag=True
    def regex(self):
        global reg
        reg=Toplevel(self.login)
        reg.geometry('400x300')
        reg.title('RegisterationWindow')
        self.newuser=StringVar()
        self.newpin1=StringVar()
        self.newpin2=StringVar()
        self.l3=Label(reg,text="Username").place(x=50,y=60)
        self.l4=Label(reg,text="Pin").place(x=50,y=90)
        self.l5=Label(reg,text="Re-enter Pin").place(x=50,y=120)
        self.e3=Entry(reg,textvariable=self.newuser)
        self.e4=Entry(reg,textvariable=self.newpin1)
        self.e5=Entry(reg,textvariable=self.newpin2)
        self.e3.place(x=150,y=60)
        self.e4.place(x=150,y=90)
        self.e5.place(x=150,y=120)
        self.b3=Button(reg,text="Create Account",command=self.create).place(x=150,y=180)
    def create(self):
        user=self.newuser.get().strip()
        pin1=int(self.newpin1.get().strip())
        pin2=int(self.newpin2.get().strip())
        if pin1!=pin2:
            messagebox.showerror('pin incorrect','Pins dont match')
        else:
            self.register(user,pin1)
            reg.destroy()
    # new window for user registeratione
f=Login()
f.run()