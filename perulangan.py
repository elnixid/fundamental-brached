"""
Implementasi Perulangan
1. Ibu berkata : Baca kesepuluh buku baru itu
2. Ibu berkata : Baca kesupuluh buku itu hingga paham
Buat perulangan untuk jumlah buku yang dibaca point satu dan dua

"""
jumlah_buku = 10
print('Ibu berkata : "Baca kesepuluh bukumu"')
jumlah_buku_yang_sudah_dibaca = 0
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke-{jumlah_buku_yang_sudah_dibaca} dibaca")
