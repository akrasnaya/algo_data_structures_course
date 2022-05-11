class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 2 ** self.filter_len

    def hash1(self, str1):
        h = 1
        for c in str1:
            code = ord(c)
            h = h * 17 + code
        return abs(h) % self.filter_len

    def hash2(self, str1):
        h = 1
        for c in str1:
            code = ord(c)
            h = h * 223 + code
        return abs(h) % self.filter_len

    def add(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        self.filter = self.filter + 2 ** h1 + 2 ** h2

    def is_value(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        x1 = self.filter_len - h1
        x2 = self.filter_len - h2
        if (self.filter >> x1) & 1 == 1 and (self.filter >> x2) & 1 == 1:
            return True
        return False
