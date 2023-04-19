import json


class Kullanici:
    def __init__(self, ad, sifre, email, yas):
        self.ad = ad
        self.sifre = sifre
        self.email = email
        self.yas = yas

class Yönetici:
    def __init__(self):
        self.kullanicilar = []
        self.isLoggedIn = False

        self.loadUser()

    def loadUser(self):
        # Implement this method to load user data from some data source
        # and use it to initialize the self.kullanicilar attribute.
        pass

    def kayit(self, kullanici: Kullanici):
        self.kullanicilar.append(kullanici)
        self.loadUser()
        print('Kullanici Oluşturuldu')

    def giris(self, email, sifre):
        # Implement this method to check if the given email and password
        # match a user in the self.kullanicilar list.
        pass

    def dosyayayazdirma(self):
        list=[]
        for kullanici in self.kullanicilar:
            list.append(json.dumps(kullanici.__dict__))

        with open('kullanıcılar.json','w') as file:
             json.dump(self.kullanicilar,file)


#while True:
 #   print('Menü'.center(90))
  #  menusecim = int(input('1-Üyelik Oluştur\n 2-Giriş Yap\n 3-Çıkış Yap 4-Kullanıcı Bilgileri 5-Çıkış Yap'))
   # break
yönet=Yönetici()
menu = lambda: print('Menü'.center(90)) or int(input('1-Üyelik Oluştur\n 2-Giriş Yap\n 3-Çıkış Yap\n 4-Kullanıcı Bilgileri\n 5-Çıkış Yap\n'))

secim = menu()
while True:

    if secim == 1:
        ad=input('İsminiz')
        sifre = input('Sifre Giriniz')
        email=input(' Mail giriniz')
        yas = input('Yaş Giriniz1')
        kullanici = Kullanici(ad=ad, sifre=sifre, email=email, yas=yas)
        yönet.kayit(kullanici)
        print(yönet.kullanicilar)

    elif secim == 2:
       pass # giriş yapma işlemleri
    elif secim == 3:
        pass# çıkış yapma işlemleri
        exit()
    elif secim == 4:
        pass# kullanıcı bilgilerini gösterme işlemleri
    elif secim == 5:
        # çıkış yapma işlemleri
        break
    else:
        print("Hatalı seçim yaptınız, lütfen tekrar deneyin.")


