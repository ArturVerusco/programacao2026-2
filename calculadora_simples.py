
a = 0


while a != 5:
    print('[1] Calculadora Simples')
    print('[2] Calculadora Ângulo')
    print('[3] Sair do programa')
    a = int(input('Qual sua opção?: '))

    if a == 1:  
        
        n1,simbolo,n2 = map(input("Digite a equação: ").split())
        n1 = float
        simbolo = str
        n2 = float

        if simbolo == "+" :
            print(n1+n2)

        elif simbolo == "-" :
            print(n1-n2)

        elif simbolo == "*":
            print(n1*n2)

        elif simbolo == "/":
            print(n1/n2)

    elif a == 2:
        
        n1 = float(input())

        if n1 < 90:
            print("Ângulo Agudo!")
        
        if n1 == 90:
            print("Ângulo Reto!")
        
        if n1 > 90 and n1 < 180:
            print("Ângulo Obtuso!")

        if n1 == 180:
            print("Ângulo Raso!")

        if n1 > 180 and n1 < 360:
            print("Ângulo Côncavos!")

        if n1 == 360:
            print("Ângulo Completo!")

    elif a == 3:
        print('Encerrando programa...!')
        break
print("FIM!")