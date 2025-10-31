
# file: barang.py

class Barang:
   # Konstruktor: dijalankan saat kita membuat objek Barang baru
   def __init__(self, sku, nama, stok, harga, kategori):
      self.sku = sku
      self.nama = nama
      self.stok = stok
      self.harga = harga
      self.kategori = kategori

   # Method ini hanya menampilkan info dari SATU objek Barang
   def tampilkan_info(self, nomor=None):
      # nomor adalah parameter opsional untuk menampilkan nomor urut
      if nomor:
         print(f"{nomor}. ", end="")
         print(f"SKU : {self.sku}")
         print(f"     Nama : {self.nama}")
         print(f"     stok : {self.stok}")
         print(f"     harga : {self.harga:,.2f}")
         print(f"     kategori : {self.kategori}")
         print("-" * 25)
      else:
         print("Barang Masih Kosong")

   def jual(self, jumlah):
      if self.stok >= jumlah:
         self.stok -= jumlah
         return True # berhasil jual
      else:
         return False # gagal jual

