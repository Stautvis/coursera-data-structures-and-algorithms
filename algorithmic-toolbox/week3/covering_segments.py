# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    while len(segments) > 0:
        min_point = min([x.end for x in segments])
        print(min_point)
        points.append(min_point)
        segments = list(filter(lambda x: x.start > min_point or min_point > x.end, segments))
        print(segments)
    return points

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
