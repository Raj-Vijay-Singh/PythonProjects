from tkinter import *

master = Tk()
Label(master, text = "Name: ", font = 20).grid(row = 0, sticky = "w")
Label(master, text = "Address: ", font = 20).grid(row = 1, sticky = "w")
Entry(master, font = 20).grid(row = 0, column = 1)
Entry(master, font = 20).grid(row = 1, column = 1)
mainloop()