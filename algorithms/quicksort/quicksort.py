def quicksort(array):
    if len(array) < 2:
        return array
    else:
        piviot = array[0]
        less = [i for i in array[1:] if i <= piviot]
        greater = [i for i in array[1:] if i > piviot]
        return quicksort(less) + [piviot] + quicksort(greater)

        
print(quicksort([10, 5, 2, 3]))