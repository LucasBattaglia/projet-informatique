#!/usr/bin/env python3

# importation des bibliotheque de Python
import random
from time import *


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
    if dic_carte['couleur'] == 'P':
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
        return " {}{}".format(dic_carte['valeur'], couleur)


def afficher_reussite(liste_carte):
    """
    Afficher la suite de carte contenu dans la liste en chaine de caractère séparation par des espaces

    :param liste_carte:list
        Liste de dictionnaires, correspondant à plusieurs cartes

    :return
    None

    :effet de bord
    str
        représentant la suite des cartes donnée en argument
    """
    for carte in liste_carte:
        print(carte_to_chaine(carte), end=" ")
    print("\n")


def init_pioche_fichier(fichier_carte):
    """
    Extrait les données du fichier texte transformation des cartes sous forme de plusieurs
    chaines de caractère en liste des dictionnaire

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
    Créer une liste de cartes en fonction du nombre de cartes demandé (32 ou 52) et mélange les cartes de façon aléatoire
              
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

    :param carte1:dic
        premiere carte
    :param carte2:dic
        seconde carte

    :return
    bool
        returne True si les cartes ont la meme valeur ou la meme couleur, False sinon
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

    :return
    """
    for carte in range(len(liste_tas) - 1):
        possible = saut_si_possible(liste_tas, carte + 1)
        if possible:
            return True


def retourner_carte(liste_tas, pioche):
    """
    :param liste_tas:list
    :param pioche:list
    
    :return
    """
    carte = pioche[0]
    del pioche[0]
    liste_tas.append(carte)


def une_etape_reussite(liste_tas, pioche, affiche=False):
    """
    :param liste_tas:list
    :param pioche:list
    :param affiche:bool
    
    :return
    """
    # a revoir
    liste_tas.append(pioche[0])
    del pioche[0]
    if affiche:
        afficher_reussite(liste_tas)
        sleep(5)
    saut = saut_si_possible(liste_tas, len(liste_tas) - 2)
    while saut:
        if affiche:
            afficher_reussite(liste_tas)
            sleep(5)
        saut = verification_possible_saut(liste_tas)


def reussite_mode_auto(pioche, affiche=False):
    """
    :param pioche:
    :param affiche:
    
    :return
    """
    if affiche:
        afficher_reussite(pioche)
        sleep(5)
    pioche_tas = list(pioche)
    liste_tas = []
    while pioche_tas:
        une_etape_reussite(liste_tas, pioche_tas, affiche=affiche)
    return liste_tas


def reussite_mode_manuel(pioche, nb_tas_max=2):
    """
    :param pioche:list
    :param nb_tas_max:int
    
    :return:
    """
    # definition des donnee
    liste_tas = []
    pioche_tas = list(pioche)
    # Programme de la fonction
    while pioche_tas:
        action = input(
            "\n\n#######################################################\nRetourner une carte (taper 1)\nSaisir un "
            "saut (taper2)\nQuitter (taper Q)\n#######################################################\n\n\n")
        if action == '1':
            retourner_carte(liste_tas, pioche_tas)
        elif action == '2':
            for i in range(len(liste_tas)):
                if i < 10 or i % 10 == 0:
                    print(" ", end="")
                print(' {} '.format(i), end='')
            print("")
            afficher_reussite(liste_tas)
            num = int(input("Quel tas voulez-vous faire sauter (entrer un numero, on commence par 0): "))
            possible = saut_si_possible(liste_tas, num)
            if not possible:
                print('Impossible de faire sauter le tas numero {}'.format(num))
        elif action == 'Q':
            for carte in pioche_tas:
                liste_tas.append(carte)
            pioche_tas = []
        afficher_reussite(liste_tas)
    if len(liste_tas) <= nb_tas_max:
        print("Gagner")
    else:
        print("Perdu")
    return liste_tas


def lance_reussite(mode, nb_cartes=32, affiche=False, nb_tas_max=2):
    """
    :param mode:
    :param nb_cartes:int
    :param affiche:bool
    :param nb_tas_max:int
    
    :return:
    """
    pioche = init_pioche_alea(nb_cartes)
    if mode == 'auto':
        liste_tas = reussite_mode_auto(pioche, affiche)
    elif mode == 'manuel':
        liste_tas = reussite_mode_manuel(pioche, nb_tas_max)
    return liste_tas


if __name__ == "__main__":
    # afficher_reussite([{'valeur':7, 'couleur':'P'},{'valeur':10, 'couleur':'K'},{'valeur':'A', 'couleur':'T'}])
    # print(init_pioche_fichier("data_init.txt"))
    # ecrire_fichier_reussite('teste.txt', [{'valeur': 'V', 'couleur': 'C'}, {'valeur': '8', 'couleur': 'P'},
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
    # pioche = init_pioche_alea()
    # print(alliance({'valeur': '7', 'couleur': 'K'}, {'valeur': 'A', 'couleur': 'K'}))
    # liste = [{'valeur': '7', 'couleur': 'K'}, {'valeur': '8', 'couleur': 'P'}, {'valeur': 'A', 'couleur': 'K'}]
    # print(liste)
    # print(saut_si_possible(liste, 1))
    # print(liste)
    # une_etape_reussite(liste, pioche, affiche=True)
    # afficher_reussite(reussite_mode_auto(pioche, affiche=True))
    # reussite_mode_manuel(pioche)
    afficher_reussite(lance_reussite('manuel', nb_tas_max=5))
