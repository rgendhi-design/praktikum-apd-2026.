# ======================= [A] INISIALISASI DATA ========================
import os

# Perintah clear terminal disesuaikan dengan sistem operasi
if os.name == "nt":
    perintah_clear = "cls"
else:
    perintah_clear = "clear"

# Data pengguna (DICTIONARY) -> {username: {"password": ..., "role": ...}}
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "sinta": {"password": "sinta123", "role": "user"},
}

# Data koleksi parfum (DICTIONARY BERSARANG)
# -> {id: {"nama": ..., "brand": ..., "aroma": ...,
#         "ukuran": ..., "harga": ..., "stok": ...}}
parfum = {
    1: {"nama": "Bleu de Chanel", "brand": "Chanel", "aroma": "Woody Aromatic",
        "ukuran": 100, "harga": 1500000, "stok": 5},
    2: {"nama": "Sauvage", "brand": "Dior", "aroma": "Fresh Spicy",
        "ukuran": 60, "harga": 1250000, "stok": 8},
    3: {"nama": "Ombre Nomade", "brand": "Louis Vuitton", "aroma": "Oriental",
        "ukuran": 100, "harga": 5500000, "stok": 2},
}

program_berjalan = True
login_berhasil = False
username_aktif = ""
role_aktif = ""

# =========================== [B] MENU AWAL ============================
while program_berjalan == True:
    os.system(perintah_clear)
    print("=" * 60)
    print("        SISTEM PENCATATAN KOLEKSI PARFUM")
    print("=" * 60)
    print("  [1] Login")
    print("  [2] Register")
    print("  [3] Keluar Program")
    print("-" * 60)
    pilih_auth = input("  Pilih menu >> ")

    # ======================== [C] FITUR LOGIN =========================
    if pilih_auth == "1":
        os.system(perintah_clear)
        print("=" * 60)
        print("                          LOGIN")
        print("=" * 60)
        nama_login = input("  Username : ").lower()
        sandi_login = input("  Password : ")
        if nama_login in users and users[nama_login]["password"] == sandi_login:
            login_berhasil = True
            username_aktif = nama_login
            role_aktif = users[nama_login]["role"]
            os.system(perintah_clear)
            print("=" * 60)
            print(f"  Login berhasil! Selamat datang, {username_aktif}")
            print(f"  Status : {role_aktif.upper()}")
            print("=" * 60)
            input("  Tekan ENTER untuk melanjutkan...")
        else:
            print("-" * 60)
            print("  ERROR : Username atau password salah!")
            input("  Tekan ENTER untuk kembali...")

    # ======================= [D] FITUR REGISTER =======================
    elif pilih_auth == "2":
        os.system(perintah_clear)
        print("=" * 60)
        print("                        REGISTER")
        print("=" * 60)
        # lower() agar "ADMIN" dan "admin" dianggap username yang sama
        user_baru = input("  Username baru : ").lower()
        if user_baru == "":
            print("-" * 60)
            print("  ERROR : Username tidak boleh kosong!")
        elif user_baru in users:
            print("-" * 60)
            print("  ERROR : Username sudah digunakan!")
        else:
            sandi_baru = input("  Password baru : ")
            if sandi_baru == "":
                print("-" * 60)
                print("  ERROR : Password tidak boleh kosong!")
            else:
                users[user_baru] = {"password": sandi_baru, "role": "user"}
                print("-" * 60)
                print("  Register berhasil! Akun baru berstatus")
                print("  pengguna biasa. Silakan login.")
        input("  Tekan ENTER untuk kembali...")

    # ============== [E] KELUAR PROGRAM DAN VALIDASI MENU ==============
    elif pilih_auth == "3":
        os.system(perintah_clear)
        print("Terima kasih telah menggunakan program ini!")
        program_berjalan = False
    else:
        print("  ERROR : Pilihan tidak tersedia!")
        input("  Tekan ENTER untuk kembali...")

    # ==================== [F] MENU UTAMA APLIKASI =====================
    while login_berhasil == True and program_berjalan == True:
        os.system(perintah_clear)
        print("=" * 60)
        print("        SISTEM PENCATATAN KOLEKSI PARFUM")
        print(f"  Login sebagai : {username_aktif} ({role_aktif})")
        print("=" * 60)
        if role_aktif == "admin":
            print("  [1] Lihat Semua Koleksi        (Read)")
            print("  [2] Cari Parfum")
            print("  [3] Tambah Parfum              (Create)")
            print("  [4] Update Data Parfum         (Update)")
            print("  [5] Hapus Data Parfum          (Delete)")
            print("  [6] Logout")
            print("  [7] Keluar Program")
        else:
            print("  [1] Lihat Semua Koleksi        (Read)")
            print("  [2] Cari Parfum")
            print("  [3] Logout")
            print("  [4] Keluar Program")
        print("-" * 60)
        pilih_menu = input("  Pilih menu >> ")

        # ======================= [G] FITUR READ =======================
        if pilih_menu == "1":
            os.system(perintah_clear)
            print("=" * 95)
            print("                       DAFTAR KOLEKSI PARFUM")
            print("=" * 95)
            if len(parfum) == 0:
                print("  Data koleksi masih kosong!")
            else:
                print(f"  {'ID':<4}{'Nama Parfum':<20}{'Brand':<16}{'Aroma':<17}"
                      f"{'Ukuran (ml)':<12}{'Harga (Rp)':<14}{'Stok':>4}")
                print("-" * 95)
                for id_parfum, data in parfum.items():
                    print(f"  {id_parfum:<4}{data['nama']:<20}{data['brand']:<16}"
                          f"{data['aroma']:<17}{data['ukuran']:<12}"
                          f"{data['harga']:<14,}{data['stok']:>4}")
                print("-" * 95)
                print(f"  Total koleksi : {len(parfum)} parfum")
            input("\n  Tekan ENTER untuk kembali...")

        # ======================= [H] FITUR CARI =======================
        elif pilih_menu == "2":
            os.system(perintah_clear)
            print("=" * 95)
            print("                          CARI PARFUM")
            print("=" * 95)
            kunci = input("  Kata kunci (nama/brand/aroma) : ")
            if kunci == "":
                print("  ERROR : Kata kunci tidak boleh kosong!")
            else:
                hasil_cari = {}
                for id_parfum, data in parfum.items():
                    if (kunci.lower() in data["nama"].lower()
                            or kunci.lower() in data["brand"].lower()
                            or kunci.lower() in data["aroma"].lower()):
                        hasil_cari[id_parfum] = data
                if len(hasil_cari) == 0:
                    print("  Parfum tidak ditemukan!")
                else:
                    print(f"  Ditemukan {len(hasil_cari)} parfum :")
                    print(f"  {'ID':<4}{'Nama Parfum':<20}{'Brand':<16}"
                          f"{'Aroma':<17}{'Ukuran (ml)':<12}"
                          f"{'Harga (Rp)':<14}{'Stok':>4}")
                    print("-" * 95)
                    for id_parfum, data in hasil_cari.items():
                        print(f"  {id_parfum:<4}{data['nama']:<20}"
                              f"{data['brand']:<16}{data['aroma']:<17}"
                              f"{data['ukuran']:<12}{data['harga']:<14,}"
                              f"{data['stok']:>4}")
                    print("-" * 95)
            input("\n  Tekan ENTER untuk kembali...")

        # ====================== [I] FITUR CREATE ======================
        elif pilih_menu == "3" and role_aktif == "admin":
            os.system(perintah_clear)
            print("=" * 60)
            print("                 TAMBAH PARFUM (CREATE)")
            print("=" * 60)
            id_valid = False
            while id_valid == False:
                id_baru = input("  ID Parfum    : ")
                if id_baru == "":
                    print("  ERROR : ID tidak boleh kosong!")
                elif id_baru.isdigit() == False:
                    print("  ERROR : ID harus berupa angka!")
                elif int(id_baru) in parfum:
                    print("  ERROR : ID sudah digunakan, pilih ID lain!")
                else:
                    id_baru = int(id_baru)
                    id_valid = True

            nama_valid = False
            while nama_valid == False:
                nama_baru = input("  Nama Parfum  : ")
                if nama_baru == "":
                    print("  ERROR : Nama tidak boleh kosong!")
                else:
                    nama_valid = True

            brand_valid = False
            while brand_valid == False:
                brand_baru = input("  Brand        : ")
                if brand_baru == "":
                    print("  ERROR : Brand tidak boleh kosong!")
                else:
                    brand_valid = True

            aroma_valid = False
            while aroma_valid == False:
                aroma_baru = input("  Aroma        : ")
                if aroma_baru == "":
                    print("  ERROR : Aroma tidak boleh kosong!")
                else:
                    aroma_valid = True

            ukuran_valid = False
            while ukuran_valid == False:
                ukuran_baru = input("  Ukuran (ml)  : ")
                if ukuran_baru == "":
                    print("  ERROR : Ukuran tidak boleh kosong!")
                elif ukuran_baru.isdigit() == False:
                    print("  ERROR : Ukuran harus berupa angka!")
                elif int(ukuran_baru) <= 0:
                    print("  ERROR : Ukuran harus lebih dari 0!")
                else:
                    ukuran_baru = int(ukuran_baru)
                    ukuran_valid = True

            harga_valid = False
            while harga_valid == False:
                harga_baru = input("  Harga (Rp)   : ")
                if harga_baru == "":
                    print("  ERROR : Harga tidak boleh kosong!")
                elif harga_baru.isdigit() == False:
                    print("  ERROR : Harga harus berupa angka!")
                elif int(harga_baru) <= 0:
                    print("  ERROR : Harga harus lebih dari 0!")
                else:
                    harga_baru = int(harga_baru)
                    harga_valid = True

            stok_valid = False
            while stok_valid == False:
                stok_baru = input("  Stok         : ")
                if stok_baru == "":
                    print("  ERROR : Stok tidak boleh kosong!")
                elif stok_baru.isdigit() == False:
                    print("  ERROR : Stok harus berupa angka!")
                else:
                    stok_baru = int(stok_baru)
                    stok_valid = True

            parfum[id_baru] = {
                "nama": nama_baru, "brand": brand_baru, "aroma": aroma_baru,
                "ukuran": ukuran_baru, "harga": harga_baru, "stok": stok_baru,
            }
            print("-" * 60)
            print("  Data parfum berhasil ditambahkan!")
            input("  Tekan ENTER untuk kembali...")

        # ====================== [J] FITUR UPDATE ======================
        elif pilih_menu == "4" and role_aktif == "admin":
            os.system(perintah_clear)
            print("=" * 60)
            print("                 UPDATE PARFUM (UPDATE)")
            print("=" * 60)
            id_ubah = input("  ID parfum yang akan diupdate : ")
            if id_ubah == "":
                print("  ERROR : ID tidak boleh kosong!")
                input("  Tekan ENTER untuk kembali...")
            elif id_ubah.isdigit() == False:
                print("  ERROR : ID harus berupa angka!")
                input("  Tekan ENTER untuk kembali...")
            elif int(id_ubah) not in parfum:
                print("  ERROR : ID tidak ditemukan!")
                input("  Tekan ENTER untuk kembali...")
            else:
                data = parfum[int(id_ubah)]
                print("-" * 60)
                print(f"  Data ditemukan : {data['nama']}")
                print("  Tekan ENTER untuk mempertahankan nilai lama")
                print("-" * 60)
                nama_baru = input(f"  Nama baru    [{data['nama']}] : ")
                if nama_baru != "":
                    data["nama"] = nama_baru
                brand_baru = input(f"  Brand baru   [{data['brand']}] : ")
                if brand_baru != "":
                    data["brand"] = brand_baru
                aroma_baru = input(f"  Aroma baru   [{data['aroma']}] : ")
                if aroma_baru != "":
                    data["aroma"] = aroma_baru
                ukuran_baru = input(f"  Ukuran (ml)  [{data['ukuran']}] : ")
                if ukuran_baru != "":
                    if ukuran_baru.isdigit() == True and int(ukuran_baru) > 0:
                        data["ukuran"] = int(ukuran_baru)
                    else:
                        print("  ERROR : Ukuran harus > 0, nilai lama dipakai!")
                harga_baru = input(f"  Harga (Rp)   [{data['harga']}] : ")
                if harga_baru != "":
                    if harga_baru.isdigit() == True and int(harga_baru) > 0:
                        data["harga"] = int(harga_baru)
                    else:
                        print("  ERROR : Harga harus > 0, nilai lama dipakai!")
                stok_baru = input(f"  Stok baru    [{data['stok']}] : ")
                if stok_baru != "":
                    if stok_baru.isdigit() == True:
                        data["stok"] = int(stok_baru)
                    else:
                        print("  ERROR : Stok harus angka, nilai lama dipakai!")
                print("-" * 60)
                print("  Data parfum berhasil diupdate!")
                input("  Tekan ENTER untuk kembali...")

        # ====================== [K] FITUR DELETE ======================
        elif pilih_menu == "5" and role_aktif == "admin":
            os.system(perintah_clear)
            print("=" * 60)
            print("                 HAPUS PARFUM (DELETE)")
            print("=" * 60)
            id_hapus = input("  ID parfum yang akan dihapus : ")
            if id_hapus == "":
                print("  ERROR : ID tidak boleh kosong!")
                input("  Tekan ENTER untuk kembali...")
            elif id_hapus.isdigit() == False:
                print("  ERROR : ID harus berupa angka!")
                input("  Tekan ENTER untuk kembali...")
            elif int(id_hapus) not in parfum:
                print("  ERROR : ID tidak ditemukan!")
                input("  Tekan ENTER untuk kembali...")
            else:
                id_hapus = int(id_hapus)
                print("-" * 60)
                print(f"  Nama  : {parfum[id_hapus]['nama']}")
                print(f"  Brand : {parfum[id_hapus]['brand']}")
                print(f"  Aroma : {parfum[id_hapus]['aroma']}")
                print("-" * 60)
                konfirmasi = input("  Yakin ingin menghapus? (y/t) : ")
                if konfirmasi.lower() == "y":
                    parfum.pop(id_hapus)
                    print("  Data parfum berhasil dihapus!")
                else:
                    print("  Penghapusan dibatalkan.")
                input("  Tekan ENTER untuk kembali...")

        # =========== [L] LOGOUT, KELUAR, DAN VALIDASI MENU ============
        elif ((pilih_menu == "6" and role_aktif == "admin")
                or (pilih_menu == "3" and role_aktif == "user")):
            login_berhasil = False
            os.system(perintah_clear)
            print("  Logout berhasil!")
            input("  Tekan ENTER untuk kembali ke menu login...")
        elif ((pilih_menu == "7" and role_aktif == "admin")
                or (pilih_menu == "4" and role_aktif == "user")):
            os.system(perintah_clear)
            print("Terima kasih telah menggunakan program ini!")
            program_berjalan = False
        else:
            print("  ERROR : Pilihan tidak tersedia!")
            input("  Tekan ENTER untuk kembali...")
