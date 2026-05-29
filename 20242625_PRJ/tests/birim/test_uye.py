import pytest
from uye import Uye


def test_uye_olusturma():
    uye = Uye(1, "Ayse Yilmaz")
    assert uye.no_getir() == 1
    assert uye.ad_soyad_getir() == "Ayse Yilmaz"


def test_uye_adi_bos_olamaz():
    with pytest.raises(ValueError):
        Uye(1, "")


def test_uye_no_pozitif_olmali():
    with pytest.raises(ValueError):
        Uye(-1, "Ayse Yilmaz")
