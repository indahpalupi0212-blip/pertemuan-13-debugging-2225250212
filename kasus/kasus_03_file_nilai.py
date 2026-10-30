
def baca_nilai(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                nim, teks_nilai = baris.split(",")
                nilai = float(teks_nilai)

                data_nilai.append((nim, nilai))

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except ValueError:
        print("Data nilai tidak valid.")

    return data_nilai


data = baca_nilai("data/nilai.txt")
print("Data nilai:", data)
