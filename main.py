def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    return nilai_akhir

def tampilkan_data(mahasiswa):
    print("\nDaftar Nilai Mahasiswa:")
    print("=============================================================================")
    print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10}".format("NIM", "Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"))
    print("=============================================================================")
    for nim, data in mahasiswa.items():
        print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10.2f}".format(nim, data['nama'], data['tugas'], data['uts'], data['uas'], data['nilai_akhir']))
    print("=============================================================================")

def tambah_data(mahasiswa):
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'nilai_akhir': nilai_akhir}
    print("Data mahasiswa berhasil ditambahkan!")

def ubah_data(mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang akan diubah datanya: ")
    if nim in mahasiswa:
        nama = input("Masukkan Nama baru: ")
        tugas = float(input("Masukkan Nilai Tugas baru: "))
        uts = float(input("Masukkan Nilai UTS baru: "))
        uas = float(input("Masukkan Nilai UAS baru: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

        mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'nilai_akhir': nilai_akhir}
        print("Data mahasiswa berhasil diubah!")
    else:
        print("NIM tidak ditemukan. Data tidak dapat diubah.")

def hapus_data(mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang akan dihapus datanya: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus!")
    else:
        print("NIM tidak ditemukan. Data tidak dapat dihapus.")

def cari_data(mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang akan dicari: ")
    if nim in mahasiswa:
        data = mahasiswa[nim]
        print("\nData Mahasiswa dengan NIM", nim)
        print("=============================================================================")
        print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10}".format("NIM", "Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"))
        print("=============================================================================")
        print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10.2f}".format(nim, data['nama'], data['tugas'], data['uts'], data['uas'], data['nilai_akhir']))
        print("=============================================================================")
    else:
        print("NIM tidak ditemukan.")

def main():
    mahasiswa = {}

    while True:
        print("\nMenu Pilihan:")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("5. Cari Data")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            tambah_data(mahasiswa)
        elif pilihan == '2':
            ubah_data(mahasiswa)
        elif pilihan == '3':
            hapus_data(mahasiswa)
        elif pilihan == '4':
            tampilkan_data(mahasiswa)
        elif pilihan == '5':
            cari_data(mahasiswa)
        elif pilihan == '0':
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__== "__main__":
    main()
    