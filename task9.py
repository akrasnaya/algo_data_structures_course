class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return abs(hash(key)) % self.size

    def is_key(self, key):
        return key in self.values

    def put(self, key, value):
        ind = self.hash_fun(key)
        if self.is_key(key):
            self.slots[ind] = value
        else:
            self.values[ind] = key
            self.slots[ind] = value

    def get(self, key):
        ind = self.hash_fun(key)
        if self.is_key(key):
            return self.slots[ind]
        return None
