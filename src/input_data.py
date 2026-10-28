from pathlib import Path


def baca_data(lokasi_file):
    data = []

    with Path(lokasi_file).open("r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",", maxsplit=1)

            if len(bagian) != 2:
                print(f"Baris {nomor} dilewati: format harus nama,nilai.")
                continue

            nama = bagian[0].strip()

            if not nama:
                print(f"Baris {nomor} dilewati: nama kosong.")
                continue

            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor} dilewati: nilai harus berupa angka.")
                continue

            if not 0 <= nilai <= 100:
                print(f"Baris {nomor} dilewati: nilai harus 0 sampai 100.")
                continue

            data.append({"nama": nama, "nilai": nilai})

    return data