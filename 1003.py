import sys

fibo_0_list = [0] * 41
fibo_1_list = [0] * 41

fibo_0_list[0] = 1
fibo_1_list[1] = 1

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if N == 0: print(1, 0)
    elif N == 1: print(0, 1)
    else:
        for i in range(2, N + 1):
            fibo_0_list[i] = fibo_0_list[i-1] + fibo_0_list[i-2]
            fibo_1_list[i] = fibo_1_list[i - 1] + fibo_1_list[i - 2]
        print(fibo_0_list[N], fibo_1_list[N])