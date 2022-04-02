#!/usr/bin/env python3

# importation des bibliotheque de Python
import random
import tkinter as tk
import interface_aide_Tkinter as iat
import statistique as stat
import webbrowser
from tkinter import ttk

# Variable Global
FOND = "green"  # couleur de fond de la fenetre (constante)
largeur_carte = 44  # largeur (en pixel) d'une image de carte
hauteur_carte = 64  # hauteur (en pixel) d'une image de carte
nb_carte = 32  # corespond au nombre de carte dans le packet de jeu

fenetre = tk.Tk()  # Creation de la fenetre
fenetre.configure(background=FOND)  # Mise en couleur du fond de la fenetre
fenetre.title('Jeu de la reussite')  # titre de la fenetre
fenetre.resizable(width=False, height=False)  # empeche le plein ecran

dos = tk.PhotoImage(file='affichage/imgs/carte-dos.png')  # Generation de l'image du dos d'une carte

valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A']  # Liste de valeur de carte
couleurs = ['P', 'C', 'K', 'T']  # Liste des couleur de carte
dic_photo = {}  # Dictionnaire contenant toute les carte du jeu
for c in couleurs:  # Pour chaque couleur ...
    for v in valeurs:  # ... on associe une valeur
        photo = "affichage/imgs/carte-" + v + '-' + c + '.gif'  # On les mets dans l'adresse permetant de la trouver
        dic_photo[c, v] = tk.PhotoImage(file=photo)  # Generation des image et stockage dans le dictionnaire

v = random.choice(valeurs)
c = random.choice(couleurs)
fenetre.iconphoto(True, tk.PhotoImage(file="affichage/imgs/carte-{}-{}.gif".format(v, c)))

# Entier
comp_Can1 = 0  # Compte le nombre de carte dans le canvas 1
comp_Can2 = 0  # Compte le nombre de carte dans le canvas 2
comp_Can3 = 0  # Compte le nombre de carte dans le canvas 3
comp_Can4 = 0  # Compte le nombre de carte dans le canvas 4

# liste
liste_Canevas1 = []  # liste de carte contenu dans le Canevas1
liste_Canevas2 = []  # liste de carte contenu dans le Canevas2
liste_Canevas3 = []  # liste de carte contenu dans le Canevas3
liste_Canevas4 = []  # liste de carte contenu dans le Canevas4
list_bouton = []  # liste de dictionnaire nessaissaire a bouton ({'valeur'=…, 'couleur'=…, 'bouton'=…})

# Mode
mode = "MANUEL"

message = tk.StringVar()
message.set("Bienvenue")

###############  mise en page de la fenetre  ###############

# Widget de Texte (tkinter.Label) affichant le titre en haut de la fenetre
titre = tk.Label(fenetre, text="Réussite des alliances", font=("Ink Free", 20), bg=FOND,
                 fg="Black")  # Generation du widget
titre.grid(row=0, column=1, padx=5, pady=5)  # Affichage du widget

# Widget de Texte (tkinter.Label) affichant les message a l'utilisateur
textmessage = tk.Label(fenetre, textvariable=message, font=("Ink Free", 20), bg=FOND,
                       fg="Black")  # Generation du widget
textmessage.grid(row=6, column=1, padx=5, pady=5)  # Affichage du widget

# Zone de jeu (normalement zone de dessin: tkinter.Canvas) permettant de repartir les cartes dans la fenetre
Canevas1 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
Canevas1.grid(row=1, column=1, padx=5, pady=5)  # affichage du canvas

Canevas2 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
Canevas2.grid(row=2, column=1, padx=5, pady=5)  # affichage du canvas

Canevas3 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
Canevas3.grid(row=3, column=1, padx=5, pady=5)  # affichage du canvas

Canevas4 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
Canevas4.grid(row=4, column=1, padx=5, pady=5)  # affichage du canvas


################  Definition des fonction  #################


def carte_to_chaine(dic_carte):
    """
    Transformation en chaine de caractère de dictionnaire modification apportée pour valeurs différentes de 10,
    rajout d'un espace devant


    :param dic_carte:dict
        Dictionnaire représentation de carte, valeur et couleur

    :return
    str
        Chaine de 3 caractères représentant la carte donnée en argument
    """
    """if dic_carte['couleur'] == 'P':
        couleur = chr(9824)
    elif dic_carte['couleur'] == 'C':
        couleur = chr(9825)
    elif dic_carte['couleur'] == 'K':
        couleur = chr(9826)
    elif dic_carte['couleur'] == 'T':
        couleur = chr(9827)
    if str(dic_carte['valeur']) == '10':
        return "{}{}".format(dic_carte['valeur'], couleur)
    else:
        return " {}{}".format(dic_carte['valeur'], couleur)"""
    global comp_Can1, comp_Can2, comp_Can4, comp_Can3
    c = dic_carte['couleur']
    v = dic_carte['valeur']
    image = dic_photo[c, v]
    if comp_Can1 < nb_carte / 4:
        Button = ttk.Label(Canevas1, image=image, background=FOND)
        Button.pack(side=tk.LEFT)
        comp_Can1 += 1
    elif comp_Can2 < nb_carte / 4:
        Button = ttk.Label(Canevas2, image=image, background=FOND)
        Button.pack(side=tk.LEFT)
        comp_Can2 += 1
    elif comp_Can3 < nb_carte / 4:
        Button = ttk.Label(Canevas3, image=image, background=FOND)
        Button.pack(side=tk.LEFT)
        comp_Can3 += 1
    elif comp_Can4 < nb_carte / 4:
        Button = ttk.Label(Canevas4, image=image, background=FOND)
        Button.pack(side=tk.LEFT)
        comp_Can4 += 1


def afficher_reussite(liste_carte):
    """
    # Supprime toute les cartes puis les rafiche toute avec la modification
    """
    global comp_Can1, comp_Can2, comp_Can4, comp_Can3
    for c in Canevas1.winfo_children():
        c.destroy()
        comp_Can1 = 0
    for c in Canevas2.winfo_children():
        c.destroy()
        comp_Can2 = 0
    for c in Canevas3.winfo_children():
        c.destroy()
        comp_Can3 = 0
    for c in Canevas4.winfo_children():
        c.destroy()
        comp_Can4 = 0
    for carte in liste_carte:
        carte_to_chaine(carte)
    # sleep(0.1)


def init_pioche_fichier(fichier_carte):
    """
    Extrait les données du fichier texte transformation des cartes sous forme de plusieurs chaines de caractère en liste
    des dictionnaire

    :param fichier_carte:TextIOWrapper
        Fichier texte qui contient une suite de cartes (data_init.txt)

    :return
    list
        un liste de carte qui sont sous formes de dictionnaires
    """
    liste = []
    f = open(fichier_carte, "r")
    fichier = f.read()
    f.close()
    fichier = fichier.split(" ")
    for carte in fichier:
        carte = carte.split("-")
        liste.append({'valeur': carte[0], 'couleur': carte[1]})
    return liste


def ecrire_fichier_reussite(nom_fich, pioche):
    """
    Ecrit la liste des cartes dans le fichier

    :param nom_fich:str
        nom du fichier d'enregistrement de la pioche
    :param pioche:list
        liste de cartes

    :return
    None

    :effet de bord
    TextIOWrapper
        creation et ecriture (d'une pioche) dans un fichier
    """
    f = open(nom_fich, 'w')
    for carte in pioche:
        f.write("{}-{} ".format(carte['valeur'], carte['couleur']))
    f.close()


def init_pioche_alea(nb_carte=32):
    """
    Créer une liste de cartes en fonction du nombre de cartes demandé (32 ou 52) et mélange les cartes de façon
    aléatoire

    :param nb_carte:int
        argument optionnel (valeur par défaut = 32 / autre valeur = 52)

    :return
    list
        liste de toutes les cartes mélangés
    """
    liste_carte = []
    liste_couleur = ['C', 'K', 'P', 'T']
    if nb_carte == 32:
        liste_valeur = ['7', '8', '9', '10', 'V', 'D', 'R', 'A']
    elif nb_carte == 52:
        liste_valeur = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R']
    for couleur in liste_couleur:
        for valeur in liste_valeur:
            liste_carte.append({'valeur': valeur, 'couleur': couleur})
    afficher_reussite(liste_carte)
    random.shuffle(liste_carte)
    return liste_carte


def alliance(carte1, carte2):
    """
    Teste si deux cartes ont soit la meme valeur, soit la meme couleur

    :param carte1:dict
        premiere carte
    :param carte2:dict
        seconde carte

    :return:
    bool
        returne True si les carte on la meme valeur ou la meme couleur, False sinon
    """
    return carte1['valeur'] == carte2['valeur'] or carte1['couleur'] == carte2['couleur']


def saut_si_possible(liste_tas, num_tas):
    """
    Teste si saut possible,
        si oui : modification de la liste donnée en argument
    Teste si une modification a été effectué

    :param liste_tas:list
        liste de cartes visibles sur les tas de la réussite
    :param num_tas:int
        numéro d'une carte du tas qui se trouve entre deux cartes de meme couleur ou de meme valeur

    :return
    bool
        retour de booléen mais pas d'affichage
    """
    if num_tas < 1 or num_tas == len(liste_tas) - 1:
        return False
    if alliance(liste_tas[num_tas - 1], liste_tas[num_tas + 1]):
        del liste_tas[num_tas - 1]
        return True
    else:
        return False


def verification_possible_saut(liste_tas):
    """
    :param liste_tas:list
        liste de cartes visibles sur les tas de la réussite
    :param liste_tas:list
        Representation de la premiere carte de chaque tas present sur la table

    :return
    bool
        retour booléen true si possibilité de sauter une carte, False si non
    """
    for carte in range(len(liste_tas) - 1):
        possible = saut_si_possible(liste_tas, carte + 1)
        if possible:
            return True


def retourner_carte(liste_tas, pioche):
    """

    Suppression de la premiere carte de la liste de la pioche et ajout de cette meme carte dans la liste des tas

    :param liste_tas:list
    :param pioche:list

    :return
    None
    """
    carte = pioche[0]
    del pioche[0]
    liste_tas.append(carte)


def une_etape_reussite(liste_tas, pioche, affiche=False):
    """

    Selection de la premiere carte de la pioche, placement de cette carte dans la liste du tas de cartes et suppression de cette carte de la pioche
    Effectuer la vérification possible d'un saut
    Tant que le saut est fait,
    Affichage de la réussite à chaque des étapes (sauts et pioche)

    :param pioche:list
    :param affiche:bool

    :return
    None
    """
    # a revoir
    liste_tas.append(pioche[0])
    del pioche[0]
    if affiche:
        afficher_reussite(liste_tas)
    saut = saut_si_possible(liste_tas, len(liste_tas) - 2)
    while saut:
        if affiche:
            afficher_reussite(liste_tas)
        saut = verification_possible_saut(liste_tas)


def reussite_mode_auto(pioche, affiche=False):
    """
    :param pioche:list
    :param affiche:bool

    :return
    list

    """
    if affiche:
        afficher_reussite(pioche)
    pioche_tas = list(pioche)
    liste_tas = []
    while pioche_tas:
        une_etape_reussite(liste_tas, pioche_tas, affiche=affiche)
    return liste_tas


def saut(nb_tas, liste_tas):
    possible = saut_si_possible(liste_tas, nb_tas)
    import_proc(liste_tas)
    if not possible:
        message.set("Impossible de faire sauter ce tas")


def cree_bouton(carte, liste_carte):
    global comp_Can1, comp_Can2, comp_Can4, comp_Can3
    c = liste_carte[carte]['couleur']
    v = liste_carte[carte]['valeur']
    image = dic_photo[c, v]
    if comp_Can1 < nb_carte / 4:
        Button = tk.Button(Canevas1, image=image, background="green", command=lambda: saut(carte, liste_carte))
        Button.pack(side=tk.LEFT)
        comp_Can1 += 1
    elif comp_Can2 < nb_carte / 4:
        Button = tk.Button(Canevas2, image=image, background="green", command=lambda: saut(carte, liste_carte))
        Button.pack(side=tk.LEFT)
        comp_Can2 += 1
    elif comp_Can3 < nb_carte / 4:
        Button = tk.Button(Canevas3, image=image, background="green", command=lambda: saut(carte, liste_carte))
        Button.pack(side=tk.LEFT)
        comp_Can3 += 1
    elif comp_Can4 < nb_carte / 4:
        Button = tk.Button(Canevas4, image=image, background="green", command=lambda: saut(carte, liste_carte))
        Button.pack(side=tk.LEFT)
        comp_Can4 += 1


def import_proc(liste_carte):
    global comp_Can1, comp_Can2, comp_Can3, comp_Can4
    for c in Canevas1.winfo_children():
        c.destroy()
        comp_Can1 = 0
    for c in Canevas2.winfo_children():
        c.destroy()
        comp_Can2 = 0
    for c in Canevas3.winfo_children():
        c.destroy()
        comp_Can3 = 0
    for c in Canevas4.winfo_children():
        c.destroy()
        comp_Can4 = 0
    message.set("")
    for carte in range(len(liste_carte)):
        cree_bouton(carte, liste_carte)


def fpioche(liste_tas, pioche, bouton):
    retourner_carte(liste_tas, pioche)
    if not pioche:
        bouton.grid_forget()
    import_proc(liste_tas)
    if (not pioche) and len(liste_tas)==2:
        message.set("Felicitation")



def fTerminer(liste_tas, pioche, bPioche, bTerminer):
    for carte in pioche:
        liste_tas.append(carte)
    pioche = []
    bPioche.grid_forget()
    bTerminer.grid_forget()
    import_proc(liste_tas)
    if (not pioche) and len(liste_tas)==2:
        bTerminer.grid_forget()
    if len(liste_tas)==2:
        message.set("Felicitation")
    else:
        message.set("PERDU")


def reussite_mode_manuel(pioche, nb_tas_max=2):
    """
    :param pioche:list
    :param nb_tas_max:int

    :return
    list
    """

    # initialisation de variables
    liste_tas = []
    pioche_tas = list(pioche)
    # creation du bouton de pioche
    bPioche = tk.Button(fenetre, image=dos, bg="green", command=lambda: fpioche(liste_tas, pioche, bPioche))
    bPioche.grid(column=1, row=5)
    # Creation d'un bouton pour terminer (la partie)
    quiter = tk.PhotoImage(file="affichage/imgs/Stop.png")
    bTerminer = tk.Button(fenetre, image=quiter, bg="green",
                          command=lambda: fTerminer(liste_tas, pioche, bPioche, bTerminer))
    bTerminer.grid(column=2, row=1)
    print("Ok creation des bouton")
    #  Boucle de jeu
    while (pioche_tas or len(liste_tas) != 2) and quitter:
        quitter=False
        print("boucle")


def lance_reussite(mode, nb_cartes=32, affiche=False, nb_tas_max=2):
    """
    :param mode:str
        chaine de caractères qui représente le mode joué ('manuel' ou 'auto')

    :param nb_cartes:int


    :param affiche:bool

    :param nb_tas_max:int

    :return
    list
    """
    textmessage.config(fg="red")
    message.set("")
    pioche = []
    pioche = init_pioche_alea(nb_cartes)
    if mode == 'auto':
        liste_tas = reussite_mode_auto(pioche, affiche)
    elif mode == 'manuel':
        liste_tas = reussite_mode_manuel(pioche, nb_tas_max)
    return liste_tas


##############  Creation de la barre de menu  ###############

menu_bar = tk.Menu(fenetre)  # Creation de la barre de menu

mode_menu = tk.Menu(menu_bar, tearoff=0)  # Creation d'un sous-menu dans la barre de menu
mode_menu.add_command(label="Manuel",
                      command=lambda: lance_reussite('manuel'))  # Ajout d'une commande dans le sous-menu precedent
mode_menu.add_command(label="Automatique", command=lambda: lance_reussite('auto',
                                                                          affiche=True))  # Ajout d'une seconde commande dans le sous-menu precedent

help_menu = tk.Menu(menu_bar, tearoff=0)  # Creation d'un second sous-menu dans la barre de menu
help_menu.add_command(label="regle", command=lambda: webbrowser.open(
    "https://projetinfomi3-bin08.wixsite.com/reussite_alliances-1/post/la-r%C3%A9ussite-des-alliances"))  # Ajout d'une commande dans le sous-menu precedent
help_menu.add_command(label="aide", command=iat.aide)  # Ajout d'une seconde commande dans le sous-menu precedent

menu_bar.add_cascade(label="Mode de jeu", menu=mode_menu)  # Ajout d'un sous menu en cascade dans la barre de menu
menu_bar.add_cascade(label="help", menu=help_menu)  # Ajout d'un sous menu en cascade dans la barre de menu
menu_bar.add_command(label="Statistiques", command=stat.conf_stat)
menu_bar.add_command(label="Quitter", command=fenetre.destroy)  # Ajout d'une commande dans la barre de menu

fenetre.config(menu=menu_bar)  # affichage de la barre de menu a l'ecran

if __name__ == "__main__":
    fenetre.mainloop()
