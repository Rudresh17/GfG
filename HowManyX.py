cases=int(input(""))
answers=[]
for r in range(0,cases):
    integerFind=int(input(""))
    low=int(input(""))
    high=int(input(""))
    #low,high = [int(x) for x in input("").split()]
    result=0
    for i in range(low+1,high):
        string=str(i)
        length=len(string)
        for j in range(0,length):
            if(int(string[j])==integerFind):
                result=result+1
                
    answers.append(result)  
    
for m in (answers):
        print(int(m))
    
                
            

        


    
