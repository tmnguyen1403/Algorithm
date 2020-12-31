class MergeSort:
    def __init__(self):
        self.CUTOFF = 10

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

    #Use insertionSort for small size array 10 ~ 20 items
    def insertionSort(self, arr, lo, hi):
        for index in range(lo + 1, hi + 1):
            pivot = index
            while pivot > lo and arr[pivot] < arr[pivot - 1]:
                tmp = arr[pivot]
                arr[pivot] = arr[pivot - 1]
                arr[pivot - 1] = tmp
                pivot -= 1

    def performSort(self, arr,lo, hi):
        if lo >= hi:
            return
        if (hi <= lo + self.CUTOFF - 1):
            self.insertionSort(arr, lo, hi)

        mid = int(lo + (hi - lo)/2)
        self.performSort(arr, lo, mid)
        self.performSort(arr, mid + 1, hi)
        #will not merge if already sorted
        if (arr[mid + 1] > arr[mid]):
            return
        self.merge(arr, lo, mid, hi)

    def sort(self, arr):
        self.performSort(arr, 0, len(arr) - 1)

        return

data = [5,6,9,10,12,7,-1,5,5,5,8,9,10,5,6,9,10,12,7,-1,5,5,5,8,9,10,5,6,9,10,12,7,-1,5,5,5,8,9,10]
ob = MergeSort()
print(data)
ob.sort(data)
print("sorted")
print(data)