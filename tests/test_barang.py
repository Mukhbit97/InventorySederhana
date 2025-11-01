
# tests/test_barang.py
import pytest
import sys
import os
from pathlib import Path 

project_root = Path(__file__).parent.parent.resolve()
# Tambahkan path folder induk ke sys.path
sys.path.append(str(project_root))

# Sekarang Python tahu harus mencari di folder induk
from barang import Barang
from inventory_system import InventorySystem

def test_barang_creation():
   """Test apakah objek Barang bisa dibuat dengan benar."""
   barang = Barang("LPT001", "Laptop", 10, 15000000, "Elektronik")
   assert barang.sku == "LPT001"
   assert barang.nama == "Laptop"
   assert barang.stok == 10

def test_barang_jual_berhasil():
   """Test apakah method jual berhasil mengurangi stok."""
   barang = Barang("LPT001", "Laptop", 10, 15000000, "Elektronik")
   hasil = barang.jual(3)
   assert hasil is True # Method jual harus mengembalikan True jika berhasil
   assert barang.stok == 7

def test_barang_jual_gagal():
   """Test apakah method jual gagal jika stok tidak cukup."""
   barang = Barang("LPT001", "Laptop", 10, 15000000, "Elektronik")
   hasil = barang.jual(15)
   assert hasil is False # Method jual harus mengembalikan False jika gagal
   assert barang.stok == 10 # Stok tidak boleh berubah