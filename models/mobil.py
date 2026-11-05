from . import Kendaraan


class Mobil(Kendaraan):
    def __init__(self, kode: str, seri: str, tahun: int, brand: str, tipe_bahan_bakar: str, status_bekas: bool, harga: int, jumlah_kursi: int):
        super().__init__(kode, seri, tahun, brand, tipe_bahan_bakar, status_bekas, harga)
        self.jumlah_kursi = jumlah_kursi

    def info(self) -> str:
        return f"Mobil | {super().info()} | Jumlah kursi: {self.jumlah_kursi}"

    def harga_jual(self) -> int:
        return super().harga_jual()
