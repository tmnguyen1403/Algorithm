print("Hello World")
#quick union: use for social networks (a group of friends)
#init an array size n with id from 0..n-1
#methods: root, connected, union

class QuickUnionUF:
    def __init__(self, n):
        self.id = [i for i in range(0, n)]
    
    #Time complexity: O(n)
    def root(self, index):
        while (index != self.id[index]):
            index = self.id[index]
        return index

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    #Time complexity: O(n)
    def union(self, p, q):
        #Change root of p equal to root of q
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

    def printData(self):
        for i in range(0, len(self.id)):
            print(i)
#Test data
n = 5
test = QuickUnionUF(n)
test.union(1,2)
test.union(1,3)
test.union(2,4)
print(test.id)

