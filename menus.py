from datetime import datetime
import time

# Constantes pour les couleurs
jaune = '\033[0;93m'
vert = '\033[0;92m'
rouge = '\033[0;91m'
cyan = '\033[0;96m'
magenta = '\033[0;35m'
reset = '\033[0m'

def accueil(contenu):
    print("******************************************************")
    print(f'\t{contenu}\n')
    print("******************************************************")

def afficher_menu():
    print("MENU")
    print("1: Gestion des élèves")
    print("2: Gestion des professeurs")
    print("3: Gestion des utilisateurs") 
    print("0: Quitter()")
    print(f"Date et Heure Système : {datetime.now().strftime('%d/%m/%Y  %H:%M')} ")

def affiche_Elev():
    print("MENU")
    print("1: Ajouter un élève")
    print("2: Supprimer un élève")
    print("3: Modifier les informations de l'élève")
    print("4: Lister les élèves")
    print("5: Retour")
    print("0: Accueil")

def afficherSousMenuProf():
    print("MENU")
    print("1: Ajouter un professeur")
    print("2: Supprimer un professeur")
    print("3: Modifier les informations du professeur")
    print("4: Lister les professeurs")
    print("5: Retour")    
    print("0: Accueil")

def afficherSousMenuUtil():
    print("MENU")
    print("1: Ajouter un utilisateur")
    print("2: Supprimer un utilisateur")
    print("3: Modifier les informations d'un utilisateur")
    print("4: Lister les utilisateurs")
    print("5: Retour")    
    print("0: Accueil")

def quitter(debut):
    fin = time.time()
    dure = fin - debut
    minutes, seconds = divmod(dure, 60)
    print("Merci d'avoir utilisé l'application ! À bientôt.")
    print(f"Durée de la session : {int(minutes)} minutes et {int(seconds)} secondes")
