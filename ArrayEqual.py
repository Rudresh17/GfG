cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    listone=list(map(int,input().split()))
    listtwo=list(map(int,input().split()))
    listone.sort()
    listtwo.sort()
    #setone=set(listone)
    #settwo=set(listtwo)
    if(listone==listtwo):
        print("1")
    else:
        print("0")