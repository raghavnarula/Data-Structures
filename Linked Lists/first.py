# 10 students and each have 4 marks
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