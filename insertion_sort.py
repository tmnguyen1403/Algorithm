class InsertionSort:
    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def sort(self, arr):
        if len(arr) == 1:
            return
        #every item on the left is sorted
        for i in range(1, len(arr)):
            pivot = i
            while pivot > 0 and arr[pivot] < arr[pivot - 1]:
                self.swap(arr, pivot, pivot - 1)
                pivot = pivot - 1

data = [5,6,9,10,12,7,-1,5,5,5,8,9,10]
ob = InsertionSort()
print(data)
ob.sort(data)
print("sorted")
print(data)
