
# api.py
from flask import Flask, jsonify
from inventory_system import InventorySystem # Impor class Anda

# Buat aplikasi Flask
app = Flask(__name__)

# Buat instance dari sistem inventaris
sistem = InventorySystem()

# Buat endpoint (URL) untuk mendapatkan semua barang
@app.route('/api/barang', methods=['GET'])
def get_all_barang():
   # Ubah objek Barang menjadi dictionary agar bisa dijadikan JSON
   hasil = []
   for barang_objek in sistem.daftar_barang.values():
      hasil.append({
         "sku": barang_objek.sku,
         "nama": barang_objek.nama,
         "stok": barang_objek.stok,
         "harga": barang_objek.harga,
         "kategori": barang_objek.kategori
      })
   return jsonify(hasil)

# Jalankan servernya
if __name__ == '__main__':
   app.run(debug=True)