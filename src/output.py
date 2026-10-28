def tampilkan_ringkasan(hasil, batas=60):
    print("\n=== REKAP NILAI MATEMATIKA ===")
    print(f"Jumlah siswa       : {hasil['jumlah']}")
    print(f"Rata-rata nilai    : {hasil['rata_rata']:.2f}")

    if hasil["minimum"] is None:
        print("Nilai minimum      : -")
        print("Nilai maksimum     : -")
    else:
        print(f"Nilai minimum      : {hasil['minimum']:g}")
        print(f"Nilai maksimum     : {hasil['maksimum']:g}")

    print(f"Batas kelulusan    : {batas}")
    print(f"Jumlah lulus       : {hasil['lulus']}")
    print(f"Belum lulus        : {hasil['belum_lulus']}")