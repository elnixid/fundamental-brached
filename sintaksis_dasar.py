"""
Sekuensial : langkah berurutan
Percabangan : langkah melompat ke kondisi yang terpenuhi
Pengulangan : mengulah langkah yang sama berkali-kali selama kondisi terpenuhi

"""

# Sekuensial
print("Ibu berkata kepada anak : Tolong sebotol susu")
print("Anak menjawab : Siap")
print("Anak pergi ke toko")
print("Anak mengecek apakah ada susu")
print("Ibu bertanya : Bila ada telur beli enam")
print("Anak membeli sebotol susu")
print("Anak menyerahkan hasil belanja nya ke Ibu")

# Pecabangan
jumlah_botol_susu = 173
jumlah_telur = 1034

print(f"Jumlah susu : {jumlah_botol_susu} botol")
# print(f"Jumlah telur : {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Anak mengecek harga dan uangnya cukup")
    if jumlah_telur == 0:
        print("Anak beli sebotol susu")
    else:
        print(f"Jumlah telur yang ada : {jumlah_telur} butir")
        print("Anak beli sebotol susu dan enam telur")
else:
    print("Anak tidak jadi beli susu")

print("Anak pulang ke rumah")
print("Menyampaikan barangnya ke Ibu")


