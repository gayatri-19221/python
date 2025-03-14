##Interchange first and last elements in a list
list=["1","2","3","4","5"]
a=list[0]
print("a:",a)
b=list[4]
print("b:",b)
print("original list:",list)
temp=list[0]
list[0]=list[4]
list[4]=temp
print("After interchange the list:",list)