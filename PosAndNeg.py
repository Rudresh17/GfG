cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    numbers=list(map(int,input().split()))
    answers=[]
    pos,neg,results=[],[],[]
    for i in range(0,size):
        if(numbers[i]>=0):
            no=-(numbers[i])
            if(numbers.count(no)>0):
                answers.append(no)
        else:
            no=-(numbers[i])
            if(numbers.count(no)>0):
                answers.append(no)
                
    for r in range(0,len(answers)):
        if(answers[r]>0):
            pos.append(answers[r])
        else:
            neg.append(answers[r])
    neg.sort(reverse=True)

    for k in range(0,len(neg)):
        results.append(neg[k])
        results.append(-neg[k])
    
    if(len(neg)==0):
        print("0")
    else:
        print(" ".join(map(str, results)))
   