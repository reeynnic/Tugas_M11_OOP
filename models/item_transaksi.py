class ItemTransaksi:
  def __init__(self, kendaraan, jumlah):
    self.kendaraan = kendaraan
    self.jumlah = jumlah

  def info(self):
    return f"{self.kendaraan.info()} | Jumlah: {self.jumlah} | Subtotal: Rp{self.subtotal():,}"

  def subtotal(self):
    return self.kendaraan.harga_jual() * self.jumlah