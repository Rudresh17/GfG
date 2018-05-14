cases=int(input(""))
positive=[]
negative=[]
result=[]
for r in range(0,cases):
    size=int(input(""))
    numbers= list(map(int, input (). split ()))
    for a in range(0,size):
        if(numbers[a]>=0):
            positive.append(numbers[a])
        else:
            negative.append(numbers[a])

    result=positive+negative
    print(" ".join(map(str, result)))
    result.clear()
    positive.clear()
    negative.clear()

