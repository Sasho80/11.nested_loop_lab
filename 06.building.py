num_floor = int(input())
num_flat = int(input())

for i in range(num_floor, 0, -1):
    for j in range(0, num_flat):
        if i == num_floor:
            print("L{0}{1} ".format(i, j), end="")
        else:
            if i % 2 == 0:
                print("O{0}{1} ".format(i, j), end="")
            else:
                print("A{0}{1} ".format(i, j), end="")
    print(" ")
