class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = bin(2 ** self.filter_len)[2:]

    def hash1(self, str1):
        h = 1
        for c in str1:
            code = ord(c)
            h = h * 17 + code
        return abs(h) % self.filter_len

    def hash2(self, str1):
        # 223
        h = 1
        for c in str1:
            code = ord(c)
            h = h * 223 + code
        return abs(h) % self.filter_len

    def add(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        self.filter[h1] = '1'
        self.filter[h2] = '1'

    def is_value(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        if self.filter[h1] == '1' and self.filter[h2] == '1':
            return True
        return False
