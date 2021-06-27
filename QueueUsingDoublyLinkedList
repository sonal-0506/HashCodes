class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 
        

class QueueUsingDoublyLL:

    def __init__(self):
        self.front = None
        self.rear = None
        self.length  = 0
        
    def enque(self, data):
        node = Node(data)
        if (self.front and self.rear)==None:
            self.front=node
            self.rear=node
            
        else:
            if self.front==self.rear:
                self.rear=node
                self.rear.prev=self.front
                self.front.next = self.rear
            else:
                node.prev= self.rear
                self.rear.next=node
                self.rear = node
        self.length = self.length+1
    
    def deque(self):
        if (self.front and self.rear) is None:
            return "Queue is empty, Underflow"
        
        if(self.front!=self.rear.next):
            temp = self.front
            self.front = temp.next
        self.length = self.length -1
        return temp.data
     

q = QueueUsingDoublyLL()

for i in range(5):
    q.enque(i)
    
for i in range(7):
    print(q.deque())
