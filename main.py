
x = [2, 1, -1, -2, -2, -1, 1, 2]
y = [1, 2, 2, 1, -1, -2, -2, -1]


def possible_moves(e, f, l):
    for i, j in zip(x, y):
        r, s = i + e, j + f
        if 0 < r <= 8 and 0 < s <= 8:
            l.add((r, s))


def solve(input):
    data = [int(i) for i in input.split()]
    p, q, n = data[0], data[1], data[2]

    l = set([(p, q),])
    q = set()
    for move in range(1, n + 1):
        for data_move in l:
            possible_moves(data_move[0], data_move[1], q)
        l = q
        q = set()
    return sorted(list(l), key=lambda element: (element[0], element[1]))


input = '1 3 2' # staring position x and y and number of steps.
out_ = solve(input)
print(out_)
