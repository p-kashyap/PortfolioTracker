import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np
from mysqlx import Column
import login
import webscraping
import webbrowser
import db
LARGEFONT =("Verdana", 35)
class StartPage():
	def __init__(self):
		self.user=None
		self.window=tk.Tk()
		self.window.title('HomePage')
		self.window.geometry('800x800')
		# label of frame Layout 2
		f=webscraping.storage()
		f.find()
		# button to show frame 2 with text
		# layout2
	
		l2 = ttk.Label(self.window, text ="News", font = LARGEFONT)
		l2.grid(row = 0, column = 20, padx = 40, pady = 10)
		#Create a Label to display the link
		x=15
		newentries=[]
		for i in f.store:
			e=tk.Label(self.window,text=f'{i}',width=50)
			e.grid(row=x,column=20,padx=40)
			link = tk.Label(self.window, text="--- Link")
			link.grid(row=x,column=60,pady=10)
			link.bind("<Button-1>", lambda e:self.callback(f"{f.store[i]}"))
			x+=3
		# Dropdown menu options
		l3 = ttk.Label(self.window, text ="ADD/DROP Coins", font = LARGEFONT)
		l3.grid(row = 30, column = 20, padx = 40, pady = 10)
		options = [
    		"BTC","SHIB","ETH","POL"
			]
  
# datatype of menu text 
		self.window.clicked=tk.StringVar()
		self.window.quantity=tk.StringVar()
# initial menu text
		self.window.clicked.set( "Select a Coin" )
# Create Dropdown menu
		label=ttk.Label(text='ADD/DROP COINS')
		entry =tk.Entry(self.window,textvariable=self.window.quantity)
		entry.grid(row=68,column=30)
		drop = tk.OptionMenu( self.window , self.window.clicked , *options )
		drop.grid(row=80,column=20)
		self.window.l1=tk.Listbox(self.window,height=20)
		self.window.l1.grid(row=70,column=20)
# Create button, it will change label text
		button = ttk.Button( self.window , text = "ADD" , command = self.keep ).grid(row=45,column=30)
		button1 = ttk.Button(self.window, text ="Portfolio",command = self.findprofitloss)
		# putting the button in its place by
		# using grid
		button1.grid(row = 80, column = 30, padx = 10, pady = 10)
	def keep(self):
		coin=self.window.clicked.get()
		quant=int(self.window.quantity.get().strip())
		self.window.l1.insert(1,f'{quant},{coin}')
	def findprofitloss(self):
		fig = plt.figure()
		ax = fig.add_axes([0,0,1,1])
		ax.axis('equal')
		langs = ['C', 'C++', 'Java', 'Python', 'PHP']
		students = [23,17,35,29,12]
		ax.pie(students, labels = langs,autopct='%1.2f%%')
		plt.show()
		pass
	def callback(self,url):
   		webbrowser.open_new_tab(url)
app=login.Login()
app.run()
if app.flag:
	new=StartPage()
	new.user=app.user
	new.window.mainloop()

