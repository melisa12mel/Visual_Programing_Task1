class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Input Data Diri Kalian
mel = Mahasiswa("Melisa Putri Dwi Anggari", "B", "Pendidikan Komputer", "FKIP", "Perjuangan 7", "Kukar"
)

# Menampilkan informasi mahasiswa
print(f"Nama: {mel.nama}")
print(f"Kelas: {mel.kelas}")
print(f"Prodi: {mel.prodi}")
print(f"Fakultas: {mel.fakultas}")
print(f"Tempat Tinggal: {mel.tempat_tinggal}")
print(f"Asal: {mel.asal}")

