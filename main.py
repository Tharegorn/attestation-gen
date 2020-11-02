from tkinter import Tk
from tkinter.ttk import Button, Label, Combobox
from tkinter import messagebox
from pdf import maker
import os
import tkinter as tk

files = os.listdir("./profiles/")
ctt = 0

for f in files:
    files[ctt] = f.replace(".json", "")
    ctt+=1
window = Tk()

window.title("Generateur de Justificatifs de déplacements")

window.geometry('453x100')

lbl = Label(window, text="Merci de sélectionner votre profile et la raison de votre déplacement.")
combo = Combobox(window)
combo['values'] = files
combo.current(0)  # set the selected item
reason = Combobox(window)
reason['values'] = ("Sélectionner la raison", "travail",
                    "achats", "sante", "famille", "handicap",
                    "convocation", "missions", "enfants",
                    "sport_animaux")
reason.current(0)  # set the selected item
lbl.grid(column=5, row=0)
combo.grid(column=5, row=1)
reason.grid(column=5, row=2)


def profile():
    if (combo.get() != "Sélectionner le profile" and reason.get() != "Sélectionner la raison"):
        maker(combo.get(), reason.get())
        window.destroy()


btn = Button(window, text="Créer l'attestation", command=profile)
btn.grid(column=5, row=3)
window.mainloop()
