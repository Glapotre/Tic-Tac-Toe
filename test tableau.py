m = [[1, 3, 4],
     [5, 6, 8],
     [2, 1, 3],
     [7, 8, 15]]
nb_colonne = 3
nb_ligne = 4
for i in range(0, nb_ligne):
	for j in range(0, nb_colonne):
		a = m[i][j]
		print(a)
print(m[2][1])