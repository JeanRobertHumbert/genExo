import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

from baseMaths import *

def calculMentalFractionN1(n=3):
    itemQ = r""" """
    itemR=r""" """
    for i in range(0,3*n):
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = random.randint(1,10)
        d = random.randint(1,10)
        op = random.randint(1,3)
        if op==1:
            operator = " + "
            answer = sp.Rational(a*d+b*c, b*d)
        if op==2:
            operator = " - "
            answer = sp.Rational(a*d-b*c, b*d)
        if op==3:
            operator = r""" \times """
            answer = sp.Rational(a*c, b*d)
        itemQ=itemQ+r"""                \item $\dfrac{"""+str(a)+r"""}{"""+str(b)+r"""}"""+operator+r"""\dfrac{"""+str(c)+r"""}{"""+str(d)+r"""}=.............$
    """
        itemR=itemR+r"""                \item $\dfrac{"""+str(a)+r"""}{"""+str(b)+r"""}"""+operator+r"""\dfrac{"""+str(c)+r"""}{"""+str(d)+r"""}=\color{red}{\dfrac{"""+str(answer.numerator)+r"""}{"""+str(answer.denominator)+r"""}}$
    """

    exo=r"""
    \Question Calcule mentale : effectuez les calculs suivants :
        \begin{multicols}{3}
            \begin{enumerate}
"""+itemQ+r"""
            \end{enumerate}
        \end{multicols}
    """
    correction=r"""
    \Question Calcule mentale : effectuez les calculs suivants :
        \begin{multicols}{3}
            \begin{enumerate}
"""+itemR+r"""
            \end{enumerate}
        \end{multicols}
    """
    return(exo, correction)

def exoPourcentage2ndv1():
    nbEleves, nbFilles, nbGarcons, nb2GT1, nb2GT3, partGarcons, partFilles, part2GT1, part2GT3 = symbols('nbEleves nbFilles nbGarcons nb2GT1 nb2GT3 partGarcons partFilles part2GT1 part2GT3') 
    nbFilles = random.randint(10,20) #values[0]
    nbGarcons = random.randint(5,15) #values[1]
    nbEleves = nbFilles+nbGarcons
    nb2GT1 = random.randint(5,nbEleves-5) #values[2]
    nb2GT3 = nbEleves-nb2GT1
    partGarcons = Rational(nbGarcons/nbEleves)
    partFilles = Rational(nbFilles/nbEleves)
    part2GT1 =  Rational(nb2GT1/nbEleves)
    part2GT3 =  Rational(nb2GT3/nbEleves)
    exo=r"""
        \Question Un groupe est composé de """+str(nbEleves)+r""" élèves, """+str(nbFilles)+r""" filles et """+str(nbGarcons)+r""" garçons. """+str(nb2GT1)+r""" élèves de ce groupe sont en 2GT1  et les """+str(nb2GT3)+r""" autres viennent de la 2GT3.
            \begin{parts}
                \Part[2] Quelle est la part des garçons dans ce groupe ?
                    \fillwithlines{15mm}
                \Part[2] Quelle est la part des filles dans ce groupe ?
                    \fillwithlines{15mm}
                \Part[2]  Quelle est la part des élèves issus de 2GT1 ?
                    \fillwithlines{15mm}
                \Part[2]  Quelle est la part des élèves issus de 2GT3 ?
                    \fillwithlines{15mm}
            \end{parts}
    """
    correction=r"""
        \Question Un groupe est composé de """+str(nbEleves)+r""" élèves, """+str(nbFilles)+r""" filles et """+str(nbGarcons)+r""" garçons. """+str(nb2GT1)+r""" élèves de ce groupe sont en 2GT1  et les """+str(nb2GT3)+r""" autres viennent de la 2GT3.
            \begin{parts}
                \Part[2] Quelle est la part des garçons dans ce groupe ?
                    \begin{solution}
                        La part de garçons représente $\dfrac{"""+str(nbGarcons)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(partGarcons.round(4))+r"""$ soit $"""+str(partGarcons.round(4)*100)+r"""\%$
                    \end{solution}
                \Part[2] Quelle est la part des filles dans ce groupe ?
                    \begin{solution}
                        La part de filles représente $\dfrac{"""+str(nbFilles)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(partFilles.round(4))+r"""$ soit $"""+str(partFilles.round(4)*100)+r"""\%$
                    \end{solution}
                \Part[2]  Quelle est la part des élèves issus de 2GT1 ?
                    \begin{solution}
                        La part des élèves de 2GT1 représente $\dfrac{"""+str(nb2GT1)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(part2GT1.round(4))+r"""$ soit $"""+str(part2GT1.round(4)*100)+r"""\%$
                    \end{solution}
                \Part[2]  Quelle est la part des élèves issus de 2GT3 ?
                    \begin{solution}
                        La part des élèves de 2GT3 représente $\dfrac{"""+str(nb2GT3)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(part2GT3.round(4))+r"""$ soit $"""+str(part2GT3.round(4)*100)+r"""\%$
                    \end{solution}
            \end{parts}
    """
    return(exo,correction)

def exoPourcentage2ndv2():
    nbMachines, nbJoint, nbProg, nbProgOnly, nbProgJoint  = symbols('nbMachines nbJoint nbProg nbProgOnly nbProgJoint') 
    nbMachines = random.randint(300,400)
    nbJoint = random.randint(100,200) #values[1]
    nbProg = nbMachines-nbJoint
    nbProgJoint = random.randint(10,nbProg-50) #values[2]
    nbProgOnly = nbProg-nbProgJoint
    partJoint = Rational(nbJoint/nbMachines)
    partProgOnly = Rational(nbProgOnly/nbMachines)
    exo=r"""
        \Question Benoît a réparé """+str(nbMachines)+r""" machines à laver. Il a changé le joint sur """+str(nbJoint)+r""" machines et le programmateur sur les autres dont """+str(nbProgJoint)+r""" présentaient aussi un défaut de joint qu'il a aussi remplacé.
            \begin{parts}
                \Part[2] Quel est le pourcentage de machines ayant un joint défectueux ?
                    \fillwithlines{15mm}
                \Part[4] Quel est le pourcentage de machines ayant seulement le programmateur défectueux ?
                    \fillwithlines{15mm}
            \end{parts}
    """
    correction=r"""
        \Question Benoît a réparé """+str(nbMachines)+r""" machines à laver. Il a changé le joint sur """+str(nbJoint)+r""" machines et le programmateur sur les autres dont """+str(nbProgJoint)+r""" présentaient aussi un défaut de joint qu'il a aussi remplacé.
            \begin{parts}
                \Part[2] Quel est le pourcentage de machines ayant un joint défectueux ?
                    \begin{solution}
                        Sur les """+str(nbMachines)+r""" machines, il y a $"""+str(nbJoint)+r"""$ machines ayant un joint défectueux. Le pourcentage de machines ayant un joint défectueux est donc :
                        \begin{center}
                            $\dfrac{"""+str(nbJoint)+r"""}{"""+str(nbMachines)+r"""}\approx """+str(partJoint.round(4))+r"""$ soit $"""+str(partJoint.round(4)*100)+r"""\%$
                        \end{center}
                    \end{solution}
                \Part[4] Quel est le pourcentage de machines ayant seulement le programmateur défectueux ?
                    \begin{solution}
                        Sur les """+str(nbMachines)+r""" machines, il y a $"""+str(nbMachines)+r"""-"""+str(nbJoint)+r"""$ soit $"""+str(nbProg)+r"""$ machines qui ont le programmateur défectueux mais $"""+str(nbProgJoint)+r"""$ présentent également un joint défectueux.\\
                        Il y a donc $"""+str(nbProg)+r"""-"""+str(nbProgJoint)+r"""$ soit $"""+str(nbProgOnly)+r"""$ machines qui n'ont que le programmateur défectueux.\\
                        La part de machines ayant uniquement le programmateur défectueux est donc :
                        \begin{center}
                            $\dfrac{"""+str(nbProgOnly)+r"""}{"""+str(nbMachines)+r"""}\approx """+str(partProgOnly.round(4))+r"""$ soit $"""+str(partProgOnly.round(4)*100)+r"""\%$
                        \end{center}
                    \end{solution}
            \end{parts}
    """
    return(exo,correction)

def genfonctionAffine():
    af, bf, x, f = symbols('af bf x f')
    ag, bg, g = symbols('ag bg g')
    ah, bh, h = symbols('ah bh h')
    values = nonEqRandomValue(n=3, notNull=True)
    af = values[0] 
    ag = values[1] 
    ah = values[2]
    values = nonEqRandomValue(n=3, notNull=True)
    bf = values[0]
    bg = values[1]
    bh = values[2]
    f = af*x+bf
    g = ag*x+bg
    h = ah*x+bh
    g0 = bg
    g1 = ag*ag.denominator+bg
    solfg = solve(f-g, rational=True)
    solf = solve(f, rational=True)
    xI = (bh-bf)/(af-ah)
    fh = f-h
    yI = af*(bh-bf)/(af-ah)+bf
    # Pour le tableau de signe et variation
    tabSigneVar = r"""
    					\tkzTabLine
					     { , - , z , + , }
					   \tkzTabVar
					     { -/$-\infty$, R/ ,  +/$+\infty$}
    """
    if af<0:
        tabSigneVar = r"""
					   \tkzTabLine
					     { , + , z , - , }
					   \tkzTabVar
					     { +/$+\infty$, R/ ,  -/$-\infty$}
          """
    exo=r"""
    \clearpage
    \Question Fonctions Affines\\
        Dans le repère orthonormé ci-dessous, la courbe $\mathcal{C}_f$ est la représentation graphique de $f$ une fonction définie par $f(x)="""+Latex(f)+r"""$.
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[
                        axis x line=middle,
                        axis y line=middle,
                        xmin = -10, xmax = 10,
                        ymin = -10, ymax = 10,
                        xtick distance = 1,
                        ytick distance = 1,
                        grid = both,
                        minor tick num = 1,
                        major grid style = {gray},
                        minor grid style = {gray!25},
                        width = \textwidth,
                        height = \textwidth
                        ]
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};
                    \draw (axis cs:0,0) circle node [left, below] {$O$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        blue,
                        ] {"""+str(f)+r"""} node[pos=0.35,above,] {$\mathcal{C}_f$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        green,
                        ] {"""+str(h)+r"""} node[pos=0.55,above,] {$\mathcal{C}_h$};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{parts}
        \small{
            \Part[2] Représenter la fonction $g(x)="""+Latex(g)+r"""$
                \fillwithlines{25mm}
            \Part[1] Donner le coefficient directeur et l'ordonnée à l'origine de la fonction $g$.
                \fillwithlines{20mm}
            \Part[4] Résoudre $f(x)=g(x)$ et donner une interprétation de votre résultat.
                \fillwithlines{25mm}
            \Part[4] Déterminer l'expression algébrique de la fonction $h$ dont la représentation graphique est la droite $\mathcal{C}_h$
                \fillwithlines{25mm}
            \Part[4] Déterminer les coordonnées du point $I$, intersection de la courbe $\mathcal{C}_f$ et $\mathcal{C}_h$.
                \fillwithlines{25mm}
            \Part[2] Résoudre $f(x)=0$
                \fillwithlines{25mm}
            \Part[4] Compléter le tableau de signe et variations de $f$ ci-dessous
                \begin{center}
                    \begin{tikzpicture}
                        \tkzTabInit %[lgt=3]
                            {$x$ / 1 , Signe de $f$ / 1, Variations de $f$ / 3 }
                            {$+\infty$, , $+\infty$}
                        \tkzTabLine
                            { ,  ,  ,  , }
                        \tkzTabVar
                            { ,  ,  }
                    \end{tikzpicture}
                \end{center}
            }
        \end{parts}
        """
    correction=r"""
    \clearpage
        \Question Fonctions Affines (Correction)\\
        Dans le repère orthonormé ci-dessous, la courbe $\mathcal{C}_f$ est la représentation graphique de $f$ une fonction définie par $f(x)="""+Latex(f)+r"""$.
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[
                        axis x line=middle,
                        axis y line=middle,
                        xmin = -10, xmax = 10,
                        ymin = -10, ymax = 10,
                        xtick distance = 1,
                        ytick distance = 1,
                        grid = both,
                        minor tick num = 1,
                        major grid style = {gray},
                        minor grid style = {gray!25},
                        width = \textwidth,
                        height = \textwidth
                        ]
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};
                    \draw (axis cs:0,0) circle node [left, below] {$O$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        blue,
                        ] {"""+str(f)+r"""} node[pos=0.35,above,] {$\mathcal{C}_f$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        green,
                        ] {"""+str(h)+r"""} node[pos=0.55,above,] {$\mathcal{C}_h$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        red,
                        ] {"""+str(g)+r"""} node[pos=0.6,above,] {$\mathcal{C}_g$};
                    \draw[red] (axis cs:0,"""+str(g0)+r""") circle(3pt) node [left, below] {$G_1$};
                    \draw[red] (axis cs:"""+str(ag.denominator)+r""","""+str(g1)+r""") circle(3pt) node [left, below] {$G_2$};
                    \draw (axis cs:"""+str(xI)+r""","""+str(yI)+r""") circle(3pt) node [left, below] {$I$};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{parts}
        \small{
            \Part Représenter la fonction $g(x)="""+Latex(g)+r"""$
    %        			\fillwithlines{25mm}
                \\La fonction $g$ est une fonction affine ( forme $ax+b$). La représentation graphique de $g$ est donc une droite. \\
                Selon le premier axiome d'Euclide, il faut deux points pour définir de façon unique une droite. nous allons donc déterminer deux couples antécédent-image qui constitueront les coordonnées des deux points dont nous avons besoin.
                \begin{enumerate}
                    \item On choisi par commodité 0 comme premier antécédent d'où :\\
                    $g(0)="""+Latex(g0)+r"""$ on a donc le premier point $G_1$ aux coordonnées $(0;"""+Latex(g0)+r""")$
                    \item On détermine maintenant l'image d'un deuxième antécédent d'où :\\
                    $g("""+Latex(ag.denominator)+r""")="""+Latex(g1)+r"""$ on a donc le deuxième point $G_2$ aux coordonnées $("""+Latex(ag.denominator)+r""";"""+Latex(g1)+r""")$
                    \item On place les points $G_1$ et $G_2$ puis on trace la droite passant par ses deux points et on la nomme $\mathcal{C}_g$.
                \end{enumerate}
            \Part Donner le coefficient directeur et l'ordonnée à l'origine de la fonction $g$.
    %        			\fillwithlines{20mm}
                \\Comme énoncé à la question précédente, la fonction $g$ est une fonction affine donc sa forme est $ax+b$ où $a$ est appelé "coefficient directeur" et $b$ "ordonnée à l'origine".\\
                Donc par analogie entre $"""+Latex(g)+r"""$ et $ax+b$, le coefficient directeur est $"""+Latex(ag)+r"""$ et l'ordonnée à l'origine est $"""+Latex(bg)+r"""$.
            \Part Résoudre $f(x)=g(x)$ et donner une interprétation de votre résultat.
    %	        		\fillwithlines{25mm}
                \begin{align*}
                    f(x)&=g(x)\text{    (On remplace $f$ et $g$ par leurs expressions)}\\
                    \Leftrightarrow """+Latex(f)+r""" &= """+Latex(g)+r"""\\
                    \Leftrightarrow """+Latex(f-g)+r""" &= 0\\
                    \Leftrightarrow x &= """+Latex(solfg[0])+r"""
                \end{align*}
                Donc pour que $f(x)=g(x)$ il faut que $x="""+Latex(solfg[0])+r"""$. Cette solution de l'équation est la seule valeur d'antécédent pour laquelle $f$ et $g$ donnent la même image.\\
                Il s'agit donc de l'abscisse du point d'intersection des deux droite représentative de $f$ et $g$ ($\mathcal{C}_f$ et $\mathcal{C}_g$).
                \Part Déterminer l'expression algébrique de la fonction $h$ dont la représentation graphique est la droite $\mathcal{C}_h$
                %	        		\fillwithlines{25mm}
                \\ La courbe $\mathcal{C}_h$ est une droite donc l'expression algébrique de la fonction $h$ est de la forme $ax+b$.\\
                On remarque que $\mathcal{C}_h$ passe par le point $(0;"""+Latex(bh)+r""")$ ce qui signifie que $b="""+Latex(bh)+r"""$.\\
                A partir de ce point, on remarque que si l'on se déplace de """+str(ah.denominator) +r""" sur l'axe des abscisses, on évolue de """+str(ah.numerator)+r""" sur l'axe des ordonnées. On peut en déduire que :\\
                $a=\dfrac{"""+str(ah.numerator)+r"""}{"""+str(ah.denominator) +r"""}$\\
                Donc l'expression de $h$ est $h(x)="""+Latex(h)+r"""$.
            \Part Déterminer les coordonnées du point $I$, intersection de la courbe $\mathcal{C}_f$ et $\mathcal{C}_h$.\\
            %	        		\fillwithlines{25mm}
                Le point $I(x_I;y_I)$ avec $x_I$ solution de $f(x)=h(x)$ et $y_I=f(x_I)=h(x_I)$
                On résous donc $f(x)=h(x)$ :
                \begin{align*}
                    f(x)&=h(x)\text{    (On remplace $f$ et $h$ par leurs expressions)}\\
                    \Leftrightarrow """+Latex(f)+r""" &= """+Latex(h)+r"""\\
                    \Leftrightarrow """+Latex(f-h)+r""" &= 0\\
                    \Leftrightarrow x &= """+Latex(xI)+r"""
                \end{align*}
                Donc $S=\lbrace"""+Latex(xI)+r"""\rbrace$ et $x_I="""+Latex(xI)+r"""$.\\
                On $y_I$ image de la fonction $f$ ou $h$ de $x_I$ :\\
                $y_I="""+Latex(af)+r"""\times"""+Latex(xI)+r"""+"""+Latex(bf)+r"""="""+Latex(yI)+r"""$\\
                Donc $I\left("""+Latex(xI)+r""";"""+Latex(yI)+r"""\right)$
            \Part Résoudre $f(x)=0$\\
                %	        		\fillwithlines{25mm}
                \begin{align*}
                    f(x)&=0\text{    (On remplace $f$ par son expression)}\\
                    \Leftrightarrow """+Latex(f)+r""" &= 0\\
                    \Leftrightarrow """+Latex(af*x)+r""" &= """+Latex(-bf)+r"""\\
                    \Leftrightarrow x &= """+Latex(-bf/af)+r"""
                \end{align*}
                Donc $f(x)=0$ pour $x="""+Latex(-bf/af)+r"""$
            \Part Compléter le tableau de signe et variations de $f$ ci-dessous\\
                \begin{center}
                    \begin{tikzpicture}
                    \tkzTabInit %[lgt=3]
                    {$x$ / 1 , Signe de $f$ / 1, Variations de $f$ / 3 }
                    {$+\infty$, $"""+Latex(-bf/af)+r"""$, $+\infty$}
                    """+tabSigneVar+r"""
                    \end{tikzpicture}
                \end{center}
        }
    \end{parts}
    """

    return(exo,correction)

def exoAffineReprEtExpression():
    n=6
    alphabet = list(string.ascii_lowercase)
    fonctions = random.sample(alphabet, n)
    fonctions.sort()
    # print(fonctions)
    itemRepr = r""""""
    itemLect = r""""""
    itemLectCorrection = r""""""
    addplot = r""""""
    addplotCorrection = r""""""
    f1 = fonctions[:3]
    f2 = fonctions[3:]
    for f in f1:
        k = nonEqRandomValue(n=2, notNull=True, tier=False, quart=False)
        p = affine(f, k[0], k[1])
        pos=0.55
        if p.a>0:
            pos = min(0.95,0.45+p.supTo(5)/10)
        if p.a<0:
            pos = min(0.95,0.45+p.supTo(-5)/10)
            # pos = max(0.1,0.45+p.supTo(5)/10)
            # print("("+str(p.a)+";"+str(p.b)+") -> "+str(p.supTo(5).evalf()))
        addplot = addplot + r"""\addplot[thick, color=red] {"""+str(p.a)+r"""*x+"""+str(p.b)+r"""} node[above, sloped, pos = """+str(pos)+r"""] {$\mathcal{C}_"""+p.name+r"""$};
        """
        itemLect = itemLect + r"""
                            \item $\mathcal{C}_"""+p.name+r"""$ : $"""+p.name+r"""(x)=......................$
        """
        itemLectCorrection = itemLectCorrection + r"""
                            \item $\mathcal{C}_"""+p.name+r"""$ : {\color{red} """+p.latexString()+r"""}
        """
    n=3
    for f in f2:
        k = nonEqRandomValue(n=2, notNull=True, tier=True)
        p = affine(f, k[0], k[1])
        pos=0.55
        if p.a>0:
            pos = min(0.95,0.45+p.supTo(5)/10)
        if p.a<0:
            pos = min(0.95,0.45+p.supTo(-5)/10)
        addplotCorrection = addplotCorrection + r"""\addplot[thick, color=blue] {"""+str(p.a)+r"""*x+"""+str(p.b)+r"""} node[above, sloped, pos = """+str(pos)+r"""] {$\mathcal{C}_"""+p.name+r"""$};
        """
        itemRepr = itemRepr + r"""
        					\item {\color{blue} """+p.latexString()+r"""}
        """

    exo=r"""
        \Question Représentation et Expression algébrique de fonctions affines
                    \begin{multicols}{2}
                    \begin{parts}
                        \Part[6] Représentez graphiquement les fonctions suivantes :
                        \begin{enumerate}
                            """+itemRepr+r"""
                        \end{enumerate}
                        \Part[6] Donnez les expressions algébrique des fonctions associées aux droites suivantes :
                        \begin{enumerate}
                            """+itemLect+r"""
                        \end{enumerate}
                    \end{parts}
                        \vfill
                        \columnbreak
                        \begin{center}
                            \begin{tikzpicture}[scale=1]
                                \begin{axis}[
                                    scale only axis,
                                    grid=major,
                                    axis lines=middle,
                                    inner axis line style={=>},
                                    ytick={-5,-4,...,5},
                                    xtick={-5,-4,...,5},
                                    ymin=-5,
                                    ymax=5,
                                    xmin=-5,
                                    xmax=5,
                                ]
                                """+addplot+r"""
                                \end{axis}
                            \end{tikzpicture}
                        \end{center}
                    \end{multicols}
                    Zone de travail :
                    \fillwithlines{90mm}
    """
    correction=r"""
        \Question Représentation et Expression algébrique de fonctions affines
                    \begin{multicols}{2}
                    \begin{parts}
                        \Part[6] Représentez graphiquement les fonctions suivantes :
                        \begin{enumerate}
                            """+itemRepr+r"""
                        \end{enumerate}
                        \Part[6] Donnez les expressions algébrique des fonctions associées aux droites suivantes :
                        \begin{enumerate}
                            """+itemLectCorrection+r"""
                        \end{enumerate}
                    \end{parts}
                        \vfill
                        \columnbreak
                        \begin{center}
                            \begin{tikzpicture}[scale=1]
                                \begin{axis}[
                                    scale only axis,
                                    grid=major,
                                    axis lines=middle,
                                    inner axis line style={=>},
                                    ytick={-5,-4,...,5},
                                    xtick={-5,-4,...,5},
                                    ymin=-5,
                                    ymax=5,
                                    xmin=-5,
                                    xmax=5,
                                ]
                                """+addplot+addplotCorrection+r"""
                                \end{axis}
                            \end{tikzpicture}
                        \end{center}
                    \end{multicols}
    """
    return(exo , correction)

def ThalesPythagore():
    values = nonEqRandomValue(n=3, debut=1, fin=5, demi=True, tier=False, notNull=False)
    ab, bd, ac, ad, ce, bc, de = symbols('ab bd ac ad ce bc de') 
    ab = random.randint(1,4) #values[0]
    bd = random.randint(1,3) #values[1]
    ac = random.randint(1,4) #values[2]
    ad = ab+bd
    ce = Rational(ac*ad/ab-ac)
    ae = ac+ce
    bc = sqrt(ab**2+ac**2)
    exo=r"""
        	\clearpage
		\Question Thalès et Pythagore\\
			Dans la figure ci-dessous, $AB="""+str(ab)+r"""$, $DB="""+str(bd)+r"""$, $AC="""+str(ac)+r"""$ et $AE="""+Latex(ae)+r"""$
			\begin{center}
				\begin{tikzpicture}[scale=1] % fixed points
					\tkzDefPoint(2,3){A}
					\tkzDefShiftPoint[A](0:"""+str(ab)+r"""){B}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDefShiftPoint[A](90:"""+str(ae)+r"""){E}					
					\tkzDefShiftPoint[A](0:"""+str(ad)+r"""){D}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDrawSegments(A,B B,C C,A A,D A,E D,E)
%					\tkzMarkSegments[mark=|](A,B A,C)
					\tkzDrawPoints(A,B,C,D,E)
					\tkzLabelPoints(B,D)
					\tkzLabelPoints[above left](A,C,E)
				\end{tikzpicture}
			\end{center}
			\begin{parts}
				\Part[4] Montrer que $(BC)$ et $(DE)$ sont parallèles
					\fillwithlines{35mm}
				\Part[4] Sachant que le triangle $ABC$ est rectangle en $A$
					\begin{enumerate}
						\item Calculer $BC$
							\fillwithlines{30mm}
						\item Calculer $DE$
							\fillwithlines{30mm}
					\end{enumerate}
			\end{parts}
    """
    correction=r"""
    	\clearpage
		\Question Thalès et Pythagore\\
			Dans la figure ci-dessous, $AB="""+str(ab)+r"""$, $DB="""+str(bd)+r"""$, $AC="""+str(ac)+r"""$ et $AE="""+Latex(ae)+r"""$
			\begin{center}
				\begin{tikzpicture}[scale=1] % fixed points
					\tkzDefPoint(2,3){A}
					\tkzDefShiftPoint[A](0:"""+str(ab)+r"""){B}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDefShiftPoint[A](90:"""+str(ae)+r"""){E}					
					\tkzDefShiftPoint[A](0:"""+str(ad)+r"""){D}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDrawSegments(A,B B,C C,A A,D A,E D,E)
%					\tkzMarkSegments[mark=|](A,B A,C)
					\tkzDrawPoints(A,B,C,D,E)
					\tkzLabelPoints(B,D)
					\tkzLabelPoints[above left](A,C,E)
				\end{tikzpicture}
			\end{center}
			\begin{parts}
				\Part Montrer que $(BC)$ et $(DE)$ sont parallèles\\
%					\fillwithlines{35mm}
					Selon le théorème de Thalès, on a la double égalité suivante :
					\begin{center}
						$\dfrac{AB}{AD}=\dfrac{AC}{AE}=\dfrac{BC}{DE}$
					\end{center}
					On sait que  $AB="""+str(ab)+r"""$, $DB="""+str(bd)+r"""$, $AC="""+str(ac)+r"""$ et $AE="""+str(ae)+r"""$. Donc $AD=AB+BD="""+str(ab)+r"""+"""+str(bd)+r"""="""+str(ad)+r"""$.\\
					On calcule séparément $\dfrac{AB}{AD}=\dfrac{"""+str(ab)+r"""}{"""+str(ad)+r"""}$ et $\dfrac{AC}{AE}=\dfrac{"""+str(ac)+r"""}{"""+Latex(ae)+r"""}="""+Latex(ac/ae)+r"""$\\
					Les deux quotients sont égaux, on peut donc en déduire que $(BC)$ et $(DE)$ sont parallèles.
				\Part Sachant que le triangle $ABC$ est rectangle en $A$
					\begin{enumerate}
						\item Calculer $BC$
%							\fillwithlines{30mm}
							Si le triangle $ABC$ est rectangle en $A$ alors le théorème de Pythagore s'applique et on a donc l'égalité suivante :
							\begin{center}
								$BC^2=AB^2+AC^2$
							\end{center}
							$BC^2="""+str(ab)+r"""^2+"""+str(ac)+r"""^2="""+str(ab**2)+r"""+"""+str(ac**2)+r"""="""+str(bc**2)+r"""$ donc $BC=\sqrt{"""+str(bc**2)+r"""}="""+Latex(bc)+r"""$
						\item Calculer $DE$
%							\fillwithlines{30mm}
							Selon la double égalité de Thalès de la première question, on a :
							\begin{center}
								$\dfrac{AB}{AD}=\dfrac{BC}{DE}$\\
								donc $\dfrac{"""+Latex(ab)+r"""}{"""+Latex(ad)+r"""}=\dfrac{"""+Latex(bc)+r"""}{DE}$\\
								d'où $DE="""+Latex(bc)+r"""\times \dfrac{"""+Latex(ad)+r"""}{"""+Latex(ab)+r"""}="""+Latex(bc*ad/ab)+r"""$
							\end{center}
					\end{enumerate}
			\end{parts}
    """
    return(exo,correction)

def main():
    # exo,correction=lectureGraphiqueAffine()
    # print(exo)
    # print(correction)
    pass

if __name__ == '__main__':
    main()