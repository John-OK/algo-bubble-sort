sequence = [4, 3, 5, 0, 1]
swaps = 0
result = []

def bubble_sort(seq):
    i = 0
    j = 1
    has_swapped = False
    global swaps
    swaps = 0

    while has_swapped == False and j < len(seq):
        if seq[j] < seq[i]:
            seq[j], seq[i] = seq[i], seq[j]
            has_swapped = True
            swaps += 1
            i = 0
            j = 1

        if has_swapped == False:
            i += 1
            j += 1

        has_swapped = False
    global result
    result = seq
    return seq


def real_bubble_sort(seq):
    i = 0
    j = 1
    has_swapped = True
    global swaps
    swaps = 0

    while has_swapped == True:
        has_swapped = False
        while j < len(seq):
            if seq[j] < seq[i]:
                seq[j], seq[i] = seq[i], seq[j]
                has_swapped = True
                i += 1
                j += 1
                swaps += 1
            else:
                i += 1
                j += 1
        i = 0
        j = 1
    global result
    result = seq
    return seq

print("BUBBLE SORT 1")        
bubble_sort(sequence)
print(f"Final result: {result}")
print(f"Swaps: {swaps}")
print("-----------")

print("REAL BUBBLE SORT")
real_bubble_sort([4, 3, 5, 0, 1])
print(f"Final result: {result}")
print(f"Swaps: {swaps}")
