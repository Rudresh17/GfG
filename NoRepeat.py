cases=int(input(""))
for m in range(0,cases):
    size=int(input(""))
    nrepeat=[]
    line=str(input(""))
    for i in range(0,len(line)):
        if(line.count(line[i])<2):
            nrepeat.append(line[i])
    if(len(nrepeat)==0):
        print("-1")
    else:
         print(nrepeat[0])
    nrepeat.clear()

    