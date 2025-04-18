destination = input()
min_budget = float(input())
sum_budget = 0.0

while True:
    while min_budget > sum_budget:
        budget = float(input())
        sum_budget += budget
        break
    if min_budget <= sum_budget:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End":
            break
        min_budget = float(input())
        sum_budget = 0
