import sys
import math

N = int(sys.stdin.readline())
difficulties = [ int(sys.stdin.readline().rstrip()) for _ in range(N) ]

if N == 0:
    print(0)
else:
    except_count = math.floor(N * 0.3 * 0.5 + 0.5)
    difficulties.sort()
    print(math.floor(sum(difficulties[except_count : N - except_count])/ (N - except_count * 2 ) + 0.5))

# Python의 round 함수는 오사오입이 원칙이다
# 따라서 사사오입을 적용하기 위해서는 별도 구현이 필요하다
# 1. 연산하고자 하는 값에 0.5 더한 후 내림(floor) 하기. 음수일 경우 0.5를 빼야한다. 
# 2. round 함수를 이용하여 사사오입 함수 구현하기