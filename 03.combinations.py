num = int(input())

counter_true_num = 0
result = 0

for x1 in range(0,num+1):
    for x2 in range(0, num+1):
        for x3 in range(0, num+1):
            result = x1 + x2 + x3
            if result == num:
                counter_true_num += 1
            else:
                continue

print(counter_true_num)
