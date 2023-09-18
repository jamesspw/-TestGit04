def merges(arr):
  if len(arr) > 1:
    l_arr = arr[:len(arr)//2]
    r_arr = arr[len(arr)//2:]
    merges(l_arr)
    merges(r_arr)

    x = y = z = 0
    while x < len(l_arr) and y < len(r_arr):
      if l_arr[x] < r_arr[y]:
        arr[z] = l_arr[x]
        x += 1
      else:
        arr[z] = r_arr[y]
        y += 1
      z += 1
    while x < len(l_arr):
      arr[z] = l_arr[x]
      x += 1
      z += 1
    while y < len(r_arr):
      arr[z] = r_arr[y]
      y += 1
      z += 1


Before = [3, 5, 8, 6, 7, 4, 1 ,2]
print('Before Merge :', Before)
merges(Before)
print('After Merge :', Before)
