class SearchingAlgorithm:
    def __init__(self, data: list[dict]):
        self.data = data

    def linearSearch(self, target_id: int):
        step = 0
        for i in range(len(self.data)):
            step += 1
            product = self.data[i]
            if target_id == product['id']:
                return product, step

        print(f'data with ID: {target_id} is not found')
        return None, step

    def binarySearch(self, target_id: int):
        low = 0
        high = len(self.data) - 1
        step = 0

        while low <= high:
            step += 1

            mid = (low + high) // 2
            guess = self.data[mid]

            if guess['id'] == target_id:
                return guess, step

            elif guess['id'] < target_id:
                low = mid + 1

            else:
                high = mid - 1

        print('Target is not found')
        return None, step

    def interpretationSearch(self, target_id: int):
        low = 0
        high = len(self.data) - 1
        step = 0

        while low <= high and target_id >= self.data[low]['id'] and target_id <= self.data[high]['id']:
            step += 1

            if self.data[high]['id'] == self.data[low]['id']:
                if target_id == self.data[low]['id']:
                    return self.data[low], step
                return None, step

            pos = low + \
                ((target_id - self.data[low]['id']) * (high -
                 low) // (self.data[high]['id'] - self.data[low]['id']))

            print(f'Low: {low}, High: {high}, Pos: {pos}')

            guess = self.data[pos]

            if guess['id'] == target_id:
                return guess, step

            elif guess['id'] < target_id:
                low = pos + 1

            else:
                high = pos - 1

        print('Target is not found')
        return None, step
