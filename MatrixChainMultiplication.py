p = input("Enter P values with \",\" separated: ").split(",")
p = [int(i) for i in p]
rows, cols = 0, 1
len_p = len(p) - 1
table = [[0 for i in range(len_p)] for j in range(len_p)]
formula = lambda i, j, k: table[i][k] + table[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
while cols < len_p:
    r, c = rows, cols
    while c < len_p:
        t = r
        min_ = []
        while t < c:
            min_.append(formula(r, c, t))
            t += 1
        table[r][c] = min(min_)
        c += 1
        r += 1
    cols += 1

for row in table:
    print(row)
