cases=int(input(""))
flag=0
flag1=0
results=[]
for m in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input(). split()))
    for i in range(0,size):
        no=str(numbers[i])
        end=len(no)
        for r in range(0,end):
            if(int(no[r])==1 or int(no[r])==2 or int(no[r])==3 and flag==0):
                flag=1

        if(flag==1):
                results.append(no)
                flag=0
                flag1=1
        flag=0
                
    
            

    if(flag1==1):
        results.sort()
        print(" ".join(map(str, results)))
        results.clear()
        flag=0 
    else:
        print("-1")
    
    
    
