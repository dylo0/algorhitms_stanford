def checkfile():
    f = open("IntegerArray.txt", "r")
    A = []
    for line in f:
        A.append(int(line))
    return sort_count(A)[1]

def sort_count(arr):
    if len(arr) == 0 or len(arr) == 1:
       C, count = arr, 0
    else:
        A = sort_count(arr[:(len(arr)/2)])
        B = sort_count(arr[(len(arr)/2):])
        C= []
        i = 0
        j = 0
        count = A[1] + B[1]
        for _ in range(len(arr)):
            if A[0][i] <= B[0][j]:
                C.append(A[0][i])
                i += 1
                if i >= len(A[0]):
                    C.extend(B[0][j:])
                    break
            else:
                C.append(B[0][j])
                j += 1
                count += len(A[0])-i
                if j >= len(B[0]):
                    C.extend(A[0][i:])
                    break
    return (C, count)

print checkfile()




