# ===== COMPARISON OPERATORS =====
# Comparison operator digunakan untuk membandingkan dua nilai.
# Hasil dari perbandingan ini SELALU Boolean: True atau False

# ==  (Equal)
# Mengecek apakah dua nilai sama
# Contoh:
# x == y  -> True jika nilai x sama dengan y

# !=  (Not Equal)
# Mengecek apakah dua nilai tidak sama
# Contoh:
# x != y  -> True jika nilai x berbeda dengan y

# >  (Greater Than)
# Mengecek apakah nilai kiri lebih besar dari nilai kanan
# Contoh:
# x > y   -> True jika x lebih besar dari y

# <  (Less Than)
# Mengecek apakah nilai kiri lebih kecil dari nilai kanan
# Contoh:
# x < y   -> True jika x lebih kecil dari y

# >=  (Greater Than or Equal To)
# Mengecek apakah nilai kiri lebih besar ATAU sama dengan nilai kanan
# Contoh:
# x >= y  -> True jika x lebih besar atau sama dengan y

# <=  (Less Than or Equal To)
# Mengecek apakah nilai kiri lebih kecil ATAU sama dengan nilai kanan
# Contoh:
# x <= y  -> True jika x lebih kecil atau sama dengan y

x = 5 
y = 3
print(x == y)   # Output: False
print(x != y)   # Output: True
print(x > y)    # Output: True
print(x < y)    # Output: False
print(x >= y)   # Output: True
print(x <= y)   # Output: False
# Dalam contoh di atas, berbagai operator perbandingan digunakan untuk membandingkan nilai x dan y

x = 5
print ( 1 < x < 10)   # Output: True
print ( x > 1 and x < 10)  # Output: True
# Dalam contoh di atas, kita memeriksa apakah x berada di antara 1 dan