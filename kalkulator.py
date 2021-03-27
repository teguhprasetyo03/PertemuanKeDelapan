print('Membuat Kalkulator Dengan Python')

print('1. Pembagian')
print('2. Perkalian')
print('3. Penjumlahan')
print('4. Pengurangan')

pil = int(input('\nMasukkan Pilihan Operasi :'))

x = int(input('Masukkan Bilangan 1 : '))
y = int(input('Masukkan Bilangan 2 : '))

if pil == 1:
    result = x/y
elif pil == 2:
    result = x*y
elif pil == 3:
    result = x+y
elif pil == 4:
    result = x-y

print('Hasil : %d' %result)
