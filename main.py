# Inisialisasi list untuk menyimpan data Mahasiswa
data_mahasiswa = []

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    return nilai_akhir

# Perulangan untuk memasukkan data Mahasiswa
while True:
    # Meminta input data Mahasiswa
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    nilai_tugas = float(input("Masukkan Nilai Tugas: "))
    nilai_uts = float(input("Masukkan Nilai UTS: "))
    nilai_uas = float(input("Masukkan Nilai UAS: "))

    # Menghitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

    # Menambahkan data Mahasiswa ke dalam list
    data_mahasiswa.append({
        'Nama': nama,
        'NIM' : nim,
        'Tugas': nilai_tugas,
        'UTS': nilai_uts,
        'UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir
    })

    # Menanyakan apakah ingin menambahkan data lagi
    tanya = input("Tambahkan data lagi? (y/t): ")
    if tanya.lower() != 'y':

        break

# Menampilkan daftar data Mahasiswa
print("\nDaftar Data Mahasiswa:")
print("===================================================================")
print("  Nama\t\tNIM\tTugas\tUTS\tUAS\tNilai Akhir")
print("===================================================================")
for mahasiswa in data_mahasiswa:
    print(f"{mahasiswa['Nama']}\t\t{mahasiswa['NIM']}\t{mahasiswa['Tugas']}\t{mahasiswa['UTS']}\t{mahasiswa['UAS']}\t{mahasiswa['Nilai Akhir']}")

