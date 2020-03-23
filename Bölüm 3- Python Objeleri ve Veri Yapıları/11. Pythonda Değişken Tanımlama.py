print(5000-(5000*0.27))

# 3650.0

maasAli = 5000
maasAhmet = 4000
vergi=0.27

print(maasAli-maasAli*vergi)
print(maasAhmet-maasAhmet*vergi)

# 3650.0
# 4000

#değişkeler rakam ile başlayamaz
# büyük-küçük harf duyarlıdır
# türkçe karakter kullanılmaz

x = 1            #int
y = 2.0          #float
name = "Çınar"   #string
isStudent = True #bool

print(type(x))         # <class 'int'>
print(type(y))         # <class 'float'>
print(type(name))      # <class 'string'> 
print(type(isStudent)) # <class 'bool'>

#Pythonda ayrı satırlarda yapılan değişken tanımlaması aynı satırda da yapılabilir;

x, y, name, isStudent = 1, 2.3, 'Çınar', True

#string birleştirme + ile yapılırsa arka arkaya yazar
a = "50"             # sayısal olarak 50 değeri tanımladık
b = "50"             # sözel (string) olarak 50 değeri tanımladık.
print(a + b)         # a + b' nin sonucu 5050 olur.