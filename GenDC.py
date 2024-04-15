import random
import subprocess
import os
import shutil
from fractions import Fraction
import csv
from baseExo import *
import sqlite3 as sl

import GT2nd
import STMG1er


def getEleve(fichier):
    """Récupère dans une liste la première colonne d'un CSV sauf la première ligne

    Args:
        fichier (str): Le nom du fichier avec l'extension
                        exemple : 'Export TSTMG1.csv'
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

def getEleve1(fichier):
    """Récupère dans une liste la première colonne d'un CSV sauf la première ligne

    Args:
        fichier (str): Le nom du fichier avec l'extension
                        exemple : 'Export TSTMG1.csv'
    """    
    directory = os.path.dirname(__file__)
    listeEleves=[]
    with open(directory+'\\'+fichier, newline='', encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in spamreader:
            listeEleves.append([row[0] , row[2]] )
    listeEleves = listeEleves[1:]
    usersToCreate = []
    for eleve in listeEleves:
        student = eleve[0].split()
        firstname = student[-1]
        del student[-1]
        lastname = ' '.join(student)
        password = eleve[1].replace('/', '')
        usersToCreate.append([lastname , firstname , password])
    print(usersToCreate)

def genDocument(classeName="", path="", eleve=""):
    """Génére un sujet et sa correction

    Args:
        eleve (str, optional): le nom: de l'élève s'il y a lieu. Defaults to "".
    """    
    if path=="":
        path = os.path.dirname(__file__)

    genCode = str(random.randint(1111111111,9999999999))
    racineNom = "202403"
    fileSujet = path + "\\" + racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.tex'
    fileSujetPDF = path + "\\" + racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.pdf'
    fileCorrection = path + "\\" + racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.tex'
    fileCorrectionPDF = path + "\\" + racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.pdf'
    fileSujetDest = path + "\\" + classeName + "\\" + racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.tex'
    fileCorrectionDest = path + "\\" + classeName + "\\" + racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.tex'
    fileSujetPDFDest = path + "\\" + classeName + "\\" + racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.pdf'
    fileCorrectionPDFDest = path + "\\" + classeName + "\\" + racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.pdf'
    # fileLogSujet = path + "\\" + racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.log'
    # fileAuxSujet = path + "\\" + racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.aux'
    # fileLogCorrection = path + "\\" + racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.log'
    # fileAuxCorrection = path + "\\" + racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.aux'
    print(eleve)
    points = 79
    bonus = 6
    corpsSujet = r""""""
    corpsCorrection = r""""""
    with open(fileSujet, 'w', encoding='utf-8') as outfile:
        with open(fileCorrection, 'w', encoding='utf-8') as correctionfile:
            consignes = [
                r"""La calculatrice est autorisée""",
                r"""Le téléphone n'est pas autorisé même comme calculatrice !!!""",
                r"""Le bonus est accordé en fonction de la qualité de rédaction"""
            ]
            headerSujet = header(eleve=eleve, titre="Baccalauréat Blanc Mars 2024 "+classeName, level=classeName, genCode=genCode, duree="2 heures", points=points, bonus=bonus, consignes=consignes)
            headerCorrection = header(eleve=eleve, titre="Baccalauréat Blanc Mars 2024 "+classeName, level=classeName, genCode=genCode, duree="2 heures", points=points, bonus=bonus, Correction="Correction",consignes=consignes)
            outfile.write(headerSujet)
            correctionfile.write(headerCorrection)
            
            
# ---- Evolution & Proportion
            
            # exo,correction = exoPourcentage2ndv1()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            # exo,correction = exoPourcentage2ndv2()
            # outfile.write(exo)
            # correctionfile.write(correction)
#------            
            # exo,correction = exoProportion(n=4)
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            # exo,correction = exoEvolutionSimple(n=4)
            # outfile.write(exo)
            # correctionfile.write(correction)
                        
            # exo,correction = exoEvolSchemas()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            # exo,correction = exoEvolConsoEau()
            # outfile.write(exo)
            # correctionfile.write(correction)
#------
            # exo,correction = exoEvolution()
            # outfile.write(exo)
            # correctionfile.write(correction)

# ---- Probabilité
            
            # exo,correction = exoProba1()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            exo,correction = STMG1er.exoProba()
            outfile.write(exo)
            correctionfile.write(correction)
            exo,correction = STMG1er.exoProba1()
            outfile.write(exo)
            correctionfile.write(correction)

            # exo,correction = exoSecondDegreSansDelta()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # exo,correction = genfonctionAffine()
            # outfile.write(exo)
            # correctionfile.write(correction)

            
            # addClearPage(outfile, correctionfile)

            # exo,correction = exoAffineReprEtExpression()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # addClearPage(outfile, correctionfile)

            # exo,correction = exoResoudreEqProduitN2()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # exo,correction = exoAffineSigneVariation()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # addClearPage(outfile, correctionfile)
            
            # exo,correction = STMG1er.exoAffineBourse()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            # exo, correction = STMG1er.lectureGraphiqueAffine()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            # exo,correction = exoVecteurN1(genCode)
            # outfile.write(exo)
            # correctionfile.write(correction)

            # exo,correction = exoVecteurN0()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # exo,correction = exoPourcentage2ndv1()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # exo,correction = exoPourcentage2ndv2()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # exo,correction,pts = exoDerivationN1()
            # corpsSujet += exo
            # corpsCorrection += correction
            # points = points + pts

            # exo,correction,pts = exoDerivationN2()
            # corpsSujet += exo
            # corpsCorrection += correction
            # points = points + pts
            
            exo,correction,pts = exoDerivation()
            corpsSujet += exo
            corpsCorrection += correction
            # points = points + pts

            # exo,correction = exoResoudreEqProduitN1()
            # outfile.write(exo)
            # correctionfile.write(correction)

            # exo,correction = exoVecteurAffine2nd()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
    # ---- Suites
            # exo,correction = addClearPage()
            # outfile.write(exo)
            # correctionfile.write(correction)
            # exo,correction = suiteGenerale()
            # outfile.write(exo)
            # correctionfile.write(correction)
    # Evaluation -------------------------------------------------------------------------------------------------------

            # exo, correction = exoQCM3ieme(n=10)
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            # exo, correction = STMG1er.lectureGraphiqueAffine()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            exo, correction = STMG1er.polyDegre2_Factor()
            outfile.write(exo)
            correctionfile.write(correction)
            
            # exo, correction = STMG1er.polyDegre2_DisN1()
            # outfile.write(exo)
            # correctionfile.write(correction)
            
            exo,correction = addClearPage()
            outfile.write(exo)
            correctionfile.write(correction)
            
            exo, correction, point = exoDerivationN1(n=4)  # Dérivation de polynômes
            outfile.write(exo)
            correctionfile.write(correction)
            
            exo,correction = suiteGenerale()
            outfile.write(exo)
            correctionfile.write(correction)
            
            
    # Test -------------------------------------------------------------------------------------------------------------
            # for i in range(5):
            #     exo,correction = ThalesPythagore()
            #     outfile.write(exo)
            #     correctionfile.write(correction)
    # Rappel de cours --------------------------------------------------------------------------------------------------
            # exo,correction = addClearPage()
            # outfile.write(exo)
            # correctionfile.write(correction)
            # exo = rappelTSTMG()
            # outfile.write(exo)
            # correctionfile.write(correction)
    # ------------------------------------------------------------------------------------------------------------------
            # ajuster le bonus pour avoir un total de points qui tombe sur un multiple de 10

            outfile.write(corpsSujet)
            correctionfile.write(corpsCorrection)
            outfile.write(ender(rappel=False))
            correctionfile.write(ender(rappel=False))
    # On appel 2 fois la compilation pour que les numéros de pages soient correctes
    subprocess.call('pdflatex -quiet '+fileSujet)
    subprocess.call('pdflatex -quiet '+fileSujet)
    # subprocess.call('pdflatex -quiet '+racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.tex >> nul')
    subprocess.call('pdflatex -quiet '+fileCorrection)
    subprocess.call('pdflatex -quiet '+fileCorrection)
    # subprocess.call('pdflatex -quiet '+racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.tex')
    # os.startfile('2022DS-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.pdf')
    # os.startfile('2022DS-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.pdf')
    if classeName!="":
        shutil.move(fileSujet, fileSujetDest)
        shutil.move(fileCorrection, fileCorrectionDest)
        shutil.move(fileSujetPDF, fileSujetPDFDest)
        shutil.move(fileCorrectionPDF, fileCorrectionPDFDest)

    os.remove(racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.log')
    os.remove(racineNom+'-Sujet-'+eleve.replace(' ','_')+'-'+genCode+'.aux')
    os.remove(racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.log')
    os.remove(racineNom+'-Correction-'+eleve.replace(' ','_')+'-'+genCode+'.aux')

def genDocByEleve(classeName, path, listeEleves):
    """Génération d'un sujet et sa correction par élève.

    Args:
        listeEleves (list): doit contenir une liste de chaîne de caractère ( le nom des élèves)
    """    
    for eleve in listeEleves:
        genDocument(classeName, path, eleve)
        
def genNDoc(n=1):
    for i in range(0,n):
        genDocument()

if __name__ == '__main__':
    directory = os.path.dirname(__file__)
    classes = [
        ["","6",""],
        ["1STMG1","","1STMG1.csv"],
        ["1STMG2","","1STMG2.csv"],
        ["TSTMG1","","TSTMG1.csv"],
        ["TSTMG2","","TSTMG2.csv"],
        ["TSTMG3","","TSTMG3.csv"],
    ]

    for c in classes:
        classeName = c[0]
        doIt = c[1]
        classeFile = c[2]
        if doIt=="x":           #   Gestion d'une classe
            path = directory    # + "\\" + classeName
            isExist = os.path.exists(path)
            if not isExist:
                os.makedirs(path)
            listeEleves = getEleve(classeFile)          # On récupère la liste des élèves
            genDocByEleve(classeName, path, listeEleves)
        if classeName=="" and doIt!="":      #   Gestion des sujets génériques
            genNDoc(n=int(doIt))
    # genNDoc(n=1)