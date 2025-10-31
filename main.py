
from inventory_system import *
from barang import *

def main():
   # Buat SATU objek InventorySystem untuk seluruh aplikasi
   sistem_inventaris = InventorySystem()

   while True:
      print("\n--- Pilihan Menu Inventory ---")
      print("1. Tambah Data Barang")
      print("2. Lihat Daftar Barang")
      print("3. Jual Barang")
      print("4. Hapus Barang")
      print("5. Update Barang")
      print("6. Keluar")

      try:
         perintah = int(input("Masukkan pilihan menu anda: "))

         if perintah == 1:
            # Panggil method dari objek sistem_inventaris
            sistem_inventaris.tambah_barang()
         elif perintah == 2:
            sistem_inventaris.lihat_inventory()
         elif perintah == 3:
            sistem_inventaris.jual_barang()
         elif perintah == 4:
            sistem_inventaris.hapus_barang()
         elif perintah == 5:
            sistem_inventaris.update_barang()
         elif perintah == 6:
            sistem_inventaris.simpan_data()
            print("Terima kasih, sampai jumpa!")
            break
         else:
            print("Pilihan tidak valid.")
      except ValueError:
         print("Input yang anda masukkan salah.")

# Jalankan program utama
if __name__ == "__main__":
   main()

