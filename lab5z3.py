import random


def BubbleSort(A):
    a1 = 0
    a2 = 0
    v1 = 0
    v2 = 0

    for i in range(len(A)-1):
        for j in range(len(A)-1):
            buf = 0
            a1 = j
            a2 = j+1
            v1 = A[a1]
            v2 = A[a2]
            if v1 < v2:
                A[a1], A[a2] = A[a2], A[a1]


B = [random.randint(1,100) for i in range(21)]
print('несортированный массив')
print(B)

BubbleSort(B)

print('сортированный массив')
print(B)
