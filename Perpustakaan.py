class Buku:
    def __init__(self, judul, penulis, tahun_terbit, stok):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.stok = stok

    def info_buku(self):
        print("--- INFORMASI BUKU ---")
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Stok: {self.stok}")
        print("----------------------")

    def pinjam_buku(self, jumlah, nama_peminjam):
        if self.stok >= jumlah:
            self.stok -= jumlah
            print(f"Buku '{self.judul}' berhasil dipinjam oleh {nama_peminjam}. Sisa stok: {self.stok}")
        else:
            print(f"Buku '{self.judul}' tidak tersedia untuk dipinjam. karena stok hanya tersisa {self.stok}")

    def kembalikan_buku(self, jumlah_dipinjam, jumlah_dikembalikan, nama_peminjam):
        self.stok += jumlah_dikembalikan
        if jumlah_dikembalikan < jumlah_dipinjam:
            sisa_pinjam = jumlah_dipinjam - jumlah_dikembalikan
            print(f"{nama_peminjam} mengembalikan buku {self.judul} berjumlah {jumlah_dikembalikan}. Masih ada {sisa_pinjam} buku yang belum dikembalikan.")
        else:
            print(f"{nama_peminjam} sudah mengembalikan semua buku {self.judul} berjumlah {jumlah_dikembalikan}.")

        print(f"Buku '{self.judul}' sudahd ikembalikan oleh {nama_peminjam}. Stok tersedia: {self.stok}")

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        print(f"Stok buku '{self.judul}' berhasil ditambahkan. Stok sekarang: {self.stok}")



#uji coba
buku1 = Buku("Jokowi : Pemimpin Rakyat Berjiwa Rocker", "Yon Thayrun", 2012, 19)
buku2 = Buku("Siksa Neraka", " MB. Rahimsyah (MB. Rahimsyah AR)", 1970, 7)


buku1.info_buku()
buku1.pinjam_buku(2, "Andy")
buku1.pinjam_buku(4, "Supri")
buku1.pinjam_buku(15, "Buming")
buku1.kembalikan_buku(2, 1, "Andy")
buku1.tambah_stok(3)

buku2.info_buku()
buku2.pinjam_buku(3, "Buming")
buku2.pinjam_buku(5, "Kaesang")
buku2.kembalikan_buku(3, 3, "Buming")
buku2.tambah_stok(5)