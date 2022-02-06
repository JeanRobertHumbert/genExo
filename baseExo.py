import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

def coeffPoly3Deg(genCode="9999999999"):
	directory = os.path.dirname(__file__)
	print(directory)
	xa = 2+random.randint(1,3)*3
	ya = 0.0
	xc = 6+random.randint(1,3)*2
	yc = 0.0
	xb = (xa+xc)/2.0
	yb = -2.0
	A = np.array([[xa**2,xa,1], [xb**2,xb,1], [xc**2,xc,1]], dtype=float)
	B = np.array([ya,yb,yc], dtype=float)

	sol = np.linalg.solve(A, B)
	print(sol)
	dd = random.randint(10,15)
	x = np.linspace(0, 15, 30)
	y = (sol[0]*x**3)/3+(sol[1]*x**2)/2+sol[2]*x+dd
	plt.plot(x, y)
	plt.xlim(0,20)
	plt.ylim(-0.5,40)
	plt.title("Coût en fonction de la quantité",fontsize=14)
	plt.xlabel("Quantité -> x",fontsize=12)
	plt.ylabel("Coût -> C(x)",fontsize=12)
	plt.savefig(directory+"\\"+genCode+'-fig1.png')
	plt.show() # affiche la figure a l'ecran
	aa = (sol[0])/3
	bb = (sol[1])/2
	cc = sol[2]
	sol = [aa, bb, cc, dd, directory+"\\"+genCode+'-fig1.png']
	return(sol)

def header(titre="", genCode="0000000000", Correction="Sujet"):
    header=r"""
%!TEX encoding = UTF-8 Unicode
% !TEX TS-program = lualatex
\documentclass[12pt,%
addpoints,%
%answers%
]{exam}

\usepackage[frenchb]{babel}
\usepackage{tikz,tkz-tab, tkz-base}
\tikzset{every picture/.style={execute at begin picture={\shorthandoff{:;!?};}}}
\tikzstyle{every picture}+=[remember picture]
\tikzstyle{na} = [shape=rectangle,inner sep=0pt]
\usepackage{pgfplots}
\usepackage{multicol}
%--------------------------------------------------------------------------------------
\usepackage{enumerate}
\usepackage{fourier}
\usepackage{xspace}
\usepackage{amsmath,amssymb,amstext,makeidx}
\usepackage{fancybox}
\usepackage{tabularx}
\usepackage[normalem]{ulem}
\usepackage{pifont}
\usepackage[euler]{textgreek}
\usepackage{textcomp,enumitem}
\newcommand{\euro}{\eurologo{}}
%\usepackage{pst-plot,pst-tree,pst-func,pstricks-add}
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\D}{\mathbb{D}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\C}{\mathbb{C}}
\usepackage[left=3.5cm, right=3.5cm, top=1.9cm, bottom=2.4cm]{geometry}
\newcommand{\vect}[1]{\overrightarrow{\,\mathstrut#1\,}}
\renewcommand{\theenumi}{\textbf{\arabic{enumi}}}
\renewcommand{\labelenumi}{\textbf{\theenumi.}}
\renewcommand{\theenumii}{\textbf{\alph{enumii}}}
\renewcommand{\labelenumii}{\textbf{\theenumii.}}
\def\Oij{$\left(\text{O}~;~\vect{\imath},~\vect{\jmath}\right)$}
\def\Oijk{$\left(\text{O}~;~\vect{\imath},~\vect{\jmath},~\vect{k}\right)$}
\def\Ouv{$\left(\text{O}~;~\vect{u},~\vect{v}\right)$}

\definecolor{aliceblue}{rgb}{0.94, 0.97, 1.0}
\usepackage{numprint}
\renewcommand\arraystretch{1.1}
\newcommand{\e}{\text{e}}
%\frenchbsetup{StandardLists=true}
\usepackage{babel}
\usepackage{enumerate}
%---Pour les arbres de probabilités----------------------------------------------------
\usepackage{pstricks,pst-node,pst-tree}
\usepackage{pst-plot,pst-tree,pst-func,pstricks-add}
\usepackage{graphicx}
\usepackage{fancybox}
\usepackage{tabularx}
%---Définition de la page et des marges------------------------------------------------
\setlength{\paperheight}{297mm}
\setlength{\paperwidth}{210mm}
\setlength{\textheight}{26cm}
\setlength{\textwidth}{15cm}
\setlength{\leftmargin}{-1cm}%
\setlength{\rightmargin}{1cm}%
%---Définition de l'entête de page et du pied de page----------------------------------
\pagestyle{headandfoot}
\firstpageheader{Nom : \\ Prénom :}
  {}
  {classe : TSTMG \\ Date : \today}
\firstpagefooter{LPO G. BRASSENS}{Page \thepage\ / \numpages}{Session 2021-22}
\runningheadrule
\runningfootrule
\lhead{Nom : \\ Prénom :}
\chead{"""+titre+r"""\small{"""+Correction+r""" - genCode : """+genCode+r"""}}
\rhead{TSTMG}
\runningfooter{LPO G. BRASSENS}{Page \thepage\ / \numpages}{Session 2021-22}



%---Définition de Question-------------------------------------------------------------
\def\Question{	
	\renewcommand*{\questionlabel}{\fbox{Exercice \thequestion : }}
	\question
}
\def\Part{
	\renewcommand*{\partlabel}{\fbox{\thepartno : }}
	\part
}
%--------------------------------------------------------------------------------------

%\usepackage{xparse,xpatch}
% redefine \part command to be \mypart
\appto\parts{\let\exampart\part\let\part\mypart}

\def\multiplechoice{54}
\def\freeresponse{46}
\makeatletter
\ExplSyntaxOn
% this will become a sequence of the part numbers and scores
% like: 1a&10&, 1b&8&, 1c&9&, 2a&6, 2b&8&, 3&12&, 4&14&, ...
\seq_new:N \g_part_scores_seq
\tl_new:N \g_grade_table_tl

\int_new:N \g_total_score_int% this will be the exam score
\int_new:N \g_number_of_scores_int
\NewDocumentCommand\mypart{o}{
  \IfNoValueTF{#1}{\exampart}{
    % don't do anything special inside solutions
    \if@insolution\exampart[#1]
    \else\exampart[#1]
      % store both the part number and score in \g_part_scores_seq
      % together with their column separators for the tabular env
      \tl_set:Nx \l_tmpa_tl { \arabic{question}\alph{partno} }
      \tl_put_right:Nn \l_tmpa_tl {&}
      \tl_put_right:No \l_tmpa_tl {#1}
      \tl_put_right:Nn \l_tmpa_tl {&}
      \seq_gput_right:No \g_part_scores_seq \l_tmpa_tl
      % increment the running total and number of scores
      \int_gadd:Nn \g_total_score_int {#1}
      \int_gincr:N \g_number_of_scores_int
    \fi
  }
}
% print row #1 of the part scores in the grade table
\cs_new:Nn \__add_row_to_grade_table:n {
   \tl_gput_right:Nx \g_grade_table_tl {\seq_item:Nn \g_part_scores_seq {#1}}
   \tl_gput_right:Nn \g_grade_table_tl { & }
   \tl_gput_right:Nx \g_grade_table_tl {\seq_item:Nn \g_part_scores_seq {#1+\g_number_of_scores_int/2}}
   \tl_gput_right:Nn \g_grade_table_tl {\\\hline}
}
\NewDocumentCommand\GradeTable{}{% the new grade table
  % we need an exam number of scores so add two
  % empty cells if we have an odd number
  \int_if_odd:nT {\g_number_of_scores_int} {
      \seq_gput_right:Nn \g_part_scores_seq {&}
      \int_ginc:N \g_number_of_scores_int
  }
  \int_gset:Nn \g_number_of_scores_int {\g_number_of_scores_int}
  \int_gadd:Nn \g_total_score_int { \multiplechoice }
  \int_gadd:Nn \g_total_score_int { \freeresponse }
  % create the grade table
  \tl_gclear:N \g_grade_table_tl
  \int_step_function:nnN {1} {\g_number_of_scores_int/2} \__add_row_to_grade_table:n
  \begin{tabular}{|c|c|c|c|c|c|}\hline
    Question & Points~Possibles & Points~Acquis & Question & Points~Possibles & Points~Acquis \\\hline
    \tl_use:N \g_grade_table_tl
    \multicolumn2{c|}{}&\multicolumn{2}{r|}{\textit{Total}}
        & \int_use:N \g_total_score_int & \\\cline{3-6}
  \end{tabular}
}
\ExplSyntaxOff
\makeatother
%-------------------------------------------------------------------------------------


\hsword{Score:}
\usepackage{lipsum}
\usepackage{mdframed}
\renewenvironment{solution}
{\begingroup\par\parshape0%
\begin{mdframed}[%skipabove=\baselineskip,
%                 innertopmargin=\baselineskip,
%                 innerbottommargin=\baselineskip,
                 userdefinedwidth=\textwidth,
                 backgroundcolor=blue!5]
\textbf{Solution:}\enspace\ignorespaces}
{\end{mdframed}\par\endgroup}



\begin{document}

\begin{titlepage}

\newcommand{\HRule}{\rule{\linewidth}{0.5mm}} 							% horizontal line and its thickness
\center 
 
% University
\textsc{\LARGE LPO G.BRASSENS}\\[1cm]

% Document info
\textsc{\Large """+titre+Correction+r"""\\ \small{genCode : """+genCode+r"""}}\\[5cm]
%\textsc{\large COURSECODE}\\[1cm] 										% Course Code
\HRule \\[0.8cm]
{ \huge \bfseries Mathématiques}\\[0.7cm]								% Assignment
\HRule \\[5cm]
\large
\emph{Consignes:}\\%[1.5cm]													% Author info
\fbox{%
\begin{minipage}{\textwidth}
   \begin{itemize}[label=$*$]
		\item Vous rédigerez vos réponses directement sur le sujet dans les espaces prévus à cet effet.
		\item La calculatrice est autorisée.
		\item L'examen est noté sur un total de 40 points.
		\item L'épreuve dure 2 heures.
		\item Vous devez écrire votre nom et prénom sur chaque entête de page dans la zone prévue à cet effet.
	\end{itemize}
\end{minipage}
}
%\includegraphics[width=0.6\textwidth]{images/TU_delft_logo.jpg}\\[1cm] 	% University logo
\vfill 
\end{titlepage}

\clearpage



	\begin{questions}
    """
    return(header)

def ender():
    exo=r"""
    \end{questions}

\end{document}
    """
    return(exo)

def exoProba():
    pT = random.randint(10,80)
    pLsachantT = random.randint(10,80)
    pLsachantA = random.randint(10,80)
    pA=100-pT
    pLBsachantT=100-pLsachantT
    pLBsachantA=100-pLsachantA
    pL = round(pT*pLsachantT+pA*pLsachantA,4)
    exo = r"""
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
                                \draw[fleche] (Rb)--(Rbb) node[etiquette] {$"""+str(pLBsachantT)+r"""\%$};
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

def exoEvolution():
    anneeStart=1998
    data =[]
    for i in range(anneeStart, anneeStart+9):
        data.append([i,random.randint(4500,8500)])
    txQc = random.randint(5,49)
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
%							\addplot [red,only marks,mark=*] coordinates {(4,"""+str(data[3][1])+r""") (7,"""+str(data[6][1])+r""")}; % Tracé point à point
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
        data.append([i,random.randint(450,650)/10])

    q1Start = random.randint(0,6)
    q1End = random.randint(1,10-q1Start)
    q1End = q1Start+q1End
    q1Taux =  int(round(((data[q1End][1]-data[q1Start][1])/data[q1Start][1])*100,0))
    q2RacineN = (1+q1Taux/100)**((q1End-q1Start)**-1)-1
    q3Taux = random.randint(100, 900)/100
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

def exoDerivation(genCode="9999999999"):
	directory = os.path.dirname(__file__)
	# On définie les trois points A(xa,ya), B(xb,yb) et C(xc,yc) par lesquels la parabole doit passé
	xa, xb, xc = symbols('xa xb xc')
	ya, yb, yc = symbols('ya yb yc')
	xa = 2+random.randint(1,2)*3
	ya = 0.0
	xc = 6+random.randint(1,3)*2+1
	yc = 0.0
	xb = (xa+xc)/2.0
	yb = -4.0
	x, a, b, c = symbols('x a b c')
	# On résoud le système d'équations :
	# f(xa)=ya
	# f(xb)=yb
	# f(xc)=yc
	# pour trouver a, b et c de f(x)=ax^2+bx+c

	equations = [
		Eq( xa**2*a+xa*b+c ,  ya ),
		Eq( xb**2*a+xb*b+c ,  yb ),
		Eq( xc**2*a+xc*b+c ,  yc )
	]

	solution = solve(equations, rational=True)
	print(solution)
	a = solution[a]
	b = solution[b]
	c = solution[c]
	a_string = latex(a).replace("\\frac","\dfrac")
	b_string = latex(b).replace("\\frac","\dfrac")
	c_string = latex(c).replace("\\frac","\dfrac")

	Cprim = a*x**2+b*x+c
	Cprim_string = latex(Cprim).replace("\\frac","\dfrac")
	delta = b**2-4*a*c
	Rdelta = sqrt(delta)
	x1 = (-b-sqrt(delta))/(2*a)
	x1_string = latex(x1).replace("\\frac","\dfrac")
	x2 = (-b+sqrt(delta))/(2*a)
	x2_string = latex(x2).replace("\\frac","\dfrac")
	dd = random.randint(10,15)
	C = integrate(Cprim) + dd

	C_coeff = C.as_coefficients_dict()
	u = C_coeff[x**3]*x**3
	v = C_coeff[x**2]*x**2
	w = C_coeff[x]*x
	z = C_coeff[1]
	C_string = latex(C).replace("\\frac","\dfrac")
	u_string = latex(u).replace("\\frac","\dfrac")
	v_string = latex(v).replace("\\frac","\dfrac")
	w_string = latex(w).replace("\\frac","\dfrac")
	z_string = latex(z).replace("\\frac","\dfrac")
	coeff_u_string = latex(C_coeff[x**3]).replace("\\frac","\dfrac")
	coeff_v_string = latex(C_coeff[x**2]).replace("\\frac","\dfrac")
	coeff_w_string = latex(C_coeff[x]).replace("\\frac","\dfrac")
	coeff_z_string = latex(C_coeff[1]).replace("\\frac","\dfrac")

	Cprim_string = latex(Cprim).replace("\\frac","\dfrac")
	uprim_string = latex(a*x**2).replace("\\frac","\dfrac")
	vprim_string = latex(b*x).replace("\\frac","\dfrac")
	wprim_string = latex(c).replace("\\frac","\dfrac")
	coeff_uprim_string = latex(a).replace("\\frac","\dfrac")
	coeff_vprim_string = latex(b).replace("\\frac","\dfrac")
	coeff_wprim_string = latex(c).replace("\\frac","\dfrac")
	print(Cprim_string)
	print(C_string)
	delta = b**2-4*a*c
	rdelta = sqrt(delta)
	rdelta_string = latex(rdelta).replace("\\frac","\dfrac")
	delta_string = latex(delta).replace("\\frac","\dfrac")
	result = C_coeff[x**3]*x2**3+C_coeff[x**2]*x2**2+C_coeff[x]*x2+dd
	result_string = latex(result).replace("\\frac","\dfrac")
	if result.denominator==1:
		result_string = result_string
	else:
		result_string = result_string+r"""\approx """+str(round(result.n(),2))
	exo=r"""
    \Question
		Une usine produit des bonbons. Le responsable "production" a modélisé le cout de production de chacune des machines en fonction du poids de bonbons produit pour une machine. Si $x$ est le poids de bonbons produit alors $C(x)$ donne le coût de production au kilogramme en fonction de $x$ avec :
		\begin{center}
			$C(x)="""+C_string+r"""$\\
		\end{center}
		\begin{parts}
			\Part[3] Déterminer $C'(x)$, la fonction dérivée de $C(x)$\\
				\fillwithlines{50mm}
			\Part[3] Résoudre $C'(x)=0$\\
				\fillwithlines{70mm}
			\Part[3] En déduire le signe de $C'$ et les variations de $C$\\
				\fillwithlines{70mm}
			\Part[3] Conclure sur la quantité optimale de production et en donner donc le coût minimal au kilogramme\\
				\fillwithlines{20mm}
		\end{parts}
    """
	correction=r"""
    \Question
		Une usine produit des bonbons. Le responsable "production" a modélisé le cout de production de chacune des machines en fonction du poids de bonbons produit pour une machine. Si $x$ est le poids de bonbons produit alors $C(x)$ donne le coût de production au kilogramme en fonction de $x$ avec :
		\begin{center}
			$C(x)="""+C_string+r"""$\\
		\end{center}
		\begin{parts}
			\Part[3] Déterminer $C'(x)$, la fonction dérivée de $C(x)$\\
			\begin{solution}
				La fonction $C(x)$ est de la forme $u+v$ on a donc :
				\begin{center}
					$C(x)=u+v+w+z$\\
					avec $u="""+coeff_u_string+r"""x^3$, $v="""+coeff_v_string+r"""x^2$, $w="""+coeff_w_string+r"""x$ et $z="""+str(dd)+r"""$
				\end{center}
				$u$, $v$, $w$ et $z$ sont de la forme $kx^n$ or $(kx^n)'=knx^{n-1}$ on a donc :
				\begin{center}
					$C'(x)=u'+v'+w'+z'$\\
					avec $u'="""+coeff_uprim_string+r"""x^2$, $v'="""+coeff_vprim_string+r"""x$, $w'="""+wprim_string+r"""$ et $z'=0$
				\end{center}
				d'où :
				\begin{center}
					$C'(x)="""+coeff_uprim_string+r"""x^2+"""+coeff_vprim_string+r"""x+"""+coeff_wprim_string+r""" +0$\\
				\end{center}
				et donc :
				\begin{center}
					$C'(x)="""+coeff_uprim_string+r"""x^2+"""+coeff_vprim_string+r"""x+"""+coeff_wprim_string+r"""$\\
				\end{center}
			\end{solution}
			\Part[3] Résoudre $C'(x)=0$\\
			\begin{solution}
				$C'(x)$ est un polynôme du second degré, on utilise donc la méthode du discriminant.\\
				On écrit donc $C'(x)$ avec :
				\begin{center}
					$C'(x)=ax^2+bx+c$\\
					$a="""+latex(a).replace("\\frac","\dfrac")+r"""$, $b="""+latex(b).replace("\\frac","\dfrac")+r"""$ et $c="""+latex(c).replace("\\frac","\dfrac")+r"""$
				\end{center}
				On calcul $\Delta=b^2-4ac$ d'où :
				\begin{align*}
					\Delta	&=b^2-4ac\\
							&="""+b_string+r"""^2-4"""+a_string+r""""""+c_string+r"""\\
							&="""+delta_string+r"""=\left("""+rdelta_string+r"""\right)^2
				\end{align*}

				Donc $\Delta>0$, il y a donc 2 solutions à l'équation $C'(x)=0$
				\begin{multicols}{2}
				\begin{align*}
					x_1&=\dfrac{-b-\sqrt{\Delta}}{2a}\\
					x_1&=\dfrac{-\left("""+b_string+r"""\right)-\sqrt{"""+delta_string+r"""}}{2\times+"""+a_string+r"""}\\
					x_1&=\dfrac{-\left("""+b_string+r"""\right)-"""+rdelta_string+r"""}{2\times+"""+a_string+r"""}\\
					x_1&="""+x1_string+r"""
				\end{align*}
				
				\begin{align*}
					x_2&=\dfrac{-b+\sqrt{\Delta}}{2a}\\
					x_1&=\dfrac{-\left("""+b_string+r"""\right)+\sqrt{"""+delta_string+r"""}}{2\times+"""+a_string+r"""}\\
					x_1&=\dfrac{-\left("""+b_string+r"""\right)+"""+rdelta_string+r"""}{2\times+"""+a_string+r"""}\\
					x_2&="""+x2_string+r"""
				\end{align*}
				\end{multicols}
				Les 2 solutions sont donc $x_1="""+x1_string+r"""$ et $x_2="""+x2_string+r"""$
			\end{solution}
			\Part[3] En déduire le signe de $C'$ et les variations de $C$\\
			\begin{solution}
				Le polynôme est du signe de $-a$ entre ses racines d'où le tableau de signe et de variation suivant :
				\begin{center}
					\begin{tikzpicture}
						\tkzTabInit{$x$/1,$C'(x)$/1,$C$/3}{$-\infty$,$"""+x1_string+r"""$,$"""+x2_string+r"""$,$\infty$}
						\tkzTabLine{,+,z,-,z,+}
						\tkzTabVar{-/$-\infty$,+/$C\left("""+x1_string+r"""\right)$,-/$C\left("""+x2_string+r"""\right)$,+/$+\infty$}
					\end{tikzpicture}
				\end{center}
			\end{solution}
			\Part[3] Conclure sur la quantité optimale de production et en donner donc le coût minimal au kilogramme\\
			\begin{solution}
				La quantité optimale à produire est $"""+x2_string+r"""$ kilogrammes pour :
				\begin{align*}
					C("""+x2_string+r""")&="""+coeff_u_string+r"""\times \left("""+x2_string+r"""\right)^3+"""+coeff_v_string+r"""\times \left("""+x2_string+r"""\right)^2+"""+coeff_w_string+r"""\times """+x2_string+r"""+"""+coeff_z_string+r"""\\
						&="""+result_string+r"""
				\end{align*}
			\end{solution}
		\end{parts}
    """

	return(exo,correction)
