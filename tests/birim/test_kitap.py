import pytest
from kitap import Kitap


def test_kitap_olusturma():
    kitap = Kitap(1, "Sefiller", "Victor Hugo")
    assert kitap.no_getir() == 1
    assert kitap.ad_getir() == "Sefiller"
    assert kitap.yazar_getir() == "Victor Hugo"


def test_kitap_adi_bos_olamaz():
    with pytest.raises(ValueError):
        Kitap(1, "", "Yazar")


def test_kitap_no_pozitif_olmali():
    with pytest.raises(ValueError):
        Kitap(0, "Kitap", "Yazar")


def test_kitap_odunc_verme():
    kitap = Kitap(1, "Sefiller", "Victor Hugo")
    kitap.odunc_ver()
    assert kitap.odunc_durumu_getir() is True


def test_kitap_iade_alma():
    kitap = Kitap(1, "Sefiller", "Victor Hugo")
    kitap.odunc_ver()
    kitap.iade_al()
    assert kitap.odunc_durumu_getir() is False
