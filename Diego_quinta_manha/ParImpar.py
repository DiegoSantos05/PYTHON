VetLido = [0] * 10
VetPar = [0] * 10
VetImpar = [0] * 10

for X in range (10):
    VetLido [X] = int(input(f'Numero {X+1}:'))

P = 0
I = 0
for X in range (10): 
    if VetLido[X] % 2 ==0:
        VetPar[P] = VetLido [X]
        P+=1
    else:
        VetImpar [I] = VetLido[X]
        I+=1
print (f'Vetor lido: {VetLido}')
print (f'Vetor PAR, tamanho {P}: {VetPar[0:P]}')
print (f'Vetor Impar, tamanho {I}: {VetImpar[0:I]}')