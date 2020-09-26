'''
A string of characters including only alphabets (lowercase letters) is provided as an input.

The first task is to compute the frequency of each character appearing in the string. In the output, the characters have to be arranged in the same order as they appear in the input string.
Then characters have to be rearranged, such that all the characters having a specific frequency, say x, come together.
Let the frequency of a character, lying in between the two characters having same frequency x, be y. The steps to be followed for getting the desired arrangement are as follows:

If y>x, then shift the character at the end.
If y<x, then shift the character at the beginning.
Input:
Line 1 contains the string of characters without spaces.
Line 2 contains an integer N.
Line 3 contains N integers separated by space, N1 N2 … NN. These are the specific frequency values whose corresponding characters should come together.
Output:
Line 1 has characters and their frequency as computed originally. Each output value is separated using a space.
Each of the following N lines contains the rearranged sequence of characters and their frequency for the given N specific frequencies. Each line in the output has output values separated using a space.
Constraints:
Number of characters in the string ranges in between 1 and 1000.
Sample Input:
nomatterhowbusyyoumaythinkyouareyoumustfindtimeforreadingorsurrenderyourself
toselfchosenignorance
3
3 1 6
Sample Output:
n 8 o 11 m 4 a 5 t 6 e 10 r 10 h 3 w 1 b 1 u 7 s 6 y 6 i 5 k 1 f 4 d 3 g 2 l 2 c 2
k 1 b 1 w 1 n 8 o 11 m 4 a 5 t 6 e 10 r 10 h 3 d 3 g 2 l 2 c 2 u 7 s 6 y 6 i 5 f 4
k 1 b 1 w 1 n 8 o 11 m 4 a 5 t 6 e 10 r 10 h 3 d 3 g 2 l 2 c 2 u 7 s 6 y 6 i 5 f 4
c 2 l 2 g 2 d 3 h 3 k 1 b 1 w 1 n 8 o 11 m 4 a 5 t 6 s 6 y 6 i 5 f 4 e 10 r 10 u 7
EXPLANATION:
First line has characters and their frequency as computed using the given input string. 
The characters are arranged in the same order as per their appearance in the original string. Second line is obtained after rearranging characters appearing thrice together. 
Similarly, Third line is generated after placing characters that are coming only once together. 
The Third line output is similar to the Second line output as targeted characters (having frequency one) automatically comes in continuation during the previous rearrangement corresponding to frequency three.
 Lastly, the Fourth line presents the final character and frequency sequence after putting characters with frequency 6 together.
'''
# first we have to calculate the things that have found

input_string = "nomatterhowbusyyoumaythinkyouareyoumustfindtimeforreadingorsurrenderyourselftoselfchosenignorance"
frequencies = {} 
  
for char in input_string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1
# n8 o 11 
print(frequencies)
list1 = []
for key, value in frequencies.items() :
    list1.append(key)
    list1.append(value)

print(list1)
# for frequencies we have to use the odd positions 
# for letters use the even position

# now search for all the frequency 1 letters


temp_list = []

for i in range(1,len(list1)-1,2):
    if list1[i] == 3: # checking the elements which have frequency of 3
        temp_list.append(i)
i = temp_list[0]
j = temp_list[-1]
x = len(temp_list)
    
# now we have the position for the last and first element with frequency 3
print(temp_list) # min is the start position and max is the end position
print(list1[max(temp_list)-1])
# now we have to merge them and move the values greater than that at end of the list and smaller than that at the beginning of the list


# for i in range(temp_list[0],temp_list[-1],2):
print(temp_list)

while list1[i-1]!='d':
    # if the frequency is greater than 3 then we have to remove and append the element at end of the list

    print(list1)
    print("element at position:",i,"  ",list1[i-1],list1[i])
    if list1[i] > 3:
        #element is appended at last
        list1.append(list1[i-1])
        list1.append(list1[i])
        # break
        #remove the element also
        del list1[i]
        del list1[i-1]
        i = i - 2
    if list1[i]<3:
        # element to be inserted at beginning 
        list1.insert(0,list1[i])
        list1.insert(0,list1[i])
        
    #     #remove the element also
        del list1[i-1+2]
        del list1[i+1]
        # i = i + 2
    i = i+2



print(list1)
