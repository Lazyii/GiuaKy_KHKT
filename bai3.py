def tinh_tien_dien(kwh):
    if kwh <= 50:
        return kwh * 1600
    elif kwh <= 100:
        return 50 * 1600 + (kwh - 50) * 2000
    else:
        return 50 * 1600 + 50 * 2000 + (kwh - 100) * 2500


while True:
    try:
        kwh = float(input("Nhập số kWh tiêu thụ: "))
        
        if kwh < 0:
            print("Số kWh không hợp lệ. Vui lòng nhập lại.")
            continue
        
        tien = tinh_tien_dien(kwh)
        print(f"Tiền điện phải trả: {tien:,.0f} đ")
        break

    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ (không nhập chữ).")