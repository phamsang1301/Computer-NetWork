from tkinter import *
from tkinter.ttk import Frame, Button, Style, Label, Entry
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
  
        self.parent = parent
        self.initUI()
   
    def initUI(self):
        self.parent.title("Resource Management")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        label_client = Label(self, text = "List Client", font = ("Arial", 18))
        label_client.pack()
        
        #create textbox to enter new Interval
        newInterval = Entry(self, width = 10)
        newInterval.pack()
        
        def getText():
            text_newInterval = newInterval.get()
            return text_newInterval
        
        getNewIntervalButton = Button(self, text = "Sent",command = getText())
        getNewIntervalButton.pack()
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.pack(side=BOTTOM)
    
root = Tk()
root.geometry("1000x700")
app = Example(root)
root.mainloop()