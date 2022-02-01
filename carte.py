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
    f = open(fichier_carte, "r")
    fichier = f.read()
    f.close()
    return fichier.split(" ")


def ecrire_fichier_reussite(nom_fich, liste_carte):
    f = open(nom_fich, 'w')
    for carte in liste_carte:
        f.write(carte)
        f.write(" ")
    f.close()


afficher_reussite([{'valeur':7, 'couleur':'P'},{'valeur':10, 'couleur':'K'},{'valeur':'A', 'couleur':'T'}])
print(init_pioche_fichier("data_init.txt"))
ecrire_fichier_reussite('teste.txt', ['1-C', '2-C', '3-C', '4-C', '5-C', '6-C', '7-C', '8-C', '9-C', '10-C', 'V-C',
                                      'D-C', 'R-C', 'A-C', '10-C', '9-K', '9-C', 'D-T', 'R-C', '8-C', 'D-K', '7-C',
                                      'A-T', '7-P', 'V-T', '7-K', 'D-C', 'A-K', 'D-P', '10-T', 'R-K', 'R-P'])