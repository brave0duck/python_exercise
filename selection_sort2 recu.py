""" 선택정렬 예제
    0부터 마지막까지 돈다
        최소값 찾는다
        그값을 0번에 배치
    1부터 마지막까지 돈다
        최소값 찾아서 1번에 배치
    필요변수 ; 최소값 , 인덱스


    """

import random
"""
def selection_sort(list):
    min=0
    index=0
    if len(list) <= 1:
         return list
    
    for i in range(len(list)):
          min = list[i]
          for j in range(i+1,len(list)):
               if list[j] < min:
                     min = list[j]
                     index = j
          if index != i:
               list[i], list[index] = list[index], list[i]
    return list

"""
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