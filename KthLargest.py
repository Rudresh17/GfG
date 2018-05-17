cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input(). split()))
    numbers.sort()
    k=int(input(""))
    print(numbers[k-1])