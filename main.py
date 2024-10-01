#program manajemen kontak

def melihat_kontak():
#melihat semua kontak
   if kontak:
      for num, item in enumerate(kontak, 1):  # Mulai dari 1
          print(f'{num}. {item["nama"]} (HP: {item["HP"]}, Email: {item["email"]})')

   else:
      print("kontak masih kosong!")
      return 1


def menambah_kontak():
   nama = input("Masukkan nama kontak yang baru: ")
   hp = input("Masukkan nomor HP kontak yang baru: ")
   email = input("Masukkan email kontak yang baru: ")
   kontak_baru = {'nama': nama, 'HP': hp, 'email': email}
   kontak.append(kontak_baru)
   print("\nKontak baru berhasil ditambahkan!")

def menghapus_kontak():
      if melihat_kontak()== '1'
         retrun
      i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
      melihat_kontak()
   except ValueError:
      print("\nInput tidak valid, masukkan angka.")

kontak1 = {'nama': "andi", 'HP': '109989303', 'email': 'Andi@python.com'}
kontak2 = {'nama': "ani", 'HP': '129553030', 'email': 'Ani@python.com'}
kontak = [kontak1, kontak2]

while True:
   # "program manajemen kontak"
   print("\nMenu Kontak")
   print("1. Melihat semua kontak")
   print("2. Menambah kontak baru")
   print("3. Menghapus kontak")
   print("4. Keluar dari kontak")
   pilihan = input("Masukkan menu pilihan kontak (1, 2, 3, atau 4): ")

   if pilihan == '1':
      Melihat_kontak()


   elif pilihan == '2':
      Menambah_kontak()


   elif pilihan == '3':
      Menghapus_kontak()


   elif pilihan == '4':
      # Keluar dari program
      print("\nKeluar dari program kontak.")
      break
   else:
      print("\nAnda memasukkan pilihan yang salah.")











