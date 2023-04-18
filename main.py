class kullanici:
    def __init__(self,ad,sifre,email,yas):
        self.ad=ad
        self.sifre=sifre
        self.email=email
        self.yas=yas


class yönetici:
    def __init__(self):
        self.kullanicil=[]
        self.isLoggedIn=False
        self.mevcut={}


        self.loadUser()

    def loadUser(self):
        pass

    def kayıt(self,kullanicil:kullanici):
        self.kullanicil.append(kullanici)
        self.loadUser()
        print('Kullanici Oluşturuldu')
        pass

    def giriş(self):
        pass

    def kayitoluştur(self):
        pass


#while True:
 #   print('Menü'.center(90))
  #  menusecim = int(input('1-Üyelik Oluştur\n 2-Giriş Yap\n 3-Çıkış Yap 4-Kullanıcı Bilgileri 5-Çıkış Yap'))
   # break

menu = lambda: print('Menü'.center(90)) or int(input('1-Üyelik Oluştur\n 2-Giriş Yap\n 3-Çıkış Yap\n 4-Kullanıcı Bilgileri\n 5-Çıkış Yap\n'))

while True:
    secim = menu()
    if secim == 1:
        username=input('Kullanici Adi')
        username = input('Kullanici Adi')
        username=input('Kullanici Adi')

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


