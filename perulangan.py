while True:
    print(f"\nMenu:")
    print(f"1. Hitung luas segitiga")
    print(f"2. Hitung luas persegi panjang")
    print(f"3. Menentukan angka ganjil dan genap")
    print(f"4. Quit")
    pilihan = input(f"Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        # Hitung luas segitiga
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(f"\nLuas segitiga adalah:", luas)

    elif pilihan == '2':
        # Hitung luas persegi panjang
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        print(f"\nLuas persegi panjang adalah:", luas)

    elif pilihan == '3':
        # Menentukan angka ganjil dan genap
        angka = int(input("\nMasukkan angka: "))
        if angka % 2 == 0:
            print(angka, "adalah angka genap")
        else:
            print(angka, "adalah angka ganjil")

    elif pilihan == '4':
        # Keluar dari program
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("!!!!!!!MASUKAN YANG ECREGGG!!!!!!!.")
                        
                        # DIMAS ANJAY MABAR