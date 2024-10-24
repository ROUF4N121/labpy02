# Kasus 1: Program Pemesanan Tiket Bioskop

# Input user
tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").lower()
is_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Harga tiket
harga_reguler = 50000
harga_vip = 100000

# Tentukan harga tiket
harga_tiket = harga_reguler if tipe_tiket == 'reguler' else harga_vip

# Jika member, berikan diskon 20%
if is_member == 'ya':
    harga_tiket *= 0.8  # diskon 20%

# Tampilkan total harga
print(f"Total harga yang harus dibayar: Rp{int(harga_tiket)}")