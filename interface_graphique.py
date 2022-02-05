# importation des bibliotheque de Python
from turtle import *

# creation de la fenetre
fenetre = Screen()
fenetre.title("Reussite des alliances")
fenetre.bgcolor("yellow")
height = fenetre.window_height()
width = fenetre.window_width()
print(height, width)
hideturtle()
tour = True


# gerer les 'Boutton' de la fenetre
def connection(x, y):
    if -(height / 2) < x < -(height / 2) + 100 and (width / 2) - 80 > y > (width / 2) - 100:
        print('auto')
    if -(height / 2) < x < -(height / 2) + 100 and (width / 2) - 120 > y > (width / 2) - 140:
        print('manuel')


def carre():
    for cote in range(4):
        if cote % 2 == 0:
            forward(100)
        else:
            forward(20)
        left(90)
    forward(50)


if __name__ == "__main__":
    # affichage des boutton
    up()
    goto(-(height / 2), (width / 2) - 100)
    down()
    carre()
    write("Mode automatique", align='center')
    up()
    goto(-(height / 2), (width / 2) - 140)
    down()
    carre()
    write("Mode manuel", align='center')
    up()

    # gerer les interaction
    onscreenclick(connection)
    print("OK")

    fenetre.mainloop()
