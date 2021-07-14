# nums = [1,2,3]
# res = []
# subset = []
# pos = 0
# print(len(nums))

# def unique(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] == arr[j]:
#                 return False
#     return True
        
# def recursion(nums,subset,start):
#     if len(subset) == len(nums):
#         # all are distinct numbers 
#         if unique(subset):
#             res.append(subset.copy())
#         # print(res)
#         return
    
#     else: # do it for a small case
        
        
#         for i in range(len(nums)):
#             subset.append(nums[i])
#             # print(subset)
#             recursion(nums,subset,start+1)
#             subset.pop()
#             # print("res after:",res)
        
          

# recursion(nums,subset,0)  
# # print(unique(nums))
# print(res)


# def permute(nums):
#     def helper(nums, answer):
#         if (len(nums)==0):
#             res.append(answer[:])
#             return 
#         for i in range(len(nums)):
#             ch = nums[i]
#             left_substr = nums[0:i]
#             right_substr = nums[i + 1:]
#             rest = left_substr + right_substr
#             # print("rest: ",left_substr ,"+", right_substr)
#             helper(rest, answer + [ch])
#     res = []
#     helper(nums, [])
#     # return res


# print(permute(nums))

def subset(nums, subset, index):
    print(*subset)
    for i in range(index, len(nums)): 
          
        subset.append(nums[i])
          
        subset(nums, subset, i + 1) 
        subset.pop(-1) 
    return
  
nums = [1, 2, 3]

subset(nums, [], 0) 
      