import csv

with open("data.txt", "r") as fo:
    rows = csv.reader(fo)
    rows = list(rows)
    rows = rows[1:]

cities = []
for row in rows:
    cities.append(row[0])
    cities.append(row[1])

cities = list(set(cities))
cities = sorted(cities)

adj_matrix = [[0] * len(cities) for _ in range(len(cities))]
adj_matrix_2 = [[0] * len(cities) for _ in range(len(cities))]

for row in rows:
    i = cities.index(row[0])
    j = cities.index(row[1])
    adj_matrix[i][j] = int(row[2])
    adj_matrix_2[i][j] = int(row[3])

# print(cities)
for row in adj_matrix_2:
    print(row)

# print(cities)