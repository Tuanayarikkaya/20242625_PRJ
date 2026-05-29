from varlik import Varlik


class Uye(Varlik):
    """Kutuphane uyesi bilgilerini tutar."""

    def __init__(self, uye_no, ad_soyad):
        super().__init__(uye_no)
        if not ad_soyad.strip():
            raise ValueError("Uye adi bos olamaz.")
        self.__ad_soyad = ad_soyad.strip()

    def ad_soyad_getir(self):
        return self.__ad_soyad
