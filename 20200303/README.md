# Конспект семинара
Сегодня будем баловаться с tkinter  
from tkinter import *  
F=Frame() //окошко  
B=Button(master=F) //кнопка  
F.pack()  
B.pack()
  
B["text"]="QQ" //текст в кнопке  
B.configure(text="QKRQ")  
  
E=Entry(master=F) //поле ввода  
E.pack()  
  
E.delete(0,END) //удаление строки из ввода  
  
B.bind("<Button-1>", fun) //обработчик на кнопку  
  
L = Label(master=F, text = "REGEH") //Надпись  


