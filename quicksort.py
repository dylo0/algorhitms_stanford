comparations = 0

def checkfile(filename, method):
    f = open(filename, "r")
    A = []
    for line in f:
        A.append(int(line))
    return quicksort(A, method)[1]

def choose_pivot1(arr,left,right):
    return left

def choose_pivot2(arr,left,right):
    return right-1

def choose_pivot3(arr,left,right):
    first = arr[left]
    middle = arr[(left+right-1)/2]
    last = arr[right-1]
    lst = [first, middle, last]
    median = sorted(lst)[1]

    if median == first:
        return left
    elif median == middle:
        return (left+right-1)/2
    else:
        return right-1

def sort_around_pivot(arr, left, right, piv_idx):
    global comparations
    arr[left], arr[piv_idx] = arr[piv_idx], arr[left]
    p = arr[left]
    i = left + 1
    for j in range(i, right):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[left], arr[i-1] = arr[i-1], arr[left]
    comparations += right - left -1
    return (arr,i)

def qshelper(arr, left, right, pivotfun):
    if right-left <= 1:
        return arr
    piv = pivotfun(arr,left,right)
    sorted = sort_around_pivot(arr, left, right, piv)
    partA = qshelper(sorted[0], left, sorted[1]-1, pivotfun)
    partB = qshelper(sorted[0], sorted[1], right, pivotfun)
    return sorted[0]

def quicksort(arr, pivotfun):
    global comparations
    comparations = 0
    return (qshelper(arr, 0, len(arr), pivotfun), comparations)

if name == __main__:
    # checks    
    print checkfile("10.txt", choose_pivot1) #25
    print checkfile("10.txt", choose_pivot2) #29
    print checkfile("10.txt", choose_pivot3) #21
    print
    print checkfile("100.txt", choose_pivot1) #615
    print checkfile("100.txt", choose_pivot2) #587
    print checkfile("100.txt", choose_pivot3) #518
    print
    print checkfile("1000.txt", choose_pivot1) #10297
    print checkfile("1000.txt", choose_pivot2) #10184
    print checkfile("1000.txt", choose_pivot3) #8921

    #ans
    print 
    print checkfile("QuickSort-data.txt", choose_pivot1)
    print checkfile("QuickSort-data.txt", choose_pivot2)
    print checkfile("QuickSort-data.txt", choose_pivot3)
