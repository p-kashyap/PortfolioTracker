from tkinter import *
import login
# MainFrame to control all the frames
class tkinterApp(Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
        
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (home,portfolio,update_portfolio):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # home,portfolio,update_portfolio respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(home)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class home:
    pass
class portfolio:
    pass
class update_portfolio:
    pass
print(login.hello())
