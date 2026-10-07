import rendi as tentukan

murid = []

jumlah_siswa = int(input("Masukkan jumlah siswa: "))

for i in  range(jumlah_siswa):
    print(f"Murid ke {i+1}")

    nama = input("Nama: ")
    kelas = input("Kelas: ")
    nilai = int(input("Nilai: "))

    status_murid = tentukan.status(nilai)

    murids = {
       "nama": nama,
       "kelas": kelas,
       "nilai": nilai,
       "status": status_murid
    }

    murid.append(murids)

print(murid)
print("\n\n")

for w in murid:
   print(f"Nama: {w['nama']} | Kelas: {w['kelas']} | Nilai: {w['nilai']} | Status: {w['status']}")
