L = ['THIS', 'IS', 'LOWER', 'STRING']
#мое решение
l = [i.lower() for i in L]
# решение курса
b = (list(map(str.lower, L)))


print(l)
print(b)