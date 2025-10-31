from barang import *
import json 
from pathlib import Path

class InventorySystem:
   # Konstruktor: dijalankan saat kita membuat sistem inventaris baru
   def __init__(self, nama_file="inventory.json"):
      # Dapatkan direktori di mana file script ini (inventory_system.py) berada
      script_dir = Path(__file__).parent.resolve()

      # Gabungkan direktori script dengan nama file untuk membuat path absolut
      self.nama_file = script_dir / nama_file

      # Ini adalah koleksi dari semua objek Barang
      self.daftar_barang = {} # Key: SKU, Value: objek Barang
      self.kategori = set()
      self.riwayat = []

      print(f"Menggunakan file data: {self.nama_file}") # Opsional: untuk debugging
      self.muat_data()

   def muat_data(self):
      """Memuat data dari file JSON ke dalam memori."""
      try:
         with open(self.nama_file, 'r') as file:
            data = json.load(file)
            # data adalah list of dictionary
            for item_dict in data:
               # Buat objek Barang dari setiap dictionary
               barang_objek = Barang(
                  sku=item_dict['sku'],
                  nama=item_dict['nama'],
                  stok=item_dict['stok'],
                  harga=item_dict['harga'],
                  kategori=item_dict['kategori']
               )
               # Masukkan objek ke dalam daftar_barang
               self.daftar_barang[barang_objek.sku] = barang_objek
               self.kategori.add(barang_objek.kategori)
         print(f"Data berhasil dimuat dari {self.nama_file}")
      except FileNotFoundError:
         print(f"File {self.nama_file} tidak ditemukan. Memulai dengan inventory kosong.")
      except json.JSONDecodeError:
         print(f"File {self.nama_file} rusak atau kosong. Memulai dengan inventory kosong.")

   def simpan_data(self):
      """Menyimpan data dari memori ke file JSON."""
      # Siapkan list kosong untuk menampung data
      data_yang_akan_disimpan = []
      
      # Konversi objek Barang menjadi dictionary
      for barang_objek in self.daftar_barang.values():
         data_dict = {
            "sku": barang_objek.sku,
            "nama": barang_objek.nama,
            "stok": barang_objek.stok,
            "harga": barang_objek.harga,
            "kategori": barang_objek.kategori
         }
         data_yang_akan_disimpan.append(data_dict)
         
      # Tulis list of dictionary ke file JSON
      with open(self.nama_file, 'w') as file:
         json.dump(data_yang_akan_disimpan, file, indent=4) # indent=4 agar rapi
      
      print(f"Data berhasil disimpan ke {self.nama_file}")

   def lihat_inventory(self):
      print("\n --- Lihat Inventory ---")
      # Cek apakah dictionary daftar_barang kosong
      if not self.daftar_barang:
         print("maaf, inventory masih kosong")
         return
      
      # Loop untuk setiap objek Barang di dalam dictionary
      # enumerate digunakan untuk memberi nomor urut
      for i, (sku, barang_objek) in enumerate(self.daftar_barang.items(), 1):
         # Untuk setiap objek, panggil method tampilkan_info() miliknya
         barang_objek.tampilkan_info(i)

   # --- Method untuk MENAMBAH barang ---
   def tambah_barang(self):
      print("\n --- Tambah Barang ---")
      try:
         sku = input("Masukkan SKU Barang : ")
         # cek apakah SKU sudah ada!!!
         if sku in self.daftar_barang:
            print(f"Barang dengan SKU {sku} sudah ada!")
            return
         
         nama = input("Masukan nama barang : ")
         stok = int(input("Masukkan stok barang: "))
         harga = float(input("Masukkan harga barang: "))
         kategori_input = input("Masukkan kategori barang: ")

         # Buat OBJEK Barang dari input user
         barang_baru = Barang(sku, nama, stok, harga, kategori_input)

         # Tambahkan objek tersebut ke dalam daftar
         self.daftar_barang[sku] = barang_baru
         self.kategori.add(kategori_input)

         print(f"Barang {nama} berhasil di tambahkan")

      except ValueError:
         print("\nError: Stok dan Harga harus berupa angka.")

   def jual_barang(self):
      print("\n--- Jual Barang ---")
      try:
         sku_jual = input("Masukkan kode SKU: ")
         jumlah_jual = int(input("Masukkan jumlah barang: "))

         if sku_jual in self.daftar_barang:
            # Ambil objek barang yang akan dijual
            barang_dijual = self.daftar_barang[sku_jual]

            # Panggil method jual() dari objek tersebut
            if barang_dijual.jual(jumlah_jual):
               print(f"Berhasil menjual {jumlah_jual} unit '{barang_dijual.nama}'. Sisa stok: {barang_dijual.stok}")

               # Tambahkan ke riwayat
               self.riwayat.append({"tipe": "jual", "sku": sku_jual, "jumlah": jumlah_jual})

            else:
               print(f"Gagal! Stok tidak mencukupi. Sisa: {barang_dijual.stok}")
         else:
            print(f"Barang dengan SKU '{sku_jual}' tidak ditemukan.")
      except ValueError:
         print("Input yang anda masukkan salah.")

   def hapus_barang(self):
      print("\n --- Hapus Data Barang ---")
      if not self.daftar_barang:
         print("Data barang Masih Kosong")
         return
      
      try:
         cari_barang = input("Masukan kode SKU : ")

         if cari_barang in self.daftar_barang:
            self.daftar_barang.pop(cari_barang)
            print(f"Data Barang {cari_barang} Berhasil di hapus")
      except ValueError:
         print("Data BArang yang di masukkan tidak ada")

   # di dalam file inventory_system.py

   def update_barang(self):
      print("\n--- Update Data Barang ---")
      try:
         cari_barang = input("Masukkan Kode barang yang ingin di update: ")
         
         if cari_barang in self.daftar_barang:
            # Ambil objek yang akan diupdate untuk mempermudah akses
            barang_objek = self.daftar_barang[cari_barang]
            
            print(f"Data barang Kode SKU :{cari_barang} ditemukan")
            # Tampilkan info saat ini dengan method milik objek
            barang_objek.tampilkan_info()

            print("\nApa yang ingin diupdate?")
            print("1. ubah SKU")
            print("2. ubah nama dan Kategori")
            print("3. ubah stok barang")
            print("4. ubah harga barang")
            print("5. ubah semuanya")
            pilihan_update = int(input("Masukan Pilihan anda: "))

            if pilihan_update == 1:
               sku_baru = input("Masukkan SKU baru: ")
               if sku_baru != cari_barang:
                  # Pindahkan objek ke key baru
                  self.daftar_barang[sku_baru] = barang_objek
                  # Hapus key lama
                  del self.daftar_barang[cari_barang]
                  # Update attribute SKU di dalam objek
                  barang_objek.sku = sku_baru
                  print("SKU berhasil diperbaharui")

            elif pilihan_update == 2:
               nama_baru = input("Masukkan nama baru: ")
               kategori_baru = input("masukkan kategori baru: ")
               
               # --- PERBAIKAN: Gunakan titik (.) untuk mengubah attribute objek ---
               barang_objek.nama = nama_baru
               barang_objek.kategori = kategori_baru
               self.kategori.add(kategori_baru)
               print("Nama dan Kategori berhasil diperbaharui")

            elif pilihan_update == 3:
               stok_baru = int(input("Masukkan Stok Baru: "))
               # --- PERBAIKAN ---
               barang_objek.stok = stok_baru
               print("berhasil update stok")

            elif pilihan_update == 4:
               harga_baru = float(input("Masukkan harga Baru: "))
               # --- PERBAIKAN ---
               barang_objek.harga = harga_baru
               print("berhasil update harga")

            elif pilihan_update == 5:
               # Update semua attribute objek terlebih dahulu
               sku_update = input("Masukkan SKU baru: ")
               nama_update = input("Masukkan nama baru: ")
               stok_update = int(input("Masukkan Stok Baru: "))
               harga_update = float(input("Masukkan harga Baru: ")) # Saya ubah ke float
               kategori_update = input("masukkan kategori baru: ")

               # --- PERBAIKAN: Update attribute objek, bukan buat dictionary baru ---
               barang_objek.sku = sku_update
               barang_objek.nama = nama_update
               barang_objek.stok = stok_update
               barang_objek.harga = harga_update
               barang_objek.kategori = kategori_update
               
               # Jika SKU berubah, pindahkan objek ke key baru
               if sku_update != cari_barang:
                  self.daftar_barang[sku_update] = barang_objek
                  del self.daftar_barang[cari_barang]
               
               self.kategori.add(kategori_update)
               print("Semua data berhasil diupdate!")
            else:
               print("pilihan yang anda masukkan salah")
         else:
            print(f"Barang dengan SKU {cari_barang} tidak ditemukan")
      except ValueError:
         print("Data Yang anda input salah")

