from tkinter import *

master = Tk()
var1 = IntVar()
var2 = IntVar()
Checkbutton(master, text = "Male", variable = var1).grid(row = 0, sticky = W)
Checkbutton(master, text = "Male", variable = var2).grid(row = 1, sticky = W)
mainloop()