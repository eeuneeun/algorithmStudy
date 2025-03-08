# 선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교

from random import randint
import time


# 배열에 1000개의 정수를 삽입
array = []
for _ in range (1000):
    array.append(randint(1, 100))
    
# 선택 정렬 알고리즘 시간 측정
start_time = time.time()

# 선택 정렬 프로그램 소스 코드
for i in range(len(array)):
    min_indx = i
    for j in range(i+1, len(array)):
        if array[min_indx] > array[j]:
            min_index=j
    # 스왑        
    array[i], array[min_index]=array[min_index], array[i]
    
# 결과 시간 도출
end_time = time.time()
print ("선택 정렬 수행시간 측정", end_time - start_time)


# 배열을 다시 무작위 초기화
array = []
for _ in range(1000):
    array.append(randint(1, 1000))
    
# 기본 정렬 알고리즘 시간 측정
start_time = time.time()

# 기본 정렬 라이브러리 알고리즘
array.sort()
    
# 기`본 정렬 알고리즘 시간 측정
end_time = time.time()

# 결과 시간 도출
end_time = time.time()
print ("파이썬 기본 내장 함수 정렬 수행시간 측정", end_time - start_time)

