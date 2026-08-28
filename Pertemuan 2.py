# Variabel adalah tempat menyimpan nilai/data
# jenis-jenis tipe data: 1. string  = karakter
#                        2. integer = bilangan bulat
#                        3. double/float  = bilangan desimal
#                        4. boolean = true/false

# aturan penamaan : -tidak boleh menggunakan spasi(bisa diganti dengan underscore)
#                   -tidak boleh diawali dengan angka
#                   -camelcase

Nama = input("masukan nama: ")                                  #input nama
Usia = input("masukan usia: ")                                  #input usia
Tinggi = input("masukan tinggi badan: ")                        #input tinggi

Nilai_1 = int(input("\nmasukan angka ke 1: "))                     #input nilai pertama integer
Nilai_2 = float(input("masukan angka ke 2: "))                     #input nilai kedua float
Nilai_3 = str(input("masukan angka ke 3: "))                       #input nilai ketiga string

print ( "\nNama saya adalah: ", Nama)                           
print ( "Usia Saya adalah: ", Usia)
print ( "Tinggi Saya adalah: ", Tinggi)

print ( "type Nilai_1: ", type(Nilai_1), "dan nilainya adalah", Nilai_1)
print ( "type Nilai_2: ", type(Nilai_2), "dan nilainya adalah", Nilai_2)
print ( "type Nilai_3: ", type(Nilai_3), "dan nilainya adalah", Nilai_3)

print ("\nmengubah type nilai")
Nilai_1 = float(Nilai_1)
Nilai_2 = int(Nilai_2)
Nilai_3 = float(Nilai_3)

print ( "type Nilai_1 saat ini: ", type(Nilai_1), "dan nilainya adalah", Nilai_1)
print ( "type Nilai_2 saat ini: ", type(Nilai_2), "dan nilainya adalah", Nilai_2)
print ( "type Nilai_3 saat ini: ", type(Nilai_3), "dan nilainya adalah", Nilai_3)

Nilai_1 = str(Nilai_1 + int(input("\nMasukan angka tambahan: ")))

print ("\nNilai_1 sekarang adalah ",Nilai_1)
