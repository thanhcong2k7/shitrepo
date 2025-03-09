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
mst2 = liveprov2 + str(random.randint(0,9999999).rjust(8,"0"))
print(">>> ! <<<    Đây là mã số thuế fake của nghệ sĩ: " + mst2)