while True:
    num = list(map(int, input("Digite os números: ").split()))
    
    if entrada.upper() == "FIM":
        break

    num.sort()
    
    print(num)