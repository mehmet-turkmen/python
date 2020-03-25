# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

# def yazdir(kelime, adet):
#     print(kelime * adet)

# yazdir('Merhaba\n', 10)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyeCevir(10,20,30,'Merhaba')

# print(result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalSayılariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))

# asalSayılariBul(sayi1, sayi2)



# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.


def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    
    return tamBolenler


print(tamBolenleriBul(20))


# def yazdır():
#     kelime = input("Kelimeyi giriniz: ")
#     adet = int(input("Kaç kere yazdırılsın: "))
#     n=0
#     while n < adet:
#         print(kelime)

#         n+=1

# yazdır()
 
#****************kendi yazdığım kodlar****************************************
# def makeList(*params):
#     liste = []

#     for eleman in params:
#         liste.append(eleman)

#     return liste

# print(makeList(10,20,50,123,"klsdfjdf","jklsdfkldf"))

#********************************************************

# def asalBul(sayı1, sayı2):
#     for sayi in range(sayı1, sayı2+1):
#         for i in range(2,sayi):
#             if sayi % i == 0:
#                 break
#         else:
#             print(sayi)


# asalBul(1,100)

#********************************************************

def tamBolen():
    sayi = int(input("Lütfen bir sayı giriniz: "))
    
    n = []
    for x in range(1,sayi+1):
        if sayi % x == 0:
            n.append(x)
        else:
            continue
    
    print(n)

tamBolen()

#********************************************************