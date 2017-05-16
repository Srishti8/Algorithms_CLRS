#Program to insertion sort

def inserstionSort(A):
    i = 0
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1

        A[i+1] = key

    return A

A = inserstionSort([5,2,4,1,6,3])
print(A)
