cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    results=[]
    numbers=list(map(int, input (). split ()))
    for a in range(1,size-1):
        if(numbers[a]>numbers[a-1] and numbers[a]<numbers[a+1]):
            results.append(numbers[a])
    if(len(results)>0):
        print(results[0])
    else:
        print("-1")
    results.clear()