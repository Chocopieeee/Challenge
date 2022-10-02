print ('Challenge 2')
print ('Elsa Indriani')
print ('PYTN-KS10-013')
def Terbilang(bil):
    angka = [" ","Satu","Dua","Tiga","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bil)
    if n>= 0 and n <= 11:
        return angka[n]
    elif n <20:
        return Terbilang (n-10) + " Belas "
    elif n <100:
        return Terbilang (n/10) + " Puluh " + Terbilang (n%10)
    else:
        return "Angka Hanya Sampai Sembilan puluh sembilan"

while(True):
    number = input('Masukan angka(0-99): ')
    if(int(number)==0):
        print('nol')
    else:
        angka_terbilang = Terbilang(number)
        print(angka_terbilang)