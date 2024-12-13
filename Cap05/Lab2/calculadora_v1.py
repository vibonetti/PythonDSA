# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n\n")

operacao = int(input("Selecione o número da operação desejada\n\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n\nDigite sua opção: (1; 2; 3; 4): "))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operacao == 1:
    res = num1 + num2
    print("O resultado da soma é %s" %res)
elif operacao == 2:
    res = num1 - num2
    print("O resultado da subtração é %s" %res)
elif operacao == 3:
    res = num1 * num2
    print("O resultado da multiplicação é %s" %res)
elif operacao == 4:
    res = num1 / num2
    print("O resultado da divisão é %s" %res)
else:
    print("Número de operação inválido")