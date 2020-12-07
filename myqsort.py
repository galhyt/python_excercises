

def qsort(arr):
    if len(arr) == 1:
        return arr

    lensubarr = int(len(arr) / 2)

    return qmerge(qsort(arr[:lensubarr]),qsort(arr[lensubarr:]))

def qmerge(arr1,arr2):
    arr = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1

    if i < len(arr1):
        arr.extend(arr1[i:])
    elif j < len(arr2):
        arr.extend(arr2[j:])

    return arr

