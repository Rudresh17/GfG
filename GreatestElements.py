cases=int(input(""))
for m in range(0,cases):
    size,x=[int(x) for x in input("").split()]
    numbers=list(map(int, input (). split ()))
    numbers.sort(reverse=True)
    print(" ".join(map(str, numbers[:x])))
    
    
        