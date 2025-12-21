class Sort:
    def __init__(self, data: list):
        self.data = data

    def bubble_sort(self):
        n = len(self.data)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j],self.data[j + 1] = self.data[j + 1], self.data[j]
                
    def selection_sort(self):
        n = len(self.data)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j

            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            
    def insertion_sort(self):
        n = len(self.data)

        for i in range(n - 1):
            temp = self.data[i + 1]
            j = i

            while j >= 0 and self.data[j] > temp:
                self.data[j + 1] = self.data[j]
                j -= 1

            self.data[j + 1] = temp

    def merge_sort(self, number):
        if len(number) <= 1:
            return number
        
        middle = len(number) // 2

        left = self.merge_sort(number[:middle])
        right = self.merge_sort(number[middle:])

        return self.merge(left, right)

    def merge(self, left, right):
        array = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array.append(left[i])
                i += 1
            else:
                array.append(right[j])
                j += 1

        array.extend(left[i:])
        array.extend(right[j:])

        return array
            
    def quick_sort(self, data):
        if len(data) <= 1:
            return data
        
        pivot = data.pop()

        left_data = []
        right_data = []

        for i in data:
            if i < pivot:
                left_data.append(i)
            else:
                right_data.append(i)

        return self.quick_sort(left_data) + [pivot] + self.quick_sort(right_data)