#contoh sturuktur pencabangan if
#input data dari penggunaa
nilai_ujian = float(input("masukan nilai ujian siswa: "))

#struktur kontrol pencabangan majemuk 
if nilai_ujian >=90:
   predikat = "sangat baik (A)"

elif nilai_ujian >=75:
   prediksi= "Baik (B)"

elif nilai_ujian >=60:
   predikat = "Cukup (C)"
   
else:
   predikat = "kurang (D) - memerlukan remedial"
   
#menampilkan hasil keputusan 
print("hasil evaluasi",predikat)
   