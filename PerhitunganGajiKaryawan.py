# PT. DINGIN DAMAI
# Program Hitung Gaji Karyawan

print("PROGRAM HITUNG GAJI KARYAWAN")
print("PT. DINGIN DAMAI")
print("=============================================")

nama = input("Nama Karyawan : ")
gol = int(input("Golongan Jabatan (1/2/3) : "))
pend = input("Pendidikan (SMA/D1/D3/S1) : ")
jam = int(input("Jumlah jam kerja : "))

gaji_pokok = 300000

# hitung tunjangan jabatan
if gol == 1:
    tj_jabatan = 0.05 * gaji_pokok
elif gol == 2:
    tj_jabatan = 0.10 * gaji_pokok
elif gol == 3:
    tj_jabatan = 0.15 * gaji_pokok
else:
    tj_jabatan = 0
    print("Golongan gak ada!")

# hitung tunjangan pendidikan
if pend == "SMA":
    tj_pend = 0.025 * gaji_pokok
elif pend == "D1":
    tj_pend = 0.05 * gaji_pokok
elif pend == "D3":
    tj_pend = 0.20 * gaji_pokok
elif pend == "S1":
    tj_pend = 0.30 * gaji_pokok
else:
    tj_pend = 0
    print("Pendidikan gak dikenali!")

# hitung lembur
if jam > 8:
    lembur = (jam - 8) * 3500
else:
    lembur = 0

# total
total = gaji_pokok + tj_jabatan + tj_pend + lembur

print("\n=============================================")
print("Karyawan yang bernama", nama)
print("Honor yang diterima :")
print(f"  Tunjangan Jabatan     Rp {tj_jabatan:,.0f}")
print(f"  Tunjangan Pendidikan  Rp {tj_pend:,.0f}")
print(f"  Honor Lembur          Rp {lembur:,.0f}")
print("--------------------------------------------- +")
print(f"Total Gaji             Rp {total:,.0f}")
