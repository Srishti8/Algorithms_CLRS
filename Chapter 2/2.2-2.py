#Selection sort

def selectionSort(a):
    n = len(a)

    for i in range(0,n-1):
        min = a[i]
        for j in range(i+1,n):
            if a[j] < min:
                min = a[j]
                minIndex = j

        if a[i] > a[minIndex]:
            temp = a[i]
            a[i] = a[minIndex]
            a[minIndex] = temp

    return a

a = selectionSort([4,5,1,3,7,2,6])
print(a)

'''
Worst case is O(n^2)
Best Case is O(n^2)
Average case is O(n^2)
'''