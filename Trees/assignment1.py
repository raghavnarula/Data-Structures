import re
import random


## Question1
marks = [[10,20,30,40],[43,65,66,53],[89,53,24,12],[86,54,23,76],[98,54,64,63]]

maths = []
science = []
eng = []
it = []
for i in marks:
    maths.append(i[0])
    science.append(i[1])
    eng.append(i[2])
    it.append(i[3])

def fun_maths(maths):
    print(f"Highest Marks in maths is {max(maths)}")
    print(f"Lowest Marks in maths is {min(maths)}")
    print(f"Average Marks is {sum(maths)/len(maths)}")


def fun_science(science):
    print(f"Highest Marks in science is {max(science)}")
    print(f"Lowest Marks in science is {min(science)}")
    print(f"Average Marks is {sum(science)/len(science)}")

def fun_eng(eng):
    print(f"Highest Marks in eng is {max(eng)}")
    print(f"Lowest Marks in eng is {min(eng)}")
    print(f"Average Marks is {sum(eng)/len(eng)}")

def fun_eng(it):
    print(f"Highest Marks in it is {max(it)}")
    print(f"Lowest Marks in it is {min(it)}")
    print(f"Average Marks is {sum(it)/len(it)}")

def final(maths,science,eng,it):
    print(f"Highest is ")
    average  = (sum(maths) + sum(science) + sum(eng) + sum(it))/(len(it)*4)
    highest = [max(maths),max(eng),max(science),max(it)]
    lowest = [min(maths),min(eng),min(science),min(it)]
    print(f"average is {average}")
    print(f"Max is {max(highest)}")
    print(f"Min is {min(lowest)}")
fun_maths(maths)
fun_science(science)

final(maths,science,eng,it)

## Question 2
def Question2(salary):
    # calculate it's gross salary
    hra = 0
    da = 0
    if salary <= 10000:
        hra = 0.20*salary
        da = 0.80*salary
    
    elif salary<=20000:
        hra = 0.25*salary
        da = 0.90*salary
    
    else:
        hra = 0.30*salary
        da = 0.95*salary
    gross = salary + da + hra

    print(gross)

## Question3
def Question3(passwd):
    # password is a string break string into list form
    flag = 0
    if not re.search('[0-9]', passwd):
        flag = 1

    if not re.search('[a-z]', passwd):
        flag = 1

    if not re.search('[A-Z]', passwd):
        flag = 1
        
    if not re.search('[$@#!]', passwd):
        flag = 1

    if len(passwd)<6:
        flag = 1
    if len(passwd)>16:
        flag = 1
        
    if (flag == 0):
        print ('Password is valid')
    else:
        print ('Password is invalid')

# Question 4
def question4():
    a = [10,20,30,40]
    a.append(200)
    a.append(300)

    a.remove(10)
    a.remove(30)
    print(a)

    a.sort()
    a.reverse()
    return a

## Question 5
def Question5():
    dict = {
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five"
    }
    dict[6] = "six"

    dict.pop(2)

    print(dict)

    # check for the key
    # Enter the key
    key =6
    if key in dict.keys():
        print("present")

    print(f"{len(dict)} are the elements in the Dict")

## Question 6
def Question6():
    list = []

    for i in range(100) :
        list.append(random.randint(100,900))

    odd = 0
    print("Odd numbers are :")
    for i in list :
        if i%2 != 0 :
            odd += 1
            print (i, end = " ")

    print("\nTotal odd numbers :", odd,"\n")
    even = 0
    print("Even numbers are :")
    for i in list :
        if i%2 == 0 :
            even += 1
            print(i, end = " ")

    print("\nTotal even numbers :", even, "\n")

    prime = 0
    print("Prime numbers are :")
    """for i in list :
        for j in range(2,i):
            if (i%j) != 0 :
                prime += 1
                print(i, end = " ")"""
    print("\nTotal number of prime numbers :", prime)

# Question 7
def interest(p,r,t):
    return (p*r*t)/100

# Question 8
class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name = name
        self.type = cuisine_type

    def open_restaurant(self):
        print(f"{self.name} is open!")


class User:
    def __init__(self,first_name,last_name,email,location):
        self.first = first_name
        self.last = last_name
        self.email=email
        self.location=location

    def describe_user(self):
        print(f" Your Name is : {self.first} {self.last}")
        print(f"Your Email address is : {self.email}")
        print(f"You are in : {self.location}")
    def greet_user(self):
        print(f"Hello Mr.{self.first}. Thanks for coming!")

def Question8():
    print("Question 8")
    r = Restaurant("rash","thai")
    r.open_restaurant()

    u = User("raghav","narula","raghavnarula98@gmail.com","Delhi")
    u.describe_user()
    u.greet_user()

# Question2(20000)
# Question3("raghav")
#Question4()
# Question5()
# Question6()
#Question8()
