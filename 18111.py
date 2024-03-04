import sys
from collections import Counter

# size = N * M, max block = B
[N, M, B] = list(map(int, sys.stdin.readline().rstrip().rsplit()))
heights = []

for i in range(N):
    heights.extend(list(map(int, sys.stdin.readline().rstrip().rsplit())))

heights_count = sorted(Counter(heights).items(), key=lambda x: (x[0]))

minimum = 64 * ( 10 ** 6 ) + 1
minimum_height = 0

current_height = heights_count[0][0]
max_height = heights_count[-1][0]
min_height = heights_count[0][0]
for i in range(max_height, min_height - 1, -1):
    expend_time = 0
    blocks = B
    for (h, c) in heights_count:
        if i < h:
            expend_time += (h - i) * c * 2
            blocks += (h - i) * c
        elif i > h:
            expend_time += (i - h) * c
            blocks -= (i - h) * c
    if blocks < 0:
        continue
    if minimum > expend_time:
        minimum = expend_time
        minimum_height = i
print(minimum, minimum_height)
