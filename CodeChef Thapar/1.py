input_string = input("")
frequencies = {} 
  
for char in input_string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1
list1 = []
for key, value in frequencies.items() :
    list1.append(key)
    list1.append(value)

number = int(input())                                # for size
list_numbers = list(map(int, input().split(' ')[:number]))  # to input n elements

for el in list1:
        print(el,end=" ")
print()

for num in list_numbers:
    temp_list = []
    for i in range(1,len(list1),2):
        if list1[i] == num: 
            temp_list.append(i)
    i = temp_list[0]
    j = temp_list[-1]
    maximum = max(temp_list)
    last_alpha = list1[maximum-1]
    while list1[i-1] != last_alpha:

        if list1[i] > num:
            list1.append(list1[i-1])
            list1.append(list1[i])
            del list1[i]
            del list1[i-1]
            i = i - 2
        if list1[i] < num:
            list1.insert(0,list1[i])
            list1.insert(0,list1[i])
            
            del list1[i-1+2]
            del list1[i+1]
        i = i+2
    for el in list1:
        print(el,end=" ")
    print()