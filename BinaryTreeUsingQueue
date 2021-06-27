class Queue:
    def __init__(self):
        self.array = []
    def enQueue(self, data):
        self.array.append(data)
    def deQueue(self):
        if len(self.array)==0:
            return None
        return self.array.pop(0)
    def size(self):
        return len(self.array)
    def front(self):
        if len(self.array)==0:
            return None
        return self.array[0]
    def isEmpty(self):
        return len(self.array)==0

    
class BTNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

        
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
    
    def elementInRange(self, root, a,b):
        s_range=a
        b_range=b
        if root == None:
            return
        if root.data>=s_range and root.data<=b_range:
            print(root.data)
        if root.left:
            self.elementInRange(root.left,s_range,b_range)
        if root.right:
            self.elementInRange(root.right,s_range,b_range)   
           
    def elementInRangeUsingLevelOrder(self, root,a,b):
        if root == None:
            print("Empty Data Structure ")
        q = Queue()
        q.enQueue(root)
        while not q.isEmpty():
            temp = q.deQueue()
            if temp.data >= a and temp.data <=b :
                print(temp.data)
            if temp.left:
                q.enQueue(temp.left)
            if temp.right:
                q.enQueue(temp.right)  
                
    
node1 = BTNode(10);node2 = BTNode(5);node3 = BTNode(30);node4 = BTNode(60);
node5 = BTNode(90);node6 = BTNode(7);node7 = BTNode(19);node8 = BTNode(18);
node9 = BTNode(4);
node1.left = node2;node1.right = node3;  
node2.left = node4;node2.right = node5
node4.right = node6
node5.left = node7; node5.right = node8
node8.left = node9
 
bt = BinaryTree(node1)
bt.elementInRange(node1,3,20)
bt.elementInRangeUsingLevelOrder(node1,3,20)
