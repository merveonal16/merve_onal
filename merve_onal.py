import os

"""
f = open("dosya2.txt","r")
data = f.read()
words = data.split()
data = data.replace(" ", "")
print("Dosyadaki kelime sayısı: ", len(words))
print("Dosyadaki karakter sayısı: ", len(data))
f.close()
"""

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Merhaba Dünya \n')
        print(filename, "adlı dosya oluşturma başarılı")
    except IOError:
        print("Dosya oluşturulamadı")


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            icerik = f.read()
            print(icerik)
    except IOError:
        print("Dosya okunamadı")


def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
            print(filename, "adlı dosyaya veri ekleme başarılı")
    except IOError:
        print("Dosyaya veri eklenemedi")


def delete_file(filename):
    try:
        os.remove(filename)
        print(filename, 'adlı dosya silindi')
    except IOError:
        print("Dosya silinemedi")


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print(filename, 'adlı dosya', new_filename, "adlı dosya oldu")
    except IOError:
        print("Dosyaya yeniden adlandırılamadı")


yapilacak_is = input("Dosya okumak için (r)\nDosya oluşturmak için (c)\nDosya silmek için (d)\nDosya adı değiştirmek için (m) \nDosyaya ekleme için (e)\nSeçenek Seçin: ")
if yapilacak_is == 'c':
    filename = input("Dosya adını girin: ")
    create_file(filename)
elif yapilacak_is == 'd':
    filename = input("Silinecek dosyanın adını girin: ")
    delete_file(filename)
elif yapilacak_is == 'e':
    filename = input("Veri eklemek için dosya adını girin: ")
    metin = input("Eklenecek metni girin: ")
    append_file(filename, metin)
elif yapilacak_is == 'm':
    filename = input("Dosya adını girin: ")
    new_filename = input("Yeni dosya adını girin: ")
    rename_file(filename, new_filename)
elif yapilacak_is == 'r':
    filename = input("Dosya adını girin: ")
    read_file(filename)
