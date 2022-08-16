class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 0
        for i in range(depth + 2):
            tree_size += 2 ** i
        self.Tree = [None] * tree_size # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        if self.Tree[0] is None:
            return 0


        if None not in self.Tree and key not in self.Tree:
            return None

        for node in self.Tree:
            if node is not None and node == key:
                return self.Tree.index(node)

        def search(node):
            if node is None:
                return
            elif key == node:
                ind = self.Tree.index(node)
                return ind
            elif key < node:
                ind = self.Tree.index(node)
                left = 2 * ind + 1
                if left > len(self.Tree) - 1:
                    return None
                if self.Tree[left] is None:
                    return -left
                return search(self.Tree[left])
            elif key > node:
                ind = self.Tree.index(node)
                right = 2 * ind + 2
                if right > len(self.Tree):
                    return None
                if self.Tree[right] is None:
                    return -right
                return search(self.Tree[right])

        return search(self.Tree[0])


    def AddKey(self, key):
        # добавляем ключ в массив
        if self.Tree[0] is None:
            self.Tree[0] = key
            return 0

        if self.FindKeyIndex(key) is None:
            return -1

        if self.FindKeyIndex(key) == 0:
            if self.Tree[0] == key:
                return 0

        if self.FindKeyIndex(key) > 0:
            return self.FindKeyIndex(key)
        else:
            ind = -self.FindKeyIndex(key)
            self.Tree[ind] = key
            return ind


        def search(node):
            if node is None:
                return -1
            elif key == node:
                ind = self.Tree.index(node)
                return ind
            elif key < node:
                ind = self.Tree.index(node)
                left = 2 * ind + 1
                if left > len(self.Tree) - 1:
                    return -1
                if self.Tree[left] is None:
                    self.Tree[left] = key
                    return left
                return search(self.Tree[left])
            else:
                ind = self.Tree.index(node)
                right = 2 * ind + 2
                if right > len(self.Tree):
                    return -1
                if self.Tree[right] is None:
                    self.Tree[right] = key
                    return right
                return search(self.Tree[right])

        return search(self.Tree[0])
