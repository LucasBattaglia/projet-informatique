import random

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
        liste_carte = ['7-C', '8-C', '9-C', '10-C', 'V-C', 'D-C', 'R-C', 'A-C',
                       '7-K', '8-K', '9-K', '10-K', 'V-K', 'D-K', 'R-K', 'A-K',
                       '7-P', '8-P', '9-P', '10-P', 'V-P', 'D-P', 'R-P', 'A-P',
                       '7-T', '8-T', '9-T', '10-T', 'V-T', 'D-T', 'R-T', 'A-T']
    elif nb_carte == 52:
        liste_carte = ['2-C', '3-C', '4-C', '5-C', '6-C', '7-C', '8-C', '9-C', '10-C', 'V-C', 'D-C', 'R-C', 'A-C',
                       '2-K', '3-K', '4-K', '5-K', '6-K', '7-K', '8-K', '9-K', '10-K', 'V-K', 'D-K', 'R-K', 'A-K',
                       '2-P', '3-P', '4-P', '5-P', '6-P', '7-P', '8-P', '9-P', '10-P', 'V-P', 'D-P', 'R-P', 'A-P',
                       '2-T', '3-T', '4-T', '5-T', '6-T', '7-T', '8-T', '9-T', '10-T', 'V-T', 'D-T', 'R-T', 'A-T']
    random.shuffle(liste_carte)
    return liste_carte


def alliance(carte1, carte2):
    print(carte1['valeur'], carte2['valeur'], carte1['couleur'], carte2['couleur'])
    if carte1['valeur']==carte2['valeur'] or carte1['couleur']==carte2['couleur']:
        return True
    else:
        return False


def saut_si_possible(liste_tas, num_tas):
    if num_tas<1 or num_tas==len(liste_tas):
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


def une_etape_reussite(liste_tas, pioche, affiche=False):
    ### a revoir ###
    carte = pioche[0]
    del pioche[0]
    liste_tas.append(carte)
    if affiche:
        print(liste_tas)
    saut = saut_si_possible(liste_tas, len(liste_tas)-1)
    while saut:
        saut = False
        if affiche:
            print(liste_tas)
        saut = verification_possible_saut(liste_tas)




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
#print(init_pioche_alea(52))
#print(alliance('7-K', 'A-K'))
#liste = [{'valeur': '7', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'K'}]
#print(liste)
#print(saut_si_possible(liste, 1))
#print(liste)