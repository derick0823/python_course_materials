my_list = [ 4, 3, 6, 5, 2 ]

total_rounds = len(my_list) - 1

excute_times = 0
for x in range(total_rounds):
    for idx_a, a in enumerate(my_list):
        excute_times += 1
        if idx_a < len(my_list) - 1:
            idx_b = idx_a + 1
            b = my_list[idx_b]
            if a > b:
                my_list[idx_a], my_list[idx_b] = b, a

print(excute_times)


excute_times2 = 0
for x in range(total_rounds):
    for idx_a in range(len(my_list) - x):
        excute_times2 += 1
        a = my_list[idx_a]
        if idx_a < len(my_list) - 1:
            idx_b = idx_a + 1
            b = my_list[idx_b]
            if a > b:
                my_list[idx_a], my_list[idx_b] = b, a

print(excute_times2)