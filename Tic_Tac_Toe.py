import math


def g_setup():
    global game_list
    global grid_size
    grid_size = 3
    game_list = [0]*9
    print(game_list)

g_setup()

def mover(mv):
    global game_list
    if mv%2:
        val = "X"
        location = int(input("X, its your turn "))
    else:
        val = "O"
        location = int(input("O, its your turn "))
    if game_list[location-1]!=0:
        print("invalid move!")
        mover(mv)
    else:
        game_list[location-1] = val
    return None

def printer(lst):
    global grid_size
    global game_list
    for i in range(len(lst)):
        if (i+1)%(grid_size) == 0:
            print(game_list[i],end="\n")
        else:
            print(game_list[i],end=" ")
    return None


def end():
    global game_list
    global grid_size
    horiz_test = []
    vert_test = []
    for i in range(grid_size):
        for j in range(grid_size):
            vert_test.append(game_list[i+(grid_size*j)])
            horiz_test.append(game_list[(i*grid_size)+j])
        if (set(horiz_test) == set("X")) or (set(vert_test) == set("X")):
            return "x wins"
        elif (set(horiz_test) == set("O")) or (set(vert_test) == set("O")):
            return "o wins"
        else:
            vert_test = []
            horiz_test = []
            continue
    diag_test = []
    diag_test1 = []
    for i in range(3):
        diag_test.append(game_list[i+(i*grid_size)])
        diag_test1.append(game_list[(i*grid_size)+(grid_size-i-1)])
    if (set(diag_test) == set("X")) or (set(diag_test1) == set("X")):
        return "x wins"
    elif (set(diag_test) == set("O")) or (set(diag_test1) == set("O")):
        return "o wins"
    elif 0 not in game_list:
        return "draw"
    else:
        return "continue"



def main_loop():
    move_counter = 0
    for i in range(9):
        printer(game_list)
        move_counter+=1
        mover(move_counter)
        the_end = end()
        if the_end=="continue":
            continue
        else:
            print(the_end)
            break
    g_setup()
    main_loop()


main_loop()

# tt = [
#     "X",0,"X",
#     "O","X","O",
#     "X","O","O"
# ]
# print(end(tt))
