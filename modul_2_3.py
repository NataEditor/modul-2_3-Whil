my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

d = len(my_list)

nambe = 0
while nambe != d:
    if my_list[nambe] > 0:
        print(my_list[nambe])
    elif my_list[nambe] < 0:
        break
    nambe += 1
