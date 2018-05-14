cases=int(input(""))
answers=[]
for r in range(0,cases):
    size=int(input(""))
    numbers=list(map(int,input().split()))
    for m in range(0,size):
        if(numbers.count(numbers[m])<2):
            answers.append(numbers[m])
    
    if(len(answers)>0): 
        print(answers[0])
    else:
        print("0")

    answers.clear()
