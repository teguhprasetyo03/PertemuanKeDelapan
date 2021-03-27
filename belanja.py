total_belanja = int(input('Total Belanja : '))

bayar = total_belanja

# jika barang belanjaan yang di beli lebih dari 100 ribu akan mendapatkan diskon
if total_belanja > 100000:
    print("Kamu Mendapatkan bonus minuman dingin")
    print("Dan Diskon Sebesar 5%")
elif total_belanja < 100000:
    print("Tidak Mendapatkan diskon")

    # hitung diskon
    diskon = total_belanja * 5/100
    bayar = total_belanja - diskon

    # cetak struk
    print("Total yang harus dibayar : Rp %s " %bayar)
    print("Terimakasih telah berbelanja")
    print("Silahkan datang kembali")