class Kendaraan:
    def __init__(self, kode: str, seri: str, tahun: int, brand: str, tipe_bahan_bakar: str, status_bekas: bool, harga: int):
        self.kode = kode
        self.seri = seri
        self.tahun = tahun
        self.brand = brand
        self.tipe_bahan_bakar = tipe_bahan_bakar
        self.status_bekas = status_bekas
        self.harga = harga

    def info(self):
        kondisi = "Bekas" if self.status_bekas else "Baru"
        return f"{self.kode} - {self.brand} {self.seri} ({self.tahun}) | Bahan bakar: {self.tipe_bahan_bakar} | Kondisi: {kondisi} | Harga: Rp{self.harga:,}"

    def harga_jual(self):
        return self.harga


class Dealer:
    def __init__(self, nama: str, stok=None):
        self.nama = nama
        self.stok = list(stok or [])

    def total_kendaraan(self):
        return len(self.stok)

    def nama_garasi(self):
        return self.nama

    def tambah_kendaraan(self, kendaraan: Kendaraan):
        self.stok.append(kendaraan)


class Pelanggan:
    def __init__(self, nama: str, kontak: str):
        self.nama = nama
        self.kontak = kontak

    def info(self):
        return f"Nama: {self.nama} | Kontak: {self.kontak}"


class ItemTransaksi:
    def __init__(self, kendaraan: Kendaraan, jumlah: int):
        self.kendaraan = kendaraan
        self.jumlah = jumlah

    def info(self):
        return f"{self.kendaraan.info()} | Jumlah: {self.jumlah} | Subtotal: Rp{self.subtotal():,}"

    def subtotal(self):
        return self.kendaraan.harga_jual() * self.jumlah


class Transaksi:
    def __init__(self, kode: str, tanggal: int, pelanggan: Pelanggan, dealer: Dealer, daftar_item=None):
        self.kode = kode
        self.tanggal = tanggal
        self.pelanggan = pelanggan
        self.dealer = dealer
        self.daftar_item = list(daftar_item or [])

    def info(self):
        detail_item = "\n".join(item.info() for item in self.daftar_item)
        return f"Transaksi: {self.kode} | Tanggal: {self.tanggal} | Pelanggan: {self.pelanggan.nama} | Dealer: {self.dealer.nama} | Total: Rp{self.total_harga():,}\n{detail_item}"

    def total_harga(self):
        return sum(item.subtotal() for item in self.daftar_item)

    def tambah_item(self, item: ItemTransaksi):
        self.daftar_item.append(item)


from .mobil import Mobil
from .motor import Motor

__all__ = ["Kendaraan", "Dealer", "Pelanggan", "ItemTransaksi", "Transaksi", "Mobil", "Motor"]
