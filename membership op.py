# ===== MEMBERSHIP OPERATORS =====
# Membership operator digunakan untuk mengecek apakah suatu nilai
# ADA atau TIDAK ADA di dalam sebuah objek/collection
# seperti string, list, tuple, set, atau dictionary.

# in
# Mengembalikan True jika nilai tertentu DITEMUKAN di dalam objek
# Contoh:
# x in y

# not in
# Mengembalikan True jika nilai tertentu TIDAK ditemukan di dalam objek
# Contoh:
# x not in y

buah = ["apel", "pisang", "jeruk"]

print("apel" in buah)        # True  -> ada di list
print("mangga" in buah)      # False -> ga ada di list

print("mangga" not in buah)  # True

# Contoh di string:
teks = "python itu seru"

print("python" in teks)  # True
print("java" in teks)    # False
print("java" not in teks)  # True

# Contoh di dictionary:
data = {"nama": "Thoriq", "umur": 18}

print("nama" in data)    # True  -> ngecek KEY, bukan value
print("Thoriq" in data)     # False

# Contoh lain penggunaan membership operator

buah = ["apel", "pisang", "ceri"]
print("pisang" in buah)        # Output: True

buah = ["apel", "pisang", "ceri"]
print("mangga" not in buah)    # Output: True

teks = "belajar python itu menyenangkan"
print("python" in teks)        # Output: True
print("java" not in teks)      # Output: True
