class QuickUnionWeighted:
    def __init__(self, n):
        self.id = [i for i in range(0, n)]
        self.size = [1 for i in range(0,n)]
    
    #Time complexity: lgN - based on the depth of the tree
    def root(self, index):
        while (index != self.id[index]):
            #update root of index equals to root of grandparent
            tmp = index
            index = self.id[index]
            self.id[tmp] = self.id[index] 
        return index
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    #Time complexity: lgN - time complexity of finding root
    def union(self, p, q):
        pRoot = self.root(p)
        qRoot = self.root(q)
        if self.size[pRoot] > self.size[qRoot]:
            #attach q to p
            self.id[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]
        else:
            #attach p to q
            self.id[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]
    
    def countGroups(self):
        groups = set(self.id)
        return len(groups)

n = 5
test = QuickUnionWeighted(n)
test.union(1,2)
test.union(1,3)
test.union(2,4)
print(test.id)
print(test.countGroups())