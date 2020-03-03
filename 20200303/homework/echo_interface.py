from tkinter import *

s = "echo"
s1 = "echo"
def fun(*arg):
	global s, s1
	s1 = s
	L_main = Label(master = F, text = s)
	L_main.grid(sticky = "NEWS", column = 0, row = 0)
	E.delete(0,END)

def fun1(*arg):
	global s1
	s1 += " -n"
	L_main = Label(master = F, text = s1)
	L_main.grid(sticky = "NEWS", column = 0, row = 0)

def fun2(*arg):
	global s1
	s1 += " -e"
	L_main = Label(master = F, text = s1)
	L_main.grid(sticky = "NEWS", column = 0, row = 0)

def fun3(*arg):
	global s1
	s1 += " -E"
	L_main = Label(master = F, text = s1)
	L_main.grid(sticky = "NEWS", column = 0, row = 0)

def fun4(*arg):
	global s1
	s1 += " --help"
	L_main = Label(master = F, text = s1)
	L_main.grid(sticky = "NEWS", column = 0, row = 0)

def fun5(*arg):
	global s1
	s1 += " --version"
	L_main = Label(master = F, text = s1)
	L_main.grid(sticky = "NEWS", column = 0, row = 0)

F = Frame(borderwidth = 2, relief = "ridge")
F.master.columnconfigure(0, weight = 1)
F.master.rowconfigure(0, weight = 1)
F.grid()
F.grid(sticky = "NEWS")

F.columnconfigure(0, weight = 1)
F.columnconfigure(1, weight = 1)
F.columnconfigure(2, weight = 1)
F.rowconfigure(1, weight = 1)
F.rowconfigure(2, weight = 1)
F.rowconfigure(3, weight = 1)
F.rowconfigure(4, weight = 1)
F.rowconfigure(5, weight = 1)
F.rowconfigure(0, weight = 1)

# Head
L_main = Label(master = F, text = s1)
L_main.grid(sticky = "NEWS", column = 0, row = 0)
E = Entry(master = F)
E.grid(sticky = "NEWS", column = 1, row = 0) 
B = Button(master = F, text = "Go!")
B.bind("<Button-1>", fun)
B.grid(sticky = "NEWS", column = 2, row = 0)


B1 = Button(master = F, text = "-n")
B1.bind("<Button-1>", fun1)
B1.grid(sticky = "NEWS", column = 0, row = 1)
L1 = Label(master = F, text = "do not output the trailing newline")
L1.grid(sticky = "EW", column = 1, row = 1, columnspan = 2)

B2 = Button(master = F, text = "-e")
B2.bind("<Button-1>", fun2)
B2.grid(sticky = "NEWS", column = 0, row = 2)
L2 = Label(master = F, text = "enable interpretation of backslash escapes")
L2.grid(sticky = "EW", column = 1, row = 2, columnspan = 2)

B3 = Button(master = F, text = "-E")
B3.bind("<Button-1>", fun3)
B3.grid(sticky = "NEWS", column = 0, row = 3)
L3 = Label(master = F, text = "disable interpretation of backslash escapes (default)")
L3.grid(sticky = "EW", column = 1, row = 3, columnspan = 2)

B4 = Button(master = F, text = "--help")
B4.bind("<Button-1>", fun4)
B4.grid(sticky = "NEWS", column = 0, row = 4)
L4 = Label(master = F, text = "display help and exit")
L4.grid(sticky = "EW", column = 1, row = 4, columnspan = 2)

B5 = Button(master = F, text = "--version")
B5.bind("<Button-1>", fun5)
B5.grid(sticky = "NEWS", column = 0, row = 5)
L5 = Label(master = F, text = "output version information and exit")
L5.grid(sticky = "EW", column = 1, row = 5, columnspan = 2)

mainloop()
