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
                self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                j -= 1

            