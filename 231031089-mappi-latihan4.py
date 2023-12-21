# Latihan 4
# Menerima input pendapatan dari pengguna dan mengonversinya menjadi integer
pendapatan = int(input("Masukkan pendapatan karyawan: "))

# Pernyataan if...elif...else untuk menentukan persentase bonus
if pendapatan <= 1000:
    persentase = 0
elif pendapatan <= 2000:
    persentase = 10
elif pendapatan <= 3000:
    persentase = 20
elif pendapatan <= 4000:
    persentase = 30
elif pendapatan <= 5000:
    persentase = 40

# Menghitung nilai bonus
bonus = pendapatan * (persentase / 100)

# Menghitung total pendapatan
total = pendapatan + bonus

# Cetak output
print("Pendapatan karyawan:", pendapatan)
print("Persentase bonus:", persentase, "%")
print("Bonus yang diterima:", bonus)
print("Total pendapatan:", total)