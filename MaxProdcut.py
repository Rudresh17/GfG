cases=int(input(""))
result=0
for r in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input (). split ()))
    numbers.sort()
    a=numbers[size-1]
    b=numbers[size-2]
    result=a*b
    print(result)