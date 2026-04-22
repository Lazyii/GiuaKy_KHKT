students = []

while True:
    name = input("Nhập tên sinh viên (nhập 0 để dừng): ")
    
    if name == "0":
        break
    
    if not all(part.isalpha() for part in name.split()):
        print("Tên không hợp lệ! Chỉ được nhập chữ cái.")
        continue
    
    try:
        score = float(input(f"Nhập điểm của {name}: "))
        
        if score < 0 or score > 10:
            print("Điểm phải nằm trong khoảng từ 0 đến 10!")
            continue
            
    except ValueError:
        print("Điểm không hợp lệ, vui lòng nhập số!")
        continue
    
    students.append({"name": name, "score": score})

if len(students) == 0:
    print("Không có dữ liệu sinh viên.")
else:
    total_score = sum(s["score"] for s in students)
    avg_score = total_score / len(students)
    
    top_student = max(students, key=lambda x: x["score"])
    
    print(f"\nĐiểm trung bình của lớp: {avg_score:.2f}")
    print(f"Sinh viên cao điểm nhất: {top_student['name']} ({top_student['score']})")
    
    with open("diem_thi.txt", "w", encoding="utf-8") as f:
        f.write("Danh sách sinh viên:\n")
        for s in students:
            f.write(f"{s['name']} - {s['score']}\n")

    print("Đã lưu vào file diem_thi.txt")