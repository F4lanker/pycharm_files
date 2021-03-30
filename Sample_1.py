def insert_sort(a):
    '''The function input unsort massive, doing sorting by isert.'''
    n=len(a)
    for top in range (1, n):
        k=top
        while k>=1 and a[k-1]>a[k]:
            a[k-1], a[k]=a[k], a[k-1]
            k-=1
    return a
def choice_sort(a):
    n = len(a)
    for pos in range(0, n-1):
        for k in range (pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
    return a

def bubble_sort(a):
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]

print(insert_sort([4, 2, 5, 1, 3 ]))
print(insert_sort(list(range(10,20)) + list(range(0, 10))))

print(choice_sort([4, 2, 5, 1, 3 ]))
print(choice_sort(list(range(10,20)) + list(range(0, 10))))