valor1 = float(input())
valor2 = float(input())
valor3 = float(input())

if valor1 >= valor2 and valor1 >= valor3:
    print("O primeiro valor é o maior.")

elif valor2 >= valor1 and valor2 >= valor3:
    print("O segundo valor é o maior.")

elif valor3 >= valor1 and valor3 >= valor2:
    print("O terceiro valor é o maior.")

elif valor1 == valor2 and valor1 == valor3:
    print("Os valores são iguais.")