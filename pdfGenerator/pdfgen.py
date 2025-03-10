#Chạy các lệnh sau để cài đủ gói trước khi chạy:
#pip install python-docx

import datetime
from datetime import datetime,date,timedelta
import time
import random
#get user info
print('Tool tạo PDF gậy v1.0\nĐược viết vào ngày 07/3/2025 bởi @realEtheriaa (YT)\nLưu ý: Thông tin của bạn có thể fake, nhưng thông tin tác giả phải chính xác để đảm bảo gậy đáp trên 95%! (Có thể tra Google/Wikipedia)')
user = input('>>> Nhập tên của bạn (đầy đủ có dấu): ')
fm = int(input('>>> Nhập 1 = nam, 2 = nữ: '))
dob = input('>>> Nhập ngày tháng năm sinh (dd/mm/YYYY): ')
proc_dob = datetime.strptime(dob, "%d/%m/%Y").date()
male=0
female=1
if proc_dob.year <= 2000:
    male=0
    female=1
elif proc_dob.year <= 2010:
    male=2
    female=3
elif proc_dob.year <= 2020:
    male=4
    female=5
elif proc_dob <= 2030:
    male=6
    female=7
elif proc_dob <= 2040:
    male=8
    female=9

province = [
  { "ma_tinh": "01", "ten_tinh": "Hà Nội" },
  { "ma_tinh": "02", "ten_tinh": "Hà Giang" },
  { "ma_tinh": "04", "ten_tinh": "Cao Bằng" },
  { "ma_tinh": "06", "ten_tinh": "Bắc Kạn" },
  { "ma_tinh": "08", "ten_tinh": "Tuyên Quang" },
  { "ma_tinh": "10", "ten_tinh": "Lào Cai" },
  { "ma_tinh": "11", "ten_tinh": "Điện Biên" },
  { "ma_tinh": "12", "ten_tinh": "Lai Châu" },
  { "ma_tinh": "14", "ten_tinh": "Sơn La" },
  { "ma_tinh": "15", "ten_tinh": "Yên Bái" },
  { "ma_tinh": "17", "ten_tinh": "Hòa Bình" },
  { "ma_tinh": "19", "ten_tinh": "Thái Nguyên" },
  { "ma_tinh": "20", "ten_tinh": "Lạng Sơn" },
  { "ma_tinh": "22", "ten_tinh": "Quảng Ninh" },
  { "ma_tinh": "24", "ten_tinh": "Bắc Giang" },
  { "ma_tinh": "25", "ten_tinh": "Phú Thọ" },
  { "ma_tinh": "26", "ten_tinh": "Vĩnh Phúc" },
  { "ma_tinh": "27", "ten_tinh": "Bắc Ninh" },
  { "ma_tinh": "30", "ten_tinh": "Hải Dương" },
  { "ma_tinh": "31", "ten_tinh": "Hải Phòng" },
  { "ma_tinh": "33", "ten_tinh": "Hưng Yên" },
  { "ma_tinh": "34", "ten_tinh": "Thái Bình" },
  { "ma_tinh": "35", "ten_tinh": "Hà Nam" },
  { "ma_tinh": "36", "ten_tinh": "Nam Định" },
  { "ma_tinh": "37", "ten_tinh": "Ninh Bình" },
  { "ma_tinh": "38", "ten_tinh": "Thanh Hóa" },
  { "ma_tinh": "40", "ten_tinh": "Nghệ An" },
  { "ma_tinh": "42", "ten_tinh": "Hà Tĩnh" },
  { "ma_tinh": "44", "ten_tinh": "Quảng Bình" },
  { "ma_tinh": "45", "ten_tinh": "Quảng Trị" },
  { "ma_tinh": "46", "ten_tinh": "Thừa Thiên Huế" },
  { "ma_tinh": "48", "ten_tinh": "Đà Nẵng" },
  { "ma_tinh": "49", "ten_tinh": "Quảng Nam" },
  { "ma_tinh": "51", "ten_tinh": "Quảng Ngãi" },
  { "ma_tinh": "52", "ten_tinh": "Bình Định" },
  { "ma_tinh": "54", "ten_tinh": "Phú Yên" },
  { "ma_tinh": "56", "ten_tinh": "Khánh Hòa" },
  { "ma_tinh": "58", "ten_tinh": "Ninh Thuận" },
  { "ma_tinh": "60", "ten_tinh": "Bình Thuận" },
  { "ma_tinh": "62", "ten_tinh": "Kon Tum" },
  { "ma_tinh": "64", "ten_tinh": "Gia Lai" },
  { "ma_tinh": "66", "ten_tinh": "Đắk Lắk" },
  { "ma_tinh": "67", "ten_tinh": "Đắk Nông" },
  { "ma_tinh": "68", "ten_tinh": "Lâm Đồng" },
  { "ma_tinh": "70", "ten_tinh": "Bình Phước" },
  { "ma_tinh": "72", "ten_tinh": "Tây Ninh" },
  { "ma_tinh": "74", "ten_tinh": "Bình Dương" },
  { "ma_tinh": "75", "ten_tinh": "Đồng Nai" },
  { "ma_tinh": "77", "ten_tinh": "Bà Rịa - Vũng Tàu" },
  { "ma_tinh": "79", "ten_tinh": "TP. Hồ Chí Minh" },
  { "ma_tinh": "80", "ten_tinh": "Long An" },
  { "ma_tinh": "82", "ten_tinh": "Tiền Giang" },
  { "ma_tinh": "83", "ten_tinh": "Bến Tre" },
  { "ma_tinh": "84", "ten_tinh": "Trà Vinh" },
  { "ma_tinh": "86", "ten_tinh": "Vĩnh Long" },
  { "ma_tinh": "87", "ten_tinh": "Đồng Tháp" },
  { "ma_tinh": "89", "ten_tinh": "An Giang" },
  { "ma_tinh": "91", "ten_tinh": "Kiên Giang" },
  { "ma_tinh": "92", "ten_tinh": "Cần Thơ" },
  { "ma_tinh": "93", "ten_tinh": "Hậu Giang" },
  { "ma_tinh": "94", "ten_tinh": "Sóc Trăng" },
  { "ma_tinh": "95", "ten_tinh": "Bạc Liêu" },
  { "ma_tinh": "96", "ten_tinh": "Cà Mau" }
]
print(">>> Dưới đây là danh sách mã tỉnh: ")
for i in province:
    print(i["ma_tinh"], " ------", i["ten_tinh"])
liveprov = ""
boole = True
while boole:
    live = input('>>> Nhập mã tỉnh nơi bạn sống: ')
    for i in province:
        if str(live) == str(i["ma_tinh"]):
            liveprov = live
            boole = False
            break
    if boole:
        print("Mã tỉnh không hợp lệ!")
y = abs(proc_dob.year) % 100
randomIDnum = str(0) + str(liveprov) + str(male if fm % 2 != 0 else female) + str(y if y > 10 else str(0) + str(y)) + str(random.randint(0, 99999)).rjust(6, "0")
print(">>> ! <<<    Đây là mã CCCD fake của bạn: " + randomIDnum)
mst = liveprov + str(random.randint(0,9999999)).rjust(8,"0")
addr = input(">>> Nhập địa chỉ mà bạn nghĩ ra (phải cùng tỉnh với tỉnh bạn đã chọn): ")
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))
def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)
toda = date.today()
past = toda + timedelta(days=-4*365)
mailg = input(">>> Nhập email gậy/email cổ của bạn: ")

user2 = input('>>> Nhập tên của nghệ sĩ (đầy đủ có dấu): ')
user3 = input('>>> Nhập nghệ danh của nghệ sĩ (VD: MONO, ...): ')
fm2 = int(input('>>> Nhập 1 = nam, 2 = nữ: '))
dob2 = input('>>> Nhập ngày tháng năm sinh (dd/mm/YYYY): ')
proc_dob2 = datetime.strptime(dob, "%d/%m/%Y").date()
male=0
female=1
if proc_dob2.year <= 2000:
    male=0
    female=1
elif proc_dob2.year <= 2010:
    male=2
    female=3
elif proc_dob2.year <= 2020:
    male=4
    female=5
elif proc_dob2.year <= 2030:
    male=6
    female=7
elif proc_dob2.year <= 2040:
    male=8
    female=9
liveprov2 = ""
boole2 = True
while boole2:
    live = input('>>> Nhập mã tỉnh nơi nghệ sĩ sống: ')
    for i in province:
        if str(live) == str(i["ma_tinh"]):
            liveprov2 = live
            boole2 = False
            break
    if boole2:
        print("Mã tỉnh không hợp lệ!")
y = abs(proc_dob2.year) % 100
randomIDnum2 = str(0) + str(liveprov2) + str(male if fm2 % 2 != 0 else female) + str(y if y > 10 else str(0) + str(y)) + str(random.randint(0, 99999)).rjust(6, "0")
print(">>> ! <<<    Đây là mã CCCD fake của nghệ sĩ: " + randomIDnum2)
mst2 = liveprov2 + str(random.randint(0,9999999)).rjust(8,"0")
print(">>> ! <<<    Đây là mã số thuế fake của nghệ sĩ: " + mst2)

prod_name = input(">>> Nhập tên tác phẩm:")
rel_date = input(">>> Nhập ngày phát hành tác phẩm (dd/mm/yyyy): ")
proc_rdate = datetime.strptime(rel_date, "%d/%m/%Y")
signed_date = None
if proc_rdate >= datetime.strptime("30/09/2024", "%d/%m/%Y"):
    signed_date = random_date(proc_rdate.strftime("%d/%m/%Y"), date.today(), random.random())
else:
    signed_date = random_date("30/09/2024", date.today().strftime('%d/%m/%Y'), random.random())

#process
from docx import Document
doc = Document('./sample.docx')
replace_word = {
    'date': signed_date,
    'user1': user,
    'user2': user2,
    'alias': user3,
    'cccd1': randomIDnum,
    'mst1': mst,
    'mst2': mst2,
    'capngay1': random_date(past.strftime('%d/%m/%Y'), toda.strftime('%d/%m/%Y'), random.random()),
    'capngay2': random_date(past.strftime('%d/%m/%Y'), toda.strftime('%d/%m/%Y'), random.random()),
    'addr1': addr,
    'email': mailg
}
for word in replace_word:
    for p in doc.paragraphs:
        if p.text.find(word) >= 0:
            p.text = p.text.replace(word, replace_word[word])
 
doc.save('note_demo.docx')