from typing import List

num_list = input('Please enter a list of numbers separated by space : ' ).split()
num_list = [int(v) for v in num_list]

class SortedArray(object):
    def __init__(self, num_list: List[int]):
        self.num_list = num_list

        def partition(numbers: List[int], low: int, high: int) -> int:
            i = low - 1
            pivot = numbers[high]
            for j in range(low, high):
                if numbers[j] <= pivot:
                    i += 1
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
            return i + 1

        def arraySort(numbers: List[int]) -> List[int]:
            def _arraySort(numbers: List[int], low: int, high: int) -> None:
                if low < high:
                    partition_index = partition(numbers, low, high)
                    _arraySort(numbers, low, partition_index-1)
                    _arraySort(numbers, partition_index+1, high)
    
            _arraySort(numbers, 0, len(numbers)-1)
            return numbers
        
        sorted_list = arraySort(num_list)
        self.sorted_list = sorted_list

    
    def sorted(self):
        print(self.sorted_list)
    
    def reversed(self):
        reversed_list = self.sorted_list[::-1]
        print(reversed_list)

sortedArray = SortedArray(num_list)
sortedArray.sorted()
sortedArray.reversed()

