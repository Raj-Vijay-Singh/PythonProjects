from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, "a")
Lb.insert(2, "b")
Lb.insert(3, "c")
Lb.insert(4, "d")
Lb.pack()
top.mainloop()