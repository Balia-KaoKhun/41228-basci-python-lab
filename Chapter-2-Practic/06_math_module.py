import math

x1, y1, x2, y2 = map(float, input().split())

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(round(distance, 1))
