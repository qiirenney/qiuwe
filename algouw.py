# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:53:08 2024

@author: Qirana
"""

class Data:
    def __init__(self, nama="", nilai=0):  # Perbaikan pada __init__
        self.__nama = nama
        self.__nilai = nilai

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai):
        self.__nilai = nilai


def menu():
    print("\n===== Program OOP =====")
    print("1. Menambahkan Objek")
    print("2. Menampilkan Objek")
    print("3. Mengubah Nilai Objek")
    print("4. Menghapus Objek")
    print("5. Keluar Dari Program")
    pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): ")
    return pilihan


data_list = []

while True:
    pilihan = menu()
    if pilihan == "1":
        nama = input("Masukkan Nama: ")
        nilai = int(input("Masukkan Nilai: "))
        obj = Data(nama, nilai)
        data_list.append(obj)
        print("Data Berhasil Ditambahkan")
    elif pilihan == "2":
        if data_list:
            print("\n===== Data Objek =====")
            for i, obj in enumerate(data_list):
                print(f"{i + 1}. Nama: {obj.get_nama()}, Nilai: {obj.get_nilai()}")
        else:
            print("Tidak Ada Data Untuk Ditampilkan")
    elif pilihan == "3":
        if data_list:
            print("\n===== Data Objek =====")
            for i, obj in enumerate(data_list):
                print(f"{i + 1}. Nama: {obj.get_nama()}, Nilai: {obj.get_nilai()}")
            indeks = int(input("Masukkan Nomor Objek yang Akan Diubah: ")) - 1
            if 0 <= indeks < len(data_list):
                nama_baru = input("Masukkan Nama Baru: ")
                nilai_baru = int(input("Masukkan Nilai Baru: "))
                data_list[indeks].set_nama(nama_baru)
                data_list[indeks].set_nilai(nilai_baru)
                print("Data Berhasil Diubah")
            else:
                print("Nomor Objek Tidak Valid")
        else:
            print("Tidak Ada Data Untuk Diubah")
    elif pilihan == "4":
        if data_list:
            print("\n===== Data Objek =====")
            for i, obj in enumerate(data_list):
                print(f"{i + 1}. Nama: {obj.get_nama()}, Nilai: {obj.get_nilai()}")
            indeks = int(input("Masukkan Nomor Objek yang Akan Dihapus: ")) - 1
            if 0 <= indeks < len(data_list):
                data_list.pop(indeks)
                print("Data Berhasil Dihapus")
            else:
                print("Nomor Objek Tidak Valid")
        else:
            print("Tidak Ada Data Untuk Dihapus")
    elif pilihan == "5":
        print("Keluar Dari Program. Terima Kasih!")
        break
    else:
        print("Pilihan Tidak Valid, Silakan Coba Lagi")
