# ===== IDENTITY OPERATORS =====
# Identity operator digunakan untuk membandingkan IDENTITAS objek,
# bukan sekadar nilainya sama atau tidak.
# Yang dicek adalah: apakah dua variabel menunjuk ke OBJEK YANG SAMA
# di lokasi memori yang sama.

# is
# Menghasilkan True jika kedua variabel menunjuk ke objek yang sama persis
# (satu objek, satu lokasi memori)
# Contoh:
# x is y

# is not
# Menghasilkan True jika kedua variabel TIDAK menunjuk ke objek yang sama
# walaupun nilainya bisa saja sama
# Contoh:
# x is not y

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)   # True  -> nilainya sama
print(a is b)   # True  -> objeknya sama

print(a == c)   # True  -> nilainya sama
print(a is c)   # False -> objeknya beda (memori beda)

x = ["apple" , "mango"]
y = ["apple" , "mango"]
z = x
print(x is z)        # Output: True
print(x is y)        # Output: False
print(x == y)        # Output: True
# Dalam contoh di atas, variabel x dan z menunjuk ke objek yang sama,
# sedangkan y adalah objek yang berbeda meskipun nilainya sama dengan x

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)    # Output: True
# Dalam contoh di atas, x dan y adalah objek yang berbeda,

# perbedaan is dan ==
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)   # True  -> nilainya sama
print(x is y)   # False -> objeknya beda
# Dalam contoh di atas, meskipun x dan y memiliki nilai yang sama,
# mereka adalah objek yang berbeda di memori, sehingga x is y menghasilkan False
