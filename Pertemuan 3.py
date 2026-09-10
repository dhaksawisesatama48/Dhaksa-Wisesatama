a = 10
b = 3

hasil = a + b
print(hasil)

hasil = a - b
print(hasil)

hasil = a * b
print (hasil)

hasil = a / b
print (hasil)

hasil = a ** b
print (hasil)

hasil = a % b
print (hasil)

hasil = a // b
print(hasil)

celcius = float(input("Masukan suhu dalam celcius : ")) 
print ("suhu adalah", celcius, "Celcius")

reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

fahrenheit = ((9/5) * celcius) + 32 
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")

a = 4 
b = 2

print("=============== lebih besar dari (>)") 
hasil = a > 3 
print(a,'>',b,'=',hasil) 
hasil = b > 3 
print(b,'>',3,'=',hasil) 
hasil = b > 2 
print(b,'>',2,'=',hasil) 

print("============== kurang dari (<)") 
hasil = a < 3 
print(a,'<',b,'=',hasil) 
hasil = b < 3 
print(b,'<',3,'=',hasil) 
hasil = b < 2 
print(b,'<',2,'=',hasil) 

# lebih dari sama dengan >= 
print("=============== lebih dari sama dengan (>=)") 
hasil = a >= 3 
print(a,'>=',b,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2 
print(b,'>=',2,'=',hasil) 

# kurang dari sama dengan <= 
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,'<=',b,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil) 

# sama dengan (==)
print("=============== sama dengan (==)")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print("=============== sama dengan (!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# ‘is’ sebagai komparasi obj identity (bukan literal) 
x = 5 # ini adalah assignment membuat object 
y = 5 
hasil = x is y
print('x is y =',hasil)
# ‘is not’ sebagai komparasi obj identity (bukan literal)
x = 5 # ini adalah assignment membuat object 
y = 6 
hasil = x is not y
print('x is not y =',hasil)  

panjang = 12
lebar = 5
tinggi = 8

Luas = 2 * (panjang*lebar + lebar*tinggi + tinggi*panjang)
volome = panjang * lebar * tinggi
keliling = 4 * (panjang + lebar + tinggi)

print (Luas)
print (volome)
print (keliling)
print (Luas > 50)
print (volome == 480)