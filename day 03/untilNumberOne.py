# Q. 1이 될 때 까지 문제
#   어떠한 수 N 이 1이 될 때까지 다음ㅇ의 두 과정 중  하나를 반복적으로 선택하여 수행하려고 한다.
#   단, 두 번째 연산은 N 이 K 로 나누어 떨어질 때만 선택 할 수 있다.
#   1. N에서 1을 뺀다. 
#   2. N을 K로 나눈다. 

# P. 해설 포인트
# → "주어진 N에 대하여 최대한 많이 나누기를 수행하면 됨"

# A. 답안 코드

n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n-=1
        result+=1
    
    n//=k
    result+=1
    
while n>1:
    n-=1
    result+=1
    
print(result)
