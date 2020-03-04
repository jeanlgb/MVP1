class Utilisateur:

    listeUtilisateurs = []

    def __init__(self, nomUtilisateur, mdp, type):
        self.nomUtilisateur = nomUtilisateur
        self.mdp = mdp
        self.type = type

    def creerUtilisateur(self):
        listeUtilisateurs.append(Utilisateur)

    def get_nom(self):
        return self.nomUtilisateur

    def get_mdp(self):
        return self.mdp

    def get_type(self):
        return self.type

u1 = Utilisateur('g', '1', 'Secretaire')
u2 = Utilisateur('o', '2', 'Medecin')
u3 = Utilisateur('j', '3', 'Medecin')

listeUtilisateurs = [u1, u2, u3]


for i in listeUtilisateurs:
     print(Utilisateur.get_nom(i))