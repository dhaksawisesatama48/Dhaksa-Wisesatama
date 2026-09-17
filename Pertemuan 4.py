a = True
b = False
c = not a
d = not b

#Not
print(not a)
print(not b)
print(not c)
print(not d)

#OR
print(a or b)
print(c or b)
print(a or d)

#And
print(a or b)
print(c or b)
print(a or d)

#xor
print(a or b)
print(c or b)
print(a or d)

umur = int(input("masukan angka:"))

if umur < 12:
   print("anak-anak")
elif umur > 12 and umur < 18:
    print("remaja ")
elif umur > 18 and umur < 59:
    print("dewasa ")
else :
    print("lansia")