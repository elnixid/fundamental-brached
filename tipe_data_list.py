daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
print(daftar_buku)
print('\nMenampilkan daftar buku semua dengan for....in...')
for buku in daftar_buku:
    print(buku)

print('\nMenampilkan daftar buku menggunakan index')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nMenampilkan daftar buku dengan menggunakan for ... in ... range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Naruto 1', -224, 3.14]
print('\nMenampilkan dengan for in range data element nya berbeda-beda tipe datanya')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembali ke daftar buku yang awal')
daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
print('\nMenambahkan daftar buku dengan perintah Append')
daftar_buku.append('Lean Start Up')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMenghapus isi dari daftar buku dengan perintah clear()')
daftar_buku.clear()
print('\n----------------------')
daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
daftar_buku[0] = 'Delapan Habit'
print('\nDaftar buku yang baru')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil buku yang ada di list dengan perintah pop()')
buku_ambil = daftar_buku.pop(1)
print('\nBuku yang tersisa di list :')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil adalah:')
print(buku_ambil)

daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
print('\nDaftar buku yang ada:')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    # print('\n--------------------------')

print('\nMengambil data di list dengan pop minus, -1, -2, dsb')
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

