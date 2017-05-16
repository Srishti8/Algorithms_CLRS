#Linear Search

def linearSearch(A,v):
    for i in range(0, len(A)):
        if A[i] == v:
            return i

    return None

index = linearSearch([2,3,4,7,8,1],2)
print(index)