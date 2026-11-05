def valid_kode(kode: str) -> bool:
    return isinstance(kode, str) and len(kode.strip()) > 0

def valid_jumlah(jumlah: int) -> bool:
    return isinstance(jumlah, int) and jumlah > 0

def valid_harga(harga: (int, float)) -> bool:
    return isinstance(harga, (int, float)) and harga > 0

def valid_kontak(kontak: str) -> bool:
    return isinstance(kontak, str) and len(kontak.strip()) >= 5
