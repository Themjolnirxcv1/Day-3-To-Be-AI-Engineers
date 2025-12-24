# ===== LOGICAL OPERATORS =====
# Logical operator digunakan untuk menggabungkan beberapa kondisi (conditional statements).
# Hasil akhirnya SELALU Boolean: True atau False

# and
# Menghasilkan True jika SEMUA kondisi bernilai True
# Jika salah satu False, hasilnya False
# Contoh:
# x < 5 and x < 10
# Artinya: x harus lebih kecil dari 5 DAN juga lebih kecil dari 10

# or
# Menghasilkan True jika SALAH SATU kondisi bernilai True
# Jika dua-duanya False, baru hasilnya False
# Contoh:
# x < 5 or x < 4
# Artinya: cukup salah satu kondisi terpenuhi

# not
# Membalik hasil kondisi
# True jadi False, False jadi True
# Contoh:
# not (x < 5 and x < 10)
# Artinya: kebalikan dari hasil kondisi di dalam kurung

umur = 18
punya_ktp = True

print(umur >= 17 and punya_ktp)  # True -> lolos syarat
print(umur < 17 or punya_ktp)    # True -> salah satu terpenuhi
print(not punya_ktp)             # False -> karena punya_ktp = True
# Dalam contoh di atas, operator logika and, or, dan not digunakan untuk mengevaluasi kondisi berdasarkan nilai variabel umur dan punya_ktp

x = 5 
print ( x > 0 and x < 10)
# Output: True

x = 5
print(x < 5  or x > 10)
# Output: False

x = 5
print(not (x > 3 and x < 10))
# Output: False
# Dalam contoh di atas, berbagai operator logika digunakan untuk mengevaluasi nilai x terhadap kondisi