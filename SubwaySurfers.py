class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties (nama, skor = 0, koin = 0, is_running = True)
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # TODO 2: Buat behavior agar karakter mulai berlari (cetak pesan dan ubah is_running menjadi True)
        print(f"{self.nama} mulai berlari. Karena {self.nama} Dikejar oleh wowok dan Sianjing")
        self.is_running = True

    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan jumlah koin ke properties koin dan berikan output informasi
        self.koin += jumlah
        print(f"{self.nama} mengambil {jumlah} koin. Total koin: {self.koin}")

    def tabrak_rintangan(self):
        # TODO 4: Jika menabrak rintangan, ubah is_running menjadi False dan cetak pesan game over
        self.is_running = False
        print(f"{self.nama} menabrak rintangan! Game Over. Kamu tertanggkap oleh wowok dan Sianjing.")

    def info_player(self):
        # TODO 5: Cetak status terkini (nama, skor, jumlah koin, dan status berlari)
        print(f"Nama: {self.nama}")
        print(f"Skor: {self.skor}")
        print(f"Koin: {self.koin}")
        print(f"Status Berlari: {'Ya' if self.is_running else 'Tidak'}")

# --- PENGUJIAN OBJEK ---
# Buat objek dengan nama variabel "player1" (misal: "Jake")
player1 = KarakterSurfer("Joko")
player1.info_player()
player1.berlari()
player1.ambil_koin(105)
player1.ambil_koin(190)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()