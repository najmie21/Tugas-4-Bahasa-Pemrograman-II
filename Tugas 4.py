# Matriks A dan B 5x5
A = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2],
    [1, 1, 1, 1, 1]
]

B = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]
]

# Matriks hasil perkalian 5x5, inisialisasi dengan nilai 0
hasil = [[0 for _ in range(5)] for _ in range(5)]

# Perkalian matriks
for i in range(5):
    for j in range(5):
        for k in range(5):
            hasil[i][j] += A[i][k] * B[k][j]

# Menampilkan hasil matriks perkalian
print("Hasil perkalian matriks A dan B:")
for row in hasil:
    print(row)
