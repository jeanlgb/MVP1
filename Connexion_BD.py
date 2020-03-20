import mysql.connector

cursor = None


class Connexion_DB:

    def connexion_DB(self):
        global conn
        global cursor
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="in-pecbd")
        cursor = conn.cursor()

    def creation_patient(self, numero, nom, prenom,
                         genre):  # rajouter les dates et numéro de dossier Magic. Vérifier que le patient n'existe déja pas
        patient = {"numero_pat": numero, "nom": nom, "prenom": prenom, "genre": genre}
        cursor.execute(
            """INSERT INTO donnees_administratives (Numéro_patient, Nom, Prénom, Genre) VALUES(%(numero_pat)s, %(nom)s, %(prenom)s, %(genre)s)""",
            patient)
        conn.commit()

    def verification_patient_pas_dans_bd(self, nom, prenom):  # Finir le where
        patient = {"nom": nom, "prenom": prenom}
        cursor.execute("""SELECT Numéro_patient, FROM donnees_administratives WHERE Prénom = prenom AND Nom = nom""",
                       patient)
        rows = cursor.fetchall()
        conn.commit()
        if rows is None:
            return True
        else:
            return False

    def selectionner_patient(self, nom, prenom):
        patient = {"nom": nom, "prenom": prenom}
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

    # On récupére le numéro de la consultation
    def recuperer_numero_consultation(self, nom, prenom):  # select numéro patient puis numéro consultation
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
        cursor.execute("""INSERT INTO score mjoa (Numéro_score, Résultat_MJOA) VALUES(%(numero)s, %(score)s)""",
                       score_mjoa)
        conn.commit()

    def ajouter_score_ndi(self, numero, score):
        score_ndi = {"numero": numero, "score": score}
        cursor.execute("""INSERT INTO score ndi (Numéro_score, Résultat_NDI) VALUES(%(numero)s, %(score)s)""",
                       score_ndi)
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

    def ajouter_pathologie_degeneratif(self, numero_Pathologie, numero_Patient, numero_Zone, contexte, finalite, niveaux, recalibrage, cote_Lateralite, arthrodese):
        numero_Pathologie = self.generer_numero("pathologie_degeneratif")
        pathologie = {"numero_pathologie": numero_Pathologie, "numero_patient": numero_Patient, "numero_zone": numero_Zone, "contexte": contexte, "finalite": finalite, "niveaux": niveaux, "recalibrage": recalibrage, "cote_lateralite": cote_Lateralite, "arthrodese": arthrodese}
        cursor.execute("""INSERT INTO pathologie_degeneratif (Numéro_pathologie, Numéro_patient, Numéro_zone, Contexte, Finalité_neurologique, Niveaux, Recalibrage, Coté_latéralité, Arthrodèse) VALUES(%(numero_pathologie)s, %(numero_patient)s, %(numero_zone)s,
        %(contexte)s, %(finalite)s, %(niveaux)s, %(recalibrage)s, %(cote_lateralite)s, %(arthrodese)s)""", pathologie)
        conn.commit()

    # permet d'ajouter une resuête dans la bd
    def ajouter_pathologie(self, numero, famille, zone):
        pathologie = {"numero": numero, "famille": famille, "zone": zone}
        cursor.execute("""INSERT INTO pathologie (Numéro_patient, familles, Zone_cervicale) VALUES(%(numero)s, 
        %(famille)s, %(zone)s)""", pathologie)
        conn.commit()

    def verification_num_patient_pas_dans_bd(num):
        patient = {"num": num}
        num = str(num)
        print(num)
        cursor.execute("""SELECT Nom, Prénom FROM donnees_administratives WHERE Numéro_patient = %(num)s""", patient)
        rows = cursor.fetchall()
        print(rows)
        if rows == []:
            return True
        else:
            return False

        # Créer la consultatio
    def creation_consultation(self, numero_patient,
                                  type):  # rajouter les dates et numéro de dossier Magic. Vérifier que le patient n'existe déja pas
            numero_consultation = self.generer_numero("consultation")
            consultation = {"Numéro_consultation": numero_consultation, "Numéro_patient": numero_patient, "type": type}
            cursor.execute(
                """INSERT INTO consultation (Numéro_consultation, Numéro_patient, Type_consultation) VALUES(%(Numéro_consultation)s, %(Numéro_patient)s, %(type)s)""",
                consultation)
            conn.commit()

        # Ajoute les scores. Elle regarde, pour un numéro patient donné, si il existe une consultation pour laquelle les scores ont TOUS la valeur null. Si oui, elle les remplit.
    def ajouter_scores(self, numeroMagic, glassman, evac, eval, ndi, mjoa, oswestry):
            cursor.execute(
                """UPDATE consultation SET Numéro_score_glassman = %s, Numéro_score_eva_cervical = %s, Numéro_score_eva_lombaire = %s, Numéro_score_ndi = %s, Numéro_score_mjoa = %s, Numéro_score_oswestry = %s WHERE Numéro_patient=%s AND Numéro_score_glassman IS NULL AND Numéro_score_eva_cervical IS NULL AND Numéro_score_eva_lombaire IS NULL AND Numéro_score_ndi IS NULL AND Numéro_score_mjoa IS NULL AND Numéro_score_oswestry IS NULL""",
                (glassman, evac, eval, ndi, mjoa, oswestry, numeroMagic))
            conn.commit()

            # permet d'ajouter une resuête dans la bd

    def ajouter_formuaire_recalibrage(self, numero, voie, infos, hernie):
        pathologie = {"numero": numero, "voie": voie, "infos": infos, "hernie": hernie}
        cursor.execute("""INSERT INTO formulaire_recalibrage (Numéro_patient, Voie, Informations, Hernie_discale_associée) VALUES(%(numero)s, 
            %(voie)s, %(infos)s, %(hernie)s)""", pathologie)
        conn.commit()

    def ajouter_formuaire_arthrodese(self, numero, voie, fixation, greffe):
        pathologie = {"numero": numero, "voie": voie, "fixation": fixation, "greffe": greffe}
        cursor.execute("""INSERT INTO formulaire_arthrodese (Numéro_patient, Voie, Fixation, Greffe) VALUES(%(numero)s, 
            %(voie)s, %(fixation)s, %(greffe)s)""", pathologie)
        conn.commit()


