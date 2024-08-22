my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
d = len(my_list)
#print(d)
nambe = 0
while nambe < d:
    if my_list[nambe] > 0:
        print(my_list[nambe])
        nambe = nambe + 1
    else:
        print("stop")
        break
