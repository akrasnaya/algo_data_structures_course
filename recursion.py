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
    array = X
    if (array == []):
        return 0
    array.pop(0)
    return 1 + pop_len(array)

def palindrom(s):
    return len(s) < 2 or (s[0] == s[-1] and palindrom(s[1: -1]))

def print_even_elements(X):
    if X[0] % 2 == 0 and len(X) > 0:
        print(X[0])
    if len(X) > 0:
        print_even_elements(X[1:])

def print_even_indexes(X):
    if len(X) > 0:
        print(X[0])
        print_even_indexes(X[2:])

def find_max(array):
    if len(array) > 1:
        max = find_max(array[1:])
        if array[0] < max:
            return max
        return array[0]
    elif len(array) == 1:
        return array[0]

def second_max(X):
    array = X
    max1 = find_max(array)
    array.remove(max1)
    if len(array) > 0:
        return find_max(array)

def get_files(path, level = 1):
    for f in os.listdir(path):
        if os.path.isdir(path + '/' + f):
            print(os.listdir(path + '/' + f))
            get_files(path + '/' + f, level + 1)

def find_files(path):
    get_files(path)

