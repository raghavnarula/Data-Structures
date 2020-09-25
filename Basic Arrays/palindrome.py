# using two pointer technique for palindrome operations
a = "A man, a plan, a canal: Panama"
# take only range of ord values
# from 65 to 122
import sys
i = 0
j = len(str(a))-1

pal_string = "".join(char for char in a if char.isalnum()).lower()
print(pal_string)
print(pal_string == pal_string[::-1])
