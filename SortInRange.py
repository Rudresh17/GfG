#sort in a given range
def insertionSort(arr,a,b):
 
    # Traverse through 1 to len(arr)
    for i in range(a+1,b+1):
 
        key = arr[i]
 
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
cases=int(input(""))
numbers=[]
sort=[]
left=[]
right=[]
result=[]

for m in range(0,cases):
    size=int(input(""))
    numbers=list(map(int, input (). split ()))
    a,b = [int(x) for x in input("").split()]
    if(a<b):
        insertionSort(numbers,a,b)
        print(numbers)
        
    else:
        insertionSort(numbers,b,a)
        print(numbers)
        
        

