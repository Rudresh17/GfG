cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input (). split ()))
    numbers.reverse()
    print(" ".join(map(str, numbers)))

    
