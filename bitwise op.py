# ===== BITWISE OPERATORS =====
# Bitwise operator digunakan untuk operasi langsung ke
# representasi BINARY (0 dan 1) dari sebuah angka.
# Jadi yang diolah bukan angkanya, tapi bit-bit di dalamnya.
# AND (&)
# Setiap bit akan bernilai 1 JIKA KEDUA bit bernilai 1
# Contoh:
# 5  -> 0101
# 3  -> 0011
# 5 & 3 = 0001 (1)
print(5 & 3)  # output: 1

# OR (|)
# Setiap bit akan bernilai 1 jika SALAH SATU bit bernilai 1
# Contoh:
# 5 | 3 = 0111 (7)
print(5 | 3)  # output: 7

# XOR (^)
# Setiap bit bernilai 1 JIKA HANYA SALAH SATU yang 1
# Kalau dua-duanya sama (1-1 atau 0-0) hasilnya 0
print(5 ^ 3)  # output: 6

# NOT (~)
# Membalik semua bit (0 jadi 1, 1 jadi 0)
# Di Python hasilnya bisa terlihat aneh karena sistem bilangan signed
print(~5)     # output: -6

# Left Shift (<<)
# Geser bit ke KIRI, tambahin 0 dari kanan
# Efeknya sama kayak mengalikan dengan 2^n
print(5 << 2)  # 5 * 2^2 = 20

# Right Shift (>>)
# Geser bit ke KANAN
# Efeknya sama kayak pembagian integer 2^n
print(20 >> 2)  # output: 5

# Ringkasan biar nyantol:

# & → dua-duanya harus 1

# | → salah satu 1 cukup

# ^ → beda sendiri baru 1

# ~ → kebalikan total

# << → geser kiri = kali

# >> → geser kanan = bagi