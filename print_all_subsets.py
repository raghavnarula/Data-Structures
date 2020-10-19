a = [10,20,30]

# print all subsets of the given set

'''
start with null 
then add 1st element till nth element
then the second element till nth elemnt
and so onn
'''
# final = []
# def subset(a,start,end):
#     list1 = []
#     if start == end:
#         return 
#     else:
#         for i in range(start,end+1):
#             list1.append(a[i]) # 1st is appended in the list
#             print(list1)
#             subset(a,start+1,end)
#             ## ending statement that 
#             list1.pop()

# # subset(a,0,2)


# print(list)
# prints all the subsets starting with 1 
def help(a,i):
    if i==len(a):
        return 
    else:
        list.append(a[i])
        print(list)
        i = i + 1
        help(a,i)

for i in range(2):
    list = []
    help(a,i)