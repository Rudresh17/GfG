cases=int(input(""))
results=[]
for r in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input (). split ()))
    for a in range(0,size):
        num=numbers[a]
        count=numbers.count(num)
        if(count%2==0):
            continue 
        else:
           if(results.count(num)>0):
               continue 
           else:
                results.append(num)

    print(" ".join(map(str, results)))
    results.clear()
           

    

    
    