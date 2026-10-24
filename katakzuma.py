class KatakZuma:
	def __init__(self, warna_awal):
		self.warna_peluru = warna_awal
		self.skor = 0
		self.is_active = True

	def ganti_warna(self, warna_baru):
		self.warna_peluru = warna_baru
		self.load_gambar(warna_baru)

	def load_gambar(self, warna):
		#mekanisme load gambar
		pass


	def tembak(self):
		if self.is_active:
			self.skor += 50

	def info_status(self):
		status = "Aktif" if self.is_active else "Tidak aktif"
		print(f"Warna peluru: {self.warna_peluru}")
		print(f"Skor: {self.skor}")
		print(f"Status: {status}")


# uji program
katak = KatakZuma("Merah")
katak.info_status()

katak.ganti_warna("Hijau")
katak.tembak()
katak.tembak()
katak.info_status()