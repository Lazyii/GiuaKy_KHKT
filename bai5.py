import matplotlib.pyplot as plt

rainfall = {
    'Tháng 1': 45.5,
    'Tháng 2': 112.0,
    'Tháng 3': 89.5
}

# Tính toán
tong = sum(rainfall.values())
thang_min = min(rainfall, key=rainfall.get)
thang_max = max(rainfall, key=rainfall.get)
trung_binh = tong / len(rainfall)

print(f"Tổng lượng mưa: {tong} mm")
print(f"Thấp nhất: {thang_min} ({rainfall[thang_min]} mm)")
print(f"Cao nhất: {thang_max} ({rainfall[thang_max]} mm)")
print(f"Trung bình: {trung_binh:.2f} mm")

# Chuẩn bị dữ liệu
thang = list(rainfall.keys())
luong_mua = list(rainfall.values())

# Vẽ biểu đồ
plt.figure()
plt.plot(thang, luong_mua, marker='o')

# Hiển thị giá trị trên từng điểm
for i, value in enumerate(luong_mua):
    plt.text(i, value, f"{value}", ha='center', va='bottom')

# Đường trung bình
plt.axhline(trung_binh, linestyle='--', label=f"Trung bình: {trung_binh:.1f} mm")

# Highlight max/min
plt.scatter(thang[luong_mua.index(max(luong_mua))], max(luong_mua))
plt.scatter(thang[luong_mua.index(min(luong_mua))], min(luong_mua))

plt.title("Biểu đồ lượng mưa Quý 1")
plt.xlabel("Tháng")
plt.ylabel("Lượng mưa (mm)")
plt.legend()
plt.grid()

plt.show()
