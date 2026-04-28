from sys import stdin


def points_cover_naive(starts, ends, points):
    """
    Count segments covering each point using sweep line algorithm.
    Time: O((n+m) log (n+m)), Space: O(n+m)
    """
    assert len(starts) == len(ends)
    
    # Create events: (position, type, segment_index)
    # type: 0 = segment start, 1 = segment end+1, 2 = point query
    events = []
    
    for i, (start, end) in enumerate(zip(starts, ends)):
        events.append((start, 0, i))          # Segment starts
        events.append((end + 1, 1, i))        # Segment ends (exclusive)
    
    point_indices = {}
    for i, point in enumerate(points):
        if point not in point_indices:
            point_indices[point] = []
        point_indices[point].append(i)
        events.append((point, 2, i))
    
    # Sort events: by position, then type (start < query < end)
    events.sort()
    
    count = [0] * len(points)
    active_segments = 0
    
    for pos, event_type, idx in events:
        if event_type == 0:          # Segment start
            active_segments += 1
        elif event_type == 1:        # Segment end
            active_segments -= 1
        else:                        # Point query
            count[idx] = active_segments
    
    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
