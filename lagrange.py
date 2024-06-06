import matplotlib.pyplot as plt
import numpy as np

# Function interpolasi Lagrange
def lagrange(points, x):
    hasil = 0.0
    n = len(points)  # Jumlah titik data
    for i in range(n):
        xi, yi = points[i]  # Titik data ke-i (xi, yi)
        term = yi  # Awalnya term bernilai yi
        for j in range(n):
            if i != j:  # Menghindari pembagian dengan nol
                xj, _ = points[j]  # Titik data ke-j (xj, _)
                term *= (x - xj) / (xi - xj)  # Menghitung term Lagrange
        hasil += term  # Menambahkan term ke hasil
    
    return hasil

# Data pengukuran (tegangan, waktu patah)
points = [(5, 40), (10, 30), (15, 25), (20, 40), (25, 18), (30, 20), (35, 22), (40, 15)]

x = 25  # Tegangan yang ingin diinterpolasi

# Menghitung nilai interpolasi pada tegangan x
hasil_value = lagrange(points, x)

# Menampilkan hasil interpolasi
print(f"P({x}) = {hasil_value:.5f}")
print(f"Jadi nilai interpolasi pada x = {x} yaitu {hasil_value:.5f}")

# Plot grafik hasil interpolasi untuk rentang tegangan 5 <= x <= 40
x_values = np.arange(5, 40.1, 0.1) 
y_values = [lagrange(points, x) for x in x_values]

# Membuat plot
plt.plot(x_values, y_values, "b") 
plt.scatter(*zip(*points), color='black')
plt.grid() 
plt.xlim(0, 40)
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinomial Lagrange')

# Menampilkan grafik
plt.show()