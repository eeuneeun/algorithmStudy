# 숫자 카드 게임

# P. 가장 큰 숫자가 적혀 있는 카드를 뽑는 게임
#   단, 정해진 규칙을 따라야 하고 규칙은 다음과 같다.
#   1. 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다.
#      N = 행, M = 열
#   2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택.
#   3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
#   4. 따라서 처음 행을 선택 할 때, 이후에 해당 행에서 숫자가 가장 낮은 카드를 뽑을 것을 고려하여,
#       최종적으로 가장 숫자가 높은 카드를 뽑을 수 있도록 전략을 세워야 함

# Q. 첫 째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.
#    (1<=N<=100)
#    둘째 줄 부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 
#    각 숫자는 1 이상 10,000 이하의 자연수이다.

# A. 각 행마다 가장 작은 수를 찾은 뒤에 그 수중에서 가장 큰 수를 찾는다. 

# 1. python 의 min() 함수를 이용하는 방법
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)

# 2. 이중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    
    for j in range:
        min_value = min(min_value, j)
    
    result = max(result, min_value)
    
print(result)

