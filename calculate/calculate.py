import cmath


def manhattan_distance(x1, y1, x2, y2):
    distance = (x2 - x1) + (y2 - y1)
    return distance


def euclidean_distance(x1, y1, x2, y2):
    distance = cmath.sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)
    return distance
