#find the missing number in the array
cases=int(input(""))
numbers=[]
result=[]
count=0
count1=0
for r in range(0,cases):
    size=int(input(""))
    numbers= list(map(int, input (). split ()))
    count=len(numbers)
    for k in range(1,size):
        count1=numbers.count(k)
        if(count1>0):
            continue
        else:
            result.append(k)
        
for a in result:
    print(int(a))
     
        
        