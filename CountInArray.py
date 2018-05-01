cases=int(input(""))
for r in range(0,cases):
    size,x=[int(x) for x in input("").split()]
    numbers=list(map(int, input (). split ()))
    result=numbers.count(x)
    if(result>0):
        print(result)
    else:
        print("-1")
    