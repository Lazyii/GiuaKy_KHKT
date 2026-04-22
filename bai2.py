import re

def chuan_hoa_ma(sp):
    return re.sub(r"\s+", "", sp).upper()

def xu_ly_danh_sach(ds):
    ds_chuan = [chuan_hoa_ma(sp) for sp in ds]
    return sorted(ds_chuan, reverse=True)

# Ví dụ
ds = [" sp-001 ", "SP-006 \n", "  sP-003", "SP-  004"]
print(xu_ly_danh_sach(ds))