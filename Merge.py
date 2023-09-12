def merges(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left1 = arr[:mid]
    right1 = arr[mid:]

    left01 = merges(left1)
    right01 = merges(right1)

    return merge(left01, right01)

def merge(left, right):
    merged = []
    leftindex, rightindex = 0, 0

    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            merged.append(left[leftindex])
            leftindex += 1
        else:
            merged.append(right[rightindex])
            rightindex += 1

    merged.extend(left[leftindex:])
    merged.extend(right[rightindex:])

    return merged

if __name__ == "__main__":
    arr = [2, 10, 4, 3, 6, 1, 8]
    sorted_arr = merges(arr)
    print("Sorted by \n =", sorted_arr)
