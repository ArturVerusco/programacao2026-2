while True:
    num = list(map(int, input("Digite os números: ").split()))
    
    if num.upper() == "FIM":
        break

    num.sort()
    
    print(num)