start_interval = int(input())
end_interval = int(input())
magic_num = int(input())

counter_consecutive_combinations = 0
counter_all_combinations = 0

for i in range(start_interval, end_interval+1):
    for j in range(start_interval, end_interval+1):
        counter_all_combinations += 1
        if (i + j) == magic_num:
            counter_consecutive_combinations = counter_all_combinations
            print(f"Combination N:{counter_consecutive_combinations} ({i} + {j} = {magic_num})")
            break
        else:
            continue
    if (i + j) == magic_num:
        break
else:
    print(f"{counter_all_combinations} combinations - neither equals {magic_num}")
