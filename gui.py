from shunting_yard import tokenize
from shunting_yard import infix_to_postfix
from shunting_yard import evaluate_postfix

import tkinter as tk
import keyboard


def affiche():
    shunt_yarded.config(text=f"postfix : {infix_to_postfix(tokenize(valeur.get()))}")
    resultat.config(
        text=f"{evaluate_postfix(infix_to_postfix(tokenize(valeur.get())))}"
    )
    try:
        if type(evaluate_postfix(infix_to_postfix(tokenize(valeur.get())))[0]) is type(BaseException):
            execute_erreur_(evaluate_postfix(infix_to_postfix(tokenize(valeur.get())))[1])
    except TypeError:
        None

def execute_erreur_(message):
    print(message)
    shunt_yarded.config(text="postfix : erreur")
    resultat.config(text="resultat : erreur")
    erreur_page.config(text= f"{message}")


def fonction_quit():
    fenetre.destroy()


fenetre = tk.Tk()
keyboard.add_hotkey("esc", fonction_quit)
fenetre.title("Shunting_yard Alogritme")

valeur = tk.Entry(fenetre, text="calculer")

tk.Button(fenetre, text="afficher", command=affiche).grid(
    row=3, column=5, padx=5, pady=5
)
shunt_yarded = tk.Label(fenetre, text="postfix")
resultat = tk.Label(fenetre, text="resultat")
erreur_page = tk.Label(fenetre, text=" ")

valeur.grid(row=1, column=5, padx=5, pady=5)
shunt_yarded.grid(row=4, column=5, padx=5, pady=5)
resultat.grid(row=5, column=5, padx=5, pady=5)
erreur_page.grid(row=6, column=5, padx=5, pady=5)

fenetre.mainloop()
