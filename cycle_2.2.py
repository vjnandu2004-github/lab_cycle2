# read a string containing numbers seperated by space and convert it into int list
strlist=list(map(str,input().split()))
print(strlist)
intlist=[int(i) for i in strlist]

    
#intlist : rotate the elements into kth position
k=int(input("enter k:"))
lst2=[]
for index in range (len(intlist)):
    val=intlist[index]
    position=(index+k)%len(intlist)
    
    lst2.insert(position,val)
print(lst2)



for y in lst2:
    if lst2.count(lst2[y])!=1:
        lst2.remove(lst2[y])
        
tpl1=tuple(lst2)
print(tpl1)
lst3=list(tpl1)

lst3.sort()
print(lst3)
lst4=[(x**2-x) for x in lst3]
print(lst4)
lst5=lst4+lst3
lst5.sort()
print(lst5)

