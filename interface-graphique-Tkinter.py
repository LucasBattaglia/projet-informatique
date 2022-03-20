import tkinter as tk
import carte
import interface_aide_Tkinter as iat
import statistique as stat
import webbrowser
import random

#####################################################################################
#############################   Creation des fonction    ############################
#####################################################################################


def auto():
    print("Ok")
    print("liste_bouton : {} --> {}\n\nsauv_pioche : {} --> {}\n\n can1 : {} --> {} / {}\n\ncan2 : {} --> {} / {}\n\ncan3 : {} --> {} / {}\n\n can4: {} --> {} / {}".format(list_bouton, len(list_bouton), sauv_pioche, len(sauv_pioche), liste_Canevas1, len(liste_Canevas1), comp_Can1, liste_Canevas2, len(liste_Canevas2), comp_Can2, liste_Canevas3, len(liste_Canevas3), comp_Can3, liste_Canevas4, len(liste_Canevas4), comp_Can4))


def modif_list_bouton(dictionnaire):
    # On mets a jour le bouton dans la liste general des canvas
    for i in range(len(list_bouton)):
        if list_bouton[i]['couleur'] == dictionnaire['couleur'] and list_bouton[i]['valeur'] == dictionnaire['valeur']:
            print(list_bouton[i])
            list_bouton[i]['bouton'] = bouton
            print(list_bouton[i])


def ChangeCan():
    global comp_Can1, comp_Can2, comp_Can3, comp_Can4, bouton
    print("changecan")
    print("can1 : {}\ncan2 : {}\ncan3 : {}\nnb_carte/4 : {}".format(comp_Can1, comp_Can2, comp_Can3, nb_carte / 4))

    # Initialisation du dictionnaire correspondant a 1 bouton (couleur, valeur, canvas, widget)
    dictionnaire = {}

    print(len(liste_Canevas1))
    print(len(liste_Canevas2))

    # On verifie que les canvas on bien le bon nombre de bouton (le nombre de carte total diviser par 4)
    # et on repart si c'est pas le cas
    if comp_Can1 < nb_carte / 4 and len(liste_Canevas2) > 0:
        print("canvas2-->1")
        image = dic_photo[liste_Canevas2[0]['couleur'], liste_Canevas2[0]['valeur']]  # On recupere l'image a afficher
        dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire["Can"] = liste_Canevas2[0]['couleur'], liste_Canevas2[0]['valeur'], "Can1"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
        bouton = tk.Button(Canevas1, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # On cree le bouton
        dictionnaire['bouton'] = bouton  # On ajoute le bouton au dictionnaire
        dictionnaire['bouton'].pack(side=tk.LEFT)  # On affiche le bouton dans le bon canvas
        liste_Canevas2[0]['bouton'].pack_forget()  # On efface le bouton de l'ancien canvas
        print(dictionnaire)
        liste_Canevas1.append(dictionnaire)  # On ajoute le bouton dans la liste du bon canvas
        del liste_Canevas2[0]  # On efface le bouton de la liste de l'ancien canvas
        comp_Can1 += 1  # On ajoute une carte au nouveau canvas
        comp_Can2 -= 1  # On en supprime une dans l'ancien canvas
        modif_list_bouton(dictionnaire)

    print(len(liste_Canevas3))

    if comp_Can2 < nb_carte / 4 and len(liste_Canevas3) > 0:
        print("canvas3-->2")
        image = dic_photo[liste_Canevas3[0]['couleur'], liste_Canevas3[0]['valeur']]  # On recupere l'image a afficher
        dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire["Can"] = liste_Canevas3[0]['couleur'], liste_Canevas3[0]['valeur'], "Can2"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
        bouton = tk.Button(Canevas2, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # On cree le bouton
        dictionnaire['bouton'] = bouton  # On ajoute le bouton au dictionnaire
        dictionnaire['bouton'].pack(side=tk.LEFT)  # On affiche le bouton dans le bon canvas
        liste_Canevas3[0]['bouton'].pack_forget()  # On efface le bouton de l'ancien canvas
        liste_Canevas2.append(dictionnaire)  # On ajoute le bouton dans la liste du bon canvas
        del liste_Canevas3[0]  # On efface le bouton de la liste de l'ancien canvas
        comp_Can2 += 1  # On ajoute une carte au nouveau canvas
        comp_Can3 -= 1  # On en supprime une dans l'ancien canvas
        modif_list_bouton(dictionnaire)

    print(len(liste_Canevas4))

    if comp_Can3 < nb_carte / 4 and len(liste_Canevas4) > 0:
        print("canvas4-->3")
        image = dic_photo[liste_Canevas4[0]['couleur'], liste_Canevas4[0]['valeur']]  # On recupere l'image a afficher
        dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire["Can"] = liste_Canevas4[0]['couleur'], liste_Canevas4[0]['valeur'], "Can3"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
        bouton = tk.Button(Canevas3, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # On cree le bouton
        dictionnaire['bouton'] = bouton  # On ajoute le bouton au dictionnaire
        dictionnaire['bouton'].pack(side=tk.LEFT)  # On affiche le bouton dans le bon canvas
        liste_Canevas4[0]['bouton'].pack_forget()  # On efface le bouton de l'ancien canvas
        liste_Canevas3.append(dictionnaire)  # On ajoute le bouton dans la liste du bon canvas
        del liste_Canevas4[0]  # On efface le bouton de la liste de l'ancien canvas
        comp_Can3 += 1  # On ajoute une carte au nouveau canvas
        comp_Can4 -= 1  # On en supprime une dans l'ancien canvas
        modif_list_bouton(dictionnaire)

    #else:
     #   image = dic_photo[liste_Canevas4[0]['couleur'], liste_Canevas4[0]['valeur']]  # On recupere l'image a afficher
      #  dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire["Can"] = liste_Canevas4[0]['couleur'], liste_Canevas4[0]['valeur'], "Can3"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
       # bouton = tk.Button(Canevas4, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # On cree le bouton
        #dictionnaire['bouton'] = bouton  # On ajoute le bouton au dictionnaire




def supr_list_can(canvas, couleur, valeur):
    global liste_Canevas1, liste_Canevas2, liste_Canevas3, liste_Canevas4

    # On enleve la carte supprimer de la liste du canvas associer
    # 1) Selection du canvas associer
    # 2) parcourt de la liste du canvas
    # 3) verification que se soit bien notre carte
    # 4) Suppression de la carte (si c'est la bonne
    if canvas == "Can1":
        for i in range(len(liste_Canevas1) - 1):
            if liste_Canevas1[i]['couleur'] == couleur and liste_Canevas1[i]['valeur'] == valeur:
                del liste_Canevas1[i]

    elif canvas == "Can2":
        for i in range(len(liste_Canevas2) - 1):
            if liste_Canevas2[i]['couleur'] == couleur and liste_Canevas2[i]['valeur'] == valeur:
                del liste_Canevas2[i]

    elif canvas == "Can3":
        for i in range(len(liste_Canevas3) - 1):
            if liste_Canevas3[i]['couleur'] == couleur and liste_Canevas3[i]['valeur'] == valeur:
                del liste_Canevas3[i]

    elif canvas == "Can4":
        for i in range(len(liste_Canevas4) - 1):
            if liste_Canevas4[i]['couleur'] == couleur and liste_Canevas4[i]['valeur'] == valeur:
                del liste_Canevas4[i]


def Saut(couleur, valeur):
    global tas, comp_Can3, comp_Can1, comp_Can2, comp_Can4
    print("saut {}-{}".format(valeur, couleur))

    # recherche du bouton a supprimmer
    for i in range(len(list_bouton)):
        if list_bouton[i]['couleur'] == couleur and list_bouton[i]['valeur'] == valeur:
            tas = i - 1  # On enleve 1 car on veut suprimer la carte precedent la carte appuyer
    print(len(list_bouton), tas)

    # preparation suppresion des listes
    print("supre {}-{}".format(list_bouton[tas]['couleur'], list_bouton[tas]['valeur']))
    list_bouton[tas]['bouton'].pack_forget()  # On cache le canevas

    if list_bouton[tas]['can'] == "Can1":
        comp_Can1 -= 1  # On decremente le canevas contenant la carte
        print("can 1 : {}".format(comp_Can1))

    elif list_bouton[tas]['can'] == "Can2":
        comp_Can2 -= 1  # On decremente le canevas contenant la carte
        print("can 2 : {}".format(comp_Can2))

    elif list_bouton[tas]['can'] == "Can3":
        comp_Can3 -= 1  # On decremente le canevas contenant la carte
        print("can 3 : {}".format(comp_Can3))

    elif list_bouton[tas]['can'] == "Can4":
        comp_Can4 -= 1
        print("can 4 : {}".format(comp_Can4))

    # on supprime le bouton
    # 1) De la liste du canvas
    supr_list_can(list_bouton[tas]['can'], list_bouton[tas]['couleur'], list_bouton[tas]['valeur'])
    # 2) de la liste general des bouton
    del list_bouton[tas]
    print(len(list_bouton))

    #  on verifie que l'on est pas besoin de passer une carte du canvas 2 a 1, etc
    ChangeCan()


def new_carte(Bpioche):
    """
    affiche a chaque appel un nouvelle carte, si tout les carte sont poser supprime le bouton pioche

    :param Bpioche: Widget TKINTER
        correspond a au bouon pioche permets de le supprimer
    :return:
    None

    :effet de bord
        appelle de la fonction Saut
    """
    global comp_Can1, comp_Can2, comp_Can3, comp_Can4, liste_Canevas1, liste_Canevas2, liste_Canevas3, liste_Canevas4, list_bouton

    # On recupere l'image que l'on va afficher sur le bouton
    image = dic_photo[pioche[0]['couleur'], pioche[0]['valeur']]

    # Initialisation du dictionnaire correspondant a 1 bouton (couleur, valeur, canvas, widget)
    dictionnaire = {}

    print("can1 : {}\ncan2 : {}\ncan3 : {}\nnb_carte/4 : {}".format(comp_Can1, comp_Can2, comp_Can3, nb_carte / 4))

    #repartition des carte dans les canvas et affichage
    # (Quand toute les cartes sont afficher elle sont repartie equitablement dans 4 canvas)
    if comp_Can1 < nb_carte / 4:
        comp_Can1 += 1  # On ajoute une carte au canvas 1
        print(pioche[0]['couleur'], pioche[0]['valeur'])
        dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire['can'] = pioche[0]['couleur'], pioche[0]['valeur'], "Can1"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
        button = tk.Button(Canevas1, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # creation du bouton (ATTENTION appel au dictionnaire precedent)
        dictionnaire['bouton'] = button  # On ajoute le bouton au dictionnaire (qui correspond a 1 bouton)
        dictionnaire['bouton'].pack(side=tk.LEFT)  # On affiche le bouton grace a la methode .pack()
        list_bouton.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton general
        liste_Canevas1.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton du canvas ou il est afficher

    elif comp_Can2 < nb_carte / 4:
        comp_Can2 += 1  # On ajoute une carte au canvas 2
        print(pioche[0]['couleur'], pioche[0]['valeur'])
        dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire["can"] = pioche[0]['couleur'], pioche[0]['valeur'], "Can2"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
        button = tk.Button(Canevas2, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # creation du bouton (ATTENTION appel au dictionnaire precedent)
        dictionnaire['bouton'] = button  # On ajoute le bouton au dictionnaire (qui correspond a 1 bouton)
        dictionnaire['bouton'].pack(side=tk.LEFT)  # On affiche le bouton grace a la methode .pack()
        list_bouton.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton general
        liste_Canevas2.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton du canvas ou il est afficher

    elif comp_Can3 < nb_carte / 4:
        comp_Can3 += 1  # On ajoute une carte au canvas 3
        print(pioche[0]['couleur'], pioche[0]['valeur'])
        dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire['can'] = pioche[0]['couleur'], pioche[0]['valeur'], "Can3"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
        button = tk.Button(Canevas3, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # creation du bouton (ATTENTION appel au dictionnaire precedent)
        dictionnaire['bouton'] = button  # On ajoute le bouton au dictionnaire (qui correspond a 1 bouton)
        dictionnaire['bouton'].pack(side=tk.LEFT)  # On affiche le bouton grace a la methode .pack()
        list_bouton.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton general
        liste_Canevas3.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton du canvas ou il est afficher

    else:
        comp_Can4 += 1
        print(pioche[0]['couleur'], pioche[0]['valeur'])
        dictionnaire['couleur'], dictionnaire['valeur'], dictionnaire['can'] = pioche[0]['couleur'], pioche[0]['valeur'], "Can4"  # On mets les premiere valeur dans le dictionnaire (qui correspond a 1 bouton)
        button = tk.Button(Canevas4, image=image, bg=FOND, command=lambda: Saut(dictionnaire['couleur'], dictionnaire['valeur']))  # creation du bouton (ATTENTION appel au dictionnaire precedent)
        dictionnaire['bouton'] = button  # On ajoute le bouton au dictionnaire (qui correspond a 1 bouton)
        dictionnaire['bouton'].pack(side=tk.LEFT)  # On affiche le bouton grace a la methode .pack()
        list_bouton.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton general
        liste_Canevas4.append(dictionnaire)  # On ajoute le dictionnaire a la liste des bouton du canvas ou il est afficher

    # puisque on a cree le bouton on le suprimme de la pioche
    del pioche[0]

    # Si on n'a plus de carte dans la pioche on supprime le bouton correspondant a la pioche
    if not pioche:
        Bpioche.grid_forget()  # cacher le bouton de la pioche
        print("---- Plus de care dans la pioche ---- {}".format(len(list_bouton)))


def manuel():
    """
    Cree un bouton pioche

    :return:
    None

    :effet de bord
        appelle de la fonction new_carte
    """
    if pioche:
        Bpioche = tk.Button(fenetre, image=dos, bg=FOND, activebackground='blue', relief=tk.GROOVE, activeforeground='yellow', command=lambda: new_carte(Bpioche))  # Creation du bouton pour la pioche
        Bpioche.grid(row=5, column=1, padx=5, pady=5)  # affichage du bouton de la pioche

#####################################################################################
#############################   Programme principale    #############################
#####################################################################################


if __name__ == "__main__":

    ############################   Creation de la fenetre    ############################

    FOND = "green"  # couleur de fond de la fenetre (constante)
    largeur_carte = 44  # largeur (en pixel) d'une image de carte
    hauteur_carte = 64  # hauteur (en pixel) d'une image de carte
    nb_carte = 32  # corespond au nombre de carte dans le packet de jeu

    fenetre = tk.Tk()  # Creation de la fenetre
    fenetre.configure(background=FOND)  # Mise en couleur du fond de la fenetre
    fenetre.title('Jeu de la reussite')  # titre de la fenetre
    fenetre.resizable(width=False, height=False)  # empeche le plein ecran

    ######################  Generation des image pour les cartes  ######################

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
    fenetre.iconphoto(True, tk.PhotoImage(file="affichage/imgs/carte-{}-{}.gif".format(v,c)))

    ###############  Generation d'une pioche aleatoire  ###############
    pioche = carte.init_pioche_alea(nb_carte=nb_carte)  # appelle de la fonction init_pioche_alea du fichier carte
    sauv_pioche = list(pioche)  # Creation d'une deuxieme liste pour sauvegarder le pioche
    carte.afficher_reussite(pioche)  # affichage de la pioche
    carte.afficher_reussite(sauv_pioche)  # affichage de la sauvegarde

    ###############  Varialble  ###############

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

    ###############  mise en page de la fenetre  ###############

    # Widget de Texte (tkinter.Label) affichant le titre en haut de la fenetre
    titre = tk.Label(fenetre, text="Réussite des alliances", font=("Ink Free", 20), bg=FOND, fg="Black")  # Generation du widget
    titre.grid(row=0, column=1, padx=5, pady=5)  # Affichage du widget

    # Menu de la fenetre (tkinter.Menu) tout en haut
    menu_bar = tk.Menu(fenetre)  # Creation de la barre de menu

    mode_menu = tk.Menu(menu_bar, tearoff=0)  # Creation d'un sous-menu dans la barre de menu
    mode_menu.add_command(label="Manuel", command=lambda: manuel())  # Ajout d'une commande dans le sous-menu precedent
    mode_menu.add_command(label="Automatique", command=auto)  # Ajout d'une seconde commande dans le sous-menu precedent

    help_menu = tk.Menu(menu_bar, tearoff=0)  # Creation d'un second sous-menu dans la barre de menu
    help_menu.add_command(label="regle", command=lambda: webbrowser.open("https://projetinfomi3-bin08.wixsite.com/reussite_alliances-1/post/la-r%C3%A9ussite-des-alliances"))  # Ajout d'une commande dans le sous-menu precedent
    help_menu.add_command(label="aide", command=iat.aide)  # Ajout d'une seconde commande dans le sous-menu precedent

    menu_bar.add_cascade(label="Mode de jeu", menu=mode_menu)  # Ajout d'un sous menu en cascade dans la barre de menu
    menu_bar.add_cascade(label="help", menu=help_menu)  # Ajout d'un sous menu en cascade dans la barre de menu
    menu_bar.add_command(label="Statistique", command= stat.conf_stat)
    menu_bar.add_command(label="Quitter", command=fenetre.destroy)  # Ajout d'une commande dans la barre de menu

    fenetre.config(menu=menu_bar)  # affichage de la barre de menu a l'ecran

    # Zone de jeu (normalement zone de dessin: tkinter.Canvas) permettant de repartir les cartes dans la fenetre
    Canevas1 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
    Canevas1.grid(row=1, column=1, padx=5, pady=5)  # affichage du canvas

    Canevas2 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
    Canevas2.grid(row=2, column=1, padx=5, pady=5)  # affichage du canvas

    Canevas3 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
    Canevas3.grid(row=3, column=1, padx=5, pady=5)  # affichage du canvas

    Canevas4 = tk.Canvas(fenetre, bg=FOND, height=hauteur_carte, highlightthickness=0)  # Creation d'un Canvas
    Canevas4.grid(row=4, column=1, padx=5, pady=5)  # affichage du canvas

    fenetre.mainloop()  # Affichage de la fenetre
