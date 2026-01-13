yes = False
for i in range(1, 10001):
    if i % 1000 == 0: print("hi"); continue
    if i % 10 == 0 or i % 100 == 0 or i % 1000 == 0 or (i % 2 == 1 and i % 5 != 0): continue
    for j in range(1, 10001):
        if j % 10 == 0 or j % 100 == 0 or j % 1000 == 0 or (j % 2 == 1 and j % 5 != 0): continue
        for k in [1, 10, 10**2, 10**3]:
            for l in [10, 10**2, 10**3]:
                if (len(str(i/k)) == len(str(j/l)) and i/k * (j/l) == i/k + (j/l)):
                    print("1:", i/k, " and 2: ",j/l)