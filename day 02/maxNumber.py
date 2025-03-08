# 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때, 
# 주어진 수들을 M 번 더하여 가장 수를 만드는 법칙이다.

# Q. 가장 큰 수 문제
# 1. 첫 째 줄에 N M K 의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
#   N ( 2 <= N <= 1000)
#   M ( 1 <= M <= 10000)
#   K ( 1 <= K <= 10000)
# 2. 둘 째 줄에 N 개의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
#   단, 각각의 자연수는 1 이상, 10000 이하의 수로 주어진다.add()
# 3. 입력으로 주어지는 K 는 항상 M 보다 작거나 같다.


# P. 해설 포인트
# → "동빈이의 큰 수의 법칙에 따라 더해진 값을 출력한다."
#   이 문제를 해결하려면 일단 입력 값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
#   연속으로 더할 수 있는 횟수는 최대 K 번 이므로 가장 큰 수를 K 번 더하고, 
#   두 번째로 큰 수를 한 번 더하는 연산을 반복하면 된다.

# A. 답안 코드

# N, M, K 를 공백으로 구분하여 입력 받기
n , m , k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력 받기
inputData = list(map(int, input().split()))

inputData.sort()
first = inputData[n-1]
second = inputData[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print (result)        
        
         
    

