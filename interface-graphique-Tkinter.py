import tkinter as tk
import carte

#####################################################################################
############################   Creation de la fenetre    ############################
#####################################################################################

FOND = "green"
largeur_carte = 44
hauteur_carte = 64

fenetre = tk.Tk()
fenetre.configure(background=FOND)
fenetre.title('Othelo')

####################################################################################
######################  Generation des image pour les cartes  ######################
####################################################################################

dos = tk.PhotoImage(file='affichage/imgs/carte-dos.png')

valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A']
couleurs = ['P', 'C', 'K', 'T']
dic_photo = {}
for c in couleurs:
    for v in valeurs:
        fichier = "affichage/imgs/carte-" + v + '-' + c + '.gif'
        dic_photo[c, v] = tk.PhotoImage(file=fichier)

# __________________________________________________________________________________________________________________#
pioche = carte.init_pioche_alea()
sauv_pioche = list(pioche)

carte.afficher_reussite(pioche)
carte.afficher_reussite(sauv_pioche)


# __________________________________________________________________________________________________________________#


#####################################################################################
#############################   Creation des fonction    ############################
#####################################################################################

def quitter():
    fenetre.destroy()


def auto():
    print("Ok")


def Saut(couleur, valeur):
    print('Saut {} {}'.format(couleur, valeur))
    print('sauv_piche=',sauv_pioche)
    global tas
    print('avant', len(sauv_pioche))
    for i in range(len(sauv_pioche)):
        print('for')
        if sauv_pioche[i] == {'couleur': couleur, 'valeur': valeur}:
            print('if')
            tas = i
    print(tas)
    print(sauv_pioche[tas - 3], sauv_pioche[tas - 2], sauv_pioche[tas - 1])
    print(carte.saut_si_possible(sauv_pioche, tas - 2))


def new_carte(Bpioche):
    global comp_carte, liste_Canevas1, liste_Canevas2, liste_Canevas3, liste_Canevas4
    image = dic_photo[pioche[0]['couleur'], pioche[0]['valeur']]
    comp_carte += 1
    print(comp_carte)
    if comp_carte <= nb_carte / 4:
        button = tk.Button(Canevas1, image=image, bg=FOND,
                           command=lambda: Saut(sauv_pioche[comp_carte-1]['couleur'], sauv_pioche[comp_carte-1]['valeur'])).pack(
            side=tk.LEFT)
        liste_Canevas1.append(pioche[0])
    elif comp_carte <= 2 * (nb_carte / 4):
        button = tk.Button(Canevas2, image=image, bg=FOND,
                           command=lambda: Saut(sauv_pioche[comp_carte-1]['couleur'], sauv_pioche[comp_carte-1]['valeur'])).pack(
            side=tk.LEFT)
        liste_Canevas2.append(pioche[0])
    elif comp_carte <= 3 * (nb_carte / 4):
        tk.Button(Canevas3, image=image, bg=FOND, command=lambda: Saut(sauv_pioche[comp_carte-1]['couleur'], sauv_pioche[comp_carte-1]['valeur'])).pack(
            side=tk.LEFT)
        liste_Canevas3.append(pioche[0])
    else:
        tk.Button(Canevas4, image=image, bg=FOND, command=lambda: Saut(sauv_pioche[comp_carte-1]['couleur'], sauv_pioche[comp_carte-1]['valeur'])).pack(
            side=tk.LEFT)
        liste_Canevas4.append(pioche[0])
    del pioche[0]
    if not pioche:
        Bpioche.grid_forget()


def manuel():
    Bpioche = tk.Button(fenetre, image=dos, bg=FOND, activebackground='blue', relief=tk.GROOVE, activeforeground='yellow',
                        command=lambda: new_carte(Bpioche))
    Bpioche.grid(row=5, column=1, padx=5, pady=5)


#####################################################################################
#############################   Programme principale    #############################
#####################################################################################

if __name__ == "__main__":
    ###############  Varialble  ###############
    comp_carte = 0
    nb_carte = 32
    liste_Canevas1 = []
    liste_Canevas2 = []
    liste_Canevas3 = []
    liste_Canevas4 = []

    titre = tk.Label(fenetre, text="Réussite des alliances", font=("Ink Free", 20), bg=FOND, fg="Black")
    titre.grid(row=0, column=1, padx=5, pady=5)

    menu_bar = tk.Menu(fenetre)

    mode_menu = tk.Menu(menu_bar, tearoff=0)
    mode_menu.add_command(label="Manuel", command=lambda: manuel())
    mode_menu.add_command(label="Automatique", command=auto)

    menu_bar.add_cascade(label="Mode de jeu", menu=mode_menu)
    menu_bar.add_command(label="Quitter", command=quitter)

    fenetre.config(menu=menu_bar)

    Canevas1 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)
    Canevas1.grid(row=1, column=1, padx=5, pady=5)

    Canevas2 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)
    Canevas2.grid(row=2, column=1, padx=5, pady=5)

    Canevas3 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)
    Canevas3.grid(row=3, column=1, padx=5, pady=5)

    Canevas4 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)
    Canevas4.grid(row=4, column=1, padx=5, pady=5)

    fenetre.mainloop()
