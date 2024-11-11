import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

label1 = tk.Label(root, text = "Number 1")
label2 = tk.Label(root, text = "Number 2")
label3 = tk.Label(root, text = "Number 3")

label1.pack()
label2.pack()
label3.pack()

root.mainloop()