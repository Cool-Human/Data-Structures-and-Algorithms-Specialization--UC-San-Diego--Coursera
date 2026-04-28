from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key=lambda x: x.end) # Sort segments by their end points.
    points = [] # Initialize an empty list to store the points that will cover the segments.
    last_point = -1 # Initialize last_point to a value less than any possible start point of the segments.

    for s in segments:
        if s.start > last_point: # If the start of the current segment is greater than the last point,
            last_point = s.end # Update the last_point to the end of the current segment.
            points.append(last_point) # Add the last_point to the list of points.
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)