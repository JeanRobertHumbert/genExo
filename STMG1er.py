import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

from baseMaths import *

def exoProportion(n=10):
    """
    The function `exoProportion` generates a set of exercises and their corresponding corrections for
    calculating proportions.
    
    :param n: The parameter `n` represents the number of proportions to be calculated. It determines how
    many items will be generated in the exercise and correction. By default, if no value is provided for
    `n`, it will be set to 10, defaults to 10 (optional)
    :return: The function `exoProportion` returns two strings: `exo` and `correction`.
    """
    taux = [10,20,30,40,50,25,75]
    valeur, t = symbols('valeur t')
    item = r""""""
    itemCorrection = r""""""
    for i in range(0,n):
        valeur = random.randint(10,40)*10*2
        t = random.choice(taux)
        item = item + r"""\item $"""+str(t)+r"""\%$ de $"""+str(valeur)+r"""$ = .....
        """
        itemCorrection = itemCorrection + r"""\item $"""+str(t)+r"""\%$ de $"""+str(valeur)+r"""$ = {\color{red}$"""+f"{valeur*t/100:.0f}"+r"""$}
        """
    exo=r"""
        \Question["""+str(n)+r"""] Calculer les proportions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+item+r"""
                \end{enumerate}
            \end{multicols}
    """
    correction=r"""
        \Question["""+str(n)+r"""] Calculer les proportions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+itemCorrection+r"""
                \end{enumerate}
            \end{multicols}
    """
    return(exo,correction)

def exoEvolutionSimple(n=2):
    taux = [10,20,30,40,50,25,75]
    valeur, t = symbols('valeur t')
    item = r""""""
    itemCorrection = r""""""
    for i in range(0,n):
        valeur = random.randint(10,40)*10*2
        t = random.choice(taux)*(sign(random.randint(-1,1)))
        item = item + r"""\item $"""+str(valeur)+r"""$ évolue de $"""+str(t)+r"""\%$ = .....
        """
        itemCorrection = itemCorrection + r"""\item $"""+str(valeur)+r"""$ évolue de $"""+str(t)+r"""\%$ = {\color{red}$"""+f"{valeur*(1+t/100):.0f}"+r"""$}
        """
    exo=r"""
        \Question["""+str(n)+r"""] Calculer les évolutions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+item+r"""
                \end{enumerate}
            \end{multicols}
    """
    correction=r"""
        \Question["""+str(n)+r"""] Calculer les évolutions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+itemCorrection+r"""
                \end{enumerate}
            \end{multicols}
    """
    return(exo,correction)

def exoEvolution():
    anneeStart=1998
    data =[]
    for i in range(anneeStart, anneeStart+9):
        data.append([i,np.random.randint(4500,8500)])
    txQc = np.random.randint(5,49)
    exo=r"""
    \Question 
        Le tableau suivant donne le nombre de morts sur les routes françaises par an de 1998 à 2006.

        \begin{center}
            \begin{tabularx}{\linewidth}{|m{2cm}|*{9}{>{\centering \arraybackslash}X|}}\hline
                Année &"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r"""\\ \hline
                Rang $\left(x_i\right)$& 1 &2 &3 &4 &5 &6 &7 &8 &9\\ \hline
                Nombre de morts $\left(y_i\right)$& """+str(data[0][1])+r""" & """+str(data[1][1])+r""" & """+str(data[2][1])+r""" & """+str(data[3][1])+r""" & """+str(data[4][1])+r""" & """+str(data[5][1])+r""" & """+str(data[6][1])+r""" & """+str(data[7][1])+r""" & """+str(data[8][1])+r"""\\ \hline
                \multicolumn{10}{r}{\footnotesize Source: d'après www.securite-routiere.gouv.fr}
            \end{tabularx}
        \end{center}
        \begin{parts}
            \Part[2] Sur le graphique ci-dessous, on a représenté une partie du nuage de points $M_i\left(x_i~;~y_i\right)$.\\
            Compléter ce nuage de points à l'aide du tableau en plaçant le point d'abscisse 4 et le point d'abscisse 7.
            \begin{center}
                \begin{tikzpicture}[scale=0.75]
                    \begin{axis}[
                            grid= both ,
                            minor tick num=1,
                            minor grid style={line width=.1pt, dashed	},
                            major grid style={line width=.4pt},
                            width=0.8\textwidth ,
                            xlabel = {Rang $\left(x_i\right)$} ,
                            ylabel = {Nombre de morts $\left(y_i\right)$} ,
                            xmin = 0, xmax = 15,
                            ymin = 2500, ymax = 10000,
                            yticklabel style={
                                /pgf/number format/.cd,%
                                scaled y ticks = false,
                                set thousands separator={},
                                fixed
                            },
                            %legend entries={Courbe 1, Courbe 2},
                            %legend style={at={(0,1)},anchor=north west}
                            ]
                        \addplot [only marks,mark=*] coordinates {(1,"""+str(data[0][1])+r""") (2,"""+str(data[1][1])+r""") (3,"""+str(data[2][1])+r""")  (5,"""+str(data[4][1])+r""") (6, """+str(data[5][1])+r""")  (8,"""+str(data[7][1])+r""") (9, """+str(data[8][1])+r""")}; % Tracé point à point
                        \addplot [very thick] expression[domain=0:15]{9142.722-485.967*x}; % Équation analytique
                        \addplot [red,dashed,very thick] expression[domain=0:13]{2800}; % Équation analytique
                    \end{axis}
                \end{tikzpicture}
            \end{center}
            \part[2] Sur le graphique ci-dessus est tracée la droite d'ajustement. À l'aide de cette droite d'ajustement, par lecture graphique, déterminer une prévision du nombre de morts en 2010.
                \fillwithlines{10mm}
            \part[2] On a observé en réalité que le nombre de personnes ayant perdu la vie sur les routes françaises en 2010 a diminué de """+str(txQc)+r"""\% par rapport à l'année 2000.
Quel est le nombre réel de victimes sur les routes françaises en 2010 ? On donnera le résultat arrondi à l'unité.
                \fillwithlines{20mm}
        \end{parts}
\clearpage
    """
    correction=r"""
        \Question 
            Le tableau suivant donne le nombre de morts sur les routes françaises par an de 1998 à 2006.
            \begin{center}
                \begin{tabularx}{\linewidth}{|m{2cm}|*{9}{>{\centering \arraybackslash}X|}}\hline
                    Année &"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r"""\\ \hline
                    Rang $\left(x_i\right)$& 1 &2 &3 &4 &5 &6 &7 &8 &9\\ \hline
                    Nombre de morts $\left(y_i\right)$& """+str(data[0][1])+r""" & """+str(data[1][1])+r""" & """+str(data[2][1])+r""" & """+str(data[3][1])+r""" & """+str(data[4][1])+r""" & """+str(data[5][1])+r""" & """+str(data[6][1])+r""" & """+str(data[7][1])+r""" & """+str(data[8][1])+r"""\\ \hline
                    \multicolumn{10}{r}{\footnotesize Source: d'après www.securite-routiere.gouv.fr}
                \end{tabularx}
            \end{center}
            \begin{parts}
                \Part[2] Sur le graphique ci-dessous, on a représenté une partie du nuage de points $M_i\left(x_i~;~y_i\right)$.\\
                Compléter ce nuage de points à l'aide du tableau en plaçant le point d'abscisse 4 et le point d'abscisse 7.

                \begin{center}
                    \begin{tikzpicture}[scale=0.75]
                        \begin{axis}[
                                grid= both ,
                                minor tick num=1,
                                minor grid style={line width=.1pt, dashed	},
                                major grid style={line width=.4pt},
                                width=0.8\textwidth ,
                                xlabel = {Rang $\left(x_i\right)$} ,
                                ylabel = {Nombre de morts $\left(y_i\right)$} ,
                                xmin = 0, xmax = 15,
                                ymin = 2500, ymax = 10000,
                                yticklabel style={
                                    /pgf/number format/.cd,%
                                    scaled y ticks = false,
                                    set thousands separator={},
                                    fixed
                                },
                                %legend entries={Courbe 1, Courbe 2},
                                %legend style={at={(0,1)},anchor=north west}
                                ]
                            \addplot [only marks,mark=*] coordinates {(1,"""+str(data[0][1])+r""") (2,"""+str(data[1][1])+r""") (3,"""+str(data[2][1])+r""")  (5,"""+str(data[4][1])+r""") (6, """+str(data[5][1])+r""")  (8,"""+str(data[7][1])+r""") (9, """+str(data[8][1])+r""")}; % Tracé point à point
                            \addplot [very thick] expression[domain=0:15]{9142.722-485.967*x}; % Équation analytique
                            \addplot [red,dashed,very thick] expression[domain=0:13]{2800}; % Équation analytique
                            \addplot [red,only marks,mark=*] coordinates {(4,"""+str(data[3][1])+r""") (7,"""+str(data[6][1])+r""")}; % Tracé point à point
                        \end{axis}
                    \end{tikzpicture}
                \end{center}
                \part[2] Sur le graphique ci-dessus est tracée la droite d'ajustement. À l'aide de cette droite d'ajustement, par lecture graphique, déterminer une prévision du nombre de morts en 2010.
%				\fillwithlines{10mm}
                    \begin{solution}
                        environ 2 800
                    \end{solution}
                \part[2] On a observé en réalité que le nombre de personnes ayant perdu la vie sur les routes françaises en 2010 a diminué de """+str(txQc)+r"""\% par rapport à l'année 2000.
Quel est le nombre réel de victimes sur les routes françaises en 2010 ? On donnera le résultat arrondi à l'unité.
%					\fillwithlines{20mm}
                    \begin{solution}
                        En 2000, il y avait """+str(data[2][1])+r""" morts; en 2010 il y en a eu :
                        \begin{center}
                            $"""+str(data[2][1])+r"""\times \left( 1-\dfrac{"""+str(txQc)+r"""}{100}\right)\approx """+str(int(data[2][1]*(1-txQc/100)))+r"""$
                        \end{center}
                    \end{solution}
            \end{parts}
\clearpage
    """
    return(exo, correction)

def exoEvolSuite():
    anneeStart=2002
    data =[]
    for i in range(anneeStart, anneeStart+11):
        data.append([i,np.random.randint(450,650)/10])

    q1Start = np.random.randint(0,6)
    q1End = np.random.randint(1,10-q1Start)
    q1End = q1Start+q1End
    q1Taux =  int(round(((data[q1End][1]-data[q1Start][1])/data[q1Start][1])*100,0))
    q2RacineN = (1+q1Taux/100)**((q1End-q1Start)**-1)-1
    q3Taux = np.random.randint(100, 900)/100
    q3Tx2020 = data[10][1]*(1+q3Taux/100)**8
    exo=r"""
    \Question
                Le tableau suivant indique, sur la période 2002-2012, en France, la proportion de déchets recyclés exprimée en pourcentage des déchets d'emballages ménagers.
                \begin{center}
                    \begin{tabularx}{1.02\linewidth}{|m{2.5cm}|*{11}{>{\centering \arraybackslash}X|}}\hline
                    Année 		&"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r""" &"""+str(data[9][0])+r""" &"""+str(data[10][0])+r"""\\ \hline
                    Pourcentage de
                    déchets recyclés (en \,$\%$)&"""+str(data[0][1])+r""" &"""+str(data[1][1])+r""" &"""+str(data[2][1])+r""" &"""+str(data[3][1])+r""" &"""+str(data[4][1])+r""" &"""+str(data[5][1])+r""" &"""+str(data[6][1])+r""" &"""+str(data[7][1])+r""" &"""+str(data[8][1])+r""" &"""+str(data[9][1])+r""" &"""+str(data[10][1])+r""" \\ \hline
                    \end{tabularx}
                \end{center}
                \begin{parts}
                    \Part[1] Montrer que le taux global d'évolution, arrondi à l'unité, entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""" est de $"""+str(q1Taux)+r"""$\,\%.
                        \fillwithlines{30mm}
                    \Part[2] Déterminer le taux annuel moyen entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""". On donnera le résultat en pourcentage arrondi au centième.
                        \fillwithlines{30mm}
                    \Part[2] On conjecture qu'à partir de 2012, le taux annuel est de $+ """+str(q3Taux)+r"""$\,\%. Avec ce modèle, quel est le taux de recyclage en 2020 ? On donnera le résultat en pourcentage arrondi au dixième.
                        \fillwithlines{30mm}
                \end{parts}
\clearpage
    """
    correction=r"""
    \Question
                Le tableau suivant indique, sur la période 2002-2012, en France, la proportion de déchets recyclés exprimée en pourcentage des déchets d'emballages ménagers.
                \begin{center}
                    \begin{tabularx}{1.02\linewidth}{|m{2.5cm}|*{11}{>{\centering \arraybackslash}X|}}\hline
                    Année 		&"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r""" &"""+str(data[9][0])+r""" &"""+str(data[10][0])+r"""\\ \hline
                    Pourcentage de
                    déchets recyclés (en \,$\%$)&"""+str(data[0][1])+r""" &"""+str(data[1][1])+r""" &"""+str(data[2][1])+r""" &"""+str(data[3][1])+r""" &"""+str(data[4][1])+r""" &"""+str(data[5][1])+r""" &"""+str(data[6][1])+r""" &"""+str(data[7][1])+r""" &"""+str(data[8][1])+r""" &"""+str(data[9][1])+r""" &"""+str(data[10][1])+r""" \\ \hline
                    \end{tabularx}
                \end{center}
                \begin{parts}
                    \Part[1] Montrer que le taux global d'évolution, arrondi à l'unité, entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""" est de $"""+str(q1Taux)+r"""$\,\%.
%						\fillwithlines{30mm}
                        \begin{solution}
                            \begin{center}
                                $\dfrac{pourcent_{"""+str(data[q1End][0])+r"""}-pourcent_{"""+str(data[q1Start][0])+r"""}}{pourcent_{"""+str(data[q1Start][0])+r"""}}\times 100 = \dfrac{"""+str(data[q1End][1])+r"""-"""+str(data[q1Start][1])+r"""}{"""+str(data[q1Start][1])+r"""}\times 100 \approx """+str(round(((data[q1End][1]-data[q1Start][1])/data[q1Start][1])*100,2))+r"""$ soit """+str(q1Taux)+r"""\%
                            \end{center}
                        \end{solution}
                    \Part[2] Déterminer le taux annuel moyen entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""". On donnera le résultat en pourcentage arrondi au centième.
%						\fillwithlines{30mm}
                        \begin{solution}
                            Le taux global qui fait passer de """+str(data[q1Start][0])+r""" à """+str(data[q1End][0])+r""" est de """+str(q1Taux)+r"""\%. Le taux moyen est donc :
                            \begin{center}
                                $t_m=\sqrt["""+str(q1End-q1Start)+r"""]{1+\dfrac{"""+str(q1Taux)+r"""}{100}}-1\approx """+str(round(q2RacineN*100,4))+r"""\%$
                            \end{center}
                        \end{solution}
                    \Part[2] On conjecture qu'à partir de 2012, le taux annuel est de $+ """+str(q3Taux)+r"""$\,\%. Avec ce modèle, quel est le taux de recyclage en 2020 ? On donnera le résultat en pourcentage arrondi au dixième.
%						\fillwithlines{30mm}
                        \begin{solution}
                            De 2012 à 2020, il y a 8 ans, le taux en 2012 était de """+str(data[10][1])+r"""\%. Le taux en 2020 est donc :
                            \begin{center}
                                $"""+str(data[10][1])+r"""\times\left(1+\dfrac{"""+str(q3Taux)+r"""}{100}\right)^8$ soit environ """+str(round(q3Tx2020,2))+r"""\%
                            \end{center}
                        \end{solution}
                \end{parts}
\clearpage
    """
    return(exo, correction)

def exoEvolSchemas():
    taux = [0.10, 0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55]
    V1 = random.randint(10,80)*10
    t1 = random.choice(taux)*(sign(random.randint(-1,1)))
    
    tr1 = 1/(1+t1)-1
    t2 = random.choice(taux)*(sign(random.randint(-1,1)))
    tr2 = 1/(1+t2)-1
    t3 = random.choice(taux)*(sign(random.randint(-1,1)))
    tr3 = 1/(1+t3)-1
    tg = (1+t1)*(1+t2)*(1+t3)-1
    trg = 1/(1+tg)-1
    V2 = V1*(1+t1)
    V3 = V2*(1+t2)
    V4 = V3*(1+t3)
    
    exo=r"""
\clearpage
        \Question[8] Complétez le schéma suivant en utilisant les formules suivantes :\\
        \textit{(Vous donnerez vos résultats arrondi à deux chiffres après la virgule)}
            \begin{itemize}
                \item $\displaystyle t=\frac{V_F-V_I}{V_I}$ (taux d'évolution entre 2 valeurs)
                \item $\displaystyle V_I\times (1+t) = V_F$ (appliquer un taux d'évolution)
                \item $\displaystyle t_R = \frac{1}{1+t}-1$ (taux réciproque du taux $t$)
            \end{itemize}
            \begin{center}
                \begin{tikzpicture}
                    % Déf. styles
                    \tikzstyle{quadri}=[rectangle,draw,text=black]
                    \tikzstyle{estun}=[->,>=latex]
                    % Noeuds
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V1) at (-4,0) {$"""+str(V1)+r"""$};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V2) at (0,0) {\fillwithdottedlines{8mm}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V3) at (4,0) {\fillwithdottedlines{8mm}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V4) at (8,0) {\fillwithdottedlines{8mm}};
                    % Taux evolution
                    \node (e) at (-2,1.4) {$"""+f"{t1*100:.2f}"+r"""\%$};
                    \node (e) at (2,1.4) {$"""+f"{t2*100:.2f}"+r"""\%$};
                    \node (e) at (6,1.4) {$"""+f"{t3*100:.2f}"+r"""\%$};
                    
                    \node (e) at (-2,-1.6) {$.....\%$};
                    \node (e) at (2.2,-1.6) {$.....\%$};
                    \node (e) at (6.2,-1.6) {$.....\%$};
                    
                    \node (e) at (2.2,3) {$.....\%$};
                    \node (e) at (2.2,-3) {$.....\%$};
                    % Flèches
                    \draw[-stealth,ultra thick] [bend left](V1.north)to(V2.north);
                    \draw[-stealth,ultra thick] (V2.south)to[bend left](V1.south);
                    
                    \draw[-stealth,ultra thick] [bend left](V2.north)to(V3.north);
                    \draw[-stealth,ultra thick] (V3.south)to[bend left](V2.south);
                    
                    \draw[-stealth,ultra thick] (V3.north)to[bend left](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left](V3.south);
                    
                    \draw[-stealth,ultra thick] (V1.north)to[bend left=60](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left=60](V1.south);
                \end{tikzpicture}
            \end{center}
            \fillwithlines{105mm}
"""
    correction=r"""
\clearpage
        \Question[8] Complétez le schéma suivant en utilisant les formules suivantes :\\
        \textit{(Vous donnerez vos résultats arrondi à deux chiffres après la virgule)}
            \begin{itemize}
                \item $\displaystyle t=\frac{V_F-V_I}{V_I}$ (taux d'évolution entre 2 valeurs)
                \item $\displaystyle V_I\times (1+t) = V_F$ (appliquer un taux d'évolution)
                \item $\displaystyle t_R = \frac{1}{1+t}-1$ (taux réciproque du taux $t$)
            \end{itemize}
            \begin{center}
                \begin{tikzpicture}
                    % Déf. styles
                    \tikzstyle{quadri}=[rectangle,draw,text=black]
                    \tikzstyle{estun}=[->,>=latex]
                    % Noeuds
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V1) at (-4,0) {$"""+f"{V1:.2f}"+r"""$};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V2) at (0,0) {{\color{red}$"""+f"{V2:.2f}"+r"""$}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V3) at (4,0) {{\color{red}$"""+f"{V3:.2f}"+r"""$}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V4) at (8,0) {{\color{red}$"""+f"{V4:.2f}"+r"""$}};
                    % Taux evolution
                    \node (e) at (-2,1.4) {$"""+f"{t1*100:.2f}"+r"""\%$};
                    \node (e) at (2,1.4) {$"""+f"{t2*100:.2f}"+r"""\%$};
                    \node (e) at (6,1.4) {$"""+f"{t3*100:.2f}"+r"""\%$};
                    
                    \node (e) at (-2,-1.6) {{\color{red}$"""+f"{tr1*100:.2f}"+r"""\%$}};
                    \node (e) at (2.2,-1.6) {{\color{red}$"""+f"{tr2*100:.2f}"+r"""\%$}};
                    \node (e) at (6.2,-1.6) {{\color{red}$"""+f"{tr3*100:.2f}"+r"""\%$}};
                    
                    \node (e) at (2.2,3) {{\color{red}$"""+f"{tg*100:.2f}"+r"""\%$}};
                    \node (e) at (2.2,-3) {{\color{red}$"""+f"{trg*100:.2f}"+r"""\%$}};
                    % Flèches
                    \draw[-stealth,ultra thick] [bend left](V1.north)to(V2.north);
                    \draw[-stealth,ultra thick] (V2.south)to[bend left](V1.south);
                    
                    \draw[-stealth,ultra thick] [bend left](V2.north)to(V3.north);
                    \draw[-stealth,ultra thick] (V3.south)to[bend left](V2.south);
                    
                    \draw[-stealth,ultra thick] (V3.north)to[bend left](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left](V3.south);
                    
                    \draw[-stealth,ultra thick] (V1.north)to[bend left=60](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left=60](V1.south);
                \end{tikzpicture}
            \end{center}
            Pour l'application des taux d'évolution : $\displaystyle V_I\times (1+t) = V_F$
                \begin{enumerate}
                    \item $\displaystyle """+str(V1)+r""" \times (1+\frac{"""+f"{t1*100:.0f}"+r"""}{100})={\color{red}"""+f"{V2:.2f}"+r"""}$
                    \item $\displaystyle """+f"{V2:.2f}"+r""" \times (1+\frac{"""+f"{t2*100:.0f}"+r"""}{100})={\color{red}"""+f"{V3:.2f}"+r"""}$
                    \item $\displaystyle """+f"{V2:.2f}"+r""" \times (1+\frac{"""+f"{t3*100:.0f}"+r"""}{100})={\color{red}"""+f"{V4:.2f}"+r"""}$
                \end{enumerate}
                Pour les taux d'évolution réciproque : $\displaystyle t_R = \frac{1}{1+t}-1$
                \begin{enumerate}
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{t1*100:.0f}"+r"""}{100})}-1={\color{red}"""+f"{tr1*100:.2f}"+r"""\%}$
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{t2*100:.0f}"+r"""}{100})}-1={\color{red}"""+f"{tr2*100:.2f}"+r"""\%}$
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{t3*100:.0f}"+r"""}{100})}-1={\color{red}"""+f"{tr3*100:.2f}"+r"""\%}$
                \end{enumerate}
            Pour le taux global et le taux réciproque global : $\displaystyle t=\frac{V_F-V_I}{V_I}$
                \begin{enumerate}
                    \item $\displaystyle ((1+\frac{"""+f"{t1*100:.0f}"+r"""}{100})\times (1+\frac{"""+f"{t2*100:.0f}"+r"""}{100})\times (1+\frac{"""+f"{t3*100:.0f}"+r"""}{100})-1={\color{red}"""+f"{tg*100:.2f}"+r"""\%}$ \\ ou \\ $\displaystyle \frac{"""+f"{V4:.2f}"+r"""-"""+f"{V1:.2f}"+r"""}{"""+f"{V1:.2f}"+r"""}={\color{red}"""+f"{tg*100:.2f}"+r"""\%}$
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{tg*100:.2f}"+r"""}{100})}-1={\color{red}"""+f"{trg*100:.2f}"+r"""\%}$
                \end{enumerate}
    """
    return(exo, correction)

def exoProba():
    pT = np.random.randint(10,80)
    pLsachantT = np.random.randint(10,80)
    pLsachantA = np.random.randint(10,80)
    pA=100-pT
    pLBsachantT=100-pLsachantT
    pLBsachantA=100-pLsachantA
    pL = round(pT*pLsachantT+pA*pLsachantA,4)
    exo = r"""
    \clearpage
        \Question 
            \begin{description}
                \item Dans un lycée, on considère les élèves ayant obtenu le baccalauréat STMG :
                    \setlength\parindent{9mm}
                    \begin{itemize}[label=\textbullet]
                        \item """+str(pT)+r"""\,\% de ces élèves poursuivent leurs études en BTS ou DUT et parmi eux, """+str(pLsachantT)+r"""\,\% après l'obtention du BTS ou DUT poursuivent leurs études et obtiennent une licence.
                        \item Les autres élèves poursuivent d'autres études après le baccalauréat, et parmi eux, """+str(pLsachantA)+r"""\,\% obtiennent une licence.
                    \end{itemize}
                    \setlength\parindent{0mm}
                    On appelle :			
                    \begin{description}
                        \item[$T$] : l'évènement: \og pour suivre ses études en BTS ou DUT\fg{} ;
                        \item[$A$] : l'évènement: \og pour suivre d'autres études après le baccalauréat\fg{} ; 
                        \item[$L$] : l' évènement : \og obtenir une licence \fg.
                        \item[$\overline{L}$]  désigne l'évènement contraire de l'évènement $L$.
                    \end{description}
            \end{description}
            \vspace{0.25cm}
            \begin{parts}
                \Part[6] compléter l'arbre suivant qui modélise la situation:
                    \begin{center}
                        \begin{tikzpicture}[xscale=0.75,yscale=0.75]
                            \tikzstyle{fleche}=[->,>=latex,thick]
                            \tikzstyle{noeud}=[fill=white,circle]
                            \tikzstyle{feuille}=[fill=white]
                            \tikzstyle{etiquette}=[midway,fill=white,draw]
                            \def\DistanceInterNiveaux{4}
                            \def\DistanceInterFeuilles{2}
                            \def\NiveauA{(0)*\DistanceInterNiveaux}
                            \def\NiveauB{(1.5)*\DistanceInterNiveaux}
                            \def\NiveauC{(2.5)*\DistanceInterNiveaux}
                            \def\InterFeuilles{(-1)*\DistanceInterFeuilles}
                            \node[noeud] (R) at ({\NiveauA},{(1.5)*\InterFeuilles}) {$ $};
                            \node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$T$};
                            \node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$L$};
                            \node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$\overline{L}$};
                            \node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$A$};
                            \node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$L$};
                            \node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$\overline{L}$};
                            \draw[fleche] (R)--(Ra) node[etiquette] {$ $};
                            \draw[fleche] (Ra)--(Raa) node[etiquette] {$ $};
                            \draw[fleche] (Ra)--(Rab) node[etiquette] {$ $};
                            \draw[fleche] (R)--(Rb) node[etiquette] {$ $};
                            \draw[fleche] (Rb)--(Rba) node[etiquette] {$ $};
                            \draw[fleche] (Rb)--(Rbb) node[etiquette] {$ $};
                        \end{tikzpicture}
                    \end{center}
                \Part[1] Déterminer la valeur de la probabilité $p(T \cap L)$.
                    \fillwithlines{20mm}
                \Part[1] Montrer que $p(L) = """+str(pL/100)+r"""\%$.
                    \fillwithlines{20mm}
                \Part[1] Déterminer la probabilité d'avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence. On arrondira le résultat à  $0,01$\,\%.
                    \fillwithlines{20mm}
                \Part[2] Déterminer la valeur arrondie à  $0,01$\,\% de la probabilité $p_L(A)$. Interpréter.
                    \fillwithlines{20mm}
            \end{parts}
\clearpage
"""
    correction = r"""
    \clearpage
        \Question 
            \begin{description}
                \item Dans un lycée, on considère les élèves ayant obtenu le baccalauréat STMG :
                    \setlength\parindent{9mm}
                    \begin{itemize}[label=\textbullet]
                        \item """+str(pT)+r"""\,\% de ces élèves poursuivent leurs études en BTS ou DUT et parmi eux, """+str(pLsachantT)+r"""\,\% après l'obtention du BTS ou DUT poursuivent leurs études et obtiennent une licence.
                        \item Les autres élèves poursuivent d'autres études après le baccalauréat, et parmi eux, """+str(pLsachantA)+r"""\,\% obtiennent une licence.
                    \end{itemize}
                    \setlength\parindent{0mm}
                    On appelle :			
                    \begin{description}
                        \item[$T$] : l'évènement: \og pour suivre ses études en BTS ou DUT\fg{} ;
                        \item[$A$] : l'évènement: \og pour suivre d'autres études après le baccalauréat\fg{} ; 
                        \item[$L$] : l' évènement : \og obtenir une licence \fg.
                        \item[$\overline{L}$]  désigne l'évènement contraire de l'évènement $L$.
                    \end{description}
            \end{description}
            \vspace{0.25cm}
            \begin{parts}
                \Part[6] compléter l'arbre suivant qui modélise la situation:
                    \begin{solution}
                        \begin{center}
                            \begin{tikzpicture}[xscale=1,yscale=1]
                                \tikzstyle{fleche}=[->,>=latex,thick]
                                \tikzstyle{noeud}=[fill=white,circle]
                                \tikzstyle{feuille}=[fill=white]
                                \tikzstyle{etiquette}=[midway,fill=white,draw]
                                \def\DistanceInterNiveaux{4}
                                \def\DistanceInterFeuilles{2}
                                \def\NiveauA{(0)*\DistanceInterNiveaux}
                                \def\NiveauB{(1.5)*\DistanceInterNiveaux}
                                \def\NiveauC{(2.5)*\DistanceInterNiveaux}
                                \def\InterFeuilles{(-1)*\DistanceInterFeuilles}
                                \node[noeud] (R) at ({\NiveauA},{(1.5)*\InterFeuilles}) {$ $};
                                \node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$T$};
                                \node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$L$};
                                \node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$\overline{L}$};
                                \node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$A$};
                                \node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$L$};
                                \node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$\overline{L}$};
                                \draw[fleche] (R)--(Ra) node[etiquette] {$"""+str(pT)+r"""\%$};
                                \draw[fleche] (Ra)--(Raa) node[etiquette] {$"""+str(pLsachantT)+r"""\%$};
                                \draw[fleche] (Ra)--(Rab) node[etiquette] {$"""+str(pLBsachantT)+r"""\%$};
                                \draw[fleche] (R)--(Rb) node[etiquette] {$"""+str(pA)+r"""\%$};
                                \draw[fleche] (Rb)--(Rba) node[etiquette] {$"""+str(pLsachantA)+r"""\%$};
                                \draw[fleche] (Rb)--(Rbb) node[etiquette] {$"""+str(pLBsachantA)+r"""\%$};
                            \end{tikzpicture}
                        \end{center}
                    \end{solution}
                \Part[1] Déterminer la valeur de la probabilité $p(T \cap L)$.
                    \begin{solution}
                        $p(T\cap L)=p(T)\times p_T(L)="""+str(pT/100)+r"""\times """+str(pLsachantT/100)+r"""="""+str(round(pT/100*pLsachantT/100,4))+r"""$
                    \end{solution}
                \Part[1] Montrer que $p(L) = """+str(pL/100)+r"""\%$.
                    \begin{solution}
                        $p(L) = p(T\cap L)+p(A\cap L) = """+str(round(pT/100*pLsachantT/100,4))+r"""+"""+str(round(pA/100,4))+r"""\times """+str(round(pLsachantA/100,4))+r"""="""+str(round(pT/100*pLsachantT/100,4))+r"""+"""+str(round(pA/100*pLsachantA/100,4))+r"""="""+str(round(pT/100*pLsachantT/100+pA/100*pLsachantA/100,4))+r"""$
                    \end{solution}
                \Part[1] Déterminer la probabilité d'avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence. On arrondira le résultat à  $0,01$\,\%.
                    \begin{solution}
                        La probabilité d'avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence, est : 
                        \begin{center}
                            $p_L(T) =\dfrac{p(L\cap T)}{p(L)}=\dfrac{"""+str(round(pT/100*pLsachantT/100,4))+r"""}{"""+str(round(pT/100*pLsachantT/100+pA/100*pLsachantA/100,4))+r"""}\approx """+str(round((pT/100*pLsachantT/100)/(pT/100*pLsachantT/100+pA/100*pLsachantA/100),4))+r"""$
                        \end{center}
                    \end{solution}
                \Part[2] Déterminer la valeur arrondie à  $0,01$\,\% de la probabilité $p_L(A)$. Interpréter.
                    \begin{solution}
                        \begin{center}
                            $p_L(A)=\dfrac{p(A\cap L)}{p(L)}=\dfrac{"""+str(round(pA/100*pLsachantA/100,4))+r"""}{"""+str(pL/100)+r"""}\approx """+str(round((pA/100*pLsachantA/100)/(pL/100),4))+r"""$
                        \end{center}
                        C'est la probabilité de ne pas avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence.
                    \end{solution}
            \end{parts}
\clearpage
"""
    return(exo, correction)

def exoProba1():
    # pS=1
    # effectifCouture=1
    # while (effectifCouture!=0):
    effectifTotal = np.random.randint(low=3,high=8)*100
    effectifStylisme = np.random.randint(low=10,high=20)*10# 50
    effectifDecoupe = np.random.randint(low=5,high=9)*10 # 100
    effectifCouture = effectifTotal-effectifStylisme-effectifDecoupe# 150
    pS = sp.Rational(effectifStylisme,effectifTotal)
    pD = sp.Rational(effectifDecoupe,effectifTotal)
    pC = sp.Rational(effectifCouture,effectifTotal)
    psA = sp.Rational(np.random.randint(25,75),100)
        # print(f"effectifCouture : {effectifCouture}")
    psAb = 1-psA
    pdA = sp.Rational(np.random.randint(25,75),100)
    pdA1 = f"{pdA.evalf()*100:.0f}%"
    pdAb = 1-pdA
    pdAb1 = f"{pdAb.evalf()*100:.0f}%"
    pcA = sp.Rational(np.random.randint(25,75),100)
    pcA1 = f"{pcA.evalf()*100:.0f}%"
    pcAb = 1-pcA
    pcAb1 = f"{pcAb.evalf()*100:.0f}%"
    pS_Inter_A = pS*psA
    pS_Inter_A1 = f"{pS_Inter_A.evalf()*100:.2f}%"
    pD_Inter_A = pD*pdA
    pD_Inter_A1 = f"{pD_Inter_A.evalf()*100:.2f}%"
    pC_Inter_A = pC*pcA
    pC_Inter_A1 = f"{pC_Inter_A.evalf()*100:.2f}%"
    pA = pS_Inter_A + pD_Inter_A + pC_Inter_A
    pA1 = f"{pA.evalf()*100:.2f}%"
    paS = pS_Inter_A/pA
    exo=r"""
\Question Une entreprise de textile emploie """+str(effectifTotal)+r""" personnes dans le secteur confection. Il est composé de trois ateliers.\\
	L'atelier de stylisme est constitué de """+str(effectifStylisme)+r""" personnes.\\L'atelier de découpe est constitué de """+str(effectifDecoupe)+r""" personnes.\\Le reste du personnel travaille dans l'atelier de couture. Après une étude sur l'absentéisme, le directeur des ressources humaines a constaté que sur une année :
	\begin{enumerate}
		\item $"""+f"{psA.evalf()*100:.0f}"+r"""\%$ des stylistes ont eu au moins une absence;
		\item $"""+f"{pdA.evalf()*100:.0f}"+r"""\%$ du personnel de découpe ont eu au moins une absence;
		\item $"""+f"{pcA.evalf()*100:.0f}"+r"""\%$ du personnel de l'atelier de couture n'ont pas eu d'absence.
	\end{enumerate}
	On choisit une personne au hasard dans cette entreprise et l'on admet que chaque personne a la même probabilité d'être choisie.\\
	On note :
	\begin{enumerate}
		\item S l'évènement : « la personne choisie travaille à l'atelier de stylisme »;
		\item D l'événement : « la personne choisie travaille à l'atelier de découpe »;
		\item C l'événement : « la personne choisie travaille à l'atelier de couture »;
		\item A l'événement : « la personne choisie a eu au moins une absence ».
	\end{enumerate}
	Rappel : Si M et N sont deux événements, on note $\overline{M}$ l'événement contraire de l'événement M et $p_N(M)$ la probabilité de l'événement M sachant N.
	\begin{parts}
		\Part[9] Construire un arbre pondéré décrivant la situation.
			\begin{center}
				% Racine à Gauche, développement vers la droite
				\begin{tikzpicture}[xscale=1,yscale=1]
					% Styles (MODIFIABLES)
					\tikzstyle{fleche}=[->,>=latex,thick]
					\tikzstyle{noeud}=[fill=white,circle]
					\tikzstyle{feuille}=[fill=white,circle]
					\tikzstyle{etiquette}=[midway,fill=white]
					% Dimensions (MODIFIABLES)
					\def\DistanceInterNiveaux{3}
					\def\DistanceInterFeuilles{2}
					% Dimensions calculées (NON MODIFIABLES)
					\def\NiveauA{(0)*\DistanceInterNiveaux}
					\def\NiveauB{(1.5)*\DistanceInterNiveaux}
					\def\NiveauC{(2.5)*\DistanceInterNiveaux}
					\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
					% Noeuds (MODIFIABLES : Styles et Coefficients d'InterFeuilles)
					\node[noeud] (R) at ({\NiveauA},{(2.5)*\InterFeuilles}) {$....$};
					\node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$....$};
					\node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$....$};
					\node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$....$};
					\node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$....$};
					\node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$....$};
					\node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$....$};
					\node[noeud] (Rc) at ({\NiveauB},{(4.5)*\InterFeuilles}) {$....$};
					\node[feuille] (Rca) at ({\NiveauC},{(4)*\InterFeuilles}) {$....$};
					\node[feuille] (Rcb) at ({\NiveauC},{(5)*\InterFeuilles}) {$....$};
					% Arcs (MODIFIABLES : Styles)
					\draw[fleche] (R)--(Ra) node[etiquette] {$....$};
					\draw[fleche] (Ra)--(Raa) node[etiquette] {$....$};
					\draw[fleche] (Ra)--(Rab) node[etiquette] {$....$};
					\draw[fleche] (R)--(Rb) node[etiquette] {$....$};
					\draw[fleche] (Rb)--(Rba) node[etiquette] {$....$};
					\draw[fleche] (Rb)--(Rbb) node[etiquette] {$....$};
					\draw[fleche] (R)--(Rc) node[etiquette] {$....$};
					\draw[fleche] (Rc)--(Rca) node[etiquette] {$....$};
					\draw[fleche] (Rc)--(Rcb) node[etiquette] {$....$};
				\end{tikzpicture}
			\end{center}
\clearpage
		\Part Déduire des informations de l'énoncé :
			\begin{multicols}{2}
				\begin{subparts}
					\subpart[3] Les probabilités p(S),p(D) et p(C) des événements S,D et C.
						\fillwithlines{20mm}
					\subpart[3] Les probabilités $p_S(A)$,$p_D(A)$ et $p_C(\overline{A})$.
						\fillwithlines{20mm}
				\end{subparts}
			\end{multicols}
		\Part[3] Calculer la probabilité de l'événement $S\cap A$, notée $p(S\cap A)$.
            \fillwithlines{30mm}
		\Part[8] Démontrer que $p(A) = """+f"{pA.evalf():.4f}"+r"""$
            \fillwithlines{30mm}
		\Part[4] On sait que la personne choisie a eu au moins une absence cette année. Quelle est la probabilité que cette personne soit un styliste ?
            \fillwithlines{30mm}
	\end{parts}
    """
    correction=r"""
\Question Une entreprise de textile emploie """+str(effectifTotal)+r""" personnes dans le secteur confection. Il est composé de trois ateliers.\\
	L'atelier de stylisme est constitué de """+str(effectifStylisme)+r""" personnes.\\L'atelier de découpe est constitué de """+str(effectifDecoupe)+r""" personnes.\\Le reste du personnel travaille dans l'atelier de couture. Après une étude sur l'absentéisme, le directeur des ressources humaines a constaté que sur une année :
	\begin{enumerate}
		\item $"""+f"{psA.evalf()*100:.0f}"+r"""\%$ des stylistes ont eu au moins une absence;
		\item $"""+f"{pdA.evalf()*100:.0f}"+r"""\%$ du personnel de découpe ont eu au moins une absence;
		\item $"""+f"{pcA.evalf()*100:.0f}"+r"""\%$ du personnel de l'atelier de couture n'ont pas eu d'absence.
	\end{enumerate}
	On choisit une personne au hasard dans cette entreprise et l'on admet que chaque personne a la même probabilité d'être choisie.\\
	On note :
	\begin{enumerate}
		\item S l'évènement : « la personne choisie travaille à l'atelier de stylisme »;
		\item D l'événement : « la personne choisie travaille à l'atelier de découpe »;
		\item C l'événement : « la personne choisie travaille à l'atelier de couture »;
		\item A l'événement : « la personne choisie a eu au moins une absence ».
	\end{enumerate}
	Rappel : Si M et N sont deux événements, on note $\overline{M}$ l'événement contraire de l'événement M et $p_N(M)$ la probabilité de l'événement M sachant N.
	\begin{parts}
		\Part Construire un arbre pondéré décrivant la situation.
			\begin{center}
				% Racine à Gauche, développement vers la droite
				\begin{tikzpicture}[xscale=1,yscale=1]
					% Styles (MODIFIABLES)
					\tikzstyle{fleche}=[->,>=latex,thick]
					\tikzstyle{noeud}=[fill=white,circle]
					\tikzstyle{feuille}=[fill=white,circle]
					\tikzstyle{etiquette}=[midway,fill=white]
					% Dimensions (MODIFIABLES)
					\def\DistanceInterNiveaux{3}
					\def\DistanceInterFeuilles{2}
					% Dimensions calculées (NON MODIFIABLES)
					\def\NiveauA{(0)*\DistanceInterNiveaux}
					\def\NiveauB{(1.5)*\DistanceInterNiveaux}
					\def\NiveauC{(2.5)*\DistanceInterNiveaux}
					\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
					% Noeuds (MODIFIABLES : Styles et Coefficients d'InterFeuilles)
					\node[noeud] (R) at ({\NiveauA},{(2.5)*\InterFeuilles}) {};
					\node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$S$};
					\node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$A$};
					\node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$\overline{A}$};
					\node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$D$};
					\node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$A$};
					\node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$\overline{A}$};
					\node[noeud] (Rc) at ({\NiveauB},{(4.5)*\InterFeuilles}) {$C$};
					\node[feuille] (Rca) at ({\NiveauC},{(4)*\InterFeuilles}) {$A$};
					\node[feuille] (Rcb) at ({\NiveauC},{(5)*\InterFeuilles}) {$\overline{A}$};
					% Arcs (MODIFIABLES : Styles)
					\draw[fleche] (R)--(Ra) node[etiquette] {$"""+Latex(pS)+r"""$};
					\draw[fleche] (Ra)--(Raa) node[etiquette] {$"""+f"{psA.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (Ra)--(Rab) node[etiquette] {$"""+f"{psAb.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (R)--(Rb) node[etiquette] {$"""+Latex(pD)+r"""$};
					\draw[fleche] (Rb)--(Rba) node[etiquette] {$"""+f"{pdA.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (Rb)--(Rbb) node[etiquette] {$"""+f"{pdAb.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (R)--(Rc) node[etiquette] {$"""+Latex(pC)+r"""$};
					\draw[fleche] (Rc)--(Rca) node[etiquette] {$"""+f"{pcA.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (Rc)--(Rcb) node[etiquette] {$"""+f"{pcAb.evalf()*100:.0f}"+r"""\%$};
				\end{tikzpicture}
			\end{center}
\clearpage
		\Part Déduire des informations de l'énoncé :
			\begin{multicols}{2}
				\begin{subparts}
					\subpart Les probabilités p(S),p(D) et p(C) des événements S,D et C.
                    {\color{red}
						$p(S) = """+Latex(pS)+r"""$ ; 
                        $p(D) = """+Latex(pD)+r"""$ ; 
                        $p(C) = """+Latex(pC)+r"""$
                    }
                        \columnbreak
					\subpart Les probabilités $p_S(A)$,$p_D(A)$ et $p_C(\overline{A})$.
                    {\color{red}
						$p_S(A) = """+f"{psA.evalf()*100:.0f}"+r"""\%$ ; 
                        $p_D(A) = """+f"{pdA.evalf()*100:.0f}"+r"""\%$ ; 
                        $p_C(\overline{A}) = """+f"{pcAb.evalf()*100:.0f}"+r"""\%$
                    }
				\end{subparts}
			\end{multicols}
		\Part Calculer la probabilité de l'événement $S\cap A$, notée $p(S\cap A)$.
            \begin{solution}
                \begin{align*}
                    p(S\cap A)  &= p(S) \times p_S(A)\\
                                &= """+Latex(pS)+r""" \times """+Latex(psA)+r"""\\
                                &= """+Latex(pS_Inter_A)+r""" \approx """+f"{pS_Inter_A.evalf()*100:.4f}"+r"""\%
                \end{align*}
            \end{solution}
		\Part Démontrer que $p(A) = """+f"{pA.evalf():.4f}"+r"""$
            \begin{solution}
                \begin{align*}
                    p(A)	&=& &p(S\cap A) &+&  &p(D\cap A)& &+& &p(C\cap a)&\\
                            &=& &"""+Latex(pS_Inter_A)+r""" &+&  &p(D)\times p_D(A)& &+& &p(C)\times p_C(A)&\\
                            &=& &"""+Latex(pS_Inter_A)+r""" &+& &"""+Latex(pD)+r"""\times """+Latex(pdA)+r"""& &+& &"""+Latex(pC)+r"""\times """+Latex(pcA)+r"""&\\
                            &=& &"""+Latex(pS_Inter_A)+r""" &+& &"""+Latex(pD*pdA)+r"""& &+& &"""+Latex(pC*pcA)+r"""&\\
                            &=& &"""+Latex(pS_Inter_A+pD_Inter_A+pC_Inter_A)+r""" \approx"""+f"{pA.evalf():.4f}"+r"""
                \end{align*}
            \end{solution}
		\Part On sait que la personne choisie a eu au moins une absence cette année. Quelle est la probabilité que cette personne soit un styliste ?
            \begin{solution}
                \begin{align*}
                    p(S\cap A)  &= p(A\cap S)\\
                                &= p(A) \times p_A(S)\\
    \dfrac{p(S\cap A)}{p(A)}    &= p_A(S)\\
    \dfrac{"""+Latex(pS_Inter_A)+r"""}{"""+Latex(pA)+r"""} &= p_A(S)\\
    """+Latex(pS_Inter_A/pA)+r""" &= p_A(S) \approx """+f"{paS.evalf():.4f}"+r"""
                \end{align*}
            \end{solution}
	\end{parts}
    """
    return(exo,correction)

def lectureGraphiqueAffine():
    alphabet = list(string.ascii_lowercase)
    fonctions = random.sample(alphabet, 4)
    fonctions.sort()
    traceFonction=r""""""
    questionExo=r""""""
    questionCorr=r""""""
    for f in fonctions:
        k = nonEqRandomValue(n=2, notNull=True, demi=True, tier=False, quart=False)
        p = affine(f, k[0], k[1])
        if p.a>0:
            minX=(-4.5-p.b)/p.a
            maxX=(4.5-p.b)/p.a
        if p.a<0:
            minX=(4.5-p.b)/p.a
            maxX=(-4.5-p.b)/p.a
        if p.a==0:
            minX=-4.5   
        minX=max(-4.5,round(float(minX),2))
        maxX=min(4.5,round(float(maxX),2))
        traceFonction=traceFonction+r"""\draw[domain="""+str(min(minX,maxX))+r""":"""+str(max(minX,maxX))+r""", smooth, variable=\x, blue] plot ({\x}, {"""+str(p.a)+r"""*\x+"""+str(p.b)+r"""}) node[below] {$\mathcal{C}_{"""+p.name+r"""}$};
        """
        questionExo = questionExo + r"""
                \Part $"""+p.name+r"""(x)=.........................$
                \fillwithlines{20mm}
"""
        questionCorr = questionCorr+r"""\Part \color{red}{"""+p.latexString()+r"""}\color{black}
        """
        
    exo=r"""
    \clearpage
        \Question[8] Fonctions affines\\
        Donnez l'expression algébrique des fonctions affines associées aux droites suivantes :
        \begin{center}
        		\begin{tikzpicture}[scale=1.5,cap=round]
                % Local definitions
                \def\costhirty{0.8660256}

                % Colors
                \colorlet{anglecolor}{green!50!black}
                \colorlet{sincolor}{red}
                \colorlet{tancolor}{orange!80!black}
                \colorlet{coscolor}{blue}

                % Styles
                \tikzstyle{axes}=[]
                \tikzstyle{important line}=[very thick]
                \tikzstyle{information text}=[rounded corners,fill=red!10,inner sep=1ex]

                % Grille
                \draw[style=help lines,step=0.5cm] (-4.4,-4.4) grid (4.4,4.4);
                
				% The graphic
                \begin{scope}[style=axes]
                    \draw[->] (-4.5,0) -- (4.5,0) node[right] {$x$};
                    \draw[->] (0,-4.5) -- (0,4.5) node[above] {$y$};
                    \draw[->, very thick] (0,0) -- (1,0) node[below, midway] {$\vect{i}$};
                    \draw[->, very thick] (0,0) -- (0,1) node[left, midway] {$\vect{j}$};
                    \node[below left] at (-0.15,-0.15) {0};
                    \foreach \x/\xtext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                    \draw[xshift=\x cm] (0pt,1pt) -- (0pt,-1pt) node[below,fill=white] {\tiny{$\xtext$}};
                    %
                    \foreach \y/\ytext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[yshift=\y cm] (1pt,0pt) -- (-1pt,0pt) node[left,fill=white] {\tiny{$\ytext$}};
                \end{scope}
"""+traceFonction+r"""
            \end{tikzpicture}
        \end{center}
        \begin{multicols}{2}
	        	\begin{parts}
"""+questionExo+r"""
        		\end{parts}
        \end{multicols}
    """
    correction=r"""
    \clearpage
        \Question[8] Fonctions affines\\
        Donnez l'expression algébrique des fonctions affines associées aux droites suivantes :
        \begin{center}
        		\begin{tikzpicture}[scale=1.5,cap=round]
                % Local definitions
                \def\costhirty{0.8660256}

                % Colors
                \colorlet{anglecolor}{green!50!black}
                \colorlet{sincolor}{red}
                \colorlet{tancolor}{orange!80!black}
                \colorlet{coscolor}{blue}

                % Styles
                \tikzstyle{axes}=[]
                \tikzstyle{important line}=[very thick]
                \tikzstyle{information text}=[rounded corners,fill=red!10,inner sep=1ex]

                % Grille
                \draw[style=help lines,step=0.5cm] (-4.4,-4.4) grid (4.4,4.4);
                
				% The graphic
                \begin{scope}[style=axes]
                    \draw[->] (-4.5,0) -- (4.5,0) node[right] {$x$};
                    \draw[->] (0,-4.5) -- (0,4.5) node[above] {$y$};
                    \draw[->, very thick] (0,0) -- (1,0) node[below, midway] {$\vect{i}$};
                    \draw[->, very thick] (0,0) -- (0,1) node[left, midway] {$\vect{j}$};
                    \node[below left] at (-0.15,-0.15) {0};
                    \foreach \x/\xtext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                    \draw[xshift=\x cm] (0pt,1pt) -- (0pt,-1pt) node[below,fill=white] {\tiny{$\xtext$}};
                    %
                    \foreach \y/\ytext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[yshift=\y cm] (1pt,0pt) -- (-1pt,0pt) node[left,fill=white] {\tiny{$\ytext$}};
                \end{scope}
"""+traceFonction+r"""
            \end{tikzpicture}
        \end{center}
        \begin{multicols}{2}
	        	\begin{parts}
"""+questionCorr+r"""
        		\end{parts}
        \end{multicols}
    """
    return(exo,correction)

def exoEvolConsoEau():
    Vol1 = random.randint(10,80)*10
    Vol2 = random.randint(10,80)*10
    t = (Vol2-Vol1)/Vol1
    tr = 1/(1+t)-1
    Annee1 = random.randint(2000,2010)
    Annee2 = Annee1+random.randint(4,10)
    n = Annee2-Annee1
    tm = np.power(1+t,1/n)-1
    
    exo=r"""
    \clearpage
            \Question Une famille a consommé """+str(Vol1)+r""" mètres cubes d'eau en """+str(Annee1)+r""" et """+str(Vol2)+r""" mètres cubes d'eau en """+str(Annee2)+r""".
                \begin{parts}
                    \Part Calculer $t$ le taux d'évolution global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                    \Part Calculer $t_R$ le taux d'évolution réciproque global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                    \Part Calculer $t_m$ le taux d'évolution moyen global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                \end{parts}
    """
    correction=r"""
    \clearpage
            \Question Une famille a consommé """+str(Vol1)+r""" mètres cubes d'eau en """+str(Annee1)+r""" et """+str(Vol2)+r""" mètres cubes d'eau en """+str(Annee2)+r""".
                \begin{parts}
                    \Part Calculer $t$ le taux d'évolution global en pourcentage (\textit{arrondi au centième}).
                        \begin{center}
                            $\displaystyle t=\frac{V_{Finale}-V_{Initiale}}{V_{Initiale}}$ d'où $\displaystyle t=\frac{"""+str(Vol2)+r"""-"""+str(Vol1)+r"""}{"""+str(Vol1)+r"""}={\color{red}"""+f"{t*100:.2f}"+r"""\%}$
                        \end{center}
                    \Part Calculer $t_R$ le taux d'évolution réciproque global en pourcentage (\textit{arrondi au centième}).
                        \begin{center}
                            $\displaystyle t_R=\frac{1}{1+t}-1$ d'où $\displaystyle t_R=\frac{1}{1+\frac{"""+f"{t*100:.2f}"+r"""}{100}}={\color{red}"""+f"{tr*100:.2f}"+r"""\%}$
                        \end{center}
                    \Part Calculer $t_m$ le taux d'évolution moyen global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                \end{parts}
    """
    return(exo, correction)

def exoAffineBourse():
    xa = sp.Rational(0)
    ya = nonEqRandomValue(debut=1,fin=4)
    ya = ya[0]
    xb = nonEqRandomValue(debut=7,fin=9)
    xb = xb[0]
    yb = nonEqRandomValue(debut=1,fin=8)
    yb = yb[0]
    while ya==yb:
        xa = sp.Rational(0)
        ya = nonEqRandomValue(debut=1,fin=4)
        ya = ya[0]
        xb = nonEqRandomValue(debut=7,fin=9)
        xb = xb[0]
        yb = nonEqRandomValue(debut=1,fin=8)
        yb = yb[0]
    
    p = affine("C",1,1)
    p.setFrom2Points(xa,ya,xb,yb)
    # k = nonEqRandomValue(n=2, notNull=True, tier=True)
    # p = affine("f", k[0], k[1])
    if p.a>0:
        pHaut = affine("H" , p.a*sp.Rational(3,4), p.b+1)
        pHaut.setFrom2Points(0,ya+1, xb,yb)
        pBas  = affine("B" , p.a*sp.Rational(5,4) , p.b-1)
        pBas.setFrom2Points(0,ya-1, xb,yb)
    if p.a<0:
        pHaut = affine("H" , p.a*sp.Rational(5,4), p.b+1)
        pHaut.setFrom2Points(0,ya+1, xb,yb)
        pBas  = affine("B" , p.a*sp.Rational(3,4) , p.b-1)
        pBas.setFrom2Points(0,ya-1, xb,yb)
    a=(yb-pHaut.imageDe(0))/(xb-0)
    b=pHaut.imageDe(0)-a*xa
    # print(p)
    # print(pHaut)
    # print(pBas)
    inter = p.intersection(pHaut)
    if inter!=False:
        ch = r"""\addplot [very thin] coordinates {"""
        x=0
        while x <= inter[0]:
            yH = pHaut.imageDe(x)
            yB = pBas.imageDe(x)
            x = x + sp.Rational(1,20)
            y = random.uniform(yB,yH)
            ch = ch + f"({x.evalf():.2f},{y.evalf():.2f}) "
        ch = ch + r"""};
        """

    exo = r"""
    \clearpage
    \Question Le graphique ci-dessous représente l'évolution d'une action boursière. La droite $(\mathcal{"""+p.name+r"""})$ représente la fonction """+p.latexString()+r""" (moyenne centrée de l'action boursière).
	\begin{center}
		\begin{tikzpicture}[scale=1]
			\begin{axis}[
						grid= both ,
						minor tick num=1,
						minor grid style={line width=.1pt, dashed	},
						major grid style={line width=.4pt},
						width=0.8\textwidth ,
						xlabel = {Heure} ,
						ylabel = {Valeur} ,
						xmin = 0, xmax = 10,
						ymin = 0, ymax = 10,
						yticklabel style={
						/pgf/number format/.cd,%
						scaled y ticks = false,
						set thousands separator={},
						fixed
						},
						%legend entries={Courbe 1, Courbe 2},
						%legend style={at={(0,1)},anchor=north west}
						]
                """+ch+r"""
                \addplot [very thick] expression[domain=0:10]{"""+p.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{C})$};
                \addplot [dashed, thin] expression[domain=0:10]{"""+pHaut.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{H}$)}; 
                \addplot [dashed, thin] expression[domain=0:10]{"""+pBas.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{B}$)};
                \end{axis}
		\end{tikzpicture}
	\end{center}
	\begin{parts}
		\Part[4] déterminez l'expression de la fonction $H(x)$ représenté par la droite $(\mathcal{H})$.
			\fillwithlines{35mm}
		\Part[4] En considérant que la droite $(\mathcal{H})$ représente le maximum de l'action boursière et la droite $(\mathcal{B})$ le minimum de la valeur.\\
			Quelles sont les valeurs minimales et maximales de l'action boursière à 4h et 5h ?
			\fillwithlines{10mm}
		\Part[3] déterminez (par le calcul), le point d'intersection des droites $(\mathcal{C})$ et $(\mathcal{H})$.
			\fillwithlines{40mm}
	\end{parts}
    """
    correction = r"""
    \clearpage
    \Question Le graphique ci-dessous représente l'évolution d'une action boursière. La droite $(\mathcal{"""+p.name+r"""})$ représente la fonction """+p.latexString()+r""" (moyenne centrée de l'action boursière).
    \begin{center}
        \begin{tikzpicture}[scale=1]
            \begin{axis}[
                        grid= both ,
                        minor tick num=1,
                        minor grid style={line width=.1pt, dashed	},
                        major grid style={line width=.4pt},
                        width=0.8\textwidth ,
                        xlabel = {Heure} ,
                        ylabel = {Valeur} ,
                        xmin = 0, xmax = 10,
                        ymin = 0, ymax = 10,
                        yticklabel style={
                        /pgf/number format/.cd,%
                        scaled y ticks = false,
                        set thousands separator={},
                        fixed
                        },
                        %legend entries={Courbe 1, Courbe 2},
                        %legend style={at={(0,1)},anchor=north west}
                        ]
                """+ch+r"""
                \addplot [very thick] expression[domain=0:10]{"""+p.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{C})$};
                \addplot [dashed, thin] expression[domain=0:10]{"""+pHaut.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{H}$)}; 
                \addplot [dashed, thin] expression[domain=0:10]{"""+pBas.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{B}$)};
                \end{axis}
        \end{tikzpicture}
    \end{center}
    \begin{parts}
        \Part déterminez l'expression de la fonction $H(x)$ représenté par la droite $(\mathcal{H})$.
            \begin{solution}
                On remarque que la représentation graphique de $H(x)$ passe par le point de coordonnées $A(0;"""+Latex(ya+1)+r""")$ et le point de coordonnées $B("""+Latex(xb)+r""";"""+Latex(yb)+r""")$ \\
                La représentation graphique de $H(x)$ est une droite non verticale donc son expression algébrique est de forme affine soit :
                $H(x)=ax+b$ avec $a=\dfrac{y_b-y_a}{x_b-x_a}$ et $b=y_a-ax_a$\\
                en appliquant, on obtient :\\
                \begin{center}
                    $a=\dfrac{"""+Latex(yb-pHaut.imageDe(0))+r"""}{"""+Latex(xb-0)+r"""}="""+Latex(a)+r"""$ et $b="""+Latex(ya)+r"""-"""+Latex(a)+r"""\times """+Latex(xa)+r"""="""+Latex(b)+r"""$
                \end{center}
                d'où {\color{red}$H(x)="""+Latex(a)+r"""x+"""+Latex(b)+r"""$} 
            \end{solution}
        \Part En considérant que la droite $(\mathcal{H})$ représente le maximum de l'action boursière et la droite $(\mathcal{B})$ le minimum de la valeur.\\
                Quelles sont les valeurs minimales et maximales de l'action boursière à 4h et 5h ?
            \begin{solution}
                Les valeurs hautes à 4h et 5h sont $"""+Latex(pHaut.imageDe(4))+r"""$ et $"""+Latex(pHaut.imageDe(5))+r"""$\\
                Les valeurs basses à 4h et 5h sont $"""+Latex(pBas.imageDe(4))+r"""$ et $"""+Latex(pBas.imageDe(5))+r"""$
            \end{solution}
        \Part déterminez (par le calcul), le point d'intersection des droites $(\mathcal{C})$ et $(\mathcal{H})$.
                \begin{solution}
                Les deux droites se croisent lorsque $C(x)=H(x)$.\\
                Nous résolvons donc cette équation :
                \begin{align*}
                    C(x)&=H(x)\\
                    """+p.latexString1()+r"""&="""+pHaut.latexString1()+r"""\\
                    """+Latex(p.a-pHaut.a)+r"""x&="""+Latex(pHaut.b-p.b)+r"""\\
                        x&="""+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r"""
                \end{align*}
                il reste à calculer l'image par l'une des deux fonctions.
                \begin{align*}
                    C("""+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r""")&="""+Latex(p.a)+r""" \times """+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r""" + ("""+Latex(p.b)+r""")\\
                                    &="""+Latex(p.imageDe((pHaut.b-p.b)/(p.a-pHaut.a)))+r"""
                \end{align*}
                donc le point d'intersection de $\mathcal{C}$ et $\mathcal{H}$ a pour coordonnées {\color{red}$("""+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r""";"""+Latex(p.imageDe((pHaut.b-p.b)/(p.a-pHaut.a)))+r""")$}
            \end{solution}
        \end{parts}
        """
    # print(correction)
    return(exo,correction)

def polyDegre2_Factor(n:int=5):
    item = r""""""
    itemCorr = r""""""
    for i in range(n):
        alpha = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        a1 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        b1 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        a2 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        b2 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        
        alphastr = latex(alpha).replace("frac","dfrac")
        a1str = latex(a1).replace("frac","dfrac")
        b1str = latex(b1).replace("frac","dfrac")
        a2str = latex(a2).replace("frac","dfrac")
        b2str = latex(b2).replace("frac","dfrac")

        x1str = latex(-b1/a1).replace("frac","dfrac")
        x2str = latex(-b2/a2).replace("frac","dfrac")
        signb1 = r"""""" if b1<0 else r"""+"""
        signb2 = r"""""" if b2<0 else r"""+"""
        item = item + r"""                    \multicolumn{1}{|c|}{$"""+alphastr+r"""\left("""+a1str+r"""x"""+signb1+b1str+r"""\right)\left("""+a2str+r"""x"""+signb2+b2str+r"""\right)$} &   &  \\ \hline
        """
        itemCorr = itemCorr+r"""                    \multicolumn{1}{|c|}{$"""+alphastr+r"""\left("""+a1str+r"""x"""+signb1+b1str+r"""\right)\left("""+a2str+r"""x"""+signb2+b2str+r"""\right)$} & \color{red}{$"""+x1str+r"""$}  &  \color{red}{$"""+x2str+r"""$} \\ \hline
        """
    exo=r"""\clearpage
    \renewcommand\arraystretch{3}
    \Question["""+str(2*n)+r"""] Pour chacun des produits suivants donnez les valeurs $x_1$ et $x_2$ qui annulent le produit (on donnera les valeurs sous forme exacte et simplifiée) :\\
        \begin{center}
            \begin{tabular}{C{3cm}|C{2cm}|C{2cm}|}
                \cline{2-3} & $x_1$ & $x_2$  \\ \hline
"""+item+r"""
            \end{tabular}
        \end{center}"""
    correction=r"""\clearpage
    \Question["""+str(2*n)+r"""] Pour chacun des produits suivants donnez les valeurs $x_1$ et $x_2$ qui annulent le produit (on donnera les valeurs sous forme exacte et simplifiée) :\\
        \begin{center}
            \begin{tabular}{C{3cm}|C{2cm}|C{2cm}|}
                \cline{2-3} & $x_1$ & $x_2$  \\ \hline
"""+itemCorr+r"""
            \end{tabular}
        \end{center}"""
    return(exo,correction)

def polyDegre2_DisN1(n:int=1, Niveau:int=2): 
    # Niveau = 1 -> Discriminant avec des entiers
    # Niveau = 2 -> Discriminant avec des fractions
    x = Symbol('x')
    
    for i in range(n):
        # signe_a = (-1 if random.randint(1,100)%2==0 else 1)
        # signe_b = (-1 if random.randint(1,100)%2==0 else 1)
        # signe_c = (-1 if random.randint(1,100)%2==0 else 1)
        if Niveau==1:
            a = random.randint(1,5)*(-1 if random.randint(1,100)%2==0 else 1)
            b = random.randint(1,5)*(-1 if random.randint(1,100)%2==0 else 1)
            c = random.randint(1,5)*(-1 if random.randint(1,100)%2==0 else 1)
            pass
        if Niveau==2:
            a = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
            b = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
            c = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)

        delta = b**2-4*a*c
        # while delta!=0:
        #     a = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        #     b = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        #     c = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        #     delta = b**2-4*a*c
        str_expr = str(a)+"*x**2"+(("+"+str(b)) if b>0 else ("-"+str(b)))+"*x"+(("+"+str(c)) if c>0 else ("-"+str(c)))
        expr = sympify(str_expr)
        solutions = real_roots(str_expr, x)
        answer = r"""
        Le polynôme est de la forme $"""+latex(expr).replace("frac","dfrac")+r"""$ avec $a="""+latex(a).replace("frac","dfrac")+r"""$, $b="""+latex(b).replace("frac","dfrac")+r"""$ et $c="""+latex(c).replace("frac","dfrac")+r"""$.\\
                        On calcul le discriminant $\Delta$:
                        \begin{equation*}
                            \begin{array}{l@{}>{\displaystyle}l}
                            \Delta	&{}= b^2-4ac \\
                                    &{}= \left("""+latex(b).replace("frac","dfrac")+r"""\right)^2-4\times\left("""+latex(a).replace("frac","dfrac")+r"""\right)\times\left("""+latex(c).replace("frac","dfrac")+r"""\right)\\
                                    &{}= """+latex(b**2-4*a*c).replace("frac","dfrac")+r"""
                            \end{array}
                        \end{equation*}"""
        if delta<0:
            answer = answer + r"""
						On a donc $\Delta<0$ donc l'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ n'a pas de solution dans $\mathbb{R}$."""
            pass
        if delta==0:
            x0 = -b/(2*a)
            answer = answer + r"""
                        On a donc $\Delta=0$ donc l'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet 1 solution :
                        \begin{equation*}
                            \begin{array}{l@{}>{\displaystyle}l}
                                x_0 &= \dfrac{-b}{2a}\\
                                x_0 &= \dfrac{-\left("""+latex(b).replace("frac","dfrac")+r"""\right)}{2\times """+latex(a).replace("frac","dfrac")+r"""}\\
                                x_0 &= """+latex(x0).replace("frac","dfrac")+r"""
                            \end{array}
                        \end{equation*}
                        L'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet donc $x_0 = """+latex(x0).replace("frac","dfrac")+r"""$ comme solutions."""
            pass
        if delta>0:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            answer = answer + r"""
                        On a donc $\Delta>0$ donc l'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet 2 solutions :
                        \begin{equation*}
                        \begin{split}
                            x_1 &= \dfrac{-b-\sqrt{\Delta}}{2a}\\
                            x_1 &= \dfrac{-\left("""+latex(b).replace("frac","dfrac")+r"""\right)-\sqrt{"""+latex(delta).replace("frac","dfrac")+r"""}}{2\times """+latex(a).replace("frac","dfrac")+r"""}\\
                            x_1 &= """+latex(x1).replace("frac","dfrac")+r"""
                        \end{split}
                            \quad\quad et \quad\quad
                        \begin{split}
                            x_2 &= \dfrac{-b+\sqrt{\Delta}}{2a}\\
                            x_2 &= \dfrac{-\left("""+latex(b).replace("frac","dfrac")+r"""\right)+\sqrt{"""+latex(delta).replace("frac","dfrac")+r"""}}{2\times """+latex(a).replace("frac","dfrac")+r"""}\\
                            x_2 &= """+latex(x2).replace("frac","dfrac")+r"""
                        \end{split}
                        \end{equation*}
                        L'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet donc $x_1 = """+latex(x1).replace("frac","dfrac")+r"""$ et $x_2 = """+latex(x2).replace("frac","dfrac")+r"""$ comme solutions."""
            pass
    exo = r"""
    \clearpage
    \renewcommand\arraystretch{1}
            \Question[20] Résoudre l'équation suivante dans $\mathbb{R}$ par la méthode du discriminant :
                \begin{enumerate}
                    \item $"""+latex(expr).replace("frac","dfrac")+r"""=0$
                        \fillwithlines{180mm}
                \end{enumerate}"""
    corr = r"""
    \clearpage
    \renewcommand\arraystretch{1}
            \Question[20] Résoudre les équations suivantes dans $\mathbb{R}$ par la méthode du discriminant :
                \begin{enumerate}
                    \item $"""+latex(expr).replace("frac","dfrac")+r"""=0$\\
                        """+answer+r"""
                \end{enumerate}"""
    return(exo,corr)

def main():
    exo,correction=polyDegre2_Factor()
    print(exo)
    print(correction)
    pass

if __name__ == '__main__':
    main()