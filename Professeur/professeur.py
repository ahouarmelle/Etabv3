import mysql.connector
from  mysql.connector import Error
#from models.personne import Personne
from Professeur.ICrudProfesseur import ICRUDProfesseur
from Professeur.IEducation import IEducation


class Professeur( IEducation, ICRUDProfesseur):
    """
        Classe représentant un professeur, héritant de Personne et implémentant des interfaces éducatives.
    """

    #__professeurs = []
    
    # Initialise un nouveau professeur avec ses informations personnelles et ses responsabilités.
    def __init__(self, date_naissance, ville, prenom, nom, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion):
        #super().__init__(date_naissance, ville, prenom, nom, telephone)
        self.__date_naissance = date_naissance
        self.__ville = ville
        self.__prenom = prenom
        self.__nom = nom
        self.__telephone = telephone
        self.__vacant = vacant
        self.__matiere_enseigne = matiere_enseigne
        self.__prochain_cours = prochain_cours
        self.__sujet_prochaine_reunion = sujet_prochaine_reunion

    # Retourne une représentation sous forme de chaîne du professeur.
    #def __str__(self):
        #statut_affiche = "Oui" if self.__vacant else "Non"
        #return f"Professeur {super().__str__()}) , vacant: {statut_affiche}, enseigne {self.__matiereEnseigne}"

    @staticmethod
    def create_connection():
    
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='etab_db'
            )
            return connection
        except Error as e:
            print(f"Erreur de connexion: {e}")
            return None
    
    @staticmethod
    def ajouter(professeur):
        connection = Professeur.create_connection()
        if connection:
            try:
                cursor =connection.cursor()
                query_professeur = """
                INSERT INTO professeurs (date_naissance, ville, prenom, nom, telephone,vacant,matiere_enseigne, prochain_cours, sujet_prochaine_reunion)
                VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)
                """
                values_professeur = (professeur.date_naissance, professeur.ville, professeur.prenom, professeur.nom, professeur.telephone, professeur.vacant, professeur.matiere_enseigne,professeur.prochain_cours,professeur.sujet_prochaine_reunion)
                cursor.execute(query_professeur, values_professeur)
                #id_personne = cursor.lastrowid()

                connection.commit()
                print(f"Professeur {professeur.vacant} {professeur.matiere_enseigne} {professeur.prochain_cours}  {professeur.sujet_prochaine_reunion} ")
            except Error as e:
                print(f"Erreur lors de l'ajout du professeur: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def modifier(professeur):
        connection = Professeur.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                #modifie les informations
                query_professeur="""
                UPDATE professeurs
                    SET date_naissance = %s, ville = %s, prenom = %s, nom = %s, telephone = %s,vacant = %s,matiere_enseigne = %s, prochain_cours = %s, sujet_prochaine_reunion = %s
                    WHERE id = %s
                """
                
                values_professeur = (professeur.date_naissance, professeur.ville, professeur.prenom, professeur.nom, professeur.telephone, professeur.vacant, professeur.matiere_enseigne,professeur.prochain_cours,professeur.sujet_prochaine_reunion)
                cursor.execute(query_professeur, values_professeur)
                connection.commit()
                print(f"Professeur {professeur.prenom} {professeur.nom} modifié avec succès.")

            except Error as e:
                print(f"Erreur lors de l'ajout du professeur: {e}")
                connection.rollback()

            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def supprimer(identifiant):
        connection = connection = Professeur.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM professeurs WHERE id = %s"
                cursor.execute(query, (identifiant,))
                connection.commit()
                print(f"Professeur avec  l'id {identifiant} supprimé avec succès.")
            except Error as e:
                print(f"Erreur lors de la suppression de l'élève : {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def obtenir_professeur():
        connection = Professeur.create_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Requête SQL pour obtenir tous les élèves
                query = """
                    SELECT id, prenom, nom, date_naissance, ville, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion
                    FROM professeurs
                """
                cursor.execute(query)
                result = cursor.fetchall()

                # Vérifier que le résultat contient bien 9 colonnes
                if result:
                    return [
                        f"Professeur n° {row[0]} : {row[1]} {row[2]}, née le {row[3]} à {row[4]}, vacant: {row[6]}, matier_enseigne: {row[7]}, téléphone: {row[5]}, prochain_cours: {row[8]}, sujet_prochaine_reunion: {row[9]} "
                        for row in result
                    ]
                else:
                    return []

            except Error as e:
                print(f"Erreur lors de l'obtention des professeurs : {e}")
                return []
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def obtenir(identifiant):
        connection = Professeur.create_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Requête SQL pour obtenir un élève par matricule
                query = """
                    SELECT id, prenom, nom, date_naissance, ville, telephone, vacant, matier_enseigne, prochain_cours, sujet_prochaine_reunion
                    FROM professeurs
                    WHERE id = %s
                """
                cursor.execute(query, (identifiant,))
                row = cursor.fetchone()

                # Vérifier que le tuple a bien 8 colonnes
                if row :
                    professeur = Professeur(
                    date_naissance=row[0],
                    ville=row[1],
                    prenom=row[2],
                    nom=row[3],
                    telephone=row[4],
                    vacant=row[5],
                    matiere_enseigne=row[6],
                    prochain_cours=row[7],
                    sujet_prochaine_reunion=row[8]
                    )
                    return professeur
                    # and len(row) == 8 return f"Élève n° {row[0]} : {row[1]} {row[2]}, née le {row[3]} à {row[4]}, classe: {row[6]}, matricule: {row[7]}, téléphone: {row[5]}"
                else:
                    print(f"Erreur : Le nombre de colonnes récupérées est insuffisant ou le professeur avec l'identifiant {identifiant} n'existe pas.")
                    return None

            except Error as e:
                print(f"Erreur lors de l'obtention du professeur : {e}")
                return None
            finally:
                cursor.close()
                connection.close()


    @property 
    def id(self):
        return self.__id

    # Retourne la date de naissance de la personne.
    @property 
    def date_naissance(self):
        return self.__date_naissance
    
    @date_naissance.setter
    def date_naissance(self, date_naissance):
        self.__date_naissance = date_naissance

    # Retourne la ville de résidence de la personne.
    @property 
    def ville(self):
        return self.__ville
    
    @ville.setter
    def ville(self, ville):
        self.__ville = ville
    # Retourne le prénom de la personne.
    @property 
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    # Retourne le nom de la personne.
    @property
    def nom(self):
        return self.__nom 
    
    @nom.setter
    def nom(self, nom):
        self.__nom = nom   

    # Retourne le numéro de téléphone de la personne.
    @property
    def telephone(self):
        return self.__telephone    
    
    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone
    
    @property 
    def vacant(self):
        return self.__vacant
    
    @property 
    def matiere_enseigne(self):
        return self.__matiere_enseigne

    @property 
    def prochain_cours(self):
        return self.__prochain_cours
    
    @property 
    def sujet_prochaine_reunion(self):
        return self.__sujet_prochaine_reunion
    
    
  
    # Retourne un message indiquant la matière enseignée par le professeur.
    def enseigner(self, matiere):
        self.__matiere_enseigne = matiere
        return f"Enseigne la matière {self.__matiere_enseigne}"
    
    # Retourne un message indiquant le sujet du prochain cours à préparer.
    def preparerCours(self, cours):
        self.__prochain_cours = cours
        return f"Prépare le contenu d'un cours sur le sujet {self.__prochain_cours}"
    
    # Retourne un message indiquant le sujet de la prochaine réunion à laquelle le professeur doit assister.
    def assisterReunion(self, sujet):
        self.__sujet_prochaine_reunion = sujet
        return f"Doit assister à une reunion sur {self.__sujet_prochaine_reunion}"

    # Implémentation des méthodes CRUD
   # def ajouter(professeur):
        #Professeur.__professeurs.append(professeur)

    #def modifier(professeur):
        #for index, prof_existe in enumerate(Professeur.__professeurs):
           # if prof_existe.id == professeur.id:
               # Professeur.__professeurs[index] = professeur
                #return True 
        #return False

    #def supprimer(identifiant):
        #for index, prof in enumerate(Professeur.__professeurs):
           # if prof.id == identifiant:
               # del Professeur.__professeurs[index]
               # return True
        #return False

        #def obtenir_professeur():
           # return [str(prof) for prof in Professeur.__professeurs]

  # def obtenir(identifiant):
        #for prof in Professeur.__professeurs:
            #if prof.id == identifiant:
               # return prof
        #return None