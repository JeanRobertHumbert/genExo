import random
import subprocess
import os
from fractions import Fraction

from baseExo import *

def appendFile(FileToInsert, Destination):
    with open(FileToInsert, encoding='utf-8') as infile:
        for line in infile:
            Destination.write(line)

for i in range(0,1):
    with open('DCSujet-'+str(i)+'.tex', 'w', encoding='utf-8') as outfile:
        with open('DCSujetCorrection-'+str(i)+'.tex', 'w', encoding='utf-8') as correctionfile:
            genCode = str(random.randint(1111111111,9999999999))
            outfile.write(header(titre="Devoir Commun 17 Février 2022", genCode=genCode, Correction=""))
            correctionfile.write(header(titre="Devoir Commun 17 Février 2022", genCode=genCode, Correction="Correction"))
            
            exo,correction = exoProba()
            outfile.write(exo)
            correctionfile.write(correction)
            
            exo,correction = exoEvolution()
            outfile.write(exo)
            correctionfile.write(correction)
            
            exo,correction = exoEvolSuite()
            outfile.write(exo)
            correctionfile.write(correction)
            
            exo,correction = exoDerivation(genCode)
            outfile.write(exo)
            correctionfile.write(correction)
            
            outfile.write(ender())
            correctionfile.write(ender())

    subprocess.call('pdflatex DCSujet-'+str(i)+'.tex')
    subprocess.call('pdflatex DCSujet-'+str(i)+'.tex')
    subprocess.call('pdflatex DCSujetCorrection-'+str(i)+'.tex')
    subprocess.call('pdflatex DCSujetCorrection-'+str(i)+'.tex')
    os.startfile('DCSujet-'+str(i)+'.pdf')
    os.startfile('DCSujetCorrection-'+str(i)+'.pdf')
    directory = os.path.dirname(__file__)
    os.remove('DCSujet-'+str(i)+'.log')
    os.remove('DCSujet-'+str(i)+'.aux')
    # os.remove('DCSujet-'+str(i)+'.dvi')
    # os.remove(directory+"\\"+genCode+'-fig-C.png')
    # os.remove(directory+"\\"+genCode+'-fig-C\'.png')
    
    os.remove('DCSujetCorrection-'+str(i)+'.log')
    os.remove('DCSujetCorrection-'+str(i)+'.aux')
    # os.remove('DCSujetCorrection-'+str(i)+'.dvi')
# exoEvolution()