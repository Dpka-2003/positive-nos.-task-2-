n=input("Enter the elements separated by space:")
list1=n.split()
list2=[]
print("List of positive numbers")
for i in list1:
    if int(i)>=0:
        list2.append(int(i))
    else:
        pass
print(list2)
