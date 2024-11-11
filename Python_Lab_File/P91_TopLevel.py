from tkinter import *

root = Tk()
Label(root, text = "This is the main window", font = 20).pack()
top_lev = Toplevel()
Label(top_lev, text = "This is the top level window", font = 20).pack()

mainloop()
