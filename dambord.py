import tkinter as tk

window = tk.Tk()
window.title('Dambord')
window.geometry("600x600")
window.config(bg='grey')
kleuren = ['white', 'black']
counter1, counter2, counter3, counter4 = 0, 0, 0, 0

for i in range(10):
    window.rowconfigure(i, weight=10)
    window.columnconfigure(i, weight=10)

for i in range(100):
    Nieuwvakje = tk.Label(window)
    Nieuwvakje.grid(column=counter1, row=counter2, ipadx='100', ipady='100')

    if counter1 > 8:
        counter1 = 0
        counter2 += 1
    else:
        counter1 += 1

    if counter3 > 0:
        counter3 = 0
    else:
        counter3 += 1
    counter4 += 1

    if counter4 == 11:
        weggehaaldekleur = kleuren.pop(0)
        kleuren.append(weggehaaldekleur)
        counter4 = 1

    Nieuwvakje.config(bg=kleuren[counter3])


window.mainloop()