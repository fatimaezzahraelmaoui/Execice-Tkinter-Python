from tkinter import *
import tkinter as tk

class InterfaceCompte:
    def _init_(self, root):
        self.root = root
        self.root.title("Création de Comptes")
        
        self.label_numero = tk.Label(root, text="Numéro du compte:")
        self.entry_numero = tk.Entry(root, state="disabled")  
        self.label_type = tk.Label(root, text="Type de compte:")
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)  
        
        self.radio_courant = tk.Radiobutton(root, text="Compte Courant", variable=self.radio_var, value=1)
        self.radio_epargne = tk.Radiobutton(root, text="Compte Épargne", variable=self.radio_var, value=2)
        self.button_creer = tk.Button(root, text="Créer Compte", command=self.creer_compte)
        
        self.label_numero.grid(row=0, column=0)
        self.entry_numero.grid(row=0, column=1)
        self.label_type.grid(row=1, column=0)
        self.radio_courant.grid(row=1, column=1)
        self.radio_epargne.grid(row=2, column=1)
        self.button_creer.grid(row=3, columnspan=2)
    
    def creer_compte(self):
        
        numero = self.entry_numero.get()
        type_compte = "Courant" if self.radio_var.get() == 1 else "Épargne"
        
if __name__ == "_main_":
    root = tk.Tk()
    app = InterfaceCompte(root)
    root.mainloop()