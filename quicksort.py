def quicksort(A,x,y):
    contador = 0
    if y - x <= 1:
        return 0
    else :
        A[x], A[y-1] = A[y-1] , A[x]
        rep = div(A,x,y)
        contador = y - x - 1
        l = quicksort(A,x,rep)
        r = quicksort(A,rep+1,y)
        return contador + l + r

def div(A,x,y):
    piv = A[x]
    i = x + 1
    for j in range(x+1,y):
        if A[j] < piv:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    A[i-1], A[x] = A[x], A[i-1]
    return i-1
    
A = [ ]
for line in open('QuickSort.txt','r').readlines():
    A.append(int(line))

quicksort(A,0,len(A))
\\164123
