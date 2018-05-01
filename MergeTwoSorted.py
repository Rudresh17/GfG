cases=int(input(""))
results=[]
for m in range(0,cases):
    size,no=[int(x) for x in input("").split()]
    numbers=list(map(int, input (). split ()))
    numbersTwo=list(map(int, input (). split ()))
    numbers.sort(reverse=True)
    numbersTwo.sort(reverse=True)
    results=numbers +numbersTwo
    results.sort(reverse=True)
    print(" ".join(map(str, results)))