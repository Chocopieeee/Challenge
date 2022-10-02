#PYTN-KS10-013
#Elsa Indriani

import random

angka = random.randint(0,9)
skorawal = 100
percobaan = 0
salah = 3
print("**********************************************")
print("**************GAME TEBAK ANGKA****************")
print("**********************************************")
print("Saya memikirkan angka dari 0-9")
print("Silakan tebak angka yang saya pikirkan")
print("Input harus berupa angka!!!")
print("Skor kamu 100!")
while salah > 0:
  while True:
      try:
        data = int(input("Silakan masukkan tebakkanmu : "))
      except ValueError:
        percobaan += 1
        skorawal -= 20
        salah -= 1
        print("Tebakan harus angka!")
        print("Pinalty! skor dikurangi 20!")
        print(f"skor kamu saat ini {skorawal}")
        print(f"sisa {salah} kali percobaan salah!")
        continue
      else:
        break
  if data == angka:
    percobaan += 1
    print('KAMU MENANG!')
    print(f"skor kamu {skorawal} !!!")
    print(f"percobaan ke {percobaan} !!!")
    break
  else:
    percobaan += 1
    skorawal -= 10
    salah -= 1
    print(
      'Tebakanmu terlalu',
      'kecil' if data < angka else 'besar')
    print(f"sisa {salah} kali percobaan salah!")
    print(f"Skor kamu {skorawal}!")
else:
  print('GAME OVER')