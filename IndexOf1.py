cases=int(input(""))
result=0
flag=-1
for r in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input (). split ()))
    for a in range(0,size):
        if(numbers[a]==1 and flag==-1):
            result=a
            flag=1
    if(result>=0):
        print(result)
    else:
        print("-1")
    result=-1
    flag=-1