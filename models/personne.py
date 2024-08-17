from datetime import datetime

class Personne:
    """
        Classe représentant une personne avec des informations personnelles.
    """

    __idUnique =  0
    # Initialise une nouvelle personne avec ses informations personnelles.
    def __init__(self, date_naissance, ville, prenom, nom, telephone):
        Personne.__idUnique += 1
        self.__id =  Personne.__idUnique 
        self.__date_naissance = date_naissance 
        self.__ville = ville 
        self.__prenom = prenom 
        self.__nom = nom 
        self.__telephone = telephone 
    
    # Retourne une représentation sous forme de chaîne de la personne.
    def __str__(self):
        return f"n° {self.__id} : {self.__nom}, prenoms {self.__prenom}, née le {self.__date_naissance} à {self.__ville}, numéro de téléphone : {self.__telephone}"

    # Calcule et retourne l'âge de la personne en années.
    def ObtenirAge(self):
        datePresent = datetime.today()
        date_naissance = datetime.strptime(self.__date_naissance, '%Y-%m-%d')
        age = datePresent.year - date_naissance.year - ((datePresent.month, datePresent.day) < (date_naissance.month, date_naissance.day))
        return age
    
    # Retourne l'identifiant unique de la personne 
    @property 
    def get_id(self):
        return self.__id

    # Retourne la date de naissance de la personne.
    @property 
    def get_date_naissance(self):
        return self.__date_naissance

    # Retourne la ville de résidence de la personne.
    @property 
    def get_ville(self):
        return self.__ville

    # Retourne le prénom de la personne.
    @property 
    def get_prenom(self):
        return self.__prenom

    # Retourne le nom de la personne.
    @property
    def get_nom(self):
        return self.__nom    

    # Retourne le numéro de téléphone de la personne.
    @property
    def get_telephone(self):
        return self.__telephone    
    @property
    def set_prenom(self, prenom):
        self.__prenom = prenom
    @property
    def set_nom(self, nom):
        self.__nom = nom
    @property
    def set_ville(self, ville):
        self.__ville = ville
    @property
    def set_date_naissance(self, date_naissance):
        self.__date_naissance = date_naissance   
    @property
    def set_telephone(self, telephone):
        self.__telephone = telephone    