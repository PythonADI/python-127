"""
0 0 0 0 0 0 0 1 0 0

🟩🟩🟩🟩🟩🧑‍🌾🟩🟩🟩🟩🟩
"""

space = [0, 0, 0, 0, 0, 0, 1, 0]

pos = space.index(1)

def move(new_pos, old_pos, space):
    if new_pos < 0 or len(space) - 1 < new_pos:
        return old_pos
    space[new_pos] = 1
    space[old_pos] = 0
    return new_pos

def move_left(space):
    return move(pos - 1, pos, space)

def move_right(space):
    return move(pos + 1, pos, space)


def draw(space):
    print("\033c")
    for cell in space:
        if cell == 1:
            print("😊", end="")
        elif cell == 0:
            print("🟩", end="")
    print()
        



while True:
    draw(space)
    direction = input(f"l (left) / r (right) ({pos}): ")
    
    if direction == "r":
        pos = move_right(space)
    elif direction == "l":
        pos = move_left(space)
    

