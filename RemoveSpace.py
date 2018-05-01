cases=int(input(""))
linee=[]
for m in range(0,cases):
    numbers=list(map(str, input (). split ()))
    count=len(numbers)
    for i in range(0,count):
        if " " in numbers[i]:
            numbers.pop(numbers[i])
    print(" ".join(map(str, numbers)))

