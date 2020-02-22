import tkinter
from tkinter import ttk
class progress:
    def __init__(self,total=100,length=400):
        self.root = tkinter.Tk()
        self.pb = ttk.Progressbar(self.root,length=length)
        self.pb.pack()
        self.total=total
        self.root.update()
    def update(self,upto):
        self.pb["value"]=upto*100/self.total
        self.root.update()
        if upto>=self.total:
            self.destroy()
    def destroy(self):
        self.root.destroy()
