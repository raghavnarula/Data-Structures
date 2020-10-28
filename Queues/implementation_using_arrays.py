class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self,element):
        #inserts and element in the queue
        self.q.append(element)
    
    def dequeue(self):
        del self.q[0]
        print(self.q)

    def display(self):
        print(self.q)
    
    def front(self):
        return self.q[0]

    def back(self):
        return self.q[-1]


w = Queue()

for i in range(5):
    w.enqueue(i*10)
    print(f"element inserted {i}",i*10)

w.display()
# for i in range(5):
w.dequeue()

print("The first element is :",)


