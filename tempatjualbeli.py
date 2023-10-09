
from prettytable import PrettyTable
import sys


#Fungsi setiap tahap

def login():
    username = str(input("Username : "))
    password = int(input("Masukkan Password : "))
    if (username == "azriel" and password == 1311) :
        menu_pilihan_admin()
    else :
        input(" username/password salah! Untuk Kembali. Tekan Enter" )

menu_sayuran = [["Tomat",8000],["Bayam",3000],["Kangkung",3000],["Sawi",4000],["Wortel",12000],["Kentang",20000]]

def tampilkan_barang():
    table = PrettyTable()
    table.title = "Daftar Barang"
    table.field_names = ["No","Nama Sayuran", "Harga Sayuran/kg"]
    for i in range(len(menu_sayuran)):
        table.add_row([i+1, menu_sayuran[i][0], "Rp. " + str(menu_sayuran[i][1]),])
    print(table)
    
def customer():
    while True:
        tampilkan_barang()
        barang_pilihan = int(input("\nMasukkan sayur pilihan anda : "))
        barang = menu_sayuran[barang_pilihan-1]
        uang = int(input("Masukkan Jumlah Uang Anda : "))
        if uang >=0 :
            input("\nTerimakasih :) . ")
        else :
            input("Uang anda kurang")

    


def menu_pilihan_admin():
    while True:
        print("Menu Admin")
        print("1. Tambah sayur")
        print("2. Tampilkan sayur")
        print("3. Edit sayur")
        print("4. Hapus sayur")
        print("5. Kembali nih?")
        pilihan = int(input("Masukkan Angka Pilihan anda: "))
        
# Cabang Pilihan        
        if  pilihan == 1:
            tampilkan_barang()
            nama_sayuran = str(input("Masukkan nama sayur : "))
            harga_sayur = str(input("\nMasukkan harga sayur : "))
            sayur = [nama_sayuran, harga_sayur]
            menu_sayuran.append(sayur)
            tampilkan_barang()
            input("sayur Berhasil Ditambahkan. Tekan ENTER Untuk Kembali. ")

        elif pilihan == 2:
            tampilkan_barang()

        elif pilihan == 3:
            tampilkan_barang()
            no_edit = int(input("Nomor Berapa Yang Ingin Diubah : "))
            nama_sayur = str(input("Masukkan nama sayur yang ingin dijual : "))
            harga_sayur = str(input("Masukkan harga sayuran yang ingin dijual : "))
            barang = [nama_sayur, harga_sayur]
            menu_sayuran[no_edit-1] = barang
            tampilkan_barang()
            input("Sayuran Berhasil Diubah. Tekan ENTER Untuk Kembali. ")

        elif pilihan == 4:
            tampilkan_barang()
            no_hapus = int(input("Nomor Berapa Yang Ingin Dihapus : "))
            menu_sayuran.pop(no_hapus-1)
            tampilkan_barang()
            input("Sayuran Berhasil Dihapus. Tekan ENTER Untuk Kembali. ")
            
        elif pilihan == 5:
            break
            
while True:
        print("Menu")
        print("1. Admin")
        print("2. Customer")
        print("3. Keluar nih?")
        bagian_login = int(input("Masukkan Pilihan Anda (1/2/3) : "))

        if bagian_login == 1: 
            login()
        elif bagian_login == 2: 
            customer()
        elif bagian_login == 3:
            sys.exit()