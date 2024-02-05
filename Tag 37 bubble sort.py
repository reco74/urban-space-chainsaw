def bubble_sort(arr):
    n = len(arr)

    # Durchlaufe alle Elemente im Array
    for i in range(n):
        # Letzte i Elemente sind bereits sortiert, daher müssen wir nur die ersten (n-i) Elemente überprüfen
        for j in range(0, n-i-1):
            # Vertausche, wenn das Element gefunden wird, das größer als das nächste Element ist
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



    # Test-Array


my_array = [64, 34, 25, 12, 22, 11, 90]

print("Unsortiertes Array:", my_array)

# Bubble Sort anwenden
bubble_sort(my_array)

print("Sortiertes Array:", my_array)