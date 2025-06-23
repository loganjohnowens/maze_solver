import pygame
import time
import sys
from maze_maker import used_cords


def set_up_display():
    global canvas
    canvas = pygame.display.set_mode((510, 510))
    pygame.display.set_caption("maze")


def start_pygame():
    pygame.init()


def define_vars():
    global size
    global current_pos
    global useable_cords
    global seen_path
    global sloved_path
    global looping
    global tools
    global done
    global start
    size = 5
    current_pos = [0, 0]
    useable_cords = [False, False, False, False]
    seen_path = []
    sloved_path = []
    looping = True
    tools = False
    done = True
    start = True


def find_useable():
    global useable_cords
    global used_cords
    global seen_path
    useable_cords = [False, False, False, False]
    unuseable_cords = [False, False, False, False]
    for i in seen_path:
        if [current_pos[0] - 1, current_pos[1]] == i:
            unuseable_cords[3] = True
        if [current_pos[0] + 1, current_pos[1]] == i:
            unuseable_cords[1] = True
        if [current_pos[0], current_pos[1] - 1] == i:
            unuseable_cords[0] = True
        if [current_pos[0], current_pos[1] + 1] == i:
            unuseable_cords[2] = True
    for i in used_cords:
        if [current_pos[0] - 1, current_pos[1]] == i and unuseable_cords[3] is False:
            useable_cords[3] = True
        if [current_pos[0] + 1, current_pos[1]] == i and unuseable_cords[1] is False:
            useable_cords[1] = True
        if [current_pos[0], current_pos[1] - 1] == i and unuseable_cords[0] is False:
            useable_cords[0] = True
        if [current_pos[0], current_pos[1] + 1] == i and unuseable_cords[2] is False:
            useable_cords[2] = True


def choose_path():
    global used_cords
    global useable_cords
    global dierectoin
    dierectoin = False
    if useable_cords[0] is True:
        dierectoin = 1
    if useable_cords[1] is True and dierectoin is not True:
        dierectoin = 2
    if useable_cords[2] is True and dierectoin is not True:
        dierectoin = 3
    if useable_cords[3] is True and dierectoin is not True:
        dierectoin = 4


def update_path(possible):
    global dierectoin
    global sloved_path
    global seen_path
    global current_pos
    global looping
    if possible is not False:
        sloved_path.append(current_pos)
        seen_path.append(current_pos)
        if dierectoin == 1:
            current_pos = [current_pos[0], current_pos[1] - 1]
        if dierectoin == 2:
            current_pos = [current_pos[0] + 1, current_pos[1]]
        if dierectoin == 3:
            current_pos = [current_pos[0], current_pos[1] + 1]
        if dierectoin == 4:
            current_pos = [current_pos[0] - 1, current_pos[1]]
    if possible is False:
        seen_path.append(current_pos)
        current_pos = sloved_path[-1]
        sloved_path.pop()


def display():
    for i in seen_path:
        pygame.draw.rect(canvas, (100, 100, 100),
                         pygame.Rect(i[0] * size, i[1] * size, size, size))
    for i in sloved_path:
        pygame.draw.rect(canvas, (150, 0, 150),
                         pygame.Rect(i[0] * size, i[1] * size, size, size))


def check_if_done():
    global current_pos
    global looping
    global size
    if [100, 100] == current_pos:
        looping = False


def maze_solver():
    global used_cords
    global useable_cords
    find_useable()
    choose_path()
    update_path(dierectoin)
    display()
    pygame.display.flip()


def dev_tools():
    global tools
    global done
    global start
    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        tools = True
        print('tools on')
    if keys[pygame.K_d] and tools is True:
        done = True
        print('slow is off')
    if keys[pygame.K_s] and tools is True:
        start = True
        print('started')


def maze_is_solve_able():
    used_cords.append([100, 100])


def make_exit_butten_work():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def start_game():
    if start is True:
        maze_solver()
        check_if_done()


def check_for_delay():
    if done is False:
        time.sleep(.01)


def show_finished_product():
    time.sleep(20)


def dispaly_maze():
    for i in used_cords:
        pygame.draw.rect(canvas, (225, 225, 225),
                         pygame.Rect(i[0] * size, i[1] * size, size, size))
        pygame.display.flip()
    pygame.draw.rect(canvas, (0, 225, 100),
                     pygame.Rect(0 * size, 0 * size, size, size))
    pygame.draw.rect(canvas, (225, 0, 100),
                     pygame.Rect(100 * size, 100 * size, size, size))
    pygame.display.flip()


def main():
    start_pygame()
    set_up_display()
    define_vars()
    maze_is_solve_able()
    dispaly_maze()
    while looping:
        dev_tools()
        start_game()
        check_for_delay()
    show_finished_product()


main()
