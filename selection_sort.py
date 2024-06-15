""" 선택정렬?
    배열0부터 끝까지 돈다 -> 돌면서 최소값 찾는다 -> 그 최소값의 인덱스 저장 . 그값을 0번값과 교환
    배열1부터 끝까지 돈다 -> 돌면서 최소값 찾는다 -> 그 최소값의 인덱스 저장 . 그값을 1번값과 교환
    ...
    이런식으로 마지막까지 돈다.

    필요변수 ; 현재 요소값과 비교할 최소값 변수 , 최소값의 인덱스
"""

import random

def selection_sort(list):
    if len(list) <= 1:
         return False
    for i in range(len(list)):
          index = i
          min = list[i]
          for j in range(i+1,len(list)):
               if list[j] < min:
                     min = list[j]
                     index = j
          if index != i:    #인덱스값이 변경되었다면(현재값보다 낮은값을 찾았으면). 값을 교환하라
            list[i], list[index] = list[index], list[i]

    return list

array=[]
for i in range(10):
      array.append(random.randint(1,10000))

print(array)
if array := selection_sort(array):
     print(f'Sort complete : {array}')
else:
     print(f"Don't need sort! {array}")