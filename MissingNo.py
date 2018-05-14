#find the missing number in the array
cases=int(input(""))

for r in range(0,cases):
    size=int(input(""))
    numbers= list(map(int, input (). split ()))
    numbers.sort()
    count=len(numbers)
    for k in range(1,size):
        if(numbers.count(k)>0):
            continue
        else:
            print(k)
       
        

        
        