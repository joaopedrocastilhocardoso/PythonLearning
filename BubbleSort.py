def bubble_sort(x):
    n = len(x)
    print(x)
    while n > 1:
        i = 0
        while i < n - 1:
            if(x[i] > x[i + 1]):
                aux = x[i]
                x[i] = x[i+1]
                x[i+1] = aux
            i += 1
        n -= 1
    print(x)

y = [5,4,3,2,1]
bubble_sort(y)
z = [100,1,3,98,25,60,27,32,51,23,79,84,67,73,21,49,69,76,52,68,37,61,50,78,8,36,2,30,86,44,94,39,
     58,96,17,54,26,56,14,19,35,45,82,65,57,85,95,43,38,91,22,55,66,63,97,6,4,41,93,15,33,42,88,11,
     7,20,72,71,62,59,29,99,9,77,75,74,46,92,80,18,10,24,5,70,16,13,40,81,48,34,64,87,31,89,12,53,47,83,28,90]
bubble_sort(z)