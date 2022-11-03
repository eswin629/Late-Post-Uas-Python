#Nama:Nico Velix Sinambela 14S19016
#Nama:Julifer Mauliate Siahaan 14S19017
#Nama:Frans Wesly Sagala 14S19018

class Manusia:
    def __init__(self, Nama, umur, jenis_kelamin,penyakit):
        self.Nama = Nama
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin
        self.penyakit = penyakit

class Dokter:
    def __init__(self):
        self.Daftar_fix_dirawat=[]
        self.kulit_dan_kelamin=0
        self.bagian_dalam=0
        self.umum=0
        self.jantung=0
    def daftarlanjut(self,yang_dirawat):
        if yang_dirawat.penyakit=='kulit_dan_kelam':
            yang_dirawat.nodaftar=int('1'+'0'*(3-len(str(self.kulit_dan_kelamin+1)))+str(self.kulit_dan_kelamin+1))
            self.kulit_dan_kelamin+=1
            self.jantung+=1
        elif yang_dirawat.penyakit=='bagian_dalam':
            yang_dirawat.nodaftar=int('2'+'0'*(3-len(str(self.bagian_dalam+1)))+str(self.bagian_dalam+1))
            self.bagian_dalam+=1
        elif yang_dirawat.penyakit=='umum':
            yang_dirawat.nodaftar=int('3'+'0'*(3-len(str(self.umum+1)))+str(umum+1))
        elif yang_dirawat.penyakit=='jantung':
            yang_dirawat.nodaftar=int('4'+'0'*(3-len(str(self.jantung+1)))+str(self.jantung+1))
            self.umum+=1
        print('Name :',yang_dirawat.Nama)
        print('No pendaftaran :',yang_dirawat.nodaftar)
        print('umur :',yang_dirawat.umur)
        print('jenis kelamin :',yang_dirawat.jenis_kelamin)
        print('penyakit:',yang_dirawat.penyakit)
        print('\n Thank you,\n')
        self.Daftar_fix_dirawat.append(yang_dirawat)
        return yang_dirawat.nodaftar

class yang_dirawat(Manusia):
    def __init__(self,Nama, umur, jenis_kelamin, penyakit):
        super().__init__(Nama, umur, jenis_kelamin,penyakit)
        self.valid=False
        self.nodaftar=None
    def Cek_Ruangan (self):

        if 1001 <= self.nodaftar <= 1030 :
            print("Pasien sakit kulit dan kelamin")
            print("Ruang untuk pasien, Ruang 1\n")
        elif 1031 <= self.nodaftar <= 1060 :
            print("Pasien sakit kulit dan kelamin")
            print("Ruang untuk pasien, Lantai 1, Ruang 2\n")

        elif 2001 <= self.nodaftar <= 2030:
            print("pasien penyakit umum")
            print("Ruang untuk pasien, Lantai 1, Ruang 3\n")
        elif 2031 <= self.nodaftar <= 2060:
            print("pasien penyakit umum")
            print("Ruang untuk pasien, Lantai 1, Ruang 4\n")


        elif 3001 <= self.nodaftar <= 3030:
            print("pasien penyakit jantung")
            print("Ruang Ujian : Gd 9, Lantai 2, Ruang 1\n")
        elif 3031 <= self.nodaftar <= 3060:
            print("pasien penyakit jantung")
            print("Ruang untuk pasien, Lantai 2, Ruang 2\n")

        elif 4001 <= self.nodaftar <= 4030:
            print("Pasien penyakit bagian dalam")
            print("Ruang untuk pasien, Lantai 2, Ruang 3\n")
        elif 4031 <= self.nodaftar <= 4060:
            print("Pasien penyait bagian dalam")
            print("Ruang untuk pasien, Lantai 2, Ruang 4\n")

loop = True
DAFTAR_pasien=list()
Dokter=Dokter()

while (loop):
    print('\nSelamat Datang pasien rumah sakit')
    print('Silahkan Anda Pilih Menu Pilihan Anda\n')
    print('ini menu nya ya')
    print('1. Daftar untuk data diri dan penyakit')
    print('2. Daftar Ulang pasien')
    print('3. Cek Ruangan')
    print('4. Keluar')
    print('\n')
    menu = input('Masukan Menu Pilihan = ')

    if menu == "1":
        Nama = input("Masukkan Nama : ")
        umur = input("Masukkan umur : ")
        jenis_kelamin = input("Masukkan jenis kelamin : ")
        penyakit = input("Masukkan penyakit : ")
        daftar_dirawat = yang_dirawat(Nama, umur,jenis_kelamin, penyakit)
        DAFTAR_pasien.append(daftar_dirawat)
        print("\nSilahkan daftar  kepada perawat 1 hari sebelum dirawat mulai\n")

    elif menu == "2":
        jumlah_pasien = int(input("Masukkan jumlah pasien: "))
        for i in range(jumlah_pasien):
            print('')
            print("Check Nama Pasien ke-" + str(i + 1) + " :")
            Nama = input("Nama : ")
            print('Find Name',Nama,'in database')
            check=False
            for _ in range(len(DAFTAR_pasien)):
                if DAFTAR_pasien[_].Nama==Nama:
                    print('Name :',DAFTAR_pasien[_].Nama)
                    print('Umur :',DAFTAR_pasien[_].umur)
                    print('jenis kelamin :',DAFTAR_pasien[_].jenis_kelamin)
                    print('penyakit:',DAFTAR_pasien[_].penyakit)
                    fix=input('\n Is that you(y/n)? ')
                        if fix.lower() == 'y':
                            nodaftar=Pengawas.daftarlanjut(DAFTAR_pasien[_])
                            DAFTAR_pasien[_].noexam=nodaftar
                            DAFTAR_pasien[_].valid=True
                            check=True
                        else:
                            print('Sorry, your name doesn\'t exit in database,please register your self')
            if check==False:
                print('Sorry, your name doesn\'t exit in database,please register your self\n')
            

    elif menu == "3":
        print("Selamat Datang pasien\nSilahkan Cek Ruangan Anda Dengan Menginput Nomor pasien Anda\n")
        print("Pasien sakit kulit dan kelamin       : 1xxx (xxx = Nomor Pendaftaran Anda, Mis, 001, 012)")
        print("Pasien penyakit bagian dalam         : 4xxx (xxx = Nomor Pendaftaran Anda, Mis, 001, 012)")
        print("Pasien penyakit umum                 : 2xxx (xxx = Nomor Pendaftaran Anda, Mis, 001, 012)")
        print("Pasien penyakit jantung              : 3xxx (xxx = Nomor Pendaftaran Anda, Mis, 001, 012)")
        print("")

        Cek_Ruangan = int(input('Masukkan Nomor pasien anda = '))
        check=False
        for _ in range(len(DAFTAR_pasien)):
            if DAFTAR_pasien[_].nodaftar==Cek_Ruangan:
                print('Name :',DAFTAR_pasien[_].Nama)
                print('Umur :',DAFTAR_pasien[_].umur)
                print('Jenis kelamin :',DAFTAR_pasien[_].jenis_kelamin)
                print('penyakit:',DAFTAR_pasien[_].penyakit)
                print('No pendaftaran :',DAFTAR_pasien[_].nodaftar)
                print('')
                DAFTAR_pasien[_].Cek_Ruangan()
                check=True
        if check==False:
            print("Maaf!\nNomor Anda Salah\nMohon Masukkan Ulang")
        

    elif menu == "4":
        print("Semoga segera pulih")
        loop=False
