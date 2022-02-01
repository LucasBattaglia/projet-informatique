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
    fichier = open(fichier_carte, "r").read()
    return fichier.split(" ")


afficher_reussite([{'valeur':7, 'couleur':'P'},{'valeur':10, 'couleur':'K'},{'valeur':'A', 'couleur':'T'}])
print(init_pioche_fichier("data_init.txt"))