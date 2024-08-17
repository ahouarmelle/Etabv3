import mysql.connector
from mysql.connector import Error
#from models.personne import Personne
from Eleve.ICrudEleve import ICRUDEleve

class Eleve(ICRUDEleve):
    """
    Classe représentant un élève, héritant de la classe Personne et de la classe ICRUDEleve.
    """
    #__eleves = []

    def __init__(self,date_naissance, ville, prenom, nom, telephone, classe, matricule):
        #super().__init__(date_naissance, ville, prenom, nom, telephone)
        self.__date_naissance = date_naissance
        self.__ville = ville
        self.__prenom = prenom
        self.__nom = nom
        self.__telephone = telephone
        self.__classe = classe
        self.__matricule = matricule

    #def __str__(self):
        #return (f" Eleve {super().__str__()}), classe: {self.__classe} et matricule: {self.__matricule}")

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
    def modifier(eleve):
        connection = Eleve.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                #modifie les informations
                query_eleve="""
                UPDATE eleves
                    SET date_naissance = %s, ville = %s, prenom = %s, nom = %s, telephone = %s, classe = %s
                    WHERE matricule = %s
                """
                
                values_eleve = (eleve.date_naissance, eleve.ville, eleve.prenom, eleve.nom, eleve.telephone,eleve.classe,eleve.matricule)
                cursor.execute(query_eleve, values_eleve)
                connection.commit()
                print(f"Élève {eleve.prenom} {eleve.nom} modifié avec succès.")

            except Error as e:
                print(f"Erreur lors de l'ajout de l'élève: {e}")
                connection.rollback()

            finally:
                cursor.close()
                connection.close()


    @staticmethod
    def ajouter(eleve):
        connection = Eleve.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query_eleve = """
                    INSERT INTO eleves (date_naissance, ville, prenom, nom, telephone,classe,matricule)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values_eleve = (eleve.date_naissance, eleve.ville, eleve.prenom, eleve.nom, eleve.telephone, eleve.classe, eleve.matricule)
                cursor.execute(query_eleve, values_eleve)#EXECUTE LA REQUETE
                connection.commit() #VALIDER LA TRANSACTION

                #Eleve.__eleves.append(eleve)  # Ajout de l'élève à la liste en mémoire
                print(f"Élève {eleve.prenom} {eleve.nom} ajouté avec succès.")
            except Error as e:
                print(f"Erreur lors de l'ajout de l'élève: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        else:
            print("Erreur de connexion, impossible d'ajouter l'élève.")

    @staticmethod
    def supprimer(identifiant):
        connection = connection = Eleve.create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM eleves WHERE matricule = %s"
                cursor.execute(query, (identifiant,))
                connection.commit()
                print(f"Élève avec matricule {identifiant} supprimé avec succès.")
            except Error as e:
                print(f"Erreur lors de la suppression de l'élève : {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def obtenir_eleve():
        connection = Eleve.create_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Requête SQL pour obtenir tous les élèves
                query = """
                    SELECT id, prenom, nom, date_naissance, ville, telephone, classe, matricule
                    FROM eleves
                """
                cursor.execute(query)
                result = cursor.fetchall()

                # Vérifier que le résultat contient bien 8 colonnes
                if result:
                    return [
                        f"Élève n° {row[0]} : {row[1]} {row[2]}, née le {row[3]} à {row[4]}, classe: {row[6]}, matricule: {row[7]}, téléphone: {row[5]}"
                        for row in result
                    ]
                else:
                    return []

            except Error as e:
                print(f"Erreur lors de l'obtention des élèves : {e}")
                return []
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def obtenir(identifiant):
        connection = Eleve.create_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Requête SQL pour obtenir un élève par matricule
                query = """
                    SELECT id, prenom, nom, date_naissance, ville, telephone, classe, matricule
                    FROM eleves
                    WHERE matricule = %s
                """
                cursor.execute(query, (identifiant,))
                row = cursor.fetchone()

                # Vérifier que le tuple a bien 8 colonnes
                if row :
                    eleve = Eleve(
                    date_naissance=row[0],
                    ville=row[1],
                    prenom=row[2],
                    nom=row[3],
                    telephone=row[4],
                    classe=row[5],
                    matricule=row[6]
                    )
                    return eleve
                    # and len(row) == 8 return f"Élève n° {row[0]} : {row[1]} {row[2]}, née le {row[3]} à {row[4]}, classe: {row[6]}, matricule: {row[7]}, téléphone: {row[5]}"
                else:
                    print(f"Erreur : Le nombre de colonnes récupérées est insuffisant ou l'élève avec le matricule {identifiant} n'existe pas.")
                    return None

            except Error as e:
                print(f"Erreur lors de l'obtention de l'élève : {e}")
                return None
            finally:
                cursor.close()
                connection.close()



    #@property 
    #def get_matricule(self):
        #return self.__matricule
    
    #@property 
    #def get_classe(self):
        #return self.__classe
    
    #def set_classe(self, classe):
        #self.__classe = classe            

    #def set_matricule(self, matricule):
        #self.__matricule = matricule
    
   
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
    def classe(self):
        return self.__classe
    
    @classe.setter
    def classe(self, classe):
        self.__classe = classe

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, matricule):
        self.__matricule = matricule

    #def modifier(self, eleve):
        #for index, eleve_existe in enumerate(Eleve.__eleves):
            #if eleve_existe.get_matricule() == eleve.get_matricule():
                #Eleve.__eleves[index] = eleve
                #return True
        #return False
    
    #def ajouter(eleve):
        #Eleve.__eleves.append(eleve)
        

    #def supprimer(self,identifiant):
        #for eleve in Eleve.__eleves:
            #if eleve.get_matricule() == identifiant:
                #del Eleve.__eleves[index]
                #Eleve.__eleves.remove(eleve)
                #return True
        #return False
    # Obtenir les élèves
    #def obtenirEleve():
        #for eleve in Eleve.__eleves:
            #print(eleve)


    # Obtenir un élève par son id
    #def obtenir(identifiant):
        #for eleve in Eleve.__eleves:
            #if eleve.get_matricule == identifiant:
                #return eleve
        #return None
    
  
