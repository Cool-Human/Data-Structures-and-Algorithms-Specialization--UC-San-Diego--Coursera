from sys import stdin


def min_refills(distance, tank, stops):
    if tank <= 0:
        return -1

    stops = sorted(stops) + [distance]
    current_position = 0
    refills = 0
    i = 0

    while i < len(stops):
        # find farthest stop reachable from current_position
        last_position = current_position
        while i < len(stops) and stops[i] - current_position <= tank:
            last_position = stops[i]
            i += 1

        if last_position == current_position:
            return -1

        if last_position == distance:
            return refills

        # refill at farthest reachable stop
        refills += 1
        current_position = last_position

    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))