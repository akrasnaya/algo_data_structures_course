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

