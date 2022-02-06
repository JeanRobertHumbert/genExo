import random
import subprocess
import os

a = 7
b = 100
c = -77
d = 100
e = 49
f = 20
k = 10
for i in range(0,1):
    with open('result'+str(i)+'.tex', 'w') as outfile:
        with open("p1.txt") as infile:
            for line in infile:
                outfile.write(line)
        coeff = random.randint(2,10)
        outfile.write("			$C(x)=\dfrac{"+str(a*coeff)+"}{"+str(b)+"}x^3+\dfrac{"+str(c*coeff)+"}{"+str(d)+"}x^2+\dfrac{"+str(e*coeff)+"}{"+str(f)+"}x+{"+str(k*coeff)+"}$")
        with open("p2.txt") as infile:
            for line in infile:
                outfile.write(line)
    subprocess.call('pdflatex result'+str(i)+'.tex')
    os.remove('result'+str(i)+'.log')
    os.remove('result'+str(i)+'.aux')
    os.remove('result'+str(i)+'.tex')