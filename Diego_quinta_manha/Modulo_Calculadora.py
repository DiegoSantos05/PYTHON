def divisao(a, b):
    ret = float(a) / b
    
    return ret

def multiplicacao(a, b):
    ret = a * b
    
    return ret

def soma(a, b):
    ret = a + b
    
    return ret

def subtracao(a, b):
    ret = a - b
    
    return ret

# Main
print("Digite o Primeiro Numero")
a = int(input())
print("Digite o Segundo Numero")
b = int(input())
print("Escolha uma Operação: (+,-,*,/)")
oPCAO = input()
if oPCAO == "+":
    rESULTADO = soma(a, b)
    print("O resultado da Soma é " + str(rESULTADO))
else:
    if oPCAO == "-":
        rESULTADO = subtracao(a, b)
        print("O resultado da subtracao é " + str(rESULTADO))
    else:
        if oPCAO == "*":
            rESULTADO = multiplicacao(a, b)
            print("O resultado da multiplicacao é " + str(rESULTADO))
        else:
            if oPCAO == "/":
                rESULTADO = divisao(a, b)
                print("O resultado da divisao é " + str(rESULTADO))
            else:
                print("OPCAO INVALIDA")
