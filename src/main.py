from kutuphane import Kutuphane
from veritabani import Veritabani


def sayi_al(mesaj):
    while True:
        try:
            sayi = int(input(mesaj))
            if sayi <= 0:
                print("Lutfen 0'dan buyuk bir sayi giriniz.")
                continue
            return sayi
        except ValueError:
            print("Gecersiz giris. Lutfen sayi giriniz.")


def menu_yazdir():
    print("\n--- KUTUPHANE SISTEMI ---")
    print("1- Kitap ekle")
    print("2- Uye ekle")
    print("3- Kitaplari listele")
    print("4- Uyeleri listele")
    print("5- Kitap odunc ver")
    print("6- Kitap iade al")
    print("0- Cikis")


def kitaplari_yazdir(kitaplar):
    if not kitaplar:
        print("Kayitli kitap yok.")
        return
    for kitap in kitaplar:
        durum = "Oduncte" if kitap[3] == 1 else "Kutuphanede"
        print(f"No: {kitap[0]} | Ad: {kitap[1]} | Yazar: {kitap[2]} | Durum: {durum}")


def uyeleri_yazdir(uyeler):
    if not uyeler:
        print("Kayitli uye yok.")
        return
    for uye in uyeler:
        print(f"No: {uye[0]} | Ad Soyad: {uye[1]}")


def main():
    veritabani = Veritabani("../database/kutuphane.db")
    kutuphane = Kutuphane(veritabani)

    while True:
        menu_yazdir()
        secim = input("Seciminiz: ")

        try:
            if secim == "1":
                kitap_no = sayi_al("Kitap no: ")
                ad = input("Kitap adi: ")
                yazar = input("Yazar: ")
                print(kutuphane.kitap_ekle(kitap_no, ad, yazar))
            elif secim == "2":
                uye_no = sayi_al("Uye no: ")
                ad_soyad = input("Uye ad soyad: ")
                print(kutuphane.uye_ekle(uye_no, ad_soyad))
            elif secim == "3":
                kitaplari_yazdir(kutuphane.kitaplari_listele())
            elif secim == "4":
                uyeleri_yazdir(kutuphane.uyeleri_listele())
            elif secim == "5":
                kitap_no = sayi_al("Odunc verilecek kitap no: ")
                uye_no = sayi_al("Uye no: ")
                print(kutuphane.odunc_ver(kitap_no, uye_no))
            elif secim == "6":
                kitap_no = sayi_al("Iade edilecek kitap no: ")
                print(kutuphane.iade_al(kitap_no))
            elif secim == "0":
                print("Program kapatildi.")
                break
            else:
                print("Gecersiz secim.")
        except ValueError as hata:
            print(f"Hata: {hata}")
        except RuntimeError as hata:
            print(f"Sistem hatasi: {hata}")


if __name__ == "__main__":
    main()
