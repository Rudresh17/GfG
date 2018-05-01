cases=int(input(""))
results=[]
for m in range(0,cases):
    size=int(input(""))
    last,count=0,0
    numbers=list(map(int, input(). split()))
    x=int(input(""))
    count=numbers.count(x)
    for i in range(0,size):
        if(numbers[i]==x):    
          last=i
    first=(last+1)-count
    if(count!=0):
        print(first,last)
    else:
        print("-1")


    