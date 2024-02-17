# https://www.acmicpc.net/problem/2346
# 2346번: 풍선 터뜨리기

import sys 

N = int(sys.stdin.readline().rstrip())
values = list(map(int, sys.stdin.readline().rstrip().split()))

ind = 0
end_count = N - 1

def remove_balloon(ind):
    move_count = values[ind]
    values[ind] = 0
    while move_count:
        if move_count > 0: move_direction = 1
        elif move_count < 0: move_direction = -1

        ind = ind + move_direction

        if ind >= N: ind = 0
        elif ind < 0: ind = N - 1

        if values[ind] != 0:
            move_count = move_count - move_direction
    return ind

while end_count:
    print(ind + 1, end=' ')
    ind = remove_balloon(ind)
    end_count -= 1
print(ind + 1)