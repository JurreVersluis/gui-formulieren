import tkinter as tk
from tkinter import ttk
getal1 = 0
lastpressed = ''


def check():
    if getal1 > 0:
        window.config(bg="green")
    elif getal1 < 0:
        window.config(bg="red")
    else:
        window.config(bg="grey")


def upnumber(event=''):
    global getal1, lastpressed
    getal1 += 1
    lastpressed = 'up'
    getal.set(getal1)
    check()


def downnumber(event=''):
    global getal1, lastpressed
    getal1 -= 1
    lastpressed = 'down'
    getal.set(getal1)
    check()


def enter(event):
    window.config(bg="yellow")


def leave(event):
    check()


def multiplier(event):
    global getal1
    if lastpressed == 'up':
        getal1 *= 3
    elif lastpressed == 'down':
        getal1 /= 3
    getal.set(getal1)


def welkelaatstgeklikt():
    aanofuit = gechecktofniet.get()
    if aanofuit == 1:
        if lastpressed == 'up':
            upnumber()
        elif lastpressed == 'down':
            downnumber()
    getal.set(getal1)
    window.after(200, welkelaatstgeklikt)



window = tk.Tk()
window.title('Clicker v5')
window.geometry("400x600")
window.config(bg='grey')

window.bind("<Up>", upnumber)
window.bind("<+>", upnumber)
window.bind("<Down>", downnumber)
window.bind("<minus>", downnumber)
window.bind("<space>", multiplier)
getal = tk.StringVar()
getal.set(getal1)

gechecktofniet = tk.IntVar()
gechecktofniet.set(1)
checkbox = tk.Checkbutton(window, text='Autoclicker.', onvalue=1, offvalue=0, variable=gechecktofniet)
checkbox.deselect()
checkbox.pack(ipadx="5",ipady="10", pady="10")


button = tk.Button(window)
button.pack(ipadx="150",ipady="15", pady="80")
button.configure(text="Up",bg='white', command=upnumber)

label = tk.Label(window, textvariable=getal)
label.pack(ipadx="150",ipady="15")
label.bind('<Enter>', enter)
label.bind('<Leave>', leave)
label.bind('<Double-Button-1>', multiplier)
label.configure(bg='white')

button = tk.Button(window)
button.pack(ipadx="150",ipady="15", pady="80")
button.configure(text="Down",bg='white', command=downnumber)


window.after(1, welkelaatstgeklikt)
window.mainloop()