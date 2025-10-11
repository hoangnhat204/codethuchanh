from lxml import etree

tree = etree.parse("sinhvien.xml")

print("=== PHẦN 1: XPATH VỚI FILE SINHVIEN.XML ===\n")

# 1. Lấy tất cả sinh viên
print("Tất cả sinh viên:", tree.xpath("//student"))

# 2. Liệt kê tên tất cả sinh viên
print("Tên sinh viên:", tree.xpath("//student/name/text()"))

# 3. Lấy tất cả ID
print("ID:", tree.xpath("//student/@id"))

# 4. Ngày sinh của SV01
print("Ngày sinh SV01:", tree.xpath("//student[@id='SV01']/date/text()"))

# 5. Các khóa học
print("Tất cả khóa học:", tree.xpath("//course/text()"))

# 6. Thông tin sinh viên đầu tiên
print("Thông tin SV đầu tiên:", [etree.tostring(x, encoding='unicode') for x in tree.xpath("//student[1]/*")])

# 7. Mã SV học Vatly203
print("Mã SV học Vatly203:", tree.xpath("//student[enrollment/course='Vatly203']/@id"))

# 8. Tên SV học Toan101
print("Tên SV học Toan101:", tree.xpath("//student[enrollment/course='Toan101']/name/text()"))

# 9. Tên SV học Vatly203
print("Tên SV học Vatly203:", tree.xpath("//student[enrollment/course='Vatly203']/name/text()"))

# 10. Tên và ngày sinh sinh năm 1997
print("Tên + ngày sinh 1997:", tree.xpath("//student[starts-with(date,'1997')]/(name|date)/text()"))

# 11. Tên SV có ngày sinh trước 1998
print("Tên SV sinh trước 1998:", tree.xpath("//student[number(substring(date,1,4))<1998]/name/text()"))

# 12. Đếm số sinh viên
print("Tổng số sinh viên:", int(tree.xpath("count(//student)")))

# 13. SV chưa đăng ký môn nào
print("SV chưa đăng ký môn:", tree.xpath("//student[not(enrollment)]/name/text()"))

# 14. <date> anh em ngay sau <name> SV01
print("<date> sau <name> SV01:", tree.xpath("//student[@id='SV01']/name/following-sibling::date/text()"))

# 15. Sinh viên họ “Trần”
print("Sinh viên họ Trần:", tree.xpath("//student[starts-with(name,'Trần')]/name/text()"))

# 16. Năm sinh SV01
print("Năm sinh SV01:", tree.xpath("substring(//student[@id='SV01']/date,1,4)"))
