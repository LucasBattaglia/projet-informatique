import tkinter as tk

#####################################################################################
############################   Creation de la fenetre    ############################
#####################################################################################

FOND = "green"
largeur_carte = 44
hauteur_carte = 64

fenetre = tk.Tk()
fenetre.configure(background=FOND)
fenetre.title('Othelo')


#####################################################################################
#############################   Creation des fonction    ############################
#####################################################################################

def quitter():
    fenetre.destroy()


def auto():
    print("Ok")


def new_carte():
    print("new carte")


def manuel():
    dos = tk.PhotoImage(file='affichage/imgs/carte-dos.png')
    pioche = tk.Button(fenetre, image=dos, bg=FOND, command=new_carte)
    pioche.grid(row=4, column=1, padx=5, pady=5)


#####################################################################################
#############################   Programme principale    #############################
#####################################################################################

titre = tk.Label(fenetre, text="Réussite des alliances", font=("Ink Free", 20), bg=FOND, fg="Black")
titre.grid(row=0, column=1, padx=5, pady=5)

menu_bar = tk.Menu(fenetre)

mode_menu = tk.Menu(menu_bar, tearoff=0)
mode_menu.add_command(label="Manuel", command=manuel)
mode_menu.add_command(label="Automatique", command=auto)

menu_bar.add_cascade(label="Mode de jeu", menu=mode_menu)
menu_bar.add_command(label="Quitter", command=quitter)

fenetre.config(menu=menu_bar)

Canevas1 = tk.Canvas(fenetre, bg=FOND, width=(largeur_carte + 5) * 13, height=hauteur_carte, highlightthickness=0)
Canevas1.grid(row=1, column=1, padx=5, pady=5)

Canevas2 = tk.Canvas(fenetre, bg=FOND, width=(largeur_carte + 5) * 13, height=hauteur_carte, highlightthickness=0)
Canevas2.grid(row=2, column=1, padx=5, pady=5)

Canevas3 = tk.Canvas(fenetre, bg=FOND, width=(largeur_carte + 5) * 13, height=hauteur_carte, highlightthickness=0)
Canevas3.grid(row=3, column=1, padx=5, pady=5)

Canevas4 = tk.Canvas(fenetre, bg=FOND, width=(largeur_carte + 5) * 13, height=hauteur_carte, highlightthickness=0)
Canevas4.grid(row=4, column=1, padx=5, pady=5)

fenetre.mainloop()
