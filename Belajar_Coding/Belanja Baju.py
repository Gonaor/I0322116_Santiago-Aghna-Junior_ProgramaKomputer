#input
print("---------------")
print("Happy Shopping")
print("Struk Belanja Deep Store")
print("Tokan Takon Ora Tuku Rasah Moro")
Harga_Baju = int(input('Masukkan Harga Baju : '))
Total_Belanja = int(input('Jumlah : '))
Total_Harga = 0
Discount = 0
Total_Harga = Total_Belanja*Harga_Baju-Discount
if Harga_Baju > 100.000 :
    Discount = Total_Harga * 10/100.000
Jumlah_Pembayaran = Total_Harga-Discount

#proses perhitungan harga
a = Harga_Baju
b = Total_Belanja
c = Discount
d = Jumlah_Pembayaran

#total harga
print("---------------")
print('Harga Baju :', a)
print('Total Belanja :', b)
print('Discount :', c)
print('Jumlah Pembayaran :', d)
print('Terimakasih Atas Kunjungan Anda')
print('Berbelanjalah Selalu Menggunakan Pinjol')
print('Tutor Programma Komputer')
