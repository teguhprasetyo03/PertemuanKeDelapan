print('Program Menentukan Nilai Indeks Mahasiswa')

nilai_tugas = float(input('\n Masukkan Nilai Tugas : '))
nilai_uts = float(input('\n Masukkan Nilai UTS : '))
nilai_uas =float(input('\n Masukkan Nilai UAS : '))

# rumus menghitung nilai akhir = (0.15 * nilaitugas) + (0.35 * uts) + (0.50 * uas)
nilai_akhir = (0.15 * nilai_tugas) + (0.35*nilai_uts) + (0.50 * nilai_uas)

if nilai_akhir >= 80:
    indeks = 'A'
elif nilai_akhir >= 70:
    indeks = 'B'
elif nilai_akhir >= 55:
    indeks = 'C'
elif nilai_akhir >= 40:
    indeks = 'D'
else :
    indeks = 'E'

print('Nilai Akhir = %0.2f' %nilai_akhir )
print('Indeks Grade adalah = %c' % indeks)



