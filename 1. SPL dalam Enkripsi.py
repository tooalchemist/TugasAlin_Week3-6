def encrypt(z):
    return (z * 2 - 2) 
def decrypt(z):
    return ((z + 2) / 2)

again = 'y'
while again == 'y':
    menu = int(input("Pilih Mana?\n1. Encrypt\n2. Decrypt\nPilih : "))

    if(menu == 1):
        x = str(input('Pesan yang ingin di enkripsi\n: '))
        y = []
        for i in x:
            z = ord(i)
            y.append(encrypt(z))
        print("Hasil Enkripsi:",*y,sep=' ',)

    elif(menu == 2):
        x = str(input('Kode yang sudah di Enkripsi\n: '))
        y = []
        x = x.split(' ')
        for i in x:
            z = int(i)
            y.append(chr(int((decrypt(z)))))
        print("Hasil Dekripsi: ",*y,sep='')     
    else:
        break   

    again = input('Again? (y/n): ')





