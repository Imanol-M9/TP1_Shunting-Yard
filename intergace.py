from Shunting_yard import tokenize
from Shunting_yard import infix_to_postfix
from Shunting_yard import evaluate_postfix
import tkinter as tk

def affiche():
    shunt_yarded.config(text=f"postfix : {infix_to_postfix(tokenize(valeur.get()))}")
    resultat.config(
        text=f"{evaluate_postfix(infix_to_postfix(tokenize(valeur.get())))}"
    )



fenetre = tk.Tk()
fenetre.title("Shunting_yard Alogritme")

valeur = tk.Entry(fenetre, text="calculer")

tk.Button(fenetre, text="afficher", command=affiche).grid(
    row=3, column=5, padx=5, pady=5
)
shunt_yarded = tk.Label(fenetre, text="postfix")
resultat = tk.Label(fenetre, text="resultat")


valeur.grid(row=1, column=5, padx=5, pady=5)
resultat.grid(row=5, column=5, padx=5, pady=5)
shunt_yarded.grid(row=4, column=5, padx=5, pady=5)

fenetre.mainloop()
