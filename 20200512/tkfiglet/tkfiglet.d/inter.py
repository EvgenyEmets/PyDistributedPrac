from tkinter import *
import pyfiglet
import subprocess
def fun(*arg):
    global E, F, L
    t = E.get()
    L = Label(master = F, text = pyfiglet.Figlet(font=pyfiglet.DEFAULT_FONT).renderText(t), justify=LEFT, font=("Source Code Pro", "12"))
    L.grid(sticky = "W", column = 0, row = 1, columnspan = 2)
    """
    for i in range(len(txt)-1):
        print(txt[i].decode("utf-8"))
        F.rowconfigure(6 + i, weight = 1)
        L_er = Label(master = F, text = "\n")
        L_er.grid(sticky = "W", column = 0, row = 1 + i, columnspan = 2)
        L = Label(master = F, text = s, justify=LEFT, font=("Source Code Pro", "12"))
        L.grid(sticky = "W", column = 0, row = 1 + i, columnspan = 2)
        L = Label(master = F, text = txt[i].decode("utf-8"), justify=LEFT, font=("Source Code Pro", "12"))
        L.grid(sticky = "W", column = 0, row = 1 + i, columnspan = 2)
    """
    E.delete(0,END)

F = Frame(borderwidth = 2, relief = "ridge")
F.master.columnconfigure(0, weight = 1)
F.master.rowconfigure(0, weight = 1)
F.grid()
F.grid(sticky = "NEWS")

F.columnconfigure(0, weight = 1)
F.columnconfigure(1, weight = 1)
F.rowconfigure(1, weight = 1)
F.rowconfigure(0, weight = 1)

# Head
E = Entry(master = F)
E.grid(sticky = "NEWS", column = 0, row = 0) 
B = Button(master = F, text = "Go!")
B.bind("<Button-1>", fun)
B.grid(sticky = "NEWS", column = 1, row = 0)
L = Label(master = F)
L.grid(sticky = "W", column = 0, row = 1, columnspan = 2)


mainloop()
