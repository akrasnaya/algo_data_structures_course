import os

def power(N, M):
    if M == 1:
        return N
    return N * power(N, M - 1)

def sum_num(N):
    if N < 10:
        return N
    return N % 10 + sum_num(N // 10)

def pop_len(X):
    if (X == []):
        return 0
    X.pop(0)
    return 1 + pop_len(X)

def palindrom(s):
    return len(s) < 2 or (s[0] == s[-1] and palindrom(s[1: -1]))

def print_even_elements(X):
    if len(X) == 0:
        return
    if X[0] % 2 == 0 and len(X) > 0:
        print(X[0])
        print_even_elements(X[1:])

def print_even_indexes(X):
    if len(X) > 0:
        print(X[0])
        print_even_indexes(X[2:])

def find_second_max(X, max1, max2):
    array = X
    if len(array) == 0:
        return max2
    if array[0] > max1 and max2 <= max1:
        max2 = max1
        max1 = array[0]
    if array[0] < max1 and array[0] >= max2:
        max2 = array[0]
    return find_second_max(array[1:], max1, max2)

def get_second_max(X):
    if len(X) < 3:
        if X[0] > X[1]:
            return X[1]
        return X[0]
    max1 = X[0]
    max2 = X[0]
    return find_second_max(X, max1, max2)


def get_files(path, level = 1):
    for f in os.listdir(path):
        if os.path.isdir(path + os.sep + f):
            print(os.listdir(path + os.sep + f))
            get_files(path + os.sep + f, level + 1)

def find_files(path):
    get_files(path)

