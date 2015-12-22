def bubbleSort(l): 
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                
lista = [100, 45, 2, 11, 65, 25, 8, 99, 5]
bubbleSort(lista)
print(lista)