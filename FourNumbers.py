#count of four numbers equal to given number
cases=int(input(""))
results=[]
j,k,m,flag=0,0,0,0
for r in range(0,cases):
    size=int(input(""))
    numbers= list(map(int, input (). split ()))
    element=int(input(""))
    
    for i in range(0,size-3):
        if(int(numbers[i])+int(numbers[i+1])+int(numbers[i+2])+int(numbers[i+3])==element):
            flag=1

    if(flag==1):
        results.append(1)
    else:
        results.append(0)

for q in results:
    print(q)

            
