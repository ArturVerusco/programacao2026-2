num = 0

while num:
    num = list(int,input().split())
    num.sort()
    if num != "FIM":
        continue

    print(num)