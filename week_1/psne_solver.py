def solve_psne(p1_matrix, p2_matrix):

    total_rows = len(p1_matrix)
    total_cols = len(p1_matrix[0])

    psne = []

    for row in range(total_rows):
        for col in range(total_cols):

            trueone = True

            for check_row in range(total_rows):

                if p1_matrix[check_row][col] > p1_matrix[row][col]:
                    trueone = False
                    break

            truetwo = True

            for check_col in range(total_cols):

                if p2_matrix[row][check_col] > p2_matrix[row][col]:
                    truetwo = False
                    break

            if trueone and truetwo:
                psne.append((row, col))

    return psne


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Player 1 payoff matrix:")

p1_matrix = []

for i in range(rows):
    row_data = list(map(int, input().split()))
    p1_matrix.append(row_data)

print("Enter Player 2 payoff matrix:")

p2_matrix = []

for i in range(rows):
    row_data = list(map(int, input().split()))
    p2_matrix.append(row_data)

print("PSNE points are:")
print(solve_psne(p1_matrix, p2_matrix))