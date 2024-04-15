import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

from baseMaths import *



def suiteAriShema():

    # On tir au hasard une lettre pour le nom de la suite
    lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    lowercase_alphabet.remove('n') # n ne peut pas être le nom d'une suite
    suite_letter = random.choice(lowercase_alphabet)
    # On retire la lettre choisie de la liste pour éviter les doublons de tirage
    lowercase_alphabet.remove(suite_letter)
    nRef = random.randint(2,5)
    valeurRef = random.randint(2,15)
    raisonSuite = nonEqRandomValue(quart=False, tier=False, demi=True)
    u0 = valeurRef/((raisonSuite[0])**nRef)
    u1 = valeurRef*raisonSuite[0]
    u2 = u1*raisonSuite[0]
    u3 = u2*raisonSuite[0]
    exo=r"""
    \Question[8] On considère la suite géométrique $("""+suite_letter+r"""_n)$ (avec $n\in \mathbb{N}$) de terme de rang """+str(nRef)+r""" ayant pour valeur """+str(valeurRef)+r""" et de raison $"""+Latex(raisonSuite[0])+r"""$.\\
    Compléter le diagramme en répondant aux questions suivantes :\\
        \begin{center}
            \begin{tikzpicture}
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale1) at (0,0) {......};
            \node[below=1mm of ovale1] {$"""+suite_letter+r"""_{"""+str(nRef)+r"""}$}; % Texte plus proche de l'ovale
            
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale2) at (3,0) {......};
            \node[below=1mm of ovale2] {$"""+suite_letter+r"""_{"""+str(nRef+1)+r"""}$}; % Texte plus proche de l'ovale
            
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale3) at (6,0) {......};
            \node[below=1mm of ovale3] {$"""+suite_letter+r"""_{"""+str(nRef+2)+r"""}$}; % Texte plus proche de l'ovale
            
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale4) at (9,0) {......};
            \node[below=1mm of ovale4] {$"""+suite_letter+r"""_{"""+str(nRef+3)+r"""}$}; % Texte plus proche de l'ovale
            
            \draw[->, bend left] (ovale1) to node[above] {$\times .....$} (ovale2);
            \draw[->, bend left] (ovale2) to node[above] {$\times .....$} (ovale3);
            \draw[->, bend left] (ovale3) to node[above] {$\times .....$} (ovale4);
            \end{tikzpicture}
        \end{center}
        \begin{parts}
                \Part Compléter les pointillés ci-dessous pour obtenir les quatre premiers termes de la suite :
                \begin{subparts}
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef)+r"""}=\color{red}{"""+str(valeurRef)+r"""}$
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef+1)+r"""}=\color{red}{"""+suite_letter+r"""_{"""+str(nRef)+r"""}}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=\color{red}{"""+str(valeurRef)+r"""}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=\color{red}{-30}$
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef+2)+r"""}=\color{red}{"""+suite_letter+r"""_{"""+str(nRef+1)+r"""}}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=......$
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef+3)+r"""}=\color{red}{"""+suite_letter+r"""_{"""+str(nRef+2)+r"""}}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=......$
                    \subpart $a_{4}=\color{red}{15}$
                    \subpart $a_{5}=\color{red}{a_{4}}\times \color{red}{-2}=\color{red}{15}\times \color{red}{-2}=\color{red}{-30}$
                    \subpart $a_{6}=......\times ......=......$
                    \subpart $a_{7}=......\times ......=......$
                \end{subparts}
        \end{parts}
        \fillwithlines{10mm}"""
    correction=r""""""
    return(exo,correction)

def polyDegre2_1(n:int=10):
    item = r"""\clearpage
            \Question["""+str(2*n)+r"""] Résoudre les équations suivantes dans $\mathbb{R}$:
            \begin{multicols}{2}
                \begin{enumerate}
"""
    itemCorr = r"""\clearpage
            \Question["""+str(2*n)+r"""] Résoudre les équations suivantes dans $\mathbb{R}$:
            \begin{multicols}{2}
                \begin{enumerate}
"""
    for i in range(n):
        a = nonEqRandomValue(quart=True, tier=False, demi=True)[0]**2
        b = nonEqRandomValue(quart=True, tier=False, demi=True)[0]**2
        signe_b = (-1 if random.randint(1,100)%2==0 else 1) 
        x = Symbol('x')
        str_expr1 = str(a)+"*x**2"+(("+"+str(b)) if signe_b>0 else ("-"+str(b)))
        expr1 = sympify(str_expr1)
        solutions1 = real_roots(str_expr1, x)
        item = item + r"""                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                        \fillwithlines{30mm}
"""
        if len(solutions1)==0:
            itemCorr = itemCorr + r"""                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                    \begin{center}
                    	$ \color{red}{S= \O } $\\
                    	(pas de solutions dans $\mathbb{R}$)
                    \end{center}"""
        if len(solutions1)==1:
            itemCorr = itemCorr + r"""
                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                    \begin{center}
                    	$ \color{red}{S=\left\{ """+latex(solutions1[0]).replace("frac","dfrac")+r""" \right\}} $
                    \end{center}"""
        if len(solutions1)==2:
            itemCorr = itemCorr + r"""
                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                    \begin{center}
                    	$ \color{red}{S=\left\{ """+latex(solutions1[0]).replace("frac","dfrac")+r""" ; """+latex(solutions1[1]).replace("frac","dfrac")+r""" \right\}} $
                    \end{center}"""
    item = item +r"""
                \end{enumerate}
            \end{multicols}"""
    itemCorr = itemCorr + r"""
                \end{enumerate}
            \end{multicols}"""
    return(item,itemCorr)




def main():
    # exo,corr=polyDegre2_DisN1()
    print(corr)
    pass

if __name__=="__main__":
    main()
    pass