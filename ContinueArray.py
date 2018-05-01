#see if array forms continuos numbers

cases=int(input(""))
array=[]
result=[]
count=0
for r in range(cases):
    size=int(input(""))

    #for i in range(0,size):
    array1 = input("")
    lent=len(array1)
    #print(arr)
    array1 = array1.split(' ')
    #print(array1)
    array = []
    for element in array1:
        array.append(element)
        #no=int(input("")
        #array.append(no)

    #print(array)
    array.sort()

    for i in range(1):
        if(int(array[i+1])-int(array[i])==1):
            flag=1 
        else:
            flag=0  
        
    if(flag==1):
        result.append("YES")
    else:
         result.append("NO")

   
for m in (result):
    print(m)
   
        
    


    








