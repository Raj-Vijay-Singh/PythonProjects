import tkinter as tk

# LAYOUT
# 1 2 3 + <-
# 4 5 6 - C
# 7 8 9 * Undo
# (  0 ) / =

buttons = ("1", "2", "3", "+",
           "4", "5", "6", "-",
           "7", "8", "9", "*", ".",
           "(", "0", ")", "/", "=", "C", "←")

poslist = ((1, 0), (1, 1), (1,2), (1, 3),
           (2, 0), (2,1), (2,2), (2, 3),
           (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
           (4,0), (4,1), (4,2), (4, 3))

root = tk.Tk()
root.configure(bg = "beige")
display = tk.StringVar()
display.set("")

strhist = ["No history."]
eqhist = []
def writec(value):
    strt = display.get()
    display.set(strt + value)

def backspace():
    strt = display.get()
    display.set(strt[0:-1])

def equal():
    Calc = True
    strt = display.get()
    strhist.append(strt)

    for i in strt:
        if strt not in buttons:
            calc = False
            display.set("Arithmetic Error.")
            break

    if Calc:
        try:
            ans = str(round(eval(strt), 3))
            if ans[-1] == "0" and ans[-2] == ".":
                ans = str(round(float(ans)))
            eqhist.append(ans)
            display.set(ans)
        except:
            display.set("Arithmetic Error.")

    else:
        return;

def clear():
    display.set("")

def undo():
    display.set(strhist[-1])
#
# def history():
#     tk.Label(root, text = "HISTORY:", fg ="black", bg ="white", bd = 10, width = 28, font = ("Bahnschrift", 16, "bold"), anchor="w").grid(row = 6, column = 0, columnspan = 5)
#     if len(eqhist) == 0:
#         tk.Label(root, text="No history to show.", fg="black", bg="white", bd=10, width=46, font=("Bahnschrift", 10, "bold"),
#                  anchor="w").grid(row=7, column=0, columnspan=5)
#
#     else:
#         rowind = 7
#         for dis, eq in zip(strhist[::-1], eqhist[::-1]):
#             tk.Label(root, text=f"{dis} = {eq}", fg="black", bg="white", bd=10, height= 1, width=46, font=("Bahnschrift", 10, "bold"), anchor="w").grid(row = rowind, column = 0, columnspan=5)
#             rowind += 1

tk.Entry(root, textvariable = display, fg ="black", bg ="white", bd = 10, width = 21, font = ("Courier New", 20, "bold")).grid(row = 0, column = 0, columnspan = 999, sticky ="w")

for button, pos in zip(buttons, poslist):
    but = tk.Button(root, text=button, command=lambda button = button: writec(button), bg="black", bd=10, width=3, fg="white",
              font=("Bahnschrift", 20, "bold"), relief="sunken")
    but.grid(row=pos[0], column=pos[1])

bspc = tk.Button(root, text="←", command=lambda: backspace(), bg="black", bd=10, width=3, fg="white", font=("Bahnschrift", 20, "bold"), relief="sunken")
bspc.grid(row=1, column=4)

equalbut = tk.Button(root, text="=", command=lambda: equal(), bg="black", bd=10, width=3, fg="white", font=("Bahnschrift", 20, "bold"), relief="sunken")
equalbut.grid(row=4, column=4)

clearbut = tk.Button(root, text="C", command=lambda: clear(), bg="black", bd=10, width=3, fg="white", font=("Bahnschrift", 20, "bold"), relief="sunken")
clearbut.grid(row=2, column=4)

hisbut = tk.Button(root, text="Undo", command=lambda: undo(), bg="black", bd=10, width=22, fg="white", font=("Bahnschrift", 20, "bold"), relief="sunken")
hisbut.grid(row=5, column=0, columnspan = 5)

root.mainloop()