from . import Kendaraan

class Motor(Kendaraan):
    def info(self):
        return f"Motor | {super().info()}"

    def harga_jual(self):
        return super().harga_jual()
