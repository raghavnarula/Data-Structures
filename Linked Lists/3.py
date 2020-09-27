import insertion,circular_linked_lists

list = circular_linked_lists.List()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)
list.insert(6)
list.insert(7)

last = list.headval

# while last.nextval is not None:
#     last = last.nextval

# last.nextval = list.headval
# end = list.headval
# for _ in range(10):
#     end = end.nextval
# print(end.dataval)


for i in range(10):
    last = last.nextval
    if last.nextval is None:
        last.nextval = list.headval
        # here we have the list as circular

list.print_list_circular()
print(last.dataval)