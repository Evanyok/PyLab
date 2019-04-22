
def bubble_sort(arr):
    if type(arr) is list:
        if len(arr) < 2:
            print('The length is too short!')
        else:
            for i in range(len(arr) + 1)[::-1]:
                for j in range(i)[1:]:
                    if arr[j-1] > arr[j]:
                        tmp = arr[j-1]
                        arr[j-1] = arr[j]
                        arr[j] = tmp
        print(arr)
    else:
        print('Type error!')
        
bubble_sort([2,1])
bubble_sort([2,1,3,7,4,2])

