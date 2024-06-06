import numpy as np
import matplotlib.pyplot as plt

# Function interpolasi Newton
def newton_interpolation(points, x):
    n = len(points)  # Jumlah data poin

    # Inisialisasi tabel selisih terbagi
    divided_diff = np.zeros((n, n))
    
    # Mengisi kolom pertama dengan nilai y dari data poin
    for i in range(n):
        divided_diff[i][0] = points[i][1]
        
    # Menghitung selisih terbagi untuk semua kolom
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (points[i+j][0] - points[i][0])
    
    # Inisialisasi hasil dengan nilai pertama dari tabel selisih terbagi
    result = divided_diff[0][0]
    product = 1.0
    # Menghitung hasil interpolasi
    for i in range(1, n):
        product *= (x - points[i-1][0])
        result += divided_diff[0][i] * product
    
    return result

# Data pengukuran (tegangan, waktu patah)
points = [(5, 40), (10, 30), (15, 25), (20, 40), (25, 18), (30, 20), (35, 22), (40, 15)]

x = 25  # Tegangan yang ingin diinterpolasi

# Menghitung nilai interpolasi pada x = 25
interpolated_value = newton_interpolation(points, x)

print(f"P({x}) = {interpolated_value:.5f}")
print(f"Jadi nilai interpolasi pada x = {x} yaitu {interpolated_value:.5f}")

# Plot Grafik hasil interpolasi dengan 5 <= x <= 40
x_values = np.arange(5, 40.1, 0.1)
y_values = [newton_interpolation(points, x) for x in x_values]

# Membuat plot grafik interpolasi
plt.plot(x_values, y_values, "b")
plt.scatter(*zip(*points), color='black')
plt.grid()
plt.xlim(0, 40)
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinomial Newton')

plt.show()  # Menampilkan plot
