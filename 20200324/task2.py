from tkinter import *

class App(Frame):
	def __init__(self, master=None, Title="Application", **kwargs):
		Frame.__init__(self, master, **kwargs)
		self.master.rowconfigure(0, weight=1)
		self.master.columnconfigure(0, weight=1)
		self.master.title(Title)
		self.grid(sticky="NEWS")
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.S = StringVar()
		self.S.set("Wdfghgfd")
		self.E = Entry(self,text = "ffffgfd",  textvariable=self.S)
		self.E.grid(sticky = "NEWS")
		self.E1  = Entry(self,text = "ffffgfd",  textvariable=self.S)
		self.E1.grid(sticky = "NEWS")
		self.T = Text(self)
		self.T.grid(sticky = "NEWS")
		self.T.insert(1.0,"\n"
		

A = App()
A.mainloop()

