import json
import os


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
        self.mevcutKullanici = {}

        self.loadUser()

    def loadUser(self):
        if os.path.exists('kullanıcılar.json'):
            with open('kullanıcılar.json', 'r', encoding='utf-8') as file:
                kullanicilar = json.load(file)
                for kullanici in kullanicilar:
                    kullanici = json.loads(kullanici)
                    yenikullanici = Kullanici(ad=kullanici['ad'], sifre=kullanici['sifre'], email=kullanici['email'],
                                              yas=kullanici['yas'])
                    self.kullanicilar.append(yenikullanici)
            print(self.kullanicilar)

    def kayit(self, kullanici: Kullanici):
        self.kullanicilar.append(kullanici)
        self.dosyayayazdirma()
        print('Kullanici Oluşturuldu')

    def giris(self, email, sifre):
        for kullanici in self.kullanicilar:
            if kullanici.ad == ad and kullanici.sifre == sifre == sifre:
                 self.isLoggedIn = True
                 self.mevcutKullanici = kullanici
                 print('giriş yapıldı')
                 break


    def dosyayayazdirma(self):
        list = []

        for kullanici in self.kullanicilar:
            list.append((json.dumps(kullanici.__dict__)))

        with open('kullanıcılar.json', 'w') as file:
            json.dump(list, file)

    def logout(self):
        self.isLoggedIn = False
        self.mevcutKullanici = {}
        print('çıkış yapıldı')

    def kimlik(self):
        if self.isLoggedIn:
            print(f'ad{self.mevcutKullanici.ad}')
        else:
            print('giriş yapılmadi')


yönet = Yönetici()

menu = lambda: print('Menü'.center(90)) or int(
    input('1-Üyelik Oluştur\n 2-Giriş Yap\n 3-Çıkış Yap\n 4-Kullanıcı Bilgileri\n 5-Çıkış Yap\n'))

secim = menu()
while True:

    if secim == 1:
        ad = input('İsminiz')
        sifre = input('Sifre Giriniz')
        email = input(' Mail giriniz')
        yas = input('Yaş Giriniz1')
        kullanici = Kullanici(ad=ad, sifre=sifre, email=email, yas=yas)
        yönet.kayit(kullanici)
        print(yönet.kullanicilar)

    elif secim == 2:
        ad = input('kullanici adi:')
        sifre = input('sifre: ')
        yönet.kayit(ad, sifre)
    elif secim == 3:
        yönet.logout()
        exit()
    elif secim == 4:
        yönet.kimlik()
        if yönet.isLoggedIn:
            print('zaten giriş yaptınız')
        else:
            print('zaten login oldunuz')
    elif secim == 5:
        # çıkış yapma işlemleri
        break
    else:
        print("Hatalı seçim yaptınız, lütfen tekrar deneyin.")
