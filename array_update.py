########################################################     Problem   #########################################################################
# Chef Purchased an array A having N Integer values,After Playing it for while,he got bored of it and decided to update value of its element.  #
# In one second he can increase value of each array element by 1.He wants each array element’s value to become greater than or equal to K,     #
# Please Help Chef to find out the minimum amount of time it will take,for him to do so..                                                      #
# Input                                                                                                                                        #
# 3 4                                                                                                                                          #
# 1 2 5                                                                                                                                        #
# First line consists of two space separated integers denoting N and K.Second line of N space separated integers denoting the array A.         #
# Output                                                                                                                                       #
# 3                                                                                                                                            #
# print the minimum time in which all array elements will become greater than or equal to K                                                    #
################################################################################################################################################

list=[1,2,3,3,5]
x = 4
counter = 0
# in 1 sec value of whole increases by 1
counter = 0

for i in range(len(list)):
    print(list)
    flag = 0
    # comparing all elements 
    for num in list:
        if num < x:
            flag = 1
    if flag == 1:
        counter += 1
        # update all the elements by 1
        for ele in range(len(list)):
            list[ele] = list[ele] + 1
print(counter)

    


        