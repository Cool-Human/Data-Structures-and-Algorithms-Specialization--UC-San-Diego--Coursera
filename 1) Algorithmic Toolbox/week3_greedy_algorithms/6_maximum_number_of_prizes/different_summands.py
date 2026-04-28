def optimal_summands(n):

    summands = []
    current_prize = 1 # Starting with the smallest positive integer.

    while n > 0:
        if n <= 2 * current_prize: # If the remaining n has to be greater than current prize.
            summands.append(n)
            break # This breaks the while loop as we have found the last summand.
        else:
            summands.append(current_prize) # Otherwise, we add the current prize to the list and move on.
            n -= current_prize # Deduct the current prize from n to continue loop.
            current_prize += 1 # Move on to the next smallest positive integer.

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)