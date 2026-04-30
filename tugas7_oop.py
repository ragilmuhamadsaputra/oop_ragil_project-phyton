#Meminta input dari pengguna dalam satuan Kbps
kbps= float(input("masukkan jaringan mbps: "))
mbps = kbps/1000


if mbps >= 50:
   kategori ="sangat cepat "
elif mbps >= 20:
   kategori ="cepat"
elif mbps >= 5:
   kategori ="lambat"
else:
   kategori = "Kurang( - Memerlukan perbaikan"
   
#Menampilkan hasil Keputus
print("hasil evaluasi :",kategori)