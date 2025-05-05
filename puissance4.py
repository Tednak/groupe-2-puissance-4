import tkinter as tk
import random as rd
from tkinter import messagebox
import webbrowser
from tkinter import simpledialog

nom_joueur1 = ""
nom_joueur2 = ""
zone_texte_joueur1=""
zone_texte_joueur2=""
grille1=[[None for _ in range(6)] for _ in range(7)]
grille2=[[None for _ in range(6)] for _ in range(7)]
grille3=[[None for _ in range(6)] for _ in range(7)]
grille4=[[None for _ in range(6)] for _ in range(7)]
grille =[[None for _ in range(6)] for _ in range(7)]
nom1="partie vide"
nom2="partie vide"
nom3="partie vide"
manches_joueur1 = 0  # 🟡 Nombre de manches gagnées par le joueur 1
manches_joueur2 = 0  # 🟡 Nombre de manches gagnées par le joueur 2
nb_manches_gagnantes = 3  # 🟡 Nombre de manches à gagner pour remporter le set
nb_colonnes = 7 #
nb_lignes = 6 #


def manuel():
    webbrowser.open_new('https://ludikbazar.com/comment-maitriser-la-strategie-gagnante-du-puissance-4/')

def charger_grille():
    global bouton_grille4,bouton_grille5,bouton_grille6
    bouton_grille4=tk.Button(racine, text=nom1, command=lambda: charger_grille2(1), font=("helvetica", "30"))
    bouton_grille5=tk.Button(racine, text=nom2, command=lambda: charger_grille2(2), font=("helvetica", "30"))
    bouton_grille6=tk.Button(racine, text=nom3, command=lambda: charger_grille2(3), font=("helvetica", "30"))
    bouton_grille4.grid(row=1,column=100)
    bouton_grille5.grid(row=2,column=100)
    bouton_grille6.grid(row=3,column=100)

def charger_grille2(x):
    global grille, grille1, grille2, grille3,grille4
    if x == 1:
        grille = [row[:] for row in grille1]  # Charger l'état de la grille1
    if x == 2:
        grille = [row[:] for row in grille2]  # Charger l'état de la grille2
    if x == 3:
        grille = [row[:] for row in grille3]  # Charger l'état de la grille3
    if x == 4:
        grille = [row[:] for row in grille4]
    if x!=4:
        bouton_grille4.destroy()
        bouton_grille5.destroy()
        bouton_grille6.destroy()
        historique_coups=[]
    dessiner_grille()  

def enregistrer_grille():
    global bouton_grille1,bouton_grille2,bouton_grille3
    bouton_grille1=tk.Button(racine, text=nom1, command=lambda: enregistrer_grille2(1), font=("helvetica", "30"))
    bouton_grille2=tk.Button(racine, text=nom2, command=lambda: enregistrer_grille2(2), font=("helvetica", "30"))
    bouton_grille3=tk.Button(racine, text=nom3, command=lambda: enregistrer_grille2(3), font=("helvetica", "30"))
    bouton_grille1.grid(row=1,column=100)
    bouton_grille2.grid(row=2,column=100)
    bouton_grille3.grid(row=3,column=100)
    
def enregistrer_grille2(x):
    global grille,grille1,grille2,grille3,grille4,nom1,nom2,nom3
    if x==1:
        nom1=simpledialog.askstring("Nom du joueur", "Entrez le nom de la partie :")
        grille1=[row[:] for row in grille]
    if x==2:
        nom2=simpledialog.askstring("Nom du joueur", "Entrez le nom de la partie :")
        grille2=[row[:] for row in grille]
    if x==3:
        nom3=simpledialog.askstring("Nom du joueur", "Entrez le nom de la partie :")
        grille3=[row[:] for row in grille]
    if x==4:
        grille4=[row[:] for row in grille]
        return grille4
    bouton_grille1.destroy()
    bouton_grille2.destroy()
    bouton_grille3.destroy()

def verifier_noms():
    """ Vérifie si les deux noms sont remplis pour activer le bouton du jeu """
    joueur1 = zone_texte_joueur1.get().strip()
    joueur2 = zone_texte_joueur2.get().strip()
    
    if joueur1 and joueur2:
        bouton_demarrer.config(state="normal")
    else:
        bouton_demarrer.config(state="disabled")
def ia():
    messagebox.showwarning("IA", "Pour jouer contre une ia entrez -> *IA* <- dans Joueur2 ")
    
def demander_nb_manches():
    global nb_manches_gagnantes
    nb = simpledialog.askinteger("Nombre de manches", "Combien de manches gagnantes pour gagner le set ?", minvalue=1, maxvalue=10)
    if nb:
        nb_manches_gagnantes = nb    

def afficher_accueil():
    global nom_joueur1, nom_joueur2, zone_texte_joueur1, zone_texte_joueur2, bouton_demarrer, entry_pions
    accueil = tk.Tk()
    accueil.title("Page d'Accueil - Puissance 4")
    accueil.geometry("1000x700")
    accueil.minsize(1000, 700)
    accueil.config(background="#3c6175")

    frame = tk.Frame(accueil, background="#3c6175")
    frame.pack(fill="both", expand=True)

    texte = tk.Label(frame, text="Bienvenue dans Puissance 4", font=("Impact", 45), bg="#3c6175", fg="black")
    texte.pack(side="top", pady=10)

    frame_pseudos = tk.Frame(frame, background="#3c6175")
    frame_pseudos.pack(pady=60)  # Un peu plus d'espace pour décaler les champs de texte

    # Label pour le joueur 1
    tk.Label(frame_pseudos, text="Nom du Joueur 1 :", font=("Comic Sans MS", 15, "bold"), fg="indian red", bg="#3c6175").pack(pady=5)
    zone_texte_joueur1 = tk.Entry(frame_pseudos, font=("Comic Sans MS", 15, "bold"), fg="black")  # Texte en noir
    zone_texte_joueur1.pack(pady=1)
    zone_texte_joueur1.bind("<KeyRelease>", lambda: verifier_noms())

    # Label pour le joueur 2
    tk.Label(frame_pseudos, text="Nom du Joueur 2 :", font=("Comic Sans MS", 15, "bold"), fg="goldenrod", bg="#3c6175").pack(pady=5)
    zone_texte_joueur2 = tk.Entry(frame_pseudos, font=("Comic Sans MS", 15, "bold"), fg="black")  # Texte en noir
    zone_texte_joueur2.pack(pady=1)
    zone_texte_joueur2.bind("<KeyRelease>", lambda: verifier_noms())

    # Bouton pour expliquer comment mettre l'ia
    bouton_ia = tk.Button(frame, text="Ia ?", command=ia, font=("Helvetica", 15))
    bouton_ia.pack(pady=10)
    
    bouton_rouge = tk.Button(accueil, text="j1 rouge", command=modif_couleur_rouge1)
    bouton_rouge.pack(side="left", padx=0, pady=10)    
    bouton_vert = tk.Button(accueil, text="j1 vert", command=modif_couleur_vert1)
    bouton_vert.pack(side="left", padx=0, pady=10)
    bouton_marron = tk.Button(accueil, text="j1 marron", command=modif_couleur_marron1)
    bouton_marron.pack(side="left", padx=0, pady=10)    
    bouton_rose = tk.Button(accueil, text="j1 rose", command=modif_couleur_rose1)
    bouton_rose.pack(side="left", padx=0, pady=10)
    bouton_violet = tk.Button(accueil, text="j1 violet", command=modif_couleur_violet1)
    bouton_violet.pack(side="left", padx=0, pady=10)    
    bouton_orange = tk.Button(accueil, text="j1 orange", command=modif_couleur_orange1)
    bouton_orange.pack(side="left", padx=0, pady=10)
    bouton_noir = tk.Button(accueil, text="j1 noir", command=modif_couleur_noir1)
    bouton_noir.pack(side="left", padx=0, pady=10)
    
    bouton_jaune = tk.Button(accueil, text="j2 jaune", command=modif_couleur_jaune2)
    bouton_jaune.pack(side="right", padx=10, pady=10)    
    bouton_vert = tk.Button(accueil, text="j2 vert", command=modif_couleur_vert2)
    bouton_vert.pack(side="right", padx=0, pady=10)
    bouton_marron = tk.Button(accueil, text="j2 marron", command=modif_couleur_marron2)
    bouton_marron.pack(side="right", padx=0, pady=10)    
    bouton_rose = tk.Button(accueil, text="j2 rose", command=modif_couleur_rose2)
    bouton_rose.pack(side="right", padx=0, pady=10)
    bouton_violet = tk.Button(accueil, text="j2 violet", command=modif_couleur_violet2)
    bouton_violet.pack(side="right", padx=0, pady=10)    
    bouton_orange = tk.Button(accueil, text="j2 orange", command=modif_couleur_orange2)
    bouton_orange.pack(side="right", padx=0, pady=10)
    bouton_noir = tk.Button(accueil, text="j2 noir", command=modif_couleur_noir2)
    bouton_noir.pack(side="right", padx=0, pady=10)

    # Bouton pour commencer la partie
    bouton_demarrer = tk.Button(frame, text="Commencer la partie", command=lambda: demarrer_partie(accueil), font=("Helvetica", 35))
    bouton_demarrer.pack(expand=True, pady=10)

    # Bouton pour définir les manches gagnantes
    bouton_set = tk.Button(frame, text="Définir les manches gagnantes", command=demander_nb_manches, font=("Helvetica", 15))
    bouton_set.pack(pady=50)

    # Le bouton guide des stratégies (déplacé)
    bouton_manuel = tk.Button(frame, text="guide des stratégies", command=manuel, font=("Helvetica", 15))
    bouton_manuel.pack(side="left", padx=10, pady=10)  # Place à gauche

    # Le bouton Quitter (placé en bas à droite)
    bouton_quitter = tk.Button(frame, text="Quitter", command=accueil.destroy, font=("Helvetica", 20))
    bouton_quitter.pack(side="right", anchor="s", padx=10, pady=10)  # Bas droit

    #  bouton pour changer  les dimensions de la grille
    bouton_dimensions = tk.Button(frame, text="Changer dimensions", command=choisir_dimensions, font=("Helvetica", 15))
    bouton_dimensions.pack(pady=10) 

    label_pions = tk.Label(frame , text="Pions à aligner pour gagner :")
    label_pions.pack(pady=5)
    entry_pions = tk.Entry(frame, font=("Comic Sans MS", 15, "bold"), fg="black")  # Texte en noir
    entry_pions.insert(0, "4")  # valeur par défaut
    entry_pions.pack(pady=5)
    
    accueil.mainloop()

def modif_couleur_rouge1():
    global coul1, coul2
    if coul2!="red":
        coul1="red"
    else:
        coul1="yellow"
def modif_couleur_jaune1():
    global coul1, coul2
    if coul2!="yellow":
        coul1="yellow"
    else:
        coul1="red"
def modif_couleur_vert1():
    global coul1, coul2
    if coul2!="green":
        coul1="green"
    else:
        coul1="red"
def modif_couleur_marron1():
    global coul1, coul2
    if coul2!="brown":
        coul1="brown"
    else:
        coul1="red"
def modif_couleur_rose1():
    global coul1, coul2
    if coul2!="pink":
        coul1="pink"
    else:
        coul1="red"
def modif_couleur_violet1():
    global coul1, coul2
    if coul2!="violet":
        coul1="violet"
    else:
        coul1="red"
def modif_couleur_orange1():
    global coul1, coul2
    if coul2!="orange":
        coul1="orange"
    else:
        coul1="red"
def modif_couleur_noir1():
    global coul1, coul2
    if coul2!="black":
        coul1="black"
    else:
        coul1="red"

def modif_couleur_rouge2():
    global coul2, coul1
    if coul2!="red":
        coul1="red"
    else:
        coul1="yellow"        
def modif_couleur_jaune2():
    global coul2, coul1
    if coul1!="yellow":
        coul2="yellow"
    else:
        coul1="red"    
def modif_couleur_vert2():
    global coul2, coul1
    if coul1 != "green":
        coul2="green"
    else:
        coul2="yellow"
def modif_couleur_marron2():
    global coul2, coul1
    if coul1 != "brown":
        coul2="brown"
    else:
        coul2="yellow"
def modif_couleur_rose2():
    global coul2, coul1
    if coul1 != "pink":
        coul2="pink"
    else:
        coul2="yellow"
def modif_couleur_violet2():
    global coul2, coul1
    if coul1 != "violet":
        coul2="violet"
    else:
        coul2="yellow"
def modif_couleur_orange2():
    global coul2, coul1
    if coul1 != "orange":
        coul2="orange"
    else:
        coul2="yellow"
def modif_couleur_noir2():
    global coul2, coul1
    if coul1 != "black":
        coul2="black"
    else:
        coul2="yellow"

def demarrer_partie(accueil):
    global Joueur1, Joueur2, nb_pion_victoire
    Joueur1 = zone_texte_joueur1.get().strip()
    Joueur2 = zone_texte_joueur2.get().strip()
    nb_pion_victoire = int(entry_pions.get())      
    if nb_pion_victoire > max(nb_lignes, nb_colonnes):
        messagebox.showerror("Le nombre de pions à aligner ne peut pas dépasser le nombre de lignes ou de colonnes.")
        return
    
    if Joueur1 and Joueur2:
        accueil.destroy()
        jeu()
        racine.deiconify()

        label_nom_joueur1.config(text=f"Joueur 1 : {Joueur1}")
        label_nom_joueur2.config(text=f"Joueur 2 : {Joueur2}")
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer les noms des deux joueurs !")
  
def jeu():
    global joueur_act, grille, historique_coups
    joueur_act = 0
    grille = [[None for _ in range(nb_lignes)] for _ in range(nb_colonnes)] #
    historique_coups = []
    dessiner_grille()
    
def retour_accueil():
    racine.withdraw()
    reinitialiser_jeu()
    afficher_accueil()

def dessiner_grille():
    # Supprimer uniquement les cercles existants (structure de la grille)
    global largeur_case, hauteur_case
    largeur_case = CANVAS_WIDTH / nb_colonnes
    hauteur_case = CANVAS_HEIGHT / nb_lignes
    
    mon_canvas.delete("grille")  
    
    # Redessiner les cases de la grille (cercles blancs)
    for i in range(nb_colonnes):
        for j in range(nb_lignes):
            mon_canvas.create_oval(
                (i * largeur_case + 25, j * hauteur_case + 25),
                ((i + 1) * largeur_case - 25, (j + 1) * hauteur_case - 25),
                fill="white", outline="blue", tags="grille"
            )

    # Redessiner les jetons déjà placés
    for col in range(nb_colonnes):
        for row in range(nb_lignes):
            if grille[col][row] is not None:
                couleur = grille[col][row]
                mon_canvas.create_oval(
                    (col * largeur_case + 25, row * hauteur_case + 25),
                    ((col + 1) * largeur_case - 25, (row + 1) * hauteur_case - 25),
                    fill=couleur, outline=couleur, tags="jeton"
                )

coul1 = "red"
coul2 = "yellow"

def placer_jeton(x):
    global joueur_act, manches_joueur1, manches_joueur2,var_test
    colonne = x - 1  # pour la grille (de 0 à 6)
    var_test=0
    
    if grille[colonne][0] is not None:
        var_test=1
        return messagebox.showwarning("Erreur", "Cette colonne est pleine, choisissez une autre colonne")

    for row in range(nb_lignes - 1, -1, -1):
        if grille[colonne][row] is None:
            couleur = "red" if joueur_act == 0 else "yellow"
            mon_canvas.create_oval((25 + colonne * largeur_case, 25 + row * hauteur_case),
                                   ((colonne + 1) * largeur_case - 25, (row + 1) * hauteur_case - 25), 
                                   fill=couleur, outline=couleur, tags="jeton")

            grille[colonne][row] = couleur
            historique_coups.append((colonne, row, couleur))  
            print(historique_coups)  
            label_joueur.config(text="")  

            if verifier_victoire(couleur):
                var1=1
                if couleur == "red":
                    messagebox.showinfo("Félicitations!", "Bravo " + Joueur1 + ", tu as gagné !")
                    manches_joueur1 += 1
                else: 
                    messagebox.showinfo("Félicitations!", "Bravo " + Joueur2 + ", tu as gagné !")
                    manches_joueur2 += 1

                if manches_joueur1 == nb_manches_gagnantes:
                    messagebox.showinfo("Victoire du Set", Joueur1 + " remporte le set avec " + str(manches_joueur1) + " manches gagnées !")
                    manches_joueur1 = 0
                    manches_joueur2 = 0
                    retour_accueil()
                    return

                if manches_joueur2 == nb_manches_gagnantes:
                    messagebox.showinfo("Victoire du Set", Joueur2 + " remporte le set avec " + str(manches_joueur2) + " manches gagnées !")
                    manches_joueur1 = 0
                    manches_joueur2 = 0
                    retour_accueil()
                    return

                reinitialiser_jeu()
                return

            if all(grille[c][0] is not None for c in range(nb_colonnes)):
                messagebox.showinfo("Match nul", "La partie est terminée sans gagnant !")
                reinitialiser_jeu()
                return

            joueur_act = 1 - joueur_act
            break

    if Joueur2=="*IA*" and joueur_act==1:
        var1=0
        enregistrer_grille2(4)
        for x in range(1,nb_colonnes+1):
            placer_jetonia(x,0)
            if verifier_victoire("yellow")==True :
                messagebox.showinfo("Félicitations!", "Bravo " + Joueur2 + ", tu as gagné !")
                manches_joueur2 += 1
                if manches_joueur2 == nb_manches_gagnantes:
                    messagebox.showinfo("Victoire du Set", Joueur2 + " remporte le set avec " + str(manches_joueur2) + " manches gagnées !")
                    manches_joueur1 = 0
                    manches_joueur2 = 0
                    retour_accueil()
                    return
                else:
                    retour_accueil()
                    return
            annuler_coup()
            charger_grille2(4)
        for x in range(1,nb_colonnes+1):
            placer_jetonia(x,1)
            if verifier_victoire("red")==True :
                charger_grille2(4)
                placer_jetonia(x,0)
                joueur_act=0
                return print("test")
            charger_grille2(4)
        if var1==0:
            x=rd.randint(1,nb_colonnes+1)
            placer_jetonia(x,0)
            if var_test==1:
                while var_test==1:
                    var_test=0
                    x=rd.randint(1,nb_colonnes+1)
                    placer_jetonia(x,0)
        joueur_act=0
    
        
def placer_jetonia(x,n):
    global joueur_act,var_test
    colonne = x - 1  # pour la grille (de 0 à 6)
    var_test=0
    
    if grille[colonne][0] is not None:
        var_test=1
        return print("Cette colonne est pleine, choisissez une autre colonne")
    if n==0:
        for row in range(nb_lignes - 1, -1, -1):
            if grille[colonne][row] is None:
                couleur = "yellow"
                mon_canvas.create_oval((25 + colonne * largeur_case, 25 + row * hauteur_case),
                                    ((colonne + 1) * largeur_case - 25, (row + 1) * hauteur_case - 25), 
                                    fill=couleur, outline=couleur, tags="jeton")

                grille[colonne][row] = couleur 
                historique_coups.append((colonne, row, couleur))  
                print(historique_coups)
                label_joueur.config(text="")  
                break
        return None
    if n==1:
        for row in range(nb_lignes - 1, -1, -1):
            if grille[colonne][row] is None:
                couleur = "red"
                mon_canvas.create_oval((25 + colonne * largeur_case, 25 + row * hauteur_case),
                                    ((colonne + 1) * largeur_case - 25, (row + 1) * hauteur_case - 25), 
                                    fill=couleur, outline=couleur, tags="jeton")

                grille[colonne][row] = couleur 
                label_joueur.config(text="")  
                break
        return None          


def annuler_coup():
    global joueur_act
    if len(historique_coups) == 0:  
        messagebox.showwarning("Erreur", "Aucun coup à annuler")
        return

    dernier_coup = historique_coups.pop() 
    colonne, ligne, couleur = dernier_coup

    mon_canvas.create_oval((25 + colonne * largeur_case, 25 + ligne * hauteur_case),
                           ((colonne + 1) * largeur_case - 25, (ligne + 1) * hauteur_case - 25), 
                           fill="white", outline="blue")

    grille[colonne][ligne] = None  

    joueur_act = 1 - joueur_act

def creer_boutons_colonnes():
    # Supprimer les anciens boutons
    for widget in racine.grid_slaves(row=0):
        widget.destroy()

    # Créer les boutons selon le nombre de colonnes
    if nb_colonnes == 4:
        for i in range(4):
            bouton = tk.Button(racine, text=str(i + 1), command=lambda x=i + 1: placer_jeton(x), font=("helvetica", 20))
            bouton.grid(row=0, column=i + 2, padx="2c", pady="1c")

    elif nb_colonnes == 5:
        for i in range(5):
            bouton = tk.Button(racine, text=str(i + 1), command=lambda x=i + 1: placer_jeton(x), font=("helvetica", 20))
            bouton.grid(row=0, column=i + 2, padx="1.6c", pady="1c")

    elif nb_colonnes == 6:
        for i in range(6):
            bouton = tk.Button(racine, text=str(i + 1), command=lambda x=i + 1: placer_jeton(x), font=("helvetica", 20))
            bouton.grid(row=0, column=i + 2, padx="1.2c", pady="1c")

    elif nb_colonnes == 7:
        for i in range(7):
            bouton = tk.Button(racine, text=str(i + 1), command=lambda x=i + 1: placer_jeton(x), font=("helvetica", 20))
            bouton.grid(row=0, column=i + 2, padx="1c", pady="1c")

    elif nb_colonnes == 8:
        for i in range(8):
            bouton = tk.Button(racine, text=str(i + 1), command=lambda x=i + 1: placer_jeton(x), font=("helvetica", 20))
            bouton.grid(row=0, column=i + 2, padx="0.85c", pady="1c")

    elif nb_colonnes == 9:
        for i in range(9):
            bouton = tk.Button(racine, text=str(i + 1), command=lambda x=i + 1: placer_jeton(x), font=("helvetica", 20))
            bouton.grid(row=0, column=i + 2, padx="0.75c", pady="1c")

    elif nb_colonnes == 10:
        for i in range(10):
            bouton = tk.Button(racine, text=str(i + 1), command=lambda x=i + 1: placer_jeton(x), font=("helvetica", 20))
            bouton.grid(row=0, column=i + 2, padx="0.65c", pady="1c")



def reinitialiser_jeu():
    global grille, joueur_act
    joueur_act = rd.choice([0, 1])  
    
    grille = [[None for _ in range(nb_lignes)] for _ in range(nb_colonnes)]
    
    mon_canvas.delete("jeton")
   
    dessiner_grille()  

    couleur = "Rouge" if joueur_act == 0 else "Jaune"
    label_joueur.config(text="C'est au Joueur " + str(joueur_act + 1) + " (" + couleur + ") de commencer")
    label_joueur.config(text=Joueur1 + " : " + str(manches_joueur1) + " | " + Joueur2 + " : " + str(manches_joueur2))
    
def choisir_dimensions():
    global nb_colonnes, nb_lignes, largeur_case, hauteur_case, grille , CANVAS_HEIGHT,CANVAS_WIDTH
    CANVAS_WIDTH = nb_colonnes * 100
    CANVAS_HEIGHT = nb_lignes * 100


    # Demander à l'utilisateur les dimensions
    colonnes = simpledialog.askinteger("Colonnes", "Entrez le nombre de colonnes (minimum 4) :", minvalue=4, maxvalue=10)
    lignes = simpledialog.askinteger("Lignes", "Entrez le nombre de lignes (minimum 4) :", minvalue=4, maxvalue=10)

    if colonnes and lignes:
        nb_colonnes = colonnes
        nb_lignes = lignes

        # Redimensionner la grille
        grille = [[None for _ in range(nb_lignes)] for _ in range(nb_colonnes)]

        # Recalculer la taille des cases
        largeur_case = CANVAS_WIDTH // nb_colonnes
        hauteur_case = CANVAS_HEIGHT // nb_lignes

        # Réinitialiser le canvas et les boutons
        creer_boutons_colonnes()
        dessiner_grille()

racine = tk.Tk()
racine.title("Puissance 4")
racine.withdraw()
creer_boutons_colonnes()


CANVAS_WIDTH = nb_colonnes * 100
CANVAS_HEIGHT = nb_lignes * 100

mon_canvas = tk.Canvas(racine, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="blue")
mon_canvas.grid(row=1, column=0, columnspan=20)


largeur_case = CANVAS_WIDTH//7
hauteur_case = CANVAS_HEIGHT//6

frame_bas = tk.Frame(racine)  
frame_bas.grid(row=7, column=2, columnspan=7, pady=10)  

frame_nom = tk.Frame(racine, background="#041a40")
frame_nom.grid(row=8, column=2, columnspan=7, pady=10)

bouton_annuler = tk.Button(frame_bas, text="Annuler le dernier coup", command=annuler_coup, font=("helvetica", "12"))
bouton_annuler.grid(row=0, column=0, padx=10)

bouton_reset = tk.Button(frame_bas, text="Nouvelle Partie", command=reinitialiser_jeu, font=("helvetica", "12"))
bouton_reset.grid(row=0, column=1, padx=10)

label_joueur = tk.Label(frame_bas, text="", font=("helvetica", "12"))
label_joueur.grid(row=0, column=2, padx=10)

bouton_acccueil = tk.Button(frame_bas, text="retourner à l'acceuil", command= retour_accueil,font=("helvetica", "12") )
bouton_acccueil.grid(row=0, column=3, padx=10)

label_nom_joueur1 = tk.Label(frame_bas, text="Joueur 1 : ", font=("Helvetica", 15), fg="red", bg="#041a40")
label_nom_joueur1.grid(row=2, column=0, columnspan=7, pady=10)

label_nom_joueur2 = tk.Label(frame_bas, text="Joueur 2 : ", font=("Helvetica", 15), fg="yellow", bg="#041a40")
label_nom_joueur2.grid(row=2, column=2, columnspan=7, pady=10)

bouton_charger=tk.Button(frame_bas, text="charger", command=lambda: charger_grille(), font=("helvetica", "12"))
bouton_charger.grid(row=0,column=4)

bouton_enregistrer=tk.Button(frame_bas, text="enregistrer", command=lambda: enregistrer_grille(), font=("helvetica", "12"))
bouton_enregistrer.grid(row=0, column=6)



# toute modification apres premiere evaluation

nb_pion_victoire = 4 


def verifier_victoire(couleur):
    #  horizontale

    for row in range(nb_lignes):
        compteur = 0
        for col in range(nb_colonnes):
            if grille[col][row] == couleur :
                compteur += 1
                if compteur == nb_pion_victoire:
                    return True
            else:
                compteur = 0

    #  verticale
    for col in range(nb_colonnes):
        compteur = 0
        for row in range(nb_lignes):
            if grille[col][row] == couleur :
                compteur += 1
                if compteur == nb_pion_victoire:
                    return True
            else:
                compteur = 0

    #  diagonale (\)
    for ligne in range(nb_lignes - nb_pion_victoire + 1):
        for colonne in range(nb_colonnes - nb_pion_victoire + 1):
            compteur = 0
            for i in range(nb_pion_victoire):
                if grille[ligne + i][colonne + i] == couleur:
                    compteur += 1
                    if compteur == nb_pion_victoire:
                        return True
                else:
                    break

    # diagonale (/)
    for ligne in range(nb_pion_victoire - 1, nb_lignes):
        for colonne in range(nb_colonnes - nb_pion_victoire + 1):
            compteur = 0
            for i in range(nb_pion_victoire):
                if grille[ligne - i][colonne + i] == couleur:
                    compteur += 1
                    if compteur == nb_pion_victoire:
                        return True
                else:
                    break

    return False



afficher_accueil()
reinitialiser_jeu()  

racine.mainloop()
