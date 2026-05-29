class Varlik:
    """Sistemdeki ortak nesneler icin temel sinif."""

    def __init__(self, no):
        if no <= 0:
            raise ValueError("Numara 0'dan buyuk olmalidir.")
        self._no = no

    def no_getir(self):
        return self._no
