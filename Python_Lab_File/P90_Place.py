import tkinter as tk

root = tk.Tk()
root.title("Place Example")

label1 = tk.Label(root, text = "Number 1")
label2 = tk.Label(root, text = "Number 2")
label3 = tk.Label(root, text = "Number 3")

label1.place(x = 0.5, y = 0.5)
label2.place(x = 20, y = 20)
label3.place(x = 50, y = 50)

root.mainloop()