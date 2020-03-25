# Bankamatik Uygulaması

SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCekme(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        print("Paranızı alabilirsiniz")

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekkullanım = input("Paranız yetersiz, ek hesap kullanılsın mı? (e/h)? ")
            if ekkullanım == "e":
                print("paranızı alabilirsiniz")

            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print("yetrli bakiye yoktur.")

paraCekme(SadikHesap, 4000)


















# def paraCek(hesap, miktar):
#     print(f"Merhaba {hesap['ad']}")

#     if (hesap['bakiye'] >= miktar):
#         hesap['bakiye'] -= miktar 
#         print('paranızı alabilirsiniz.')
#         bakiyeSorgula(hesap)
#     else:
#         toplam = hesap['bakiye'] + hesap['ekHesap']

#         if (toplam >= miktar):
#             ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

#             if ekHesapKullanimi == 'e':
#                 ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
#                 hesap['bakiye'] = 0
#                 hesap['ekHesap'] -= ekhesapKullanilacakMiktar
#                 print('paranızı alabilirsiniz.')
#                 bakiyeSorgula(hesap)
#             else:
#                 print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
#         else:
#             print('üzgünüz bakiye yetersiz')
#             bakiyeSorgula(hesap)


# def bakiyeSorgula(hesap):
#     print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

# paraCek(SadikHesap, 3000)

# print('*****************')

# paraCek(SadikHesap, 2000)