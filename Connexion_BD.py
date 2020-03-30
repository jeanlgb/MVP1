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
        cursor.execute("""SELECT Numéro_patient FROM consultation WHERE Prénom = %(prenom)s AND Nom = %(nom)""", patient)
        rows = cursor.fetchall()
        conn.commit()
        return rows

    def selectionner_patient_num(self, numero):
        num = {"numero": numero}
        cursor.execute(
            """SELECT Prénom, Nom FROM donnees_administratives WHERE Numéro_patient = %(numero)s""",
            num)

        rows = cursor.fetchall()
        res = str(' '.join(map(str, rows[0])))
        conn.commit()
        return res

    # On récupére le numéro de la consultation
    def recuperer_numero_consultation(self, nom, prenom):  # select numéro patient puis numéro consultation
        cursor.execute("""SELECT Numéro_patient FROM consultation WHERE Prénom = prenom AND Nom = nom""")
        conn.commit()
        rows = cursor.fetchall()
        cursor.execute("""SELECT Numéro_consultation FROM consultation WHERE Nom = %(Numeroduscore)s""")
        conn.commit()


    def generer_numero(self, table):
        requete = "SELECT COUNT(*) from " + table
        cursor.execute(requete)
        tup = cursor.fetchall()
        res = int(''.join(map(str, tup[0])))
        res = res + 1
        return res

    def ajouter_pathologie_degeneratif(self, numero_Pathologie, numero_Patient, numero_Zone, contexte, finalite, niveaux, recalibrage, cote_Lateralite, arthrodese, commentaire):
        numero_Pathologie = self.generer_numero("pathologie_degeneratif")
        pathologie = {"numero_pathologie": numero_Pathologie, "numero_patient": numero_Patient, "numero_zone": numero_Zone, "contexte": contexte, "finalite": finalite, "niveaux": niveaux, "recalibrage": recalibrage, "cote_lateralite": cote_Lateralite, "arthrodese": arthrodese, "commentaire": commentaire}
        cursor.execute("""INSERT INTO pathologie_degeneratif (Numéro_pathologie, Numéro_patient, Numéro_zone, Contexte, Finalité_neurologique, Niveaux, Recalibrage, Coté_latéralité, Arthrodèse, Commentaire) VALUES(%(numero_pathologie)s, %(numero_patient)s, %(numero_zone)s,
        %(contexte)s, %(finalite)s, %(niveaux)s, %(recalibrage)s, %(cote_lateralite)s, %(arthrodese)s, %(commentaire)s)""", pathologie)
        conn.commit()

    def ajouter_pathologie_oncologie(self, numero_Pathologie, numero_Patient, numero_Zone, contexte, finalite, topographie, origine, niveaux, recalibrage, cote, arthrodese, commentaire):
        numero_Pathologie = self.generer_numero("pathologie_oncologie")
        pathologie = {"numero_pathologie": numero_Pathologie, "numero_patient": numero_Patient, "numero_zone": numero_Zone, "contexte": contexte, "finalite": finalite, "topographie": topographie, "origine": origine, "niveaux": niveaux, "recalibrage": recalibrage, "cote": cote, "arthrodese": arthrodese, "commentaire": commentaire}
        cursor.execute("""INSERT INTO pathologie_oncologie (Numéro_pathologie, Numéro_patient, Numéro_zone, Contexte, Finalité_neurologique, Topographie, Origine, Niveaux, Recalibrage, Coté, Arthrodèse, Commentaire) VALUES(%(numero_pathologie)s, %(numero_patient)s, %(numero_zone)s,
        %(contexte)s, %(finalite)s, %(topographie)s, %(origine)s, %(niveaux)s, %(recalibrage)s, %(cote)s, %(arthrodese)s, %(commentaire)s)""", pathologie)
        conn.commit()

    def ajouter_pathologie_traumatologique(self, numero_Pathologie, numero_Patient, numero_Zone, contexte, finalite, modalite, corporeal, osteosytnhese, foyer_niveau, recalibrage, cote, arthrodese, commentaire):
        numero_Pathologie = self.generer_numero("pathologie_traumatologique")
        pathologie = {"numero_pathologie": numero_Pathologie, "numero_patient": numero_Patient, "numero_zone": numero_Zone, "contexte": contexte, "finalite": finalite, "modalite": modalite, "corporeal": corporeal, "osteosytnhese": osteosytnhese, "foyer_niveau": foyer_niveau,"recalibrage": recalibrage, "cote": cote, "arthrodese": arthrodese, "commentaire": commentaire}
        cursor.execute("""INSERT INTO pathologie_traumatologique (Numéro_pathologie, Numéro_patient, Numéro_zone, Contexte, Finalité_neurologique, Modalité, Corporéal, Ostéosynthèse, Foyer_niveaux, Recalibrage, Coté, Arthrodèse, Commentaire) VALUES(%(numero_pathologie)s, %(numero_patient)s, %(numero_zone)s,
        %(contexte)s, %(finalite)s, %(modalite)s, %(corporeal)s, %(osteosytnhese)s, %(foyer_niveau)s, %(recalibrage)s, %(cote)s, %(arthrodese)s, %(commentaire)s)""", pathologie)
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
    def creation_consultation(self, numero_patient, commentaire,
                                  type):  # rajouter les dates et numéro de dossier Magic. Vérifier que le patient n'existe déja pas
            numero_consultation = self.generer_numero("consultation")
            consultation = {"Numéro_consultation": numero_consultation, "Numéro_patient": numero_patient, "commentaire": commentaire, "type": type}
            cursor.execute(
                """INSERT INTO consultation (Numéro_consultation, Numéro_patient, Commentaire, Type_consultation) VALUES(%(Numéro_consultation)s, %(Numéro_patient)s, %(commentaire)s, %(type)s)""",
                consultation)
            conn.commit()

        # Ajoute les scores. Elle regarde, pour un numéro patient donné, si il existe une consultation pour laquelle les scores ont TOUS la valeur null. Si oui, elle les remplit.
    def ajouter_scores(self, numeroMagic, glassman, evac, eval, ndi, mjoa, oswestry):
            cursor.execute(
                """UPDATE consultation SET Numéro_score_glassman = %s, Numéro_score_eva_cervical = %s, Numéro_score_eva_lombaire = %s, Numéro_score_ndi = %s, Numéro_score_mjoa = %s, Numéro_score_oswestry = %s WHERE Numéro_patient=%s AND Numéro_score_glassman IS NULL AND Numéro_score_eva_cervical IS NULL AND Numéro_score_eva_lombaire IS NULL AND Numéro_score_ndi IS NULL AND Numéro_score_mjoa IS NULL AND Numéro_score_oswestry IS NULL""",
                (glassman, evac, eval, ndi, mjoa, oswestry, numeroMagic))
            conn.commit()

            # permet d'ajouter une resuête dans la bd

    def ajouter_formuaire_recalibrage(self, numero_Pathologie,numero, voie, infos, hernie):
        numero_Pathologie = self.generer_numero("formulaire_recalibrage")
        pathologie = {"numero_pathologie": numero_Pathologie, "numero": numero, "voie": voie, "infos": infos, "hernie": hernie}
        cursor.execute("""INSERT INTO formulaire_recalibrage (Numéro_pathologie, Numéro_patient, Voie, Informations, Hernie_discale_associée) VALUES(%(numero_pathologie)s, %(numero)s, 
            %(voie)s, %(infos)s, %(hernie)s)""", pathologie)
        conn.commit()

    def ajouter_formuaire_arthrodese(self, numero_Pathologie, numero, voie, fixation, greffe):
        numero_Pathologie = self.generer_numero("formulaire_arthrodese")
        pathologie = {"numero_pathologie": numero_Pathologie, "numero": numero, "voie": voie, "fixation": fixation, "greffe": greffe}
        cursor.execute("""INSERT INTO formulaire_arthrodese (Numéro_pathologie, Numéro_patient, Voie, Fixation, Greffe) VALUES(%(numero_pathologie)s, %(numero)s, 
            %(voie)s, %(fixation)s, %(greffe)s)""", pathologie)
        conn.commit()

    def ajouter_traumato_niveaux(self, numero_Pathologie, numero, zone, cervicales, dorsales, lombaires, sacro):
        numero_Pathologie = self.generer_numero("nb_vertebre_traumato")
        pathologie = {"numero_pathologie": numero_Pathologie, "numero": numero, "zone": zone, "cervicales": cervicales, "dorsales": dorsales, "lombaires": lombaires, "sacro": sacro}
        cursor.execute("""INSERT INTO nb_vertebre_traumato (Numéro_pathologie, Numéro_patient, Zone, Cervicales, Dorsales, Lombaires, Sacro) VALUES(%(numero_pathologie)s, %(numero)s, 
            %(zone)s, %(cervicales)s, %(dorsales)s, %(lombaires)s, %(sacro)s)""", pathologie)
        conn.commit()


