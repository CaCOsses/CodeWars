def check_peri(field, i_offset, j_offset,
                          ship_direction, checked_cells):

    for i in range(i_offset - 1, i_offset + ship_direction[0] + 1):
        if 0 <= i < 10:
            j = j_offset - 1
            if j >= 0 and not checked_cells[i*10 + j] and field[i][j]:
                return False
            j = j_offset + ship_direction[1]
            if j < 10 and not checked_cells[i*10 + j] and field[i][j]:
                return False


    for j in range(j_offset, j_offset + ship_direction[1]):
        if i < 10:
            i = i_offset + ship_direction[0]
            if field[i][j]:
                return False

    return True


def get_dir(field, i_offset, j_offset):
    i = j = 0
    while i_offset + i < 10 and field[i_offset+i][j_offset]:
        i += 1
    while j_offset + j < 10 and field[i_offset][j_offset+j]:
        j += 1
    return i, j


def validate_battlefield(field):
    ships_rest = {1: 4,
                  2: 3,
                  3: 2,
                  4: 1}
    checked_cells = [False for _ in range(10*10)]

    if sum(sum(cell for cell in row) for row in field) != 20:
        return False

    for i in range(len(field)):
        for j in range(len(field)):
            if not checked_cells[i*10 + j] and field[i][j]:
                ship_dir = get_dir(field, i, j)
                ship_len = max(ship_dir)

                if ship_len not in ships_rest or ships_rest[ship_len] == 0:
                    return False 
                if sum(ship_dir) != ship_len + 1:
                    return False  
                if not check_peri(field, i, j, ship_dir, checked_cells):
                    return False 

                for x in range(j, j + ship_dir[1]):
                    checked_cells[i*10 + x] = True
                for y in range(i, i + ship_dir[0]):
                    checked_cells[y*10 + j] = True

                ships_rest[ship_len] -= 1
            else:
                checked_cells[i*10 + j] = True

    return True