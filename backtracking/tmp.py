a = [1, 2, 3, 4, 5]
c = [0] * len(a)


print(a)
for i in range(len(a)):
    if c[i] < i:
        a[c[i] if i & 1 else 0], a[i] = a[i], a[c[i] if i & 1 else 0]
        c[i] += 1
        i = 0
        print(a)
    else:
        c[i] = 0
        i += 1
