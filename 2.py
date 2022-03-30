'''
Nama  : Tria Suci Cahyani
NIM   : 20051397054
Kelas : 2020B
'''

def createStack():
  stack = []
  return stack

def size(stack):
  return len(stack)

def isEmpty(stack):
  if size(stack) == 0:
    return True

def clear(stack):
  return stack.clear()

def push(stack, item):
  stack.append(item)

def pop(stack):
  return stack.pop()
  
def decimalToBinary(angka):
  stack = createStack()
  resConversion = ''
  storeBilDec = angka
  while angka > 0:
    push(stack, angka % 2)
    angka = angka // 2
  while isEmpty(stack) != True:
    resConversion = resConversion + str(pop(stack))
  txt = f"Hasil konversi bilangan desimal {storeBilDec} ke bilangan biner adalah {resConversion}"
  return txt

def decimalToOctal(angka):
  stack = createStack()
  resConversion = ''
  storeBilDec = angka
  while angka > 0:
    push(stack, angka % 8)
    angka = angka // 8
  while isEmpty(stack) != True:
    resConversion = resConversion + str(pop(stack))
  txt = f"Hasil konversi bilangan desimal {storeBilDec} ke bilangan oktal adalah {resConversion}"
  return txt

def decimalToHexadecimal(angka):
  stack = createStack()
  conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
  storeBilDec = angka
  resConversion = ''
  while angka > 0:
    push(stack, angka % 16)
    angka = angka // 16
  while isEmpty(stack) != True:
    resConversion = str(conversion_table[pop(stack)] + resConversion)
  resConversion = resConversion[::-1]
  txt = f"Hasil konversi bilangan desimal {storeBilDec} ke bilangan hexadesimal adalah {resConversion}"
  return txt

def main():
  cobaLagi = True
  while cobaLagi == True:
    print('---- Program Mengkonversi Bilangan Desimal ke Biner, Oktal, dan Hexadesimal ----')
    bilDesimal = input("Masukkan Bilangan Desimal: ")
    if bilDesimal:
      if bilDesimal.isnumeric():
        bilDesimal = int(bilDesimal)
        print(decimalToBinary(bilDesimal))
        print(decimalToOctal(bilDesimal))
        print(decimalToHexadecimal(bilDesimal))
        reconfirm = True
        while reconfirm == True:
          print('\n--- Pilihan ---')
          print('1. Program akan dijalankan kembali')
          print('2. Program akan diakhiri')
          konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
          if konfirmasi == '1':
            print("Baik, program dijalankan kembali\n")
            reconfirm = False
            cobaLagi = True
          elif konfirmasi == '2':
            print('Program diakhiri. Sekian, terima kasih\n')
            reconfirm = cobaLagi = False
          else:
            print('* Peringatan *')
            print(f'Mohon maaf, pilihan {konfirmasi} tidak tersedia')
            print('Mohon ketik dengan pilihan yang tersedia\n')
            reconfirm = True
      else:
        print('* Peringatan *')
        print('Bilangan desimal harus diisi dengan angka')
        print('Program dijalankan kembali\n')
    else:
      print('* Peringatan *')
      print('Bilangan desimal tidak boleh kosong')
      print('Program dijalankan kembali\n')

main()
