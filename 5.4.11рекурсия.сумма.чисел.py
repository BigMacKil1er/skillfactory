a = []
def equil(n, s):
    if s < 0:
        return False
    if n < 10:
        return n == s
    else:
        return equil(n//10, s - n % 10)

print(equil(1228, 12))