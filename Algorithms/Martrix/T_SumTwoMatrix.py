martrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
martrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
r_row = len(martrix1)
c_col = len(martrix1[0])
for i in range(r_row):
  for j in range(c_col):
    sum_matrix[i][j] = martrix1[i][j] + martrix2[i][j]
print(sum_matrix)
