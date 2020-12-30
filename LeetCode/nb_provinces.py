from typing import List
class QuickUnion:
    def __init__(self, n):
        self.id = [i for i in range(0, n)]
        self.size = [1 for i in range(0,n)]
    
    def province(self, city) -> int:
        while(city != self.id[city]):
            tmp = city
            city = self.id[city]
            self.id[tmp] = self.id[city]
        return city
    
    def connected(self, p, q):
        return self.province(p) == self.province(q)
    
    def union(self, p, q):
        provinceP = self.province(p)
        provinceQ = self.province(q)
        if provinceP == provinceQ:
            return
        if (self.size[provinceP] >= self.size[provinceQ]):
            self.id[provinceQ] = self.id[provinceP]
            self.size[provinceP] += self.size[provinceQ]
        else:
            self.id[provinceP] = self.id[provinceQ]
            self.size[provinceQ] += self.size[provinceP]
    
    def countProvinces(self) -> int:
        provinces = set()
        for city in self.id:
            provinces.add(self.province(city))
        return len(provinces)
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        finder = QuickUnion(len(isConnected))
        for row in range(0, len(isConnected)):
            for col in range(0, len(isConnected[row])):
                if isConnected[row][col] == 1:
                    finder.union(row, col)
        return finder.countProvinces()

'''
INPUT:
[[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]

OUPUT:
3
'''