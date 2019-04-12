import numpy as np

n = int(input())
Amatris = np.full((n, n) , 1.001)
Xmatris = np.full((n, 1), 0)
c = np.full(n, 0)
r = np.full(n, 0)

print("enter c :")
for i in range(0 , n):
    c[i] = int(input())
print("Enter r :")
for i in range(0 , n):
    r[i] = int(input())
for i in range(0, n) :
    for j in range(0 , n) :
        if(i-j >= 0) :
            Amatris[i,j] = c[i-j]
        else :
            Amatris[i,j] = r[j-i]

print("Toeplitz matrix :")
print(Amatris)

augmentedMatris = Amatris
i = 0
j = 0
lead = 0
det = 1
for r in range(0, n):
    flag = 0
    if n <= lead:
        break
    i = r
    while augmentedMatris[i, lead] == 0.000:
        i = i + 1
        if n == i:
            i = r
            lead = lead + 1
            if n == lead:
                break
                flag = 1 ;
    if flag == 1 :
        break

    ## swap row i and r
    hold = 0
    ## changing determinant if i != r
    if(r != i) :
        det = det * (-1)

    for x in range(0, n ):
        hold = augmentedMatris[r, x]
        augmentedMatris[r, x] = augmentedMatris[i, x]
        augmentedMatris[i, x] = hold

    if augmentedMatris[r, lead] != 0:
        hold = augmentedMatris[r, lead]
        det *= hold
        for x in range(0,n):
            h = augmentedMatris[r, x] / ( hold * 1.000)
            augmentedMatris[r, x] = h

    if augmentedMatris[r, lead] != 0:
        for x in range(0, n):
            if x != r:
                hold = augmentedMatris[x, lead]
                if hold != 0 :
                    for j in range(lead, n):
                        augmentedMatris[x, j] = augmentedMatris[x, j] - hold * augmentedMatris[r , j]

    lead = lead + 1

flag = -1
for i in range(0, n):
    if(augmentedMatris[i,i] == 0):
        flag =1
if(flag == -1):
    print("determinant : " )
    print(det)
else:
    print("determinant : ")


