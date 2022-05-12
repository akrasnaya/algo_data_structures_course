class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return abs(hash(key)) % self.size

    def is_key(self, key):
        return key in self.values

    def put(self, key, value):
        ind = self.hash_fun(key)
        if self.is_key(key):
            self.slots[ind] = value
        elif self.values.count(None) == 0 and not self.is_key(key):
            min_hits = min(self.hits)
            min_ind = self.hits.index(min_hits)
            self.hits[min_ind] = 0
            self.values[min_ind] = key
            self.slots[min_ind] = value
        else:
            self.values[ind] = key
            self.slots[ind] = value

    def get(self, key):
        ind = self.hash_fun(key)
        if self.is_key(key):
            self.hits[ind] += 1
            return self.slots[ind]
        return None
