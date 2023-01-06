#мое решение
an = ''
def num(n):
    global an
    if n !=0:
        a = n % 10
        n = n // 10
        an = an + str(a)
        num(n)
    return int(an)
# решение курса
def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res
#вызов функций
print(num(1234))
print(mirror(2552))