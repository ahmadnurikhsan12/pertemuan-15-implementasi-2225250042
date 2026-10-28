from pathlib import Path

from src.input_data import baca_data
from src.proses import ringkasan
from src.output import tampilkan_ringkasan

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "contoh_data.txt"
BATAS_LULUS = 60


def main():
    try:
        data = baca_data(DATA_FILE)
    except OSError as error:
        print(f"Gagal membaca data: {error}")
        return

    if not data:
        print("Tidak ada data valid untuk dianalisis.")
        return

    hasil = ringkasan(data, BATAS_LULUS)
    tampilkan_ringkasan(hasil, BATAS_LULUS)


if __name__ == "__main__":
    main()