class Queue:
    def __init__(self):
        self.array = []
    def enQueue(self,data):
        self.array.append(data)
    def deQueue(self):
        if len(self.array)!=0:
            return self.array.pop(0)
        else:
            print("queue is empty ")
            return None
    def size(self):
        return len(self.array)
    def front(self):
        if len(self.array)==0:
            return None
        return self.array[0]
    def isEmpty(self):
        return len(self.array)==0

class Stack: 
    def __init__(self):
        self.queue1=Queue()
        self.queue2=Queue()
            
    def isEmpty(self):
        if self.queue1.isEmpty() and self.queue2.isEmpty():
            return True
            
    def push(self,data):
        if self.queue2.isEmpty():
            self.queue1.enQueue(data)
        else:
            self.queue2.enqueue(data)
            
    def pop(self):
        if self.isEmpty():
            return -1
        if self.queue1.isEmpty():
            for i in range(self.queue2.size()-1):
                data = self.queue2.deQueue()
                self.queue1.enQueue(data)
            return self.queue2.deQueue()
        else: 
            for i in range(self.queue1.size()-1):
                data = self.queue1.deQueue()
                self.queue2.enQueue(data)
            return self.queue2.deQueue()

stk = Stack()
for i in range(20,27):
    stk. push(i)
for i in range(8):
    print(stk.pop())
