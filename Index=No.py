cases=int(input(""))
results=[]
flag=0
for m in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input(). split()))
    for i in range(0,size):
        if(numbers[i]==i+1):
            results.append(numbers[i])
            flag=1
    
    if(flag==1):
        print(" ".join(map(str, results)))
    else:
        print("Not Found")
    results.clear()
    flag=0

        
       

    
    
       