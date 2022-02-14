import mysql.connector as msq
#initialise database connection
class connect:
    def __init__(self):
        self.user=None
        self.conn = msq.connect(host='localhost',database='portfolio',user='root',password='vasu1dev2')
        self.c=self.conn.cursor()
    #show items in the table
    def show(self):
        self.c.execute("select * from news;")
        x=[]
        for i in self.c:
            x.append(i)
        return x
    #insert items into the table
    def insert(self,name,url):
        self.c.execute(f"insert into news values ('{name}','{url}')")
        self.conn.commit()
    