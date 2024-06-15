#   insert sorting
#   1. 처음부터 끝까지 돌면서 반복 
#    -> 1번째 뽑아서 임시값에 저장->왼쪽값이 작을때까지 반복-> 그 인덱스에 insert를 한다
#   2. 변수는? 임시값변수, 인덱스값
#
import random

def insert_sort(list):
    if len(list) <= 1:   #배열크기가 1이하면 정렬이 필요없다
         return False
    for i in range(1,len(list)):   # 배열의 크기만큼 반복
          index = i                # 1번째 부터시작. 현재 인덱스 i 일단 저장
          tmp = list[i]            # i값을 임시값에 할당(비교를 위해서)
          for j in range(i-1,-1,-1):    #    i값의 왼쪽으로 돌면서 비교한다. i-1부터 시작
               if list[j] > tmp:        #    만약 j값이 i번째값 보다 크다면 그 index를 저장
                     index = j
          if index != i:                #    인덱스값의 변화가 있나? (큰값을 찾았는가?)
               list.insert(index, list.pop(i))    # i번째 값을 뽑아서, 큰값 index번째 삽입 
    return list

array=[]
for i in range(10):
      array.append(random.randint(1,10000))

print(array)
if array := insert_sort(array):
     print(f'Sort complete : {array}')
else:
     print(f"Don't need sort! {array}")