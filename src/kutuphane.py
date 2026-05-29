from kitap import Kitap
from uye import Uye


class Kutuphane:
    """Kutuphane sisteminin ana islemlerini yonetir."""

    def __init__(self, veritabani):
        self.__veritabani = veritabani

    def kitap_ekle(self, kitap_no, ad, yazar):
        kitap = Kitap(kitap_no, ad, yazar)
        self.__veritabani.calistir(
            "INSERT INTO kitaplar (kitap_no, ad, yazar, odunc_alindi) VALUES (?, ?, ?, 0)",
            (kitap.no_getir(), kitap.ad_getir(), kitap.yazar_getir())
        )
        return "Kitap eklendi."

    def uye_ekle(self, uye_no, ad_soyad):
        uye = Uye(uye_no, ad_soyad)
        self.__veritabani.calistir(
            "INSERT INTO uyeler (uye_no, ad_soyad) VALUES (?, ?)",
            (uye.no_getir(), uye.ad_soyad_getir())
        )
        return "Uye eklendi."

    def kitaplari_listele(self):
        return self.__veritabani.liste_getir(
            "SELECT kitap_no, ad, yazar, odunc_alindi, alan_uye_no FROM kitaplar ORDER BY kitap_no"
        )

    def uyeleri_listele(self):
        return self.__veritabani.liste_getir(
            "SELECT uye_no, ad_soyad FROM uyeler ORDER BY uye_no"
        )

    def kitap_var_mi(self, kitap_no):
        sonuc = self.__veritabani.liste_getir(
            "SELECT kitap_no FROM kitaplar WHERE kitap_no = ?", (kitap_no,)
        )
        return len(sonuc) > 0

    def uye_var_mi(self, uye_no):
        sonuc = self.__veritabani.liste_getir(
            "SELECT uye_no FROM uyeler WHERE uye_no = ?", (uye_no,)
        )
        return len(sonuc) > 0

    def kitap_odunc_alindi_mi(self, kitap_no):
        sonuc = self.__veritabani.liste_getir(
            "SELECT odunc_alindi FROM kitaplar WHERE kitap_no = ?", (kitap_no,)
        )
        if not sonuc:
            raise ValueError("Kitap bulunamadi.")
        return sonuc[0][0] == 1

    def odunc_ver(self, kitap_no, uye_no):
        if not self.kitap_var_mi(kitap_no):
            raise ValueError("Kitap bulunamadi.")
        if not self.uye_var_mi(uye_no):
            raise ValueError("Uye bulunamadi.")
        if self.kitap_odunc_alindi_mi(kitap_no):
            raise ValueError("Kitap zaten odunc verilmis.")

        self.__veritabani.calistir(
            "UPDATE kitaplar SET odunc_alindi = 1, alan_uye_no = ? WHERE kitap_no = ?",
            (uye_no, kitap_no)
        )
        return "Kitap odunc verildi."

    def iade_al(self, kitap_no):
        if not self.kitap_var_mi(kitap_no):
            raise ValueError("Kitap bulunamadi.")
        if not self.kitap_odunc_alindi_mi(kitap_no):
            raise ValueError("Kitap zaten kutuphanede.")

        self.__veritabani.calistir(
            "UPDATE kitaplar SET odunc_alindi = 0, alan_uye_no = NULL WHERE kitap_no = ?",
            (kitap_no,)
        )
        return "Kitap iade alindi."
