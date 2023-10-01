# Import NumPy Library
import numpy as np
import sys

# Judul
print("PROGRAM MENGHITUNG KEUNTUNGAN MAKSIMUM MENGGUNAKAN GAUSS")

# Memasukkan ordo matriks
n = int(input("\nMasukkan jumlah jenis produk: "))

# Membuat numpy array berdasarkan ordo n x n+1 dan memulainya dari 0 untuk menyimpan matriks yang ditambahkan
a = np.zeros((n, n + 1))

# Petunjuk
print("\nKETERANGAN: ")
for i in range(n):
    if i == 0:
        for j in range (0, n):
            print(f"Koefisien [{i}][{j}] = Jumlah produk {j+1} -> masukkan 1")
        print(f"Koefisien [{i}][{j+1}] = Jumlah produk maksimum")
    if i == 1:
        for j in range (0, n):
            print(f"Koefisien [{i}][{j}] = Takaran bahan produk {j+1}")
        print(f"Koefisien [{i}][{j+1}] = Takaran bahan produk maksimum")
    if i == 2:
        for j in range (0, n):
            print(f"Koefisien [{i}][{j}] = Modal produk {j+1}")
        print(f"Koefisien [{i}][{j+1}] = Biaya produksi maksimum")

# Membaca koefisien matriks
print("\nMasukkan koefisien berdasarkan keterangan di atas:")
koefisien = []
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input(f"Koefisien [{i}][{j}]: "))
        koefisien.append(a[i][j])


# Mengaplikasikan metode eliminasi Gauss
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit("Kesalahan input!")

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Substitusi balik
x = np.zeros(n)
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

# Mencetak penyelesaian
Solusi = []
print("\nJumlah Produk: ")
for i in range(n):
    print(f'Produk {i+1} = {x[i]:.2f}')
    Solusi.append(x[i])

# Persentase Laba
print("\nPersentase Laba:")
persentase_laba = []
for y in range(n):
    y = float(input(f"Persentase laba produk {y+1} yang diinginkan (bentuk desimal): "))
    persentase_laba.append(y)

# Laba
print("\nLaba")
laba = [x*y for x,y in zip(koefisien[8:11], persentase_laba)]
z = 0
for i in laba:
    print(f"Produk {z+1}: Rp.", i)
    z += 1

# Harga Jual
print("\nHarga jual:")
harga = [x+y for x,y in zip(koefisien[8:11], laba)]
z = 0
for i in harga:
    print(f"Produk {z+1}: Rp.", i)
    z += 1

# Laba Maksimum
print("\nLaba maksimum:")
laba_maks = [x*y for x,y in zip(Solusi, laba)]
print("Rp.", sum(laba_maks))