from tabnanny import check
from tkinter import messagebox
from grpc import ssl_server_certificate_configuration
import mysql.connector as msq
from tkinter import *
# login credential requirements database
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
        return flag
    def register(self,username='',pin=0):
        self.c.execute(f"insert into users values('{username}',{pin})")
        pass
class login(data):
    def __init__(self):
        super().__init__()
        self.login=Tk()
        self.login.title('AlphaTracker')
        self.login.geometry('800x600')
        self.user_var=StringVar()
        self.pin_var=StringVar()
        self.newuser=StringVar()
        self.newpin1=StringVar()
        self.newpin2=StringVar()
        self.l1=Label(self.login,text="Username").pack(anchor='w')
        self.l2=Label(self.login,text='Pin').pack(anchor='w')
        self.e1=Entry(self.login,textvariable=self.user_var)
        self.e1.insert(INSERT,"Enter Your Username")
        self.e2=Entry(self.login,textvariable=self.pin_var)
        self.e2.insert(INSERT,"Enter Your Pin")
        self.e1.pack()
        self.e2.pack()
        self.b1=Button(self.login,text='Login',command=self.log).pack(anchor='e')
        self.b2=Button(self.login,text='Register',command=self.reg).pack(anchor='e')
    def run(self):
        self.login.mainloop()
    def check(self,username,pin):
        return super().check(username,pin)
    def log(self):
        user=self.user_var.get().strip()
        pin=int(self.pin_var.get().strip())
        if not self.check(user,pin):
            messagebox.showerror('unknown user','Wrong username or password')
    def reg(self):
        reg=Tk()
        reg.geometry('600x300')
        reg.title('RegisterationWindow')
        self.l1=Label(self.login,text="Username").pack(anchor='w')
        self.l2=Label(self.login,text="Pin").pack(anchor='w')
        self.l3=Label(self.login,text="Re-enter Pin").pack(anchor='w')
        e1=Entry(reg,text='Username').pack()
        e2=Entry(reg,text='Enter ur Pin').pack()
        e3=Entry(reg,text='Re-enter Pin').pack()

f=login()
f.run()