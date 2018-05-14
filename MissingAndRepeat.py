cases=int(input(""))
results_rep=[]
results_misssing=[]
for r in range(0,cases):
    size=int(input(""))
    missing,repeated,count=0,0,-1
    numbers=list(map(int, input (). split ())) 
    numbers.sort()   
    end=numbers[size-1]               
    for k in range(1,end):
        if(k not in numbers):
            results_misssing.append(k)
        count=numbers.count(k)
        if(count==2):
            results_rep.append(k)
    results_misssing.sort()
    results_rep.sort()
    print(results_rep[0],results_misssing[0])
    results_misssing.clear()
    results_rep.clear()



    