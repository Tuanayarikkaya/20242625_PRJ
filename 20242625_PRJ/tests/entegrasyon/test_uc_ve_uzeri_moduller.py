from kutuphane import Kutuphane
from veritabani import Veritabani


def test_kitap_odunc_verme_uc_modul(tmp_path):
    kutuphane = Kutuphane(Veritabani(str(tmp_path / "test.db")))
    kutuphane.kitap_ekle(1, "Sefiller", "Victor Hugo")
    kutuphane.uye_ekle(1, "Ayse Yilmaz")
    kutuphane.odunc_ver(1, 1)
    assert kutuphane.kitap_odunc_alindi_mi(1) is True


def test_kitap_iade_alma_uc_modul(tmp_path):
    kutuphane = Kutuphane(Veritabani(str(tmp_path / "test.db")))
    kutuphane.kitap_ekle(1, "Sefiller", "Victor Hugo")
    kutuphane.uye_ekle(1, "Ayse Yilmaz")
    kutuphane.odunc_ver(1, 1)
    kutuphane.iade_al(1)
    assert kutuphane.kitap_odunc_alindi_mi(1) is False
