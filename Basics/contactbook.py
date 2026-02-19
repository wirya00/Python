contact = {}

name_contact = input('Masukkan nama: ')
alamat_contact = input('Masukkan alamat: ')
nomor_contact = input('Masukkan nomor: ')
email_contact = input('Masukkan email: ')

name_contact = name_contact.lower()

contact[name_contact] = {}

contact[name_contact]['Nama'] = name_contact
contact[name_contact]['Alamat'] = alamat_contact
contact[name_contact]['Nomor hp'] = nomor_contact
contact[name_contact]['Email'] = email_contact


cari = input('Kontak siapa yang ingin anda cari? ')
cari = cari.lower()

if cari in contact:
    data = contact[cari].copy()
    data['Nama'] = data['Nama'].capitalize()
    print(data)
else:
    print('Tidak ada kontak tersebut.')