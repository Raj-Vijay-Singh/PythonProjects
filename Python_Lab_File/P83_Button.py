from tkinter import *

root = Tk()
B1 = Button(root, text = "Press to close program", fg = "white", bg = "black", bd = 10, font = 20, relief = "sunken", command = root.destroy)
B1.pack()
mainloop()