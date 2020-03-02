h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]

d = {(i, j):c for i, row in enumerate(s) for j, c in enumerate(row)}

def next_to_black(i, j):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    surroundings = ((i + a, j + b) for a, b in directions)
    colors = (d.get(cell, '.') for cell in surroundings)
    return any(color == "#" for color in colors)

black_coords = (coord for coord, c in d.items() if c == "#")
paintable = all(next_to_black(*coord) for coord in black_coords)
print("Yes" if paintable else "No")
