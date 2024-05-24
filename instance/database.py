import sqlite3

# Kết nối tới cơ sở dữ liệu
conn = sqlite3.connect('./instance/database.db')

# Tạo một con trỏ
cursor = conn.cursor()

# Chạy lệnh SQL
cursor.execute("SELECT * from User")

# Lấy tất cả các kết quả
rows = cursor.fetchall()

for row in rows:
    print(row)

# Đóng kết nối
conn.close()
