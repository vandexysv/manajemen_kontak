#program manajemen kontak
class Kontak:
   def __init__(self):
      self.kontak = []

   def melihat_kontak(self):
      # melihat semua kontak
      if self.kontak:
         for num, item in enumerate(self.kontak, 1):  # Mulai dari 1
             print(f'{num}. {item["nama"]} (HP: {item["HP"]}, Email: {item["email"]})')
      else:
         print("Kontak masih kosong!")
         return 1

   def menambah_kontak(self):
      nama = input("Masukkan nama kontak yang baru: ")
      hp = input("Masukkan nomor HP kontak yang baru: ")
      email = input("Masukkan email kontak yang baru: ")
      kontak_baru = {'nama': nama, 'HP': hp, 'email': email}
      self.kontak.append(kontak_baru)
      print("\nKontak baru berhasil ditambahkan!")

   def menghapus_kontak(self):
      if self.melihat_kontak() == 1:
         return
      try:
         i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
         if 1 <= i_hapus <= len(self.kontak):
            self.kontak.pop(i_hapus - 1)
            print("\nKontak berhasil dihapus!")
         else:
            print("\nNomor kontak tidak valid.")
      except ValueError:
         print("\nInput tidak valid, masukkan angka.")


kontak = Kontak()
kontak.kontak = [
   {'nama': "andi", 'HP': '109989303', 'email': 'Andi@python.com'},
   {'nama': "ani", 'HP': '129553030', 'email': 'Ani@python.com'}
]

while True:
   # program manajemen kontak
   print("\nMenu Kontak")
   print("1. Melihat semua kontak")
   print("2. Menambah kontak baru")
   print("3. Menghapus kontak")
   print("4. Keluar dari kontak")
   pilihan = input("Masukkan menu pilihan kontak (1, 2, 3, atau 4): ")

   if pilihan == '1':
      kontak.melihat_kontak()

   elif pilihan == '2':
      kontak.menambah_kontak()

   elif pilihan == '3':
      kontak.menghapus_kontak()

   elif pilihan == '4':
      # Keluar dari program
      print("\nKeluar dari program kontak.")
      break
   else:
      print("\nAnda memasukkan pilihan yang salah.")











