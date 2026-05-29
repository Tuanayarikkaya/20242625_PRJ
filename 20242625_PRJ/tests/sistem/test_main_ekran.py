import os
import main as ana_program


def test_sayi_al_gecersiz_sonra_dogru(monkeypatch, capsys):
    girisler = iter(["abc", "0", "5"])
    monkeypatch.setattr("builtins.input", lambda mesaj: next(girisler))
    sonuc = ana_program.sayi_al("Sayi: ")
    assert sonuc == 5
    assert "Gecersiz giris" in capsys.readouterr().out


def test_menu_yazdir(capsys):
    ana_program.menu_yazdir()
    assert "KUTUPHANE SISTEMI" in capsys.readouterr().out


def test_liste_yazdirma_fonksiyonlari(capsys):
    ana_program.kitaplari_yazdir([])
    ana_program.uyeleri_yazdir([])
    ana_program.kitaplari_yazdir([(1, "Sefiller", "Victor Hugo", 0, None)])
    ana_program.uyeleri_yazdir([(1, "Ayse Yilmaz")])
    cikti = capsys.readouterr().out
    assert "Kayitli kitap yok" in cikti
    assert "Kayitli uye yok" in cikti
    assert "Sefiller" in cikti
    assert "Ayse Yilmaz" in cikti


def test_main_tum_menu_akisi(monkeypatch, tmp_path, capsys):
    os.mkdir(tmp_path / "data")
    monkeypatch.chdir(tmp_path)
    girisler = iter([
        "1", "1", "Sefiller", "Victor Hugo",
        "2", "1", "Ayse Yilmaz",
        "3",
        "4",
        "5", "1", "1",
        "6", "1",
        "9",
        "0"
    ])
    monkeypatch.setattr("builtins.input", lambda mesaj: next(girisler))
    ana_program.main()
    cikti = capsys.readouterr().out
    assert "Kitap eklendi" in cikti
    assert "Uye eklendi" in cikti
    assert "Kitap odunc verildi" in cikti
    assert "Kitap iade alindi" in cikti
    assert "Gecersiz secim" in cikti
