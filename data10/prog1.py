score_list = set()


def get_grid(path):
    grid = []
    with open(path, 'r') as file:
        for line in file:
            grid.append(list(map(lambda val: int(val), list(line.strip()))))
    return grid


def get_next_element_up(grid, head, curr_ele):
    nxt_ele, next_ele_cords = None, None
    if head[0] != 0:
        next_ele_cords = (head[0] - 1, head[1])
        nxt_ele = grid[next_ele_cords[0]][head[1]]
        if nxt_ele != curr_ele + 1:
            nxt_ele, next_ele_cords = None, None
    return nxt_ele, next_ele_cords


def get_next_element_down(grid, head, curr_ele):
    nxt_ele, next_ele_cords = None, None
    height = len(grid) - 1
    if head[0] < height:
        next_ele_cords = (head[0] + 1, head[1])
        nxt_ele = grid[next_ele_cords[0]][next_ele_cords[1]]
        if nxt_ele != curr_ele + 1:
            nxt_ele, next_ele_cords = None, None
    return nxt_ele, next_ele_cords


def get_next_element_left(grid, head, curr_ele):
    nxt_ele, next_ele_cords = None, None
    if head[1] > 0:
        next_ele_cords = (head[0], head[1] - 1)
        nxt_ele = grid[next_ele_cords[0]][next_ele_cords[1]]
        if nxt_ele != curr_ele + 1:
            nxt_ele, next_ele_cords = None, None
    return nxt_ele, next_ele_cords


def get_next_element_right(grid, head, curr_ele):
    nxt_ele, next_ele_cords = None, None
    if head[1] < len(grid[head[0]]) - 1:
        next_ele_cords = (head[0], head[1] + 1)
        nxt_ele = grid[next_ele_cords[0]][next_ele_cords[1]]
        if nxt_ele != curr_ele + 1:
            nxt_ele, next_ele_cords = None, None
    return nxt_ele, next_ele_cords


def get_trailhead_positions(grid):
    trailHeads = []
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == 0:
                trailHeads.append((x, y))

    return trailHeads


def examine_element_all_direction(grid, head, curr_ele):
    left = get_next_element_left(grid, head, curr_ele)
    right = get_next_element_right(grid, head, curr_ele)
    down = get_next_element_down(grid, head, curr_ele)
    up = get_next_element_up(grid, head, curr_ele)

    if left[0] is not None:
        if left[0] == 9:
            score_list.add((1, left[1]))
        examine_element_all_direction(grid, left[1], left[0])

    if right[0] is not None:
        if right[0] == 9:
            score_list.add((1, right[1]))
        examine_element_all_direction(grid, right[1], right[0])

    if up[0] is not None:
        if up[0] == 9:
            score_list.add((1, up[1]))
        examine_element_all_direction(grid, up[1], up[0])

    if down[0] is not None:
        if down[0] == 9:
            score_list.add((1, down[1]))
        examine_element_all_direction(grid, down[1], down[0])

    return 0


if __name__ == '__main__':
    total_score = []
    grid = get_grid('data.txt')
    trailHeads = get_trailhead_positions(grid)
    for trailHead in trailHeads:
        examine_element_all_direction(grid, trailHead, 0)
        total_score.append(len(score_list))
        score_list = set()

    print(sum(total_score))
