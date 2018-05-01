#all vowels delete
# # before consonants
#change case

cases=int(input(""))
names=[]
for i in range(cases):
    a=str(input(""))
    names.append(a)

size=len(names)

for i in names:
    if(i is'A'):
        names.pop(i)


print(names)
