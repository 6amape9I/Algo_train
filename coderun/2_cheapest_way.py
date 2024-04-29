def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    min_matrix = [[float('inf')] * m for _ in range(n)]
    min_matrix[0][0] = matrix[0][0]

    for i in range(n):
        for j in range(m):
            if i > 0:
                min_matrix[i][j] = min(min_matrix[i][j], min_matrix[i - 1][j] + matrix[i][j])
            if j > 0:
                min_matrix[i][j] = min(min_matrix[i][j], min_matrix[i][j - 1] + matrix[i][j])
    print(min_matrix[n - 1][m - 1])


if __name__ == '__main__':
    main()