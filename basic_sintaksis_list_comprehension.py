print('\nPerintah del dengan list comprehension')
daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
del daftar_buku[0:-2] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
del daftar_buku[0::2] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list buku baru dengan tanda = ')
daftar_buku = ['Seven Habit','Blink', 'First Thinks First', 'Rich Dad']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMenghapus daftar_buku dan menampilkan daftar_buku_baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : ganjil')
daftar_buku = ['1. Seven Habit','2. Blink', '3. First Thinks First', '4. Rich Dad']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : genap')
daftar_buku = ['1. Seven Habit','2. Blink', '3. First Thinks First', '4. Rich Dad']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : memilih')
daftar_buku = ['1. Seven Habit','2. Blink', '3. First Thinks First', '4. Rich Dad']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : genap')
daftar_buku = ['1. Seven Habit','2. Blink', '3. First Thinks First', '4. Rich Dad']
print(daftar_buku[1::2])
