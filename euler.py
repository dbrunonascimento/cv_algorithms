from decimal import Decimal, getcontext

'''
 - 0.0.1b
 - Estudo: Numero de Euler com o metodo de Jakob Bernoulli 
'''
def euler(p):

    n = (10**p)-1  
    p += 1
    getcontext().prec = p
    e = (1+(Decimal(1)/n))**n
    return e

print(euler(400))

