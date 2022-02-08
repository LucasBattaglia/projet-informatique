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
global count_x
global count_y



# gerer les 'Boutton' de la fenetre
def incremente(x, y):
    if (x + 49) > (height / 2):
        x += 49
        y=y
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


def connection(x, y):
    count_x = 20
    count_y = -250
    if -(height / 2) - 50 < x < -(height / 2) + 50 and (width / 2) - 80 > y > (width / 2) - 100:
        print('auto')
    elif -(height / 2) - 50 < x < -(height / 2) + 50 and (width / 2) - 120 > y > (width / 2) - 140:
        # Boutton Quitter (Dessin)
        goto(-150, -210)
        down()
        carre()
        up()
        write("Quitter", align='center')

        # Boutton Pioche (Fenetre)
        pioche = Turtle()
        pioche.up()
        pioche.shape(dos)
        pioche.st()
        pioche.goto(150, -200)
        pioche.onclick(more_carte)
    elif -(height / 2) + 174 < x < -(height / 2) + 274 and -(width / 2) + 174 < y < -(width / 2) + 194:
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
    up()
    goto(-(height / 2) - 50, (width / 2) - 100)
    down()
    carre()
    write("Mode Automatique", align='center')
    up()
    goto(-(height / 2) - 50, (width / 2) - 140)
    down()
    carre()
    write("Mode Manuel", align='center')
    up()

    # gerer les interaction
    onscreenclick(connection)
    print("OK")

    fenetre.mainloop()
