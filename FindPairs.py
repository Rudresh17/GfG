cases=int(input(""))
no1,no2=0,0
for m in range(0,cases):
    n,m,x=[int(x) for x in input("").split()]
    arrayOne=list(map(int, input (). split ()))
    arrayTwo=list(map(int, input (). split ()))
    if(n>m):
        end=n
    else:
        end=m
    for i in range(0,end):
        if(arrayOne[i]+arrayTwo[i]==x):
            no1=arrayOne[i]
            no2=arrayTwo[i]
        else:
            continue 

    print(no1,no2)
