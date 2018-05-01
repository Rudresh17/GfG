cases=int(input(""))
arrayOne=[]
arrayTwo=[]
results=[]
for r in range(0,cases):
    size=int(input(""))
    arrayOne=list(map(int, input (). split ()))
    arrayTwo=list(map(int, input (). split ()))
    arrayOne.sort()
    arrayTwo.sort()
    count=0
    for i in range(0,size):
        if(int(arrayOne[i])<=int(arrayTwo[i])):
            count+=1
        else:
            continue  
            
    if(count==size):
        results.append("YES")
    else:
        results.append("NO")

for a in results:                    
    print(str(a))               
    
