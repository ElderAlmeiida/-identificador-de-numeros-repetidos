
from collections import Counter
import random
import numpy as np





def contadados(dados, x): 
    return dados.count(x) 


dados = []

for i in range(100):
 dados.append(random.randint(1,6))


um=1
dois=2
tres=3
quatro=4
cinco=5
seis = 6




print(dados)
print('{} = {} vezes'.format(um, contadados(dados, um)))
print('{} = {} vezes'.format(dois, contadados(dados, dois)))
print('{} = {} vezes'.format(tres, contadados(dados, tres)))
print('{} = {} vezes'.format(quatro, contadados(dados, quatro)))
print('{} = {} vezes'.format(cinco, contadados(dados, cinco)))
print('{} = {} vezes'.format(seis, contadados(dados, seis)))