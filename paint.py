import math


def paint(h, w):
    area = h * w
    no_cans = math.ceil(area / 5)
    print(no_cans)


paint(3, 8)
