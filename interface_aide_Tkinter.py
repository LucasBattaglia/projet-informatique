import tkinter as tk


def fenetrevierge(fenetre):
    for widget in fenetre.winfo_children():
        widget.destroy()


def MenuMode(fenetre):
    fenetrevierge(fenetre)


def LesMenu(fenetre):
    fenetrevierge(fenetre)
    image = tk.PhotoImage(file="affichage/imgs/menu.png")
    canevas = tk.Canvas(fenetre, bg="green", highlightthickness=0)
    canevas.create_line((50, 40), (100, 80), width=5, arrow="first")
    canevas.grid(column=0, row=0)
    textimage = tk.Label(canevas, image=image, bg="green")
    textimage.pack()
    suivant = tk.Button(fenetre, text="Suivant", command=lambda: MenuMode(fenetre))
    suivant.grid(column=0, row=1)


def aide():
    fenetre_aide = tk.Toplevel()
    fenetre_aide.configure(background="green")
    fenetre_aide.title('Aide')
    fenetrevierge(fenetre_aide)
    fenetre_aide.resizable(width=False, height=False)

    Text = tk.Label(fenetre_aide, text="""Bienvenue dans notre interface d'aide!
    \n\n
    Afin de mieux vous guider nous utiliserons plusieur page.
    \n\n
    Bonne Continuation
    """, bg="green")
    Text.grid(column=0, row=0)
    suivant = tk.Button(fenetre_aide, text="Suivant", command=lambda: LesMenu(fenetre_aide))
    suivant.grid(column=0, row=1)

