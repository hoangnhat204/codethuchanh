from lxml import etree

tree = etree.parse("quanlybanan.xml")

print("=== PHẦN 2: XPATH VỚI FILE QUANLYBANAN.XML ===\n")

# 1. Lấy tất cả bàn
print("Danh sách bàn:", tree.xpath("//table/@number"))

# 2. Lấy tất cả nhân viên
print("Tên nhân viên:", tree.xpath("//employee/name/text()"))

# 3. Lấy tất cả tên món
print("Tên món:", tree.xpath("//dish/@name"))

# 4. Tên nhân viên có mã NV02
print("Tên NV02:", tree.xpath("//employee[@id='NV02']/name/text()"))

# 5. Tên và số điện thoại của NV03
print("Tên + SĐT NV03:", tree.xpath("//employee[@id='NV03']/(name|phone)/text()"))

# 6. Tên món có giá > 50000
print("Món > 50.000:", tree.xpath("//dish[@price>50000]/@name"))

# 7. Số bàn của hóa đơn HD03
print("Số bàn HD03:", tree.xpath("//bill[@id='HD03']/@tableRef"))

# 8. Tên món có mã M02
print("Tên món M02:", tree.xpath("//dish[@id='M02']/@name"))

# 9. Ngày lập hóa đơn HD03
print("Ngày lập HD03:", tree.xpath("//bill[@id='HD03']/@date"))

# 10. Mã món trong hóa đơn HD01
print("Mã món HD01:", tree.xpath("//bill[@id='HD01']/item/@dishRef"))

# 11. Tên món trong hóa đơn HD01
print("Tên món HD01:", tree.xpath("//dish[@id=//bill[@id='HD01']/item/@dishRef]/@name"))

# 12. Tên nhân viên lập hóa đơn HD02
print("Tên NV lập HD02:", tree.xpath("//employee[@id=//bill[@id='HD02']/@employeeRef]/name/text()"))

# 13. Đếm số bàn
print("Số bàn:", int(tree.xpath("count(//table)")))

# 14. Đếm số hóa đơn lập bởi NV01
print("Số hóa đơn NV01:", int(tree.xpath("count(//bill[@employeeRef='NV01'])")))

# 15. Tên món trong hóa đơn của bàn số 2
print("Món bàn 2:", tree.xpath("//dish[@id=//bill[@tableRef=//table[@number='2']/@id]/item/@dishRef]/@name"))

# 16. Nhân viên từng lập hóa đơn cho bàn 3
print("NV bàn 3:", tree.xpath("//employee[@id=//bill[@tableRef=//table[@number='3']/@id]/@employeeRef]/name/text()"))

# 17. Hóa đơn nhân viên nữ lập
print("Hóa đơn NV nữ lập:", tree.xpath("//bill[@employeeRef=//employee[@gender='Nữ']/@id]/@id"))

# 18. Nhân viên phục vụ bàn 1
print("NV bàn 1:", tree.xpath("//employee[@id=//bill[@tableRef=//table[@number='1']/@id]/@employeeRef]/name/text()"))

# 19. Món được gọi nhiều hơn 1 lần
print("Món gọi >1 lần:", tree.xpath("//dish[@id=//item/@dishRef][count(//item[@dishRef=@id])>1]/@name"))

# 20. Tên bàn + ngày lập hóa đơn HD02
print("Bàn + Ngày HD02:", tree.xpath("concat(//table[@id=//bill[@id='HD02']/@tableRef]/@number, ' - ', //bill[@id='HD02']/@date)"))
