def sort_list_imperative(numbers):
    nums = numbers.copy()

    def partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] > pivot:
                i += 1

            j -= 1
            while nums[j] < pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]

    def quick_sort(nums):
        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

    quick_sort(nums)
    return nums

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

if __name__ == "__main__":

    numbers, numbers_i, numbers_d  = [1, 6, 4, 8, 3], [], []
    print(f"List to sort: {numbers}")

    numbers_i = sort_list_imperative(numbers)
    print(f"List sorted in imperative way: {numbers_i}")

    numbers_d = sort_list_declarative(numbers)
    print(f"List sorted in declarative way: {numbers_d}")




