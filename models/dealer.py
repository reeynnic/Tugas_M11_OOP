import kendaraan

class Dealer:
  def __init__(self, nama, stok=None):
    self.nama = nama
    self.stok = list(stok or kendaraan)

  def total_kendaraan(self):
    return len(self.stok)

  def nama_dealer(self):
    return self.nama

  def tambah_kendaraan(self, kendaraan):
    self.stok.append(kendaraan)