from tkinter import *

root = Tk()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
Label(root, text = "Choose your attended classes: ", font = 20).pack()
Checkbutton(root, text = "Morning shift", variable = var1, font = 12).pack()
Checkbutton(root, text = "Afternoon shift", variable = var2, font = 12).pack()
Checkbutton(root, text = "Evening shift", variable = var3, font = 12).pack()
mainloop()

