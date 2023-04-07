from voiture import Voiture

class BondBug(Voiture):
    def __init__(self):
        Voiture.__init__(self)
        self.marque = "Bond"
        self.modele = "Bug"
        self.nombre_roues = 3
        self.nombre_fauteuils = 2
        print(self.statut_moteur())

    def start_moteur(self):
        # Sur la ligne suivante de code, si nous ne stipulons pas expressement qu'on adresse
        # l'attribut de Voiture, Python comprendra qu'on fait reference a BondBug.start_moteur
        # a cause de la surcharge. Le self est la car nous appelons l'objet concerne de la classe
        # mere
        state = Voiture.start_moteur(self)
        print("Statut du moteur: %s" % (state))

    def stop_moteur(self):
        state = Voiture.stop_moteur(self)
        print("Statut du moteur: %s" % (state))

if __name__ == "__main__":
    my_bug = BondBug()
    my_bug.start_moteur()
    my_bug.stop_moteur()
