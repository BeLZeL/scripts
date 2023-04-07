from voiture import Voiture
from citroen import Citroen

class CitroenDs(Voiture, Citroen):
    def __init__(self):
        Voiture.__init__(self)
        Citroen.__init__(self)
        self.modele = "DS de 1967"

if __name__ == "__main__":
    ma_ds = CitroenDs()
    print(ma_ds.marque)
    print(ma_ds.modele)
    print(ma_ds.type_suspension)
    print(ma_ds.statut_moteur())
    ma_ds.start_moteur()
    print(ma_ds.statut_moteur())
