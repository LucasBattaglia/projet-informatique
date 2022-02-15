# importation des bibliotheque de Python
from turtle import *

# creation de la fenetre
fenetre = Screen()
fenetre.title("Reussite des alliances")
fenetre.bgcolor("green")
height = fenetre.window_height()
width = fenetre.window_width()
print(height, width)
hideturtle()
speed(1000)

# definition des variable
tour = True
dos = "affichage/imgs/carte-dos.gif"
fenetre.register_shape(dos)
button_auto = "affichage/imgs/button-automatique2.gif"
fenetre.register_shape(button_auto)
button_manuel = "affichage/imgs/button-automatique2.gif"
fenetre.register_shape(button_manuel)
global count_x
global count_y


# gerer les 'Boutton' de la fenetre
def incremente(x, y):
    if (x + 49) > (height / 2):
        x += 49
        y = y
    else:
        x = 20
        y -= 71
    return x, y


def more_carte(x, y):
    shape(dos)
    ht()
    speed(3)
    goto(x, y)
    st()
    goto(-(height / 2) + 20, (width / 2) - 250)
    speed(1000)


def connectionManuel(x, y):
    # Boutton Quitter (Dessin)
    goto(-150, -210)
    down()
    carre()
    up()
    write("Quitter", align='center')

    # Boutton Pioche (Fenetre)
    pioche = Turtle()
    pioche.up()
    print(type(pioche))
    pioche.shape(dos)
    pioche.st()
    pioche.goto(150, -200)
    pioche.onclick(more_carte)


def connectionAuto(x, y):
    print(auto)


def connection(x, y):
    print(x, y)
    if -(height / 2) + 174 < x < -(height / 2) + 274 and -(width / 2) + 174 < y < -(width / 2) + 194:
        print("Quitter")


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

    auto = Turtle()
    auto.up()
    auto.ht()
    print(type(fenetre), type(auto))
    auto.shape(button_auto)
    auto.goto(-(height / 2), (width / 2) - 80)
    auto.st()
    auto.onclick(connectionAuto)

    manuel = Turtle()
    manuel.up()
    manuel.ht()
    print(type(fenetre), type(manuel))
    manuel.shape(button_auto)
    manuel.goto(-(height / 2), (width / 2) - 130)
    manuel.st()
    manuel.onclick(connectionManuel)

    fenetre.mainloop()
