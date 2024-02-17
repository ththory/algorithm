# https://www.acmicpc.net/problem/10799
# 10799번: 쇠막대기
import sys

brackets = (' '.join(sys.stdin.readline())).split()
stick_pcs = 0
count = 0
razer_flag = False

for bracket in brackets:
    if bracket == '(':
        if razer_flag == True: count += 1
        else: razer_flag = True
    elif bracket == ')':
        if razer_flag == True:
            razer_flag = False
            stick_pcs += count
        else:
            stick_pcs += 1
            count -= 1
print(stick_pcs)
