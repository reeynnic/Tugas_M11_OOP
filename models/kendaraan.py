from abc import ABC, abstractmethod

class Kendaraan(ABC):
  kode = 0

  def __init__(self, seri, tahun, brand, tipe_bahan_bakar, status_bekas, harga):
    self.seri = seri
    self.tahun = tahun
    self.brand = brand
    self.tipe_bahan_bakar = tipe_bahan_bakar
    self.status_bekas = status_bekas
    self.harga = harga
    kode += 1

  def info(self) -> str:
    return f"Seri: {self.seri}\nTahun: {self.tahun}\nBrand: {self.brand}\nBahan Bakar: {self.tipe_bahan_bakar}\nBekas: {self.status_bekas}\nHarga: {self.harga}\n"

  @abstractmethod
  def harga_jual(self) -> int:
    pass