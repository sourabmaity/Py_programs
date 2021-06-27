
'''a = [[0, 3, 8, 4, 5, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 4, 7, 8, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 7, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]'''

a=[[0,3,2,6,0,0,0,0],
   [0,0,0,0,4,5,0,0],
   [0,0,0,0,3,2,4,0],
   [0,0,0,0,0,3,2,0],
   [0,0,0,0,0,0,0,1],
   [0,0,0,0,0,0,0,4],
   [0,0,0,0,0,0,0,5],
   [0,0,0,0,0,0,0,0]]

path = [-1 for i in range(len(a))]
for i in range(len(a) - 1, -1, -1):  # Reverse order
    temp = []
    for j in a[i]:  # Find non Zero values
        if j:
            temp.append(j)
    if len(temp):
        temp = min(temp)
        path[i] = a[i].index(temp)  # Store minimum value location
        for k in a:                 # Add min values with its column values
            if k[i]:
                k[i] = k[i] + temp

'''
for i in a:
    print(i)'''
print("Final cost: ", temp)
print("Final path: ", end='')
p = 0
while p != -1:
    print(p + 1, end="->")
    p = path[p]
