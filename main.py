import mysql.connector
from lxml import etree

# === 1. Đọc và kiểm tra XML với XSD ===
xml_file = 'catalog.xml'
xsd_file = 'catalog.xsd'

xml_doc = etree.parse(xml_file)
xsd_doc = etree.parse(xsd_file)
schema = etree.XMLSchema(xsd_doc)

if not schema.validate(xml_doc):
    print("❌ XML không hợp lệ!")
    for error in schema.error_log:
        print(f"Lỗi: {error.message}")
    exit()
else:
    print("✅ XML hợp lệ, tiếp tục xử lý...")

# === 2. Kết nối MySQL ===
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce"
)
cursor = conn.cursor()

# === 3. Tạo bảng nếu chưa có ===
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    currency VARCHAR(10),
    stock INT,
    categoryRef VARCHAR(10),
    FOREIGN KEY (categoryRef) REFERENCES Categories(id)
)
""")

# === 4. Dùng XPath để lấy dữ liệu ===
root = xml_doc.getroot()

# Lấy danh mục
for cat in root.xpath("//categories/category"):
    cid = cat.get("id")
    cname = cat.text
    cursor.execute("""
        INSERT INTO Categories (id, name)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE name=%s
    """, (cid, cname, cname))

# Lấy sản phẩm
for prod in root.xpath("//products/product"):
    pid = prod.get("id")
    pref = prod.get("categoryRef")
    pname = prod.findtext("name")
    pprice = float(prod.findtext("price"))
    pcurr = prod.find("price").get("currency")
    pstock = int(prod.findtext("stock"))

    cursor.execute("""
        INSERT INTO Products (id, name, price, currency, stock, categoryRef)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        name=%s, price=%s, currency=%s, stock=%s, categoryRef=%s
    """, (pid, pname, pprice, pcurr, pstock, pref,
          pname, pprice, pcurr, pstock, pref))

conn.commit()
cursor.close()
conn.close()

print("✅ Dữ liệu đã được lưu/ cập nhật vào MySQL thành công!")
