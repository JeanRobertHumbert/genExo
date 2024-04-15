# La fonction de calcul d'un nombre de Fibonacci
def fibonacci(n):
   if n < 0 :
     print("N doit être supérieur ou égal à 0")
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
 
# La fonction de calcul des nombres de Fibonacci compris entre 2 entiers positifs
def fibo_number(int_a, int_b):
  n = 0
  valueList = []
  while fibonacci(n) <= max (int_a, int_b) :
    valueList.append(fibonacci(n))
    n+=1
  return [i for i in valueList if min(int_a, int_b) <= i <= max (int_a, int_b)]

def prime_numbers(integer):
    prime_nums = []
    for num in range(integer):
        if num > 1: # tous les nombres premiers sont supérieurs strictement à 1
            for i in range(2, num):
                if (num % i) == 0: # le reste de la division d'un nombre premier par un nombre inférieur à lui est toujours différent de 0
                    break
            else:
                prime_nums.append(num)
 
    return prime_nums

def eratosthene(n):
    P = [ ]
    for i in range(2,n+1):
        if len(P) == 0:
            P.append(i)
        else:
            prem = True
            for k in P:
              if i % k == 0:
                  prem = False
            if prem == True:
              P.append(i)
    
    return P
def eratostheneL(n):
    L = [ i for i in range(2,n+1) ]
    P = [ ]
    
    while len(L) != 0:
        P.append(L[0])
        i = L[0]
        for k in L:
            if k % i == 0:
                del(L[L.index(k)])
    
    return P
print(eratostheneL(100000))
