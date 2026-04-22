import matplotlib.pyplot as plt

rainfall = {
    'Tháng 1': 45.5,
    'Tháng 2': 112.0,
    'Tháng 3': 89.5
}

# Tổng lượng mưa
tong = sum(rainfall.values())

# Tháng mưa ít nhất
thang_min = min(rainfall, key=rainfall.get)

print(f"Tổng lượng mưa quý 1: {tong} mm")
print(f"Tháng có lượng mưa ít nhất: {thang_min} ({rainfall[thang_min]} mm)")

# Vẽ biểu đồ
thang = list(rainfall.keys())
luong_mua = list(rainfall.values())

plt.plot(thang, luong_mua, marker='o')
plt.title("Biểu đồ lượng mưa quý 1")
plt.xlabel("Tháng")
plt.ylabel("Lượng mưa (mm)")
plt.grid()

plt.show()