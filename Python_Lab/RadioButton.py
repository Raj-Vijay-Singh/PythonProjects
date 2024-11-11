from tkinter import *

root = Tk()
v = IntVar()
Radiobutton(root, text = 'GfG', variable = v, value = 1).pack(anchor = 'center')
Radiobutton(root, text = 'MIF', variable = v, value = 2).pack(anchor = 'center')
mainloop()