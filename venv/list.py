list1=list()
list2=list([10,2,3,4,5,4])
#list3=list(["tom","jerry","pluto"])
#list4=list("python")

print(list1)
print(list2)
#print(list3)
#print(list4)

#Functions for a list
list3=[2,3,4,1,30]

print( 2 in list3)
print( 2 not in list3)
print(len(list3))
print(max(list3))
print(min(list3))
print(sum(list3))

#List slicing
print(list3[1:4])
print(list3[:3])
print(list3[3:])

#list operator
print(list3+list2)
print(list3*3)


'''
# Loop
for i in list2:
    if(i==3):
        break
    print(i,end=" ")
'''

#List Functions
list2.append(19)
print(list2)
print(list2.count(4))
list2.extend(list3)
print(list2)
print(list2.index(19))
list2.insert(3,56)
print(list2)