# I am utilizing list for every bucket in the table as it reduces the complexity of search operation to O(1) and used 
# the value of the element for the hashing operation

class HashTable:
    def __init__(self, ):
        self.sizing_array=[2,3,5,7,11]
        self.sizeHashTable = self.sizing_array[0]
        self.loadFactor = 5
        self.bucket_size = [0]*self.sizeHashTable 
        self.Tables = [[]*self.loadFactor]*self.sizeHashTable
        
    def hashFunction(self, key):
        return key%(self.sizeHashTable)

# calculate the avarage size of hashtable to resize it if it is more than loadfactor 
    def insert(self, data):
        avgSize_hashtable= sum(self.bucket_size)/self.sizeHashTable
        if avgSize_hashtable >= self.loadFactor:
            print("Trying to resize: Increase")
            self.resize()
            
        index = self.hashFunction(data)
        self.Tables[index].insert(0,data)
        self.bucket_size[index] = self.bucket_size[index]+1

# resizing the array to the next index
    def assignSize(self):
        idx = self.sizing_array.index(self.sizeHashTable)
        return self.sizing_array[idx+1]
    
# storing the previous size of the hashtable to rehash the bucket     
    def resize(self):
        prev_size = self.sizeHashTable
        self.sizeHashTable = self.assignSize()
        self.rehashing(prev_size)

# rehashing the bucket
    def rehashing(self,prev_size):
        item_list=[]
        for i in range(prev_size):
            for j in range(len(self.bucket_size)):
                item_list.append(self.Tables[i][j]) 
                
# reinitializing
        self.Tables = [[]*self.loadFactor] * self.sizeHashTable
        self.bucket_size = [0]*self.sizeHashTable
#storing in the rehashed table
        for k in range(len(item_list)):
            self.insert(item_list[k])
            
    def search(self, item):
#obtaining the hash key of the bucket
        hash_key= self.hashFunction(item)
        print("found it in bucket : ",hash_key)
#obtaining the index of the item in the bucket
        return self.Tables[hash_key].index(item)
    
ht = HashTable()
for i in range(1,15):
    ht.insert(i)

print("at index ",ht.search(11))
