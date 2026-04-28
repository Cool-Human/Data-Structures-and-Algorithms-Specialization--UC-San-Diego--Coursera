from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    """
    Find closest pair using divide and conquer. O(n log² n)
    """
    def closest_pair_recursive(px, py):
        n = len(px)
        
        # Base case: brute force for small inputs
        if n <= 3:
            min_dist_sq = float("inf")
            for i in range(n):
                for j in range(i + 1, n):
                    min_dist_sq = min(min_dist_sq, distance_squared(px[i], px[j]))
            return min_dist_sq
        
        # Divide
        mid = n // 2
        midpoint = px[mid]
        
        # Split py into left and right
        pyl = [p for p in py if p.x <= midpoint.x]
        pyr = [p for p in py if p.x > midpoint.x]
        
        # Conquer
        left_min = closest_pair_recursive(px[:mid], pyl)
        right_min = closest_pair_recursive(px[mid:], pyr)
        
        # Combine: find min of the two halves
        min_dist_sq = min(left_min, right_min)
        min_dist = sqrt(min_dist_sq)
        
        # Check strip: points within min_dist of the dividing line
        strip = [p for p in py if abs(p.x - midpoint.x) < min_dist]
        
        # Check points in strip (at most 7-8 comparisons per point)
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j].y - strip[i].y) ** 2 < min_dist_sq:
                min_dist_sq = min(min_dist_sq, distance_squared(strip[i], strip[j]))
                j += 1
        
        return min_dist_sq
    
    # Sort by x and y coordinates
    px = sorted(points, key=lambda p: p.x)
    py = sorted(points, key=lambda p: p.y)
    
    return closest_pair_recursive(px, py)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
