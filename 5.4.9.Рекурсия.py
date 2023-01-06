a = [4, 3, 5, 7, 1, 5, 0]
c = 0
m = a[0]

def A(li):
    global c
    global m
    count = 0
    if c != len(li)-1:
        if li[c] < li[c+1]:
            if li[c] < m:
                m = li[c]
                c += 1
                A(li)
            else:
                c += 1
                A(li)
        else:
            c += 1
            A(li)
    if li[c] < m:
        m = li[c]

    return m

def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

print(A(a))
print(min_list(a))
print("chlen")