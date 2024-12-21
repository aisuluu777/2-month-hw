list1 = [98,3,67,18,2,44,17,1,0]


def bubble_sort(list):
   for num in range(len(list)):
       for char in range(len(list) - num - 1):
           if list[char] > list[char + 1]:
            list[char], list[char + 1] = list[char + 1], list[char]

   return list

sorted_list = bubble_sort(list1)
print(sorted_list)




list2 = [19,3,78,4,67,2,7]

def selection_sort(list):
    for num in range(len(list)):
        min_num = num
        for char in range(num + 1, len(list)):
                if list[char] < list[min_num]:
                 min_num = char
        list[num], list[min_num] = list[min_num], list[num]

    return list

selected = selection_sort(list2)
print(selected)









def binary_search(Val, nums):
    N = len(nums)
    ResultOk = False
    first = 0
    last = N - 1
    Pos = -1
    while first <= last:
        middle = (first + last) // 2
        if Val == nums[middle]:
            first = middle
            last = first
            ResultOk = True
            Pos = middle
            break
        elif Val > nums[middle] :
            first = middle + 1
        else:
            last = middle - 1
    if ResultOk == True:
        return f'Элемент найден: {Pos}'
    else:
        return f'Элемент не найден'

print(binary_search(12, [2,4,6,8,10,12,14,16,18,20,22,24,26]))
