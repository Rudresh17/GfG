cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    results=[]
    count=0
    numbers=list(map(int,input().split()))
    for r in range(0,size):
        if(numbers[r]>0):
            results.append(numbers[r])
    count=numbers.count(0)
    for a in range(0,count):
        results.append(0)
    print(" ".join(map(str, results)))