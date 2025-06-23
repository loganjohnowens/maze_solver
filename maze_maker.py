import random

generator_pos = [0, 0]
used_cords = [[0, 0]]
size = [100, 100]
amount = 0


def new_random():
    global directoin
    directoin = random.randint(1, 4)


def check_if_real(generator_pos):
    while True:
        new_random()
        global check
        if directoin == 1:
            check = [generator_pos[0], generator_pos[1] - 1]
        if directoin == 2:
            check = [generator_pos[0], generator_pos[1] + 1]
        if directoin == 3:
            check = [generator_pos[0] + 1, generator_pos[1]]
        if directoin == 4:
            check = [generator_pos[0] - 1, generator_pos[1]]

        if check[0] > -1 and check[1] > -1 and check[0] < size[0] + 1 and check[1] < size[1] + 1:
            break
    check_2()


def check_2():
    global check
    global used_cords
    global fail
    global generator_pos
    global amount
    test_1 = [check[0], check[1] + 1]
    test_2 = [check[0] + 1, check[1]]
    test_3 = [check[0], check[1] - 1]
    test_4 = [check[0] - 1, check[1]]
    fail = False
    for i in used_cords:
        if i != generator_pos:
            if test_1 == i:
                fail = True
            if test_2 == i:
                fail = True
            if test_3 == i:
                fail = True
            if test_4 == i:
                fail = True
            if check == i:
                fail = True
    if fail is False:
        used_cords.append(check)
        generator_pos = check
        amount = 0
    if fail:
        amount += 1


while amount < 10:
    check_if_real(generator_pos)
for i in used_cords:
    amount = 0
    generator_pos = i 
    while amount < 10:
        check_if_real(generator_pos)
