cases=int(input(""))
flag=0
for m in range(0,cases):
    size,x=[int(x) for x in input("").split()]
    numbers=list(map(int, input (). split ()))
    for i in range(0,size):
        if(int(numbers[i])==x and flag==0):
            #print(i)
            pos=int(i)+1
            flag=1

    if(flag!=0):
        print(pos)
    else:
        print("-1")
    flag=0
    
    