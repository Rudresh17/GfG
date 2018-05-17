cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    missing=0
    results=[]
    numbers=list(map(int,input().split()))
    numbers.sort()
    for i in range(0,size-1):
        if(numbers[i]+1==numbers[i+1] and numbers[i]>=0):
            continue
        else:
            no=numbers[i]+1
            results.append(no)
    print(results[0])
    results.clear()

