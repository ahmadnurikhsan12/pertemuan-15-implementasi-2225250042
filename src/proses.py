BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)


def status_lulus(data, batas=BATAS_LULUS):
    return [
        siswa for siswa in data
        if siswa["nilai"] >= batas
    ]


def ringkasan(data, batas=BATAS_LULUS):
    nilai = [siswa["nilai"] for siswa in data]
    siswa_lulus = status_lulus(data, batas)

    return {
        "jumlah": len(data),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(siswa_lulus),
        "belum_lulus": len(data) - len(siswa_lulus),
    }