#!/usr/bin/env python3

'''
$ ./named_tuples.py 
<__main__.Joueur_classic object at 0x7efd6a811208>
Grenier
Joueur(nom='Grenier', age=31)
Grenier
'''

class Joueur_classic:
    def __init__(self,nom, age):
        self.nom = nom
        self.age = age
jdg_classic = Joueur_classic('Grenier', 31)
print(jdg_classic)
print(jdg_classic.nom)

from collections import namedtuple
Joueur_nt = namedtuple('Joueur', ['nom', 'age'])
jdg_nt = Joueur_nt('Grenier', 31)
print(jdg_nt)
print(jdg_nt.nom)
