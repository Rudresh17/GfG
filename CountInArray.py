cases=int(input(""))
for r in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input (). split ()))
    for a in numbers:
        if(numbers.count(a)==1):
            print(a)
    