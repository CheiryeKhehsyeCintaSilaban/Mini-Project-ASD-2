class Node:
    def __init__(self, id_gereja, nama, alamat, tahun_berdiri):
        self.id_gereja = id_gereja
        self.nama = nama
        self.alamat = alamat
        self.tahun_berdiri = tahun_berdiri
        self.next = None

class GerejaLinkedList:
    def __init__(self):
        self.head = None

    def create_data(self, id_gereja, nama, alamat, tahun_berdiri):
        new_node = Node(id_gereja, nama, alamat, tahun_berdiri)
        new_node.next = self.head
        self.head = new_node
        print(f'Data gereja dengan ID {id_gereja} berhasil ditambahkan.')

    def read_data(self, id_gereja=None):
        current = self.head

        if id_gereja:
            while current:
                if current.id_gereja == id_gereja:
                    print(f'Data gereja dengan ID {id_gereja}:')
                    print(f'ID Gereja: {current.id_gereja}')
                    print(f'Nama: {current.nama}')
                    print(f'Alamat: {current.alamat}')
                    print(f'Tahun Berdiri: {current.tahun_berdiri}')
                    return
                current = current.next
            print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')
        else:
            print('Data seluruh gereja:')
            while current:
                print(f'ID Gereja: {current.id_gereja}')
                print(f'Nama: {current.nama}')
                print(f'Alamat: {current.alamat}')
                print(f'Tahun Berdiri: {current.tahun_berdiri}')
                print()
                current = current.next

    def update_data(self, id_gereja, field, value):
        current = self.head

        while current:
            if current.id_gereja == id_gereja:
                if hasattr(current, field):
                    setattr(current, field, value)
                    print(f'Data {field} gereja dengan ID {id_gereja} berhasil diperbarui.')
                    return
                else:
                    print(f'Field {field} tidak valid.')
                    return
            current = current.next

        print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')

    def delete_data(self):
        if self.head:
            deleted_node = self.head
            self.head = self.head.next
            print(f'Data gereja dengan ID {deleted_node.id_gereja} berhasil dihapus.')
        else:
            print('Tidak ada data gereja untuk dihapus.')


def main():
    gereja_list = GerejaLinkedList()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Gereja")
        print("2. Tampilkan Data Gereja")
        print("3. Perbarui Data Gereja")
        print("4. Hapus Data Gereja")
        print("5. Keluar")

        pilihan = input("Silakan masukkan pilihan anda: ")

        if pilihan == '1':
            id_gereja = input("Masukkan ID gereja: ")
            nama = input("Masukkan nama gereja: ")
            alamat = input("Masukkan alamat lengkap gereja: ")
            tahun_berdiri = input("Masukkan tahun berdiri gereja tersebut: ")
            gereja_list.create_data(id_gereja, nama, alamat, tahun_berdiri)

        elif pilihan == '2':
            id_gereja = input("Masukkan ID Gereja untuk menampilkan produk (kosongkan untuk semua): ")
            gereja_list.read_data(id_gereja)

        elif pilihan == '3':
            id_gereja = input("Masukkan ID Gereja: ")
            field = input("Masukkan Nama Field yang Ingin Diperbarui: ")
            value = input("Masukkan Nilai Baru: ")
            gereja_list.update_data(id_gereja, field, value)

        elif pilihan == '4':
            gereja_list.delete_data()

        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih ulang")


if __name__ == "__main__":
    main()
