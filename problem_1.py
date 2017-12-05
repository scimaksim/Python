running_sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        running_sum += i
    print("The sum is:", i, running_sum)

