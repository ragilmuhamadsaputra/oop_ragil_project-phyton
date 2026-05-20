
#Contoh WHILE Sistem pengisian baterai laptop
#yang akan terus berjalan selama daya belum mencapai 100%. 
daya = 90
while daya < 100:
  print("Mengisi daya.. posisi:", daya, "%") 
  daya += 2 # Menambah daya setiap putaran
print("Baterai Penuh!")
