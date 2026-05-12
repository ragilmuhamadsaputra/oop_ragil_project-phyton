# Program menghitung rata-rata nilai 5 mata pelajaran

total = 75

for i in range(1, 6):
    nilai = int(input(f"\nMasukkan nilai mata pelajaran ke-{i}: "))
    total += nilai

rata_rata = total / 5

print("\nTotal nilai =", total)
print("Rata-rata nilai =", rata_rata)