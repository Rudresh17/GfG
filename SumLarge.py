#sum of x+y equal to digits in x
cases=int(input(""))
for m in range(0,cases):
    x,y=[int(x) for x in input("").split()]
    total=x+y
    lenOfSum=len(str(total))
    lenOfX=len(str(x))
    if(lenOfSum==lenOfX):
        print(total)
    else:
        print(x)