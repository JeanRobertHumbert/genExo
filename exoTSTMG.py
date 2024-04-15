import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

from baseMaths import *




def suiteAnalyseComp():
    C0 = random.randint(20,25)*10000
    tx = random.randint(2,6)
    txEvol = 100+tx
    anDeb = random.randint(2023,2025)
    nMax = random.randint(3,5)
    exo=r"""
    """
    correction=r"""
            \Question Une entreprise a commencé son activité en """+str(anDeb)+r""" avec un chiffre d'affaires de """+str(C0)+r""" euros. Chaque année, son chiffre d'affaires augmente de """+str(tx)+r"""%.
            \begin{parts}
                \Part Exprimez le chiffre d'affaires de l'entreprise en fonction de l'année n à l'aide d'une suite. L'année """+str(anDeb)+r""" correspond à n=0.\\
                    \color{red}{Le chiffre d'affaires peut être modélisé par une suite géométrique où chaque terme est égal à """+str(txEvol)+r"""\% du précédent. La formule générale de cette suite est 
                    \begin{center}
                        $C_n="""+str(C0)+r""" \times """+f"{txEvol/100:.2f}"+r"""^n$\\
                        avec n le nombre d'années après 2020.
                    \end{center}
                    }\color{black}
                
                \Part Calculez le chiffre d'affaires de l'entreprise pour les années 2021, 2022 et 2023.
                    \color{red}{
                    \begin{itemize}
                    \item Pour 2021 $(n=1)$ , $C_1="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^1 = 210000$
                    \item Pour 2022 $(n=2)$ , $C_2="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^2 \approx 220500$
                    \item Pour 2023 $(n=3)$ , $C_3="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^3 \approx 231525$
                    \end{itemize}
                    }\color{black}
                \Part Calculez le taux d'évolution global du chiffre d'affaires entre 2020 et 2023.\\
                    \color{red}{
                    Le taux d'évolution global de """+str(anDeb)+r""" à 2023 est donné par $\dfrac{C_3-C_0}{C_0}$. Donc : 
                    \begin{center}
                        $\dfrac{231525-"""+str(C0)+r"""}{"""+str(C0)+r"""}\approx 0.1576$ ou $15,76\%$
                    \end{center}
                    }\color{black}
                \Part Comparez ce taux d'évolution avec la somme des taux d'évolution annuels. Expliquez pourquoi ces deux taux sont différents.\\
                \color{red}{
                La somme des taux annuels est simplement $3 \times """+str(nMax)+r"""\%=15\%$. Cette valeur est différente du taux global car le taux d'évolution global considère l'effet cumulatif des augmentations annuelles (c'est le principe des intérêts composés).
                }\color{black}
                \Part Supposons maintenant que l'augmentation annuelle du chiffre d'affaires devient linéaire, avec une augmentation de 10 000 euros chaque année à partir de 2024. Modélisez cette situation à l'aide d'une fonction affine.\\
                \color{red}{
                La nouvelle situation peut être modélisée par une fonction affine :\\
                \begin{center}
                    $C(n)=C_3+10000\times (n-3)$, où n est le nombre d'années après """+str(anDeb)+r""".
                \end{center}
                }\color{black}
                \Part Calculez le chiffre d'affaires prévu pour l'année """+str(anDeb+nMax)+r""" avec cette nouvelle modèle.
                \color{red}{
                \begin{itemize}
                    \item Pour 2025 $(n=5)$: $C(5)=231525+10000\times (5-3)=251525$ euros.
                \end{itemize}
                }\color{black}
                \Part Comparez les chiffres d'affaires prévus pour """+str(anDeb+nMax)+r""" en utilisant les deux modèles (suite géométrique et fonction affine). Lequel est plus avantageux pour l'entreprise ?\\
                \color{red}{
                Avec le modèle géométrique, le chiffre d'affaires en 2025 serait :
                \begin{center}
                    $C_5="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^5\approx 255526$ euros.
                \end{center}
                Avec la fonction affine, le chiffre d'affaires en 2025 est de 251525 euros.\\
                }\color{black}
                \Part Discutez de la pertinence de chaque modèle dans le contexte d'une prévision à long terme.\\
                \color{red}{
                Le modèle géométrique prévoit un chiffre d'affaires légèrement plus élevé en 2025. Cependant, le modèle linéaire pourrait être plus réaliste sur le long terme, car une croissance exponentielle indéfinie est souvent peu probable dans un contexte d'affaires réel.
                }\color{black}
            \end{parts}	
    """
    return(exo,correction)

def main():
    exo,correction=suiteAnalyseComp()
    print(exo)
    print(correction)
    pass

if __name__ == '__main__':
    main()