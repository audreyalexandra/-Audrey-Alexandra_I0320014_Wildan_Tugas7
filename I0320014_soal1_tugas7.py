#SOAL 1 MENGGUNAKAN FUNGSI STRING
nama_lengkap = str(input("Masukan Nama Lengkap: "))

print(" ")
print("1. Merubah Case dari String")
print("normal = " + nama_lengkap)
#upper
nama_lengkap = nama_lengkap.upper()
print("upper = " + nama_lengkap)
#lower
nama_lengkap = nama_lengkap.lower()
print("lower = " + nama_lengkap)
print(" ")

print("2. Memotong String Berdasarkan Indeks")
print("satu arakter pertama adalah: " + nama_lengkap[:1])
print("enam karakter berikutnya adalah: " + nama_lengkap[1:7])
print("satu karakter terakhir adalah: " + nama_lengkap[-1:])
print(" ")

print("3. Indexing")
print("indeks ke-0: " + nama_lengkap[0])
print("indeks ke-3: " + nama_lengkap[3])
print("indeks ke-[0:4]: " + nama_lengkap[0:4])
print(" ")
print("="*10)
