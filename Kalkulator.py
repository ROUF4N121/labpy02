# Kasus 2: Program Kalkulator Sederhana

# Input user
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

# Operasi aritmatika berdasarkan input
if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Tidak bisa membagi dengan nol"
else:
    hasil = "Operator tidak valid"

# Tampilkan hasil
print(f"Hasil: {hasil}")