class Pelanggan:
  def __init__(self, nama, kontak):
    self.nama = nama
    self.kontak = kontak

  def info(self):
    return f"Nama: {self.nama} | Kontak: {self.kontak}"
