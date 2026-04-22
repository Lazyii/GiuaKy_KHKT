import random

choices = ["keo", "bua", "bao"]

def ket_qua(player, computer):
    if player == computer:
        return "hoa"
    elif (player == "keo" and computer == "bao") or \
         (player == "bua" and computer == "keo") or \
         (player == "bao" and computer == "bua"):
        return "thang"
    else:
        return "thua"

while True:
    try:
        so_hiep = int(input("Nhập số hiệp muốn chơi: "))
        if so_hiep <= 0:
            print("Vui lòng nhập số > 0")
            continue
        break
    except ValueError:
        print("Sai định dạng, vui lòng nhập số!")

thang = 0
thua = 0
hoa = 0

for i in range(1, so_hiep + 1):
    print(f"\n--- Hiệp {i} ---")
    
    while True:
        player = input("Nhập (keo/bua/bao): ").lower().strip()
        if player in choices:
            break
        print("Sai lựa chọn, vui lòng nhập lại!")

    computer = random.choice(choices)
    print(f"Máy chọn: {computer}")

    kq = ket_qua(player, computer)

    if kq == "thang":
        print("Bạn thắng!")
        thang += 1
    elif kq == "thua":
        print("Bạn thua!")
        thua += 1
    else:
        print("Hòa!")
        hoa += 1

print("\n=== Kết quả cuối cùng ===")
print(f"Thắng: {thang}, Thua: {thua}, Hòa: {hoa}")

with open("ket_qua_game.txt", "w", encoding="utf-8") as f:
    f.write("Kết quả trò chơi Kéo - Búa - Bao\n")
    f.write(f"Số hiệp: {so_hiep}\n")
    f.write(f"Thắng: {thang}\n")
    f.write(f"Thua: {thua}\n")
    f.write(f"Hòa: {hoa}\n")