cases=int(input(""))
for m in range(0,cases):
    num_fac=1
    n_r_fac=1
    r_fac=1
    divide,rfac=0,1
    n,r = [int(x) for x in input("").split()]
    for k in range(1,n+1):
        num_fac*=k
   # print(num_fac)
    n_r=n-r
    for r in range(1,n_r+1):
       n_r_fac*=r
    for a in range(1,r):
        r_fac*=a 
    result=float(0)
    result=long((num_fac/(n_r_fac*r_fac)))
    print(int(result))
    
    

    
    