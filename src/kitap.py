from varlik import Varlik


class Kitap(Varlik):
    """Kutuphane sistemindeki kitap bilgilerini tutar."""

    def __init__(self, kitap_no, ad, yazar):
        super().__init__(kitap_no)
        if not ad.strip() or not yazar.strip():
            raise ValueError("Kitap adi ve yazar bos olamaz.")
        self.__ad = ad.strip()
        self.__yazar = yazar.strip()
        self.__odunc_alindi = False

    def ad_getir(self):
        return self.__ad

    def yazar_getir(self):
        return self.__yazar

    def odunc_durumu_getir(self):
        return self.__odunc_alindi

    def odunc_ver(self):
        if self.__odunc_alindi:
            raise ValueError("Bu kitap zaten odunc alinmis.")
        self.__odunc_alindi = True

    def iade_al(self):
        if not self.__odunc_alindi:
            raise ValueError("Bu kitap zaten kutuphanede.")
        self.__odunc_alindi = False
