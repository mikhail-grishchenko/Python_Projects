def fill (x,y):
    a = []
    c = 1
    d = 1
    for row in range (x):
        a.append([])
        if d%2 != 0:
            for elem in range (y):
                a[row].append(c)
                c+=1
        else:
            for elem in range (y):
                a[row].append(c)
                c += 1
            a[row] = a[row][::-1]
        d += 1
    return a

x = int(input("Введите количесто строк матрицы:\n"))
y = int(input("Введите количесто столбцов матрицы:\n"))
print ("Вывод матрицы:")
for i in fill(x,y):
    print (' '.join(map(str, i)))
