def distance(x1, y1, x2, y2):
    new_distance = ((x1 - x2)**2 + (y1 - y2)**2)**1/2
    return new_distance


print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
