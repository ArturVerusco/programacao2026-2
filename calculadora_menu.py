
a = 0

while a != 3:
    print('[1] Calculadora Simples')
    print('[2] Calculadora Ângulo')
    print('[3] Sair do programa')
    a = int(input('Qual sua opção?: '))

    if a == 1:  

        menu_2 = 0

        while menu_2 != 2:
            
            n1, simbolo, n2 = input("Digite a equação: ").split()
            n1, n2 = map(float, (n1,n2))
                
            if simbolo == "+" :
                print("Resultado:", n1+n2)
                print("Escolha uma opção: ")

            elif simbolo == "-" :
                print("Resultado:", n1-n2)
                print("Escolha uma opção: ")

            elif simbolo == "*":
                print("Resultado:", n1*n2)
                print("Escolha uma opção: ")

            elif simbolo == "/":
                if n2 != 0:
                    print("Resultado:", n1 / n2)
                    print("Escolha uma opção: ")
                else:
                    print("Não é possível dividir por zero!")
                    print("Escolha uma opção: ")

            else:
                print("Símbolo inválido!")
                print("Escolha uma opção: ")

            print("\n[1] Continuar na Calculadora")
            print("[2] Voltar")
            menu_2 = int(input("Qual sua opção?: "))
            if menu_2 == 2:
                    print("Escolha uma opção: ")

    elif a == 2:
        
        n1 = float(input("Digite um Ângulo: "))

        if n1 < 90:
            print("Ângulo Agudo!")
            print("Retornando para o Menu...\n")

        if n1 == 90:
            print("Ângulo Reto!")
            print("Retornando para o Menu...\n")

        if n1 > 90 and n1 < 180:
            print("Ângulo Obtuso!")
            print("Retornando para o Menu...\n")
            
        if n1 == 180:
            print("Ângulo Raso!")
            print("Retornando para o Menu...\n")

        if n1 > 180 and n1 < 360:
            print("Ângulo Côncavos!")
            print("Retornando para o Menu...\n")

        if n1 == 360:
            print("Ângulo Completo!")
            print("Retornando para o Menu...\n")
            
    elif a == 3:
        print('Encerrando programa...!')
        break

print("FIM!")