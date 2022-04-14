import numpy as np
class Hash_table():
    def __init__(self,size) :
        self.size = size
        self.hashtable = np.array([None]*self.size)
    def hash(self,key) :
        index = (2*key+5)%11 
        if self.hashtable[index] == None :
            return index
        else :
            i = 1
            while self.hashtable[((2*index+5)+(i*i))%11] != None :
                i += 1
            return ((2*index*5)+(i*i))%11
    def insert(self,key) :
        index = self.hash(key)
        self.hashtable[index] = key
    def print_hashtable(self) :
        print("Hash table is :-\n\nindex \t value")
        for x in range(len(self.hashtable)) :
            print(x,"\t",self.hashtable[x])
    def delete(self,key):
        index=self.hash(key)
        self.hashtable[index]=0
HT = Hash_table(11)
HT.insert(3)
HT.insert(14)
HT.insert(18)
HT.insert(37)
HT.insert(9)
HT.insert(92)
HT.insert(21)
HT.insert(86)
HT.insert(11)
HT.print_hashtable()
HT.delete(3)
print("After deleting 3:\n")
HT.print_hashtable()
HT.delete(14)
print("After deleting 14:\n")
HT.print_hashtable()
HT.delete(18)
print("After deleting 18:\n")
HT.print_hashtable()
HT.delete(11)
print("After deleting 18:\n")
HT.print_hashtable()