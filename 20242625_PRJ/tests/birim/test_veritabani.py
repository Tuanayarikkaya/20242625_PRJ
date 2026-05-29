from veritabani import Veritabani


def test_veritabani_tablo_olusturur(tmp_path):
    db_yolu = tmp_path / "test.db"
    veritabani = Veritabani(str(db_yolu))
    tablolar = veritabani.liste_getir("SELECT name FROM sqlite_master WHERE type='table'")
    tablo_adlari = [tablo[0] for tablo in tablolar]
    assert "kitaplar" in tablo_adlari
    assert "uyeler" in tablo_adlari


def test_veritabani_kitap_kaydi_ekler(tmp_path):
    db_yolu = tmp_path / "test.db"
    veritabani = Veritabani(str(db_yolu))
    veritabani.calistir(
        "INSERT INTO kitaplar (kitap_no, ad, yazar, odunc_alindi) VALUES (?, ?, ?, 0)",
        (1, "Sefiller", "Victor Hugo")
    )
    sonuc = veritabani.liste_getir("SELECT ad FROM kitaplar WHERE kitap_no = 1")
    assert sonuc[0][0] == "Sefiller"
