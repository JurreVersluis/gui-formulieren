import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinter import *
from datetime import date
window = tk.Tk()


def test():
    gekozendagvar = gekozendag.get()
    gekozenmaandvar = gekozenmaand.get()
    gekozenjaarvar = gekozenjaar.get()
    print(gekozendagvar)
    print(gekozenjaarvar)
    print(gekozenmaandvar)




window.title('DayToDayCalculator')
window.geometry("515x252")
window.config(bg='grey')

gekozendag = tk.StringVar()
gekozenmaand = tk.StringVar()
gekozenjaar = tk.StringVar()

frame = tk.Frame(window)
frame.place(relx=0.0)

datetekst = tk.Label(frame, text='Date:', font='Helvetica 20 bold')
datetekst.grid(row=0, column=2, ipadx='10', ipady='3', padx=15, pady=40)

combobox1 = ttk.Combobox(frame, textvariable=gekozendag)
combobox1.grid(column=0, row=1, ipadx='5', ipady='3', padx=5)
combobox1.bind("<<ComboboxSelected>>", lambda e: window.focus())
combobox1['values'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
combobox1['state'] = 'readonly'


streepje1 = tk.Label(frame, text='-', font='Helvetica 12 bold')
streepje1.grid(column=1, row=1, ipadx='5', ipady='3')

combobox2 = ttk.Combobox(frame, textvariable=gekozenmaand)
combobox2.grid(column=2, row=1, ipadx='5', ipady='3', padx=5)
combobox2.bind("<<ComboboxSelected>>", lambda e: window.focus())
combobox2['values'] = ['Jan', 'Feb','Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
combobox2['state'] = 'readonly'

streepje2 = tk.Label(frame, text='-', font='Helvetica 12 bold')
streepje2.grid(column=3, row=1, ipadx='5', ipady='3')

entry1 = ttk.Entry(frame, textvariable=gekozenjaar)
entry1.grid(column=4, row=1, ipadx='5', ipady='3', padx=5)


button1 = ttk.Button(frame, text='test')
button1.grid(column=2, row=3, ipadx='10', ipady='8', pady=40)
button1.configure(command=test)



window.mainloop()