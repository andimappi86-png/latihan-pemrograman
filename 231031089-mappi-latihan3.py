# Latihan 3
# Membaca input dari pengguna
nama = input("Masukkan nama karyawan: ")
pendapatan = int(input("Masukkan pendapatan karyawan: "))

# Cetak nama karyawan
print("Nama karyawan:", nama)

# Cetak pendapatan karyawan
print("Pendapatan karyawan:", pendapatan)

# Periksa apakah karyawan berhak mendapatkan bonus
if pendapatan > 1000:
    print("Status: Berhak")
else:
    print("Status: Tidak Berhak")
