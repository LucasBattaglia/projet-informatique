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


print(carte_to_chaine({'valeur':'A', 'couleur':'P'}))