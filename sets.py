'''
Mathematically a set is a collection of items not in any particular order. A Python set is similar to this mathematical definition with below additional conditions.

The elements in the set cannot be duplicates.
The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

'''

Days = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months = {"Jan","Feb","march"}
Dates = {21,22,23}

print(Days,'\n',Months,'\n',Days)


# Accessing the values
print("Acessing the elements")
for d in Days:
    print(d)

print("Adding the values to the set")
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.add("Sun")
print(Days)

# Union and intersection of sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(['Mon','Sun'])
intersectionDays = DaysA & DaysB
print(intersectionDays)
unionDays = DaysA|DaysB
print(unionDays)

# comparing 2 sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes) # returns boolean values
print(SupersetRes)