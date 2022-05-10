class PowerSet:

    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def put(self, value):
        if value in self.values:
            return None
        self.values.append(value)

    def get(self, value):
        return value in self.values

    def remove(self, value):
        if value in self.values:
            self.values.remove(value)
            return True
        return False

    def intersection(self, set2):
        set3 = PowerSet()
        for value in self.values:
            if value in set2.values:
                set3.put(value)
        return set3

    def union(self, set2):
        set3 = PowerSet()
        for value in self.values:
            set3.put(value)
        for value in set2.values:
            set3.put(value)
        return set3

    def difference(self, set2):
        set3 = PowerSet()
        for value in self.values:
            if value not in set2.values:
                set3.put(value)
        return set3

    def issubset(self, set2):
        count = 0
        if set2.size() > self.size():
            return False
        for value in set2.values:
            if value in self.values:
                count += 1
        if count == set2.size():
            return True
        return False
