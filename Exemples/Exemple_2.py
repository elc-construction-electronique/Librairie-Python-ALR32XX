"""
    ************************************************************************
    *  fichier  : ALR32XX.py                                               *
    *  Fonction : Classe principale                                        *
    *  Produit  : ALR32XX                                                  *
    *  Device   :                                                          *
    *                                                                      *
    *  Copyright     : ELC, tous droits reservés                           *
    *  Auteur        : JY MOUBA                                            *
    *  Date creation : 01 aout 2021                                        *
    *  Version MAJ   : 01                                                  *
    *                                                                      *
    *  Historique :                                                        *
    *                                                                      *
    *  Version     Date       Auteur         Objet                         *
    *  ------------------------------------------------------------------- *
    *    1.0    27/09/2021    Y.M     Édition originale                    *
    ************************************************************************
"""

"""
    - numpy: package fondamental pour le calcul scientifique en Python. 
    Il s'agit d'une bibliothèque Python qui fournit un objet tableau multidimensionnel, 
    divers objets dérivés (tels que des tableaux et des matrices masqués) et un assortiment 
    de routines pour des opérations rapides sur des tableaux, notamment mathématiques, logiques, 
    manipulation de forme, tri, sélection, E/S , transformées de Fourier discrètes, algèbre linéaire de base, 
    opérations statistiques de base, simulation aléatoire et bien plus encore.
    lien=https://numpy.org/doc/stable/user/whatisnumpy.html

    - matplotlib: c'est une librairie qui permet de tracer des graphes
    lien=https://matplotlib.org/ 
"""

#Importation des bibliothèques
import time
import sys
import math
import numpy as np 
import matplotlib.pyplot as plt


#Commande pour permettre à python de lire le contenu de la libraiire ALR32XX.
sys.path.insert(0, "C:\\Users\\stagiaire2\\Desktop\\GitHub\\Librairie-Python-ALR32XX") #Lieu où se trouve la libririre ALR32XX

#Importation de la bibliothèque ALR32XX
from ALR32XX import*

#Définition des varibales
alim=ALR32XX('ALR3203')
X=[ ]
Y=[ ]

print(" ")
print("Envoie des valeurs : ")
while 1:
    for i in range (0, 360):
        temp=math.sin(i*3.14/180)
        temp_=(temp*16)+16
        alim.Ecrire_tension(temp_)
        print(temp)
    








