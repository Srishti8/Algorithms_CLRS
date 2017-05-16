'''
Consider the addition problem:
Input : Two array of length n, a and b containing n digit binary number
Output: An array c of length n+1 which contain the addition of a and b
'''

def addBinaryArray(a, b):
    n = len(a)
    c = [0 for i in range(0,n+1)]
    carry = 0

    for i in range(n-1,-1,-1):
        c[i+1] = a[i] + b[i] + carry
        if c[i+1] >= 2:
            c[i+1] -= 2
            carry = 1
        else:
            carry = 0

    c[0] = carry
    return c

c = addBinaryArray([1,0,1,1],[0,1,1,0])
print(c)