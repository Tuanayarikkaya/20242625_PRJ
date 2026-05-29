from kutuphane import Kutuphane
from veritabani import Veritabani
from kitap import Kitap
from uye import Uye


def test_kutuphane_veritabani_kitap_ekleme(tmp_path):
    kutuphane = Kutuphane(Veritabani(str(tmp_path / "test.db")))
    kutuphane.kitap_ekle(1, "Sefiller", "Victor Hugo")
    assert len(kutuphane.kitaplari_listele()) == 1


def test_kutuphane_veritabani_uye_ekleme(tmp_path):
    kutuphane = Kutuphane(Veritabani(str(tmp_path / "test.db")))
    kutuphane.uye_ekle(1, "Ayse Yilmaz")
    assert len(kutuphane.uyeleri_listele()) == 1


def test_kitap_ve_uye_siniflari_birlikte_kullanilir():
    kitap = Kitap(1, "Sefiller", "Victor Hugo")
    uye = Uye(1, "Ayse Yilmaz")
    assert kitap.no_getir() == uye.no_getir()
