from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.figure as mf
import matplotlib.backends.backend_tkagg as mbbt
import carte


def stat(nb_carte, nb_simulation):

    window = Toplevel()

    window.title('Statistique')

    window.geometry("500x500")

    ### Mise en place de la figure ###

    fig = mf.Figure(figsize=(5, 5),
                    dpi=100)  # Grossisement 100%

    point = []  # liste des point du graphique (fonction x²)
    x = []  # Nombre de tas a la fin de chaque partie


    for i in range(nb_simulation):
        x.append(len(carte.reussite_mode_auto(carte.init_pioche_alea()))) # On ajoute au dictionnaire a la fin de chaque simulation le nombre de tas restant
    print("Fin des simulations")

    for i in range(2, nb_carte+1):
        point.append(x.count(i)/nb_simulation*100) # Pour chaque tas entre 2 et 32 on ajoute dans le dictionnaire point le nombre de fois qu'elle apparer dans le dictionnaires x
        print("{} fois {} carte a la fin".format(x.count(i), i))


    for i in range(len(point)):
        if point[i] == max(point):
            print("Le maximun atteint {}% avec {} carte a fin".format(max(point), i + 2))

    plot1 = fig.add_subplot(111)  ### creation d'un add_subplot and figure ###
    plot1.set_title("Representation de la probabulite de terminer \navec un certain nombre de carte")
    plot1.set_xlabel("Nombre de carte a la fin d'une partie")
    plot1.set_ylabel("% representant la chance d'avoir une carte")

    hauteur = [i for i in range(2, nb_carte+1)]
    print(hauteur)

    plot1.plot(hauteur, point, marker='x', markerfacecolor='red', markeredgecolor='#cc0000')  # On donne les points y a add_subplot de ma figure

    canvas = mbbt.FigureCanvasTkAgg(fig,
                                    master=window)  # Creation d'un canvas dans ma fentre tkinter avec la figure
    canvas.draw()  ### On dessine dans le canvas ###

    canvas.get_tk_widget().pack()  # affichage du canvas dans la fenetre et conversion en Tkinter

    # toolbar = mbbt.NavigationToolbar2Tk(canvas, window)
    # toolbar.update()

    # canvas.get_tk_widget().pack()


def warning(nb_carte, nb_simulation, windows):
    valeur = [100, 1000, 10000, 100000, 1000000]
    value = ["100 (-1s)", "1000 (environ 2s)", "10000 (environ 15s)", "100000 (environ 3min)", "1000000 (environ 30min)"]
    temps = ["(-1s)", "(environ 2s)", "(environ 15s)", "(environ 3min)", "(environ 30min)"]
    for i in range(len(value)):
        if value[i]==nb_simulation:
            nb_simulation = valeur[i]
            duree = temps[i]
    rep = messagebox.askyesno('Etes vous sure?', 'Vous ne pourrez pas utiliser le jeu durant la durer de la simulation! {}\n Etes vous sure de vouloir la lancer maintenant?'.format(duree))
    if rep:
        windows.destroy()
        stat(nb_carte, nb_simulation)


def conf_stat():
    window_conf = Toplevel()
    window_conf.title('Configuration des statistiques')

    text_nb_carte = Label(window_conf, text="Nombre de carte pour la simulation")
    text_nb_carte.grid(column=0, row=0)

    nb_carte = IntVar()
    nb_carte.set(32)
    bouton32 = Radiobutton(window_conf, text="32", variable=nb_carte, value=32)
    bouton52 = Radiobutton(window_conf, text="52", variable=nb_carte, value=52)
    bouton32.grid(column=1, row=0)
    bouton52.grid(column=2, row=0)

    text_simulation = Label(window_conf, text="Nombre de simulation a faire")
    text_simulation.grid(column=0, row=1)

    nb_simulation = StringVar()
    list_nb_simulation = ttk.Combobox(window_conf, textvariable=nb_simulation,values=[
                                    "100 (-1s)",
                                    "1000 (environ 2s)",
                                    "10000 (environ 15s)",
                                    "100000 (environ 3min)",
                                    "1000000 (environ 30min)"])
    list_nb_simulation.current(0)
    list_nb_simulation.grid(column=1, row=1)

    button = Button(window_conf, text="lancer la simulation", command=lambda: warning(nb_carte=nb_carte.get(), nb_simulation=nb_simulation.get(), windows=window_conf))
    button.grid(column=3, row=2)