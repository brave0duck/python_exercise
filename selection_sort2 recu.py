#    selection sort - recursion version
import random
def selection_sort(list):
        if len(list) <= 1:
            return list
        min_index = list.index(min(list))
        list[0], list[min_index] = list[min_index], list[0]

        return [list[0]] + selection_sort(list[1::])

array=[]
for i in range(10):
      array.append(random.randint(1,100))
print(array)
print(f'selection : {selection_sort(array)}')
