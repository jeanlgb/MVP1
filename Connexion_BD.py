import mysql.connector

cursor = None
class Connexion_DB:

    def connexion_DB(self):
        global conn
        global cursor
        conn = mysql.connector.connect(host="localhost",user="root",password="", database="in-pecbd")
        cursor = conn.cursor()

    def creation_patient(self, numero, nom, prenom, genre): #rajouter les dates et numéro de dossier Magic. Vérifier que le patient n'existe déja pas
        patient = {"numero_patient" : numero, "nom" : nom, "prenom" : prenom, "genre" : genre}
        cursor.execute("""INSERT INTO donnees_administratives (Numéro_patient,Nom, Prénom, Genre) VALUES(%(
        numero_patient)s, %(nom)s, %(prenom)s), %(genre)s)""", patient)
        conn.commit()

    def verification_patient_pas_dans_bd(self,nom, prenom): #Finir le where
        patient = {"nom": nom, "prenom" : prenom}
        cursor.execute("""SELECT Numéro_patient, FROM donnees_administratives WHERE Prénom = prenom AND Nom = nom""", patient)
        rows = cursor.fetchall()
        conn.commit()
        if rows is None:
            return True
        else :
            return False

    def selectionner_patient(self, nom, prenom):
        patient = {"nom": nom, "prenom" : prenom}
        cursor.execute("""SELECT Numéro_patient FROM consultation WHERE Prénom = prenom AND Nom = nom""", patient)
        rows = cursor.fetchall()
        conn.commit()
        return rows

    def selectionner_patient_num(self, numero):
        num = {"numero": numero}
        cursor.execute("""SELECT Nom, Prénom FROM consultation WHERE Numéro_patient = numero""", num)
        rows = cursor.fetchall()
        conn.commit()
        return rows

    #On récupére le numéro de la consultation
    def recuperer_numero_consultation(self, nom, prenom): #select numéro patient puis numéro consultation
        cursor.execute("""SELECT Numéro_patient FROM consultation WHERE Prénom = prenom AND Nom = nom""")
        conn.commit()
        rows = cursor.fetchall()
        cursor.execute("""SELECT Numéro_consultation FROM consultation WHERE Nom = %(Numeroduscore)s""")
        conn.commit()

    def ajouter_score_Glassman(self, numero, score):
        score_glassman = {"numero": numero, "score": score}
        cursor.execute("""INSERT INTO score eva cervical (Numéro_score, Résultat_EVAC) VALUES(%(numero)s, 
        %(score)s)""", score_glassman)
        conn.commit()

    def ajouter_score_EVAC(self, numero, score):
        score_evac = {"numero": numero, "score": score}
        cursor.execute("""INSERT INTO score eva cervical (Numéro_score, Résultat_EVAC) VALUES(%(numero)s, 
        %(score)s)""", score_evac)
        conn.commit()

    def ajouter_score_EVAL(self, numero, score):
        score_eval = {"numero": numero, "score": score}
        cursor.execute("""INSERT INTO score eva lombaire (Numéro_score, Résultat_EVAL) VALUES(%(numero)s, 
        %(score)s)""", score_eval)
        conn.commit()

    def ajouter_score_mjoa(self, numero, score):
        score_mjoa = {"numero": numero, "score": score}
        cursor.execute("""INSERT INTO score mjoa (Numéro_score, Résultat_MJOA) VALUES(%(numero)s, %(score)s)""", score_mjoa)
        conn.commit()

    def ajouter_score_ndi(self, numero, score):
        score_ndi = {"numero": numero, "score": score}
        cursor.execute("""INSERT INTO score ndi (Numéro_score, Résultat_NDI) VALUES(%(numero)s, %(score)s)""", score_ndi)
        conn.commit()

    def ajouter_score_oswestry(self, score):
        numero = self.generer_numero("score_oswestry")
        score_oswestry = {"numero": numero, "score": score}
        cursor.execute("""INSERT INTO score_oswestry (Numero_score, Resultat_Oswestry) VALUES(%(numero)s, 
        %(score)s)""", score_oswestry)
        conn.commit()

    def generer_numero(self, table):
        requete = "SELECT COUNT(*) from " + table
        cursor.execute(requete)
        tup = cursor.fetchall()
        res = int(''.join(map(str, tup[0])))
        res = res + 1
        return res

    def ajouter_pathologie(self, numero_Patient, numero_Pathologie, numero_Zone, contexte, finalite, niveaux, recalibrage, cote_Lateralite, cote_GD, arthrodese):

        pathologie = {"numero_patient": numero_Patient, "numero_pathologie": numero_Pathologie, "numero_zone": numero_Zone, "contexte":contexte, "finalite":finalite, "niveaux":niveaux, "recalibrage":recalibrage, "cote_lateralite": cote_Lateralite, "cote_GD":cote_GD, "arthrodese": arthrodese}
        cursor.execute("""INSERT INTO pathologie (Numéro_pathologie, Numéro_patient, Numéro_zone, Contexte, Finalité_neurologique, Niveaux, recalibrage, Coté_latéralité, Coté_GD, Arthrodèse) VALUES(%(numero_pathologie)s, %(numero_patient)s, %(numero_zone)s
        %(contexte)s, %(finalite)s), %(niveaux)s, %(recalibrage)s, %(cote_lateralite)s, %(cote_GD)s, %(arthrodese)s)""", pathologie)
        conn.commit()




