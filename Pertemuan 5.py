angka = 1 
print(angka) 
angka = angka + 1 
print(angka) 
angka = angka + 1 
print(angka)

angka2 = [0,1,2,3,4]
print(angka2) 
for i in angka2:
    print(f"i sekarang → {i}")
print("akhiri dari program\n")

angka3 = range(5)
for i in angka3:
    print(f"i sekarang → {i}")
print("akhiri dari program\n")

angka4 = range(1,10) 
for i in angka4:
    print(f"i sekarang → {i}")
print("akhiri dari program\n")

data_str = "saya ganteng abiies"
for huruf in data_str: 
    print(huruf)
print("akhiri dari program\n")

print ("===contoh 1===\n")

angka = 10 
while angka > 100: 
    print("ipin lari ipin!!!") 

print("===contoh 2===\n")

angka = 0
print(f"angka sekarang → {angka}")

while angka < 5:  
    angka += 1
    print(f"angka sekarang → {angka}") 
    print("ipin lari ipin")

print("program berakhir, ipin sudah jauh")

angka = 0
while angka < 5:
    angka = angka + 1

    if(angka == 3):   
        pass
        print(angka)

angka = 0 
print(f"angka sekarang → {angka}")  

while angka < 5:
    angka = angka + 1
    print(f"angka sekarang → {angka}")

    if(angka == 3):
        print("nice")
        continue
    print("whasssup")

print("Pinish")

angka = 0
print(f"angka sekarang → {angka}") 

while angka < 5:
    angka = angka + 1
    print(f"angka sekarang → {angka}")

    if(angka == 3):
        print("nice")
        break  
    print("whasssup")

print("cukup mass")

#tugas======================================================

print("=== Bilangan Ganjil-Genap (1 - 50) ===")
for i in range(1, 51):
    if i % 2 == 0:
        print("\n",i,"Bilangan genap", end=" ")
    else:
        print("\n",i,"Bilangan ganjil", end=" ")

print("\nBilangan Prima (1 - 100)")
for angka in range(2, 101):
    prima = True
    
    # Cek apakah angka bisa dibagi oleh bilangan lain
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break  # Keluar dari perulangan jika terbukti bukan prima
            
    # Jika lolos pengecekan, cetak angka
    if prima:
        print(angka, end=" ")