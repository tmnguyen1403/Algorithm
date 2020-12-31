class MergeSortBottomUp:
    def merge(self, arr, lo, mid, hi):
        if lo >= hi:
            return
        left = lo
        right = mid + 1
        aux = [arr[i] for i in range(0, len(arr))]
        for index in range(lo, hi + 1):
            if left > mid:
                arr[index] = aux[right]
                right += 1
            elif right > hi:
                arr[index] = aux[left]
                left += 1
            elif aux[left] < aux[right]:
                arr[index] = aux[left]
                left += 1
            else:
                arr[index] = aux[right]
                right += 1
                
    def sort(self, arr):
        N = len(arr)
        sz = 1
        while sz < N:
            for lo in range(0, N - sz, 2*sz):
                self.merge(arr, lo, lo+sz-1, min(lo+2*sz-1, N-1))
            sz = 2*sz

data = [5,6,9,10,12,7,-1,5,5,5,8,9,10,5,6,9,10,12,7,-1,5,5,5,8,9,10,5,6,9,10,12,7,-1,5,5,5,8,9,10]
ob = MergeSortBottomUp()
print(data)
ob.sort(data)
print("sorted")
print(data)
