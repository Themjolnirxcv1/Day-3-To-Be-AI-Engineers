# ===== OPERATOR PRECEDENCE =====
# Operator precedence adalah aturan urutan eksekusi operator.
# Operator dengan prioritas lebih tinggi akan dijalankan lebih dulu.
# Jika ragu, pakai tanda kurung () biar aman dan jelas.

# 1. ()  → Parentheses
# Isi di dalam tanda kurung selalu dikerjakan lebih dulu

print((2 + 3) * 4)  # 20
# Penjelasan: 2 + 3 = 5, lalu 5 * 4 = 20

# 2. **  → Exponentiation (pangkat)
print(2 ** 3)  # 8
# Penjelasan: 2 pangkat 3 = 8

# 3. +x  -x  ~x
# Unary operator: tanda +, -, dan NOT bitwise
x = 5
print(-x)
print(~x)
# Penjelasan: -5, ~5 adalah bitwise NOT dari 5
# 5. +  -
# Penjumlahan dan pengurangan
print(10 - 3 + 2)  # 9
# Penjelasan: 10 - 3 = 7, lalu 7 + 2 = 9

# 6. <<  >>
# Bitwise shift kiri dan kanan
print(4 << 1)  # 8
# Penjelasan: 4 dalam biner adalah 100, digeser kiri jadi 1000 (8)
print(8 >> 1)  # 4
# Penjelasan: 8 dalam biner adalah 1000, digeser kanan jadi 100 (4)

# 7. &
# Bitwise AND
print(5 & 3)  # 1
# Penjelasan: 5 (0101) & 3 (0011) = 0001 (1)

# 8. ^
# Bitwise XOR
print(5 ^ 3)  # 6
# Penjelasan: 5 (0101) ^ 3 (0011) = 0110 (6)

# 9. |
# Bitwise OR
print(5 | 3)  # 7
# Penjelasan: 5 (0101) | 3 (0011) = 0111 (7)

# 10. == != > >= < <= is is not in not in
# Operator perbandingan, identitas, dan keanggotaan
print(5 > 3 and 2 < 4)  # True
# Penjelasan: 5 > 3 adalah True, 2 < 4 adalah True, jadi True and True = True

# 11. not
# Membalik hasil boolean
print(not (5 > 3))  # False
# Penjelasan: 5 > 3 adalah True, not True = False

# 12. and
# Operator logika AND   
print(True and False)  # False
# Penjelasan: True and False = False    

# 13. or
# Operator logika OR
print(True or False)  # True    
# Penjelasan: True or False = True
# Ringkasan urutan prioritas operator (dari tinggi ke rendah):