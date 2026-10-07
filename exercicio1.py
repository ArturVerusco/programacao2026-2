num = []

while True:
    numeros = input("Digite os números (ou FIM para sair): ")
    
    if numeros.upper() == "FIM":
        break
        
    for x in numeros.split():
        valor = int(x)
        
        if valor not in num:
            num.append(valor)

    num.sort() 
    print(num)
