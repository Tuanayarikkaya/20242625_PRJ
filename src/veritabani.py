import sqlite3


class Veritabani:
    """SQLite veritabani islemlerini yapar."""

    def __init__(self, dosya_yolu):
        self.__dosya_yolu = dosya_yolu
        self.tablo_olustur()

    def baglanti_ac(self):
        return sqlite3.connect(self.__dosya_yolu)

    def tablo_olustur(self):
        baglanti = None
        try:
            baglanti = self.baglanti_ac()
            imlec = baglanti.cursor()
            imlec.execute("""
                CREATE TABLE IF NOT EXISTS kitaplar (
                    kitap_no INTEGER PRIMARY KEY,
                    ad TEXT NOT NULL,
                    yazar TEXT NOT NULL,
                    odunc_alindi INTEGER NOT NULL DEFAULT 0,
                    alan_uye_no INTEGER
                )
            """)
            imlec.execute("""
                CREATE TABLE IF NOT EXISTS uyeler (
                    uye_no INTEGER PRIMARY KEY,
                    ad_soyad TEXT NOT NULL
                )
            """)
            baglanti.commit()
        except sqlite3.Error as hata:
            raise RuntimeError("Veritabani tablolari olusturulamadi.") from hata
        finally:
            if baglanti is not None:
                baglanti.close()

    def calistir(self, sorgu, parametreler=()):
        baglanti = None
        try:
            baglanti = self.baglanti_ac()
            imlec = baglanti.cursor()
            imlec.execute(sorgu, parametreler)
            baglanti.commit()
        except sqlite3.Error as hata:
            raise RuntimeError("Veritabani islemi basarisiz oldu.") from hata
        finally:
            if baglanti is not None:
                baglanti.close()

    def liste_getir(self, sorgu, parametreler=()):
        baglanti = None
        try:
            baglanti = self.baglanti_ac()
            imlec = baglanti.cursor()
            imlec.execute(sorgu, parametreler)
            return imlec.fetchall()
        except sqlite3.Error as hata:
            raise RuntimeError("Veritabani okuma islemi basarisiz oldu.") from hata
        finally:
            if baglanti is not None:
                baglanti.close()
