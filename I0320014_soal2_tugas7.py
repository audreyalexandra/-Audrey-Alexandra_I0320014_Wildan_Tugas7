#SOAL 2 MENGGUNAKAN FUNGSI NUMERIK
print("menentukan volume yang bernilai integer")
panjang = int(input("Masukan Panjang: "))
lebar = int(input("Masukan lebar: "))
tinggi = int(input("Masukan tinggi: "))

volume = panjang * lebar * tinggi
#integer (angka yang tidak ada komanya)
print("1. INTEGER")
print("Voluemenya adalah: ", volume,"kubik", type(volume))
print(" ")

panjang = float(input("Masukan Panjang: "))
lebar = float(input("Masukan lebar: "))
tinggi = float(input("Masukan tinggi: "))
volume = panjang * lebar * tinggi
print("2. FLOAT")
print("Voluemenya adalah: ", volume,"kubik", type(volume))
print(" ")

print("3. COMPLEX")
a = 5j
b = 10j
c = a + b

print(a, '+', b, '=', c)
print('Tipe dari a:', type(a))
print('Tipe dari b:', type(b))
print('Tipe dari c:', type(c))
print(" ")