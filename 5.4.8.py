def D(a, b, c):
    return b**2-4*a*c

def quadratic_solve(a,b,c):
    if D(a, b, c) < 0:
        print('Нет вещественных корней')
    elif D(a, b, c) == 0:
        return b/(2*a)
    else:
        return (-b - D(a, b, c)**0.5)/(2*a), (-b + D(a, b, c)**0.5)/(2*a)
p = {'a': 1, 'b': 0, 'c': -1}
print(*p.values())
print()
print(quadratic_solve(**p))
