class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи


    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        def max_heap(array, N, ind):

            largest = ind
            left = 2 * ind + 1
            right = 2 * ind + 2

            if left < N and array[left] > array[largest]:
                largest = left

            if right < N and array[right] > array[largest]:
                largest = right

            if largest != ind:
                array[ind], array[largest] = array[largest], array[ind]
                max_heap(array, N, largest)


        a_for_heap = a
        n = len(a_for_heap)
        start_idx = int(n // 2 - 1)

        for i in range(start_idx, -1, -1):
            max_heap(a_for_heap, n, i)

        heap_size = 0
        for i in range(depth + 1):
            heap_size += 2 ** i
        self.HeapArray = [None] * heap_size
        self.HeapArray[:n] = a_for_heap




    def GetMax(self):
    # вернуть значение корня и перестроить кучу
        def max_heap(array, ind):

            largest = ind
            left = 2 * ind + 1
            right = 2 * ind + 2

            if left < len(array) and array[left] > array[largest]:
                largest = left

            if right < len(array) and array[right] > array[largest]:
                largest = right

            if largest != ind:
                array[ind], array[largest] = array[largest], array[ind]
                max_heap(array, largest)

        if len(self.HeapArray) == 0:
            return -1  # если куча пуста
        root = self.HeapArray[0]
        if None in self.HeapArray:
            ind = self.HeapArray.index(None) - 1
        else:
            ind = -1
        self.HeapArray[0] = self.HeapArray[ind]
        self.HeapArray[ind] = None
        arr = self.HeapArray[:ind - 1]

        max_heap(arr, 0)

        self.HeapArray[:len(arr)] = arr

        return root


    def Add(self, key):
        if None not in self.HeapArray:
            return False
        ind = self.HeapArray.index(None)
        self.HeapArray[ind] = key

        i = ind
        while i > 0:
            if self.HeapArray[i] > self.HeapArray[(i - 1) // 2]:
                temp = self.HeapArray[i]
                self.HeapArray[i] = self.HeapArray[(i - 1) // 2]
                self.HeapArray[(i - 1) // 2] = temp
            i = i - 1

        pass
