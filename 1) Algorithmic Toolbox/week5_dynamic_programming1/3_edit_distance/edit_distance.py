def edit_distance(first_string, second_string):
    m, n = len(first_string), len(second_string)
    
    T = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        T[i][0] = i
    for j in range(n + 1):
        T[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_string[i - 1] == second_string[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(
                    T[i - 1][j],
                    T[i][j - 1],
                    T[i - 1][j - 1]
                )
    
    return T[m][n]



if __name__ == "__main__":
    print(edit_distance(input(), input()))