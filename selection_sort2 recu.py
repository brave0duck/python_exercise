#    selection sort - recursion version
import random
def selection_sort(list):
        if len(list) <= 1:
            return list
        min_index = list.index(min(list))        # find min value
        list[0], list[min_index] = list[min_index], list[0]        # swap value

        return [list[0]] + selection_sort(list[1::])        # function call other parts

array=[random.randint(1,100) for i in range(10)]
print(f'Before Sort : {array} \n After Sort : {selection_sort(array)}')
