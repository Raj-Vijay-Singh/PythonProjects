from tkinter import *

root = Tk()
v = IntVar()
Label(root, text = "Choose your gender: ", font = 20).pack()
Radiobutton(root, text = "Male", variable= v, value = 1, font = 12).pack()
Radiobutton(root, text = "Female", variable = v, value = 2, font = 12).pack()
mainloop()