cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input (). split ()))
    index=int(input(""))
    k=int(numbers[index])
    numbers.remove(k)
    numbers.sort()
    numbers.insert(index,k)
    print(" ".join(map(str, numbers)))

