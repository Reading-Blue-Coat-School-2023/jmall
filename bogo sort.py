import random

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogo_sort(arr):
    counter = 0
    
    while not is_sorted(arr):
        counter += 1
        random.shuffle(arr)

    return counter

lowest = 100000000
highest = 0

for i in range(500):

    unsorted_list = [4, 3, 1, 5, 2, 6, 0, 7, 9, 8]
    print("Unsorted list:", unsorted_list)
    passes = bogo_sort(unsorted_list)
    print("Sorted list in", passes, "passes:", unsorted_list)

    if passes <= lowest:
        lowest = passes
    elif passes >= highest:
        highest = passes
  
print("The lowest number of passes was: ", lowest, "\nThe highest number of passes was: ", highest)