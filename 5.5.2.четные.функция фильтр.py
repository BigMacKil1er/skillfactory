def even(x):
    return x % 2 == 0
result = filter(even, [-2, -1, 0, 1, -3, 2, -3] )
print(list(result))