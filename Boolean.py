# Boolean adalah tipe data yang hanya punya dua nilai: True atau False
# Boolean dipakai untuk pengambilan keputusan dalam program

# Setiap perbandingan akan menghasilkan nilai Boolean
# Contoh:
# 5 > 3   -> True
# 5 < 3   -> False
# 5 == 5  -> True

# Python mengevaluasi ekspresi perbandingan
# lalu mengembalikan hasil dalam bentuk True atau False

print (10 > 5)    # Output: True
print (10 == 5)   # Output: False
print (10 < 5)    # Output: False

a = 200
b = 33

if b > a:
  print("b lebih besar dari a")

else: 
    print("b tidak lebih besar dari a")
# Output: b tidak lebih besar dari a
# Dalam contoh di atas, program memeriksa apakah b lebih besar dari a
# Karena kondisi tersebut salah, program mengeksekusi blok else

#  evaluasi values dan variables
# evaluasi string dan number
print(bool("Hello"))  # Output: True
print(bool(15))       # Output: True

# evaluasi dua variabel
x = "Hello"
y = 15

print(bool (x)) # Output: True
print(bool(y)) # Output: True
# Dalam contoh di atas, string "Hello" dan angka 15 dievaluasi sebagai True karena keduanya tidak kosong atau nol   

# banyak value yang dianggap true
# value di evaluasi sebagai true jika setidaknya memiliki satu karakter atau satu angka

bool("abc")  # True
bool(123)   # True
bool(["apple", "mango", "banana"])  # True

# banyak value yang dianggap false
# value di evaluasi sebagai false jika kosong atau bernilai nol

bool("")     # False    
bool(False)  # False
bool(None)   # False
bool(0)      # False
bool([])     # False
bool(())     # False
bool({})     # False
# Dalam contoh di atas, string kosong, angka nol, dan struktur 
# data kosong dievaluasi sebagai False

# satu lagi value, atau objek di dalam case, yang dianggao false
# dan itu jika kamu mempunyai objek yanf dibuat dari class yang memiliki
# method __bool__() yang mengembalikan False atau method __len__() yang
# mengembalikan 0 atau False

class Myclass(): 
   def __len__(self):
      return 0

myobj = Myclass()
print(bool(myobj))  # Output: False

# Dalam contoh di atas, objek myobj dievaluasi sebagai False karena
# class Myclass memiliki method __len__() yang mengembalikan 0

# function bisa mengembalikan boolean
def myFunction():
   return True

print(myFunction()) # Output: True
# Dalam contoh di atas, function myFunction mengembalikan nilai Boolean True

def myFunction():
   return True

if myFunction():
    print("yes")
else:
    print("no")

# Output: yes
# Dalam contoh di atas, function myFunction mengembalikan True
# sehingga blok if dieksekusi dan mencetak "yes"

x = 200
print(isinstance(x, int))  # Output: True
# Dalam contoh di atas, fungsi isinstance() memeriksa apakah x adalah
# instance dari tipe data int dan mengembalikan True karena x adalah 200