class MergeSort:
    #divide array by half, sort both partitions, then merge
    def merge(self, arr, lo, mid, hi):
        #precondition: arr[lo..mid] is sorted
        #precondition: arr[mid+1..high] is sorted
        aux = [arr[i] for i in range(0, len(arr))]
        left = lo
        right = mid + 1
        for index in range(lo, hi + 1):
            if left > mid: #no more element from the left
                arr[index] = aux[right]
                right += 1
            elif right > hi: #no more element from the right
                arr[index] = aux[left]
                left += 1
            elif aux[left] < aux[right]:
                arr[index] = aux[left]
                left += 1
            else:
                arr[index] = aux[right]
                right += 1

    def performSort(self, arr,lo, hi):
        if lo >= hi:
            return
        mid = int(lo + (hi - lo)/2)
        self.performSort(arr, lo, mid)
        self.performSort(arr, mid + 1, hi)
        self.merge(arr, lo, mid, hi)

    def sort(self, arr):
        self.performSort(arr, 0, len(arr) - 1)

        return

data = [5,6,9,10,12,7,-1,5,5,5,8,9,10]
ob = MergeSort()
print(data)
ob.sort(data)
print("sorted")
print(data)