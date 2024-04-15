import random
import subprocess
import os
from fractions import Fraction
import csv
from baseExo import *

def getEleve(fichier):
    """Récupère dans une liste la première colonne d'un CSV sauf la première ligne

    Args:
        fichier (str): Le nom du fichier avec l'extension
                        exemple : 'Export 2GT1.csv'
    """    
    directory = os.path.dirname(__file__)
    print(directory)
    listeEleves=[]
    with open(directory+'\\'+fichier, newline='', encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in spamreader:
            listeEleves.append(row[0])
    listeEleves = listeEleves[1:]
    return(listeEleves)

def main():
    listeEleves = getEleve('Export CSV TSTMG1.csv')
    for eleve in listeEleves:
        print(eleve.replace(' ','_'))
    """structure définie la structure d'un devoir
        "Niveau":"ExoName"
        les niveaux sont :
            TSTMG, 1STMG, 2GT, 3IEME, 4IEME, 5IEME, 6IEME
    """    
    structure = [ ["Level", "ExoName", "nombre d'exercices"]
                 ["TSTMG", "Proba", "1"],
                 ["TSTMG", "Evolution", "1"],
                 ["TSTMG", "EvolutionSuite", "1"],
                 ["TSTMG", "Dérivation", "1"],
                 
                 ]
    
    
if __name__=="__main__":
    main()