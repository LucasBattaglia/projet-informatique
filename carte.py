import random
import shutil

def carte_to_chaine(dic_carte):
    if dic_carte['couleur']=='P':
        couleur = chr(9824)
    elif dic_carte['couleur']=='C':
        couleur = chr(9825)
    elif dic_carte['couleur']=='K':
        couleur = chr(9826)
    elif dic_carte['couleur']=='T':
        couleur = chr(9827)
    if str(dic_carte['valeur'])=='10':
        return "{}{}".format(dic_carte['valeur'],couleur)
    else:
        return " {}{}".format(dic_carte['valeur'],couleur)


def afficher_reussite(liste_carte):
    for carte in liste_carte:
        print(carte_to_chaine(carte), end=" ")
    print("\n")


def init_pioche_fichier(fichier_carte):
    liste = []
    f = open(fichier_carte, "r")
    fichier = f.read()
    f.close()
    fichier = fichier.split(" ")
    for carte in fichier:
        carte = carte.split("-")
        liste.append({'valeur':carte[0], 'couleur':carte[1]})
    return liste


def ecrire_fichier_reussite(nom_fich, liste_carte):
    f = open(nom_fich, 'w')
    for carte in liste_carte:
        f.write("{}-{} ".format(carte['valeur'], carte['couleur']))
    f.close()


def init_pioche_alea(nb_carte=32):
    if nb_carte == 32:
        liste_carte = [{'valeur': '7', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'C'},
                       {'valeur': '9', 'couleur': 'C'}, {'valeur': '10', 'couleur': 'C'},
                       {'valeur': 'V', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'C'},
                       {'valeur': 'R', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'C'},
                       {'valeur': '7', 'couleur': 'K'}, {'valeur': '8', 'couleur': 'K'},
                       {'valeur': '9', 'couleur': 'K'}, {'valeur': '10', 'couleur': 'K'},
                       {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'K'},
                       {'valeur': 'R', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'K'},
                       {'valeur': '7', 'couleur': 'P'}, {'valeur': '8', 'couleur': 'P'},
                       {'valeur': '9', 'couleur': 'P'}, {'valeur': '10', 'couleur': 'P'},
                       {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'D', 'couleur': 'P'},
                       {'valeur': 'R', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'P'},
                       {'valeur': '7', 'couleur': 'T'}, {'valeur': '8', 'couleur': 'T'},
                       {'valeur': '9', 'couleur': 'T'}, {'valeur': '10', 'couleur': 'T'},
                       {'valeur': 'V', 'couleur': 'T'}, {'valeur': 'D', 'couleur': 'T'},
                       {'valeur': 'R', 'couleur': 'T'}, {'valeur': 'A', 'couleur': 'T'}]
    elif nb_carte == 52:
        liste_carte = [{'valeur': '2', 'couleur': 'C'}, {'valeur': '3', 'couleur': 'C'},
                       {'valeur': '4', 'couleur': 'C'}, {'valeur': '5', 'couleur': 'C'},
                       {'valeur': '6', 'couleur': 'C'}, {'valeur': '7', 'couleur': 'C'},
                       {'valeur': '7', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'C'},
                       {'valeur': '9', 'couleur': 'C'}, {'valeur': '10', 'couleur': 'C'},
                       {'valeur': 'V', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'C'},
                       {'valeur': 'R', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'C'},
                       {'valeur': '2', 'couleur': 'K'}, {'valeur': '3', 'couleur': 'K'},
                       {'valeur': '4', 'couleur': 'K'}, {'valeur': '5', 'couleur': 'K'},
                       {'valeur': '6', 'couleur': 'K'}, {'valeur': '7', 'couleur': 'K'},
                       {'valeur': '7', 'couleur': 'K'}, {'valeur': '8', 'couleur': 'K'},
                       {'valeur': '9', 'couleur': 'K'}, {'valeur': '10', 'couleur': 'K'},
                       {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'K'},
                       {'valeur': 'R', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'K'},
                       {'valeur': '2', 'couleur': 'P'}, {'valeur': '3', 'couleur': 'P'},
                       {'valeur': '4', 'couleur': 'P'}, {'valeur': '5', 'couleur': 'P'},
                       {'valeur': '6', 'couleur': 'P'}, {'valeur': '7', 'couleur': 'P'},
                       {'valeur': '7', 'couleur': 'P'}, {'valeur': '8', 'couleur': 'P'},
                       {'valeur': '9', 'couleur': 'P'}, {'valeur': '10', 'couleur': 'P'},
                       {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'D', 'couleur': 'P'},
                       {'valeur': 'R', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'P'},
                       {'valeur': '2', 'couleur': 'T'}, {'valeur': '3', 'couleur': 'T'},
                       {'valeur': '4', 'couleur': 'T'}, {'valeur': '5', 'couleur': 'T'},
                       {'valeur': '6', 'couleur': 'T'}, {'valeur': '7', 'couleur': 'T'},
                       {'valeur': '7', 'couleur': 'T'}, {'valeur': '8', 'couleur': 'T'},
                       {'valeur': '9', 'couleur': 'T'}, {'valeur': '10', 'couleur': 'T'},
                       {'valeur': 'V', 'couleur': 'T'}, {'valeur': 'D', 'couleur': 'T'},
                       {'valeur': 'R', 'couleur': 'T'}, {'valeur': 'A', 'couleur': 'T'}]
    random.shuffle(liste_carte)
    return liste_carte


def alliance(carte1, carte2):
    if carte1['valeur']==carte2['valeur'] or carte1['couleur']==carte2['couleur']:
        return True
    else:
        return False


def saut_si_possible(liste_tas, num_tas):
    if num_tas<1 or num_tas==len(liste_tas)-1:
        return False
    carte1 = liste_tas[num_tas - 1]
    carte2 = liste_tas[num_tas + 1]
    if alliance(carte1, carte2):
        del liste_tas[num_tas-1]
        return True
    else:
        return False


def verification_possible_saut(liste_tas):
    for carte in range(len(liste_tas) - 1):
        possible = saut_si_possible(liste_tas, carte + 1)
        if possible:
            return True


def retourner_carte(liste_tas, pioche):
    carte = pioche[0]
    del pioche[0]
    liste_tas.append(carte)

def une_etape_reussite(liste_tas, pioche, affiche=False):
    ### a revoir ###
    if affiche:
        afficher_reussite(liste_tas)
    saut = saut_si_possible(liste_tas, len(liste_tas)-2)
    while saut:
        saut = False
        if affiche:
            afficher_reussite(liste_tas)
        saut = verification_possible_saut(liste_tas)

def reussite_mode_auto(pioche, affiche=False):
    if affiche:
        afficher_reussite(pioche)
    pioche_tas = list(pioche)
    liste_tas = []
    while pioche_tas!=[]:
        une_etape_reussite(liste_tas, pioche_tas, affiche=affiche)
    return liste_tas


def reussite_mode_manuel(pioche, nb_as_max=2):
    ### definition des donnee ###
    #liste
    liste_tas = []
    pioche_tas = list(pioche)

    ### Programme de la fonction ###
    while pioche_tas!=[]:
        action = input("\n\n#######################################################\nRetourner une carte (taper 1)\nSaisir un saut (taper2)\nQuiter (taper Q)\n#######################################################\n\n\n")
        if action == '1':
            retourner_carte(liste_tas, pioche_tas)
        elif action == '2':
            print(" 0   1   2   3   4   5  ...")
            afficher_reussite(liste_tas)
            num = int(input("Quel tas voulez-vous faire sauter (entrer un numero, on commence par 0): "))
            possible = saut_si_possible(liste_tas, num)
            if not possible:
                print('Impossible de faire sauter le tas numero {}'.format(num))
        elif action == 'Q':
            for carte in pioche_tas:
                liste_tas.append(carte)
            pioche_tas=[]
        afficher_reussite(liste_tas)
    if len(liste_tas)<=2:
        print("Gagner")
    else:
        print("Perdu")

#afficher_reussite([{'valeur':7, 'couleur':'P'},{'valeur':10, 'couleur':'K'},{'valeur':'A', 'couleur':'T'}])
#print(init_pioche_fichier("data_init.txt"))
#ecrire_fichier_reussite('teste.txt', [{'valeur': 'V', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'P'},
#                                      {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'C'},
#                                      {'valeur': '10', 'couleur': 'P'}, {'valeur': '8', 'couleur': 'T'},
#                                      {'valeur': '8', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'T'},
#                                      {'valeur': 'V', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'P'},
#                                      {'valeur': '10', 'couleur': 'K'}, {'valeur': '9', 'couleur': 'P'},
#                                      {'valeur': '7', 'couleur': 'T'}, {'valeur': 'R', 'couleur': 'T'},
#                                      {'valeur': '10', 'couleur': 'C'}, {'valeur': '9', 'couleur': 'K'},
#                                      {'valeur': '9', 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'T'},
#                                      {'valeur': 'R', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'C'},
#                                      {'valeur': 'D', 'couleur': 'K'}, {'valeur': '7', 'couleur': 'C'},
#                                      {'valeur': 'A', 'couleur': 'T'}, {'valeur': '7', 'couleur': 'P'},
#                                      {'valeur': 'V', 'couleur': 'T'}, {'valeur': '7', 'couleur': 'K'},
#                                      {'valeur': 'D', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'K'},
#                                      {'valeur': 'D', 'couleur': 'P'}, {'valeur': '10', 'couleur': 'T'},
#                                      {'valeur': 'R', 'couleur': 'K'}, {'valeur': 'R', 'couleur': 'P'}])
pioche = init_pioche_alea()
#print(alliance({'valeur': '7', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'K'}))
#liste = [{'valeur': '7', 'couleur': 'K'}, {'valeur': '8', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'K'}]
#print(liste)
#print(saut_si_possible(liste, 1))
#print(liste)
#une_etape_reussite(liste, pioche, affiche=True)
#afficher_reussite(reussite_mode_auto(pioche, affiche=True))
reussite_mode_manuel(pioche)