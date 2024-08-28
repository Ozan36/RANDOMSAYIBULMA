#random sınıfını dahil etme
import random 
# değişken içerisine randinti atama
rand=random.randint(1,21) 
sayac=0
while True:
    sayac+=1
    #kullanıcıdan girdi alma
    sayi=int(input("sayi giriniz:"))
    # karar yapıları
    if sayi==rand: 
        print(f"tebrikler sayıyı {sayac} . denemede buldunuz:")
        break
    # karar yapıları
    elif sayi>rand:
        print("daha küçük değer giriniz:")
        continue
    # karar yapıları
    else: 
        print("daya büyük değer giriniz:")
        continue
#random içindeki belirli bir nesne, modül, sınıf veya fonksiyon hakkında ayrıntılı bilgi sağlar.
help(random)
#Bu komut, belirli bir nesnenin veya modülün niteliklerini (değişkenler, fonksiyonlar, sınıflar vb.) listeler.
# #Genellikle bir nesneyle neler yapabileceğinizi anlamak için kullanılır.
random.__dir__()

