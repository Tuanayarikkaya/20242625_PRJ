import pytest
from kutuphane import Kutuphane
from veritabani import Veritabani


def test_sistem_senaryosu_kitap_ekle_uye_ekle_odunc_ver_iade_al(tmp_path):
    kutuphane = Kutuphane(Veritabani(str(tmp_path / "test.db")))
    kutuphane.kitap_ekle(1, "Sefiller", "Victor Hugo")
    kutuphane.uye_ekle(1, "Ayse Yilmaz")
    assert kutuphane.odunc_ver(1, 1) == "Kitap odunc verildi."
    assert kutuphane.iade_al(1) == "Kitap iade alindi."


def test_sistem_senaryosu_gecersiz_islem_engellenir(tmp_path):
    kutuphane = Kutuphane(Veritabani(str(tmp_path / "test.db")))
    kutuphane.kitap_ekle(1, "Sefiller", "Victor Hugo")
    with pytest.raises(ValueError):
        kutuphane.odunc_ver(1, 99)
