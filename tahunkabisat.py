print('Membuat Program Menentukan Tahun Kabisat')

tahun = int(input('Masukkan tahun :'))

if tahun % 400 == 0:
    print('{ } merupakan tahun kabisat'.format(tahun))
elif tahun % 100 == 0:
    print('{ } bukan merupakan tahun kabisat'.format(tahun))
elif tahun % 4 == 0:
    print('{ } merupakan tahun kabisat'.format(tahun))
else:
    print('{ } bukan merupakan tahun kabisat'.format(tahun))