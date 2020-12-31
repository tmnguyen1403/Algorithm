#Time complexity: O(n^2)
class SelectionSort:
    def sort(self, arr):
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    tmp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = tmp

data = [5,6,8,10,12,7]
ob = SelectionSort()
ob.sort(data)
print(data)
print("sorted")
print(data)
