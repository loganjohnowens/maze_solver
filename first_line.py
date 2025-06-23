import random

used_cords = [0, 0]
current_spot = [0, 0]
final_cord = 100, 100
distence = [123456789, 123456789]
directoin = 1


def find_closest():
    global current_spot
    global final_cord
    if current_spot[0] == final_cord[0]:
        distence[0] = 100000
    if current_spot[1] == final_cord[1]:
        distence[1] = 100000
    if distence[0] != 100000:
        distence[0] = final_cord[0] - current_spot[0]
    if distence[1] != 100000:
        distence[1] = final_cord[1] - current_spot[1]


def best_way():
    global directoin
    take_or_not = random.randint(1, 2)
    if take_or_not != 1:
        if distence[0] < distence[1]:
            directoin = 2
        if distence[1] < distence[0]:
            directoin = 3
    if take_or_not == 1:
        directoin = random.randint(1,2)
        if directoin == 2:
            directoin = 4


def move():
    global current_spot
    global directoin

    if directoin == 1:
        current_spot[1] -= 1
    if directoin == 2:
        current_spot[0] += 1
    if directoin == 3:
        current_spot[1] += 1
    if directoin == 4:
        current_spot[0] -= 1
    used_cords.append(current_spot)


while current_spot != final_cord:
    find_closest()
    best_way()
    move()
    print(used_cords)
