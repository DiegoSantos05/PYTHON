# Criação do vetor de 10 posições reais 
VetLido = [0.0] * 10
print (VetLido)

#Inicialização das variáveis simples
Soma = 0 
NotaAcima = 0

# loop de leitura de VClasse 
for X in range (10):
    VetLido [X] = float (input(f'Nota {X +1}: '))

# loop para a soma dos valores 
for X in range (10): 
    Soma = Soma + VetLido [X]

Media = Soma / 10 # cálculo da média 

# loop de contagem dos valores de VClasse 
for X in range (10):
    if VetLido [X] > Media:
        NotaAcima = NotaAcima + 1
print (Media)
print (VetLido)
print ("Numero de Notas acima da média: ", NotaAcima)     

#verificar posição
print (VetLido [0])
print (VetLido [1])
print (VetLido [2])
print (VetLido [3])
print (VetLido [4])
print (VetLido [5])
print (VetLido [6])
print (VetLido [7])
print (VetLido [8])
print (VetLido [9])

