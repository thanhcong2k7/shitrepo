import subprocess,sys,re
try:
    import selenium
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'selenium'])
try:
    import bs4
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
try:
    import dload
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'dload'])

import random
import string, time, traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from chromedriver_py import binary_path
from bs4 import BeautifulSoup
import platform
import os

#Check system info & work ...
chrome_options = Options()
def extract_version_registry(output):
    try:
        google_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter != '\n':
                google_version += letter
            else:
                break
        return(google_version.strip())
    except TypeError:
        return
def extract_version_folder():
    # Check if the Chrome folder exists in the x32 or x64 Program Files folders.
    for i in range(2):
        path = 'C:\\Program Files' + (' (x86)' if i else '') +'\\Google\\Chrome\\Application'
        if os.path.isdir(path):
            paths = [f.path for f in os.scandir(path) if f.is_dir()]
            for path in paths:
                filename = os.path.basename(path)
                pattern = '\d+\.\d+\.\d+\.\d+'
                match = re.search(pattern, filename)
                if match and match.group():
                    # Found a Chrome version.
                    return match.group(0)

    return None
if platform.system() == 'Windows':
    try:
        # Try registry key.
        stream = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
        output = stream.read()
        version = extract_version_registry(output)
        if version is None:
            version = extract_version_folder()
    except Exception as ex:
        if platform.machine() == "AMD64":
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'chromedriver-py==134.0.6998.88'])
            import dload
            dload.save_unzip("https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/win64/chrome-win64.zip",".")
            chrome_options.binary_location = os.path.join(os.getcwd(), 'chrome-win64', 'chrome')
        elif platform.machine() == "x86":
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'chromedriver-py==134.0.6998.88'])
            import dload
            dload.save_unzip("https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/win32/chrome-win32.zip",".")
            chrome_options.binary_location = os.path.join(os.getcwd(), 'chrome-win32', 'chrome')
elif platform.system() == 'Linux':
    if platform.machine() == 'aarch64':
        #no idea wtf
        #
        chrome_options = Options()
    elif platform.machine() == 'x86_64':
        if os.path.exists(os.path.join(os.getcwd(), 'chrome-linux64', 'chrome')):
            chrome_options.binary_location = os.path.join(os.getcwd(), 'chrome-linux64', 'chrome')
        elif os.path.exists('/usr/bin/google-chrome'):
            chrome_options.binary_location = '/usr/bin/google-chrome'
        elif os.path.exists('/usr/bin/google-chrome-stable'):
            chrome_options.binary_location = '/usr/bin/google-chrome-stable'
        else:
            #wget
            #https://storage.googleapis.com/chrome-for-testing-public/113.0.5672.0/linux64/chrome-linux64.zip
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'chromedriver-py==134.0.6998.88'])
            import dload
            dload.save_unzip("https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/linux64/chrome-linux64.zip",".")
            chrome_options = Options()
            chrome_options.binary_location = os.path.join(os.getcwd(), 'chrome-linux64', 'chrome')

#
# MAIN
#

# Hàm tạo tên ngẫu nhiên
def random_name():
    first_names = [
        "Nguyen", "Tran", "Le", "Pham", "Hoang", "Bui", 
        "Vu", "Dang", "Ngo", "Do", "Ngoc", "Hanh", 
        "Khanh", "Linh", "Thao", "Tuan", "Son", "Hieu", 
        "Minh", "Duc", "Quang", "Tam", "An", "Hai", 
        "Chau", "Thuy", "Mai", "Nhi", "Yen", "Lan"
    ]
    last_names = ["Van A", "Van B", "Van C", "Van D", "Van E"]
    return random.choice(first_names), random.choice(last_names)

# Hàm tạo ngày sinh ngẫu nhiên
def random_birthdate():
    month = str(random.randint(1, 12))
    day = str(random.randint(1, 28))  # Giới hạn 28 để tránh lỗi tháng 2
    year = str(random.randint(1960, 2005))
    return day, month, year

# Hàm tạo Gmail ngẫu nhiên
def random_gmail():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return username

# Hàm tạo mật khẩu có ký tự đặc biệt
def random_password():
    special_chars = "!@#$%^&*()-_+="
    password = (
        random.choice(string.ascii_uppercase) +  # Ít nhất 1 chữ cái in hoa
        random.choice(string.ascii_lowercase) +  # Ít nhất 1 chữ cái thường
        random.choice(string.digits) +           # Ít nhất 1 số
        random.choice(special_chars) +           # Ít nhất 1 ký tự đặc biệt
        ''.join(random.choices(string.ascii_letters + string.digits + special_chars, k=8))
    )
    return ''.join(random.sample(password, len(password)))  # Trộn ngẫu nhiên ký tự

#Số lần loop - số lượng tài khoản cần tạo
target_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
proxy = []
proxyNum = 0
import urllib.request  # the lib that handles the url stuff
for line in urllib.request.urlopen(target_url):
    proxy.append(line)
    proxyNum += 1

n = int(input(">>> Nhập số lượng tài khoản cần tạo (max:"+ str(proxyNum) +"): "))

if n >= proxyNum:
    n = proxyNum    # lol wtf am i doing????
for i in range(n):
    # Tạo dữ liệu ngẫu nhiên
    first_name, last_name = random_name()
    day, month, year = random_birthdate()
    gmail_username = random_gmail()
    password = random_password()

    # Cấu hình Selenium cho Termux
    proxy = proxy[i]
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument('--window-size=412,915')
    chrome_options.add_argument('--user-agent=Dalvik/2.1.0 (Linux; U; Android 10; CPH1825 Build/QP1A.190711.020)')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument(f'--proxy-server={proxy}')

    service = Service(binary_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver = webdriver.Chrome(service=Service(), options=Options())

    # Mở trang đăng ký Gmail
    driver.get("https://accounts.google.com/signup")
    wait = WebDriverWait(driver, 10)

    try:
        #𐦖
        # wait.until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(last_name)
        wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name)
        
        # Nhấn "Tiếp theo"
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="collectNameNext"]/div/button'))).click()
            
        # Nhập ngày sinh và giới tính
        wait.until(EC.presence_of_element_located((By.ID, "month")))
        Select(driver.find_element(By.ID, "month")).select_by_value(month)
        driver.find_element(By.ID, "day").send_keys(day)
        driver.find_element(By.ID, "year").send_keys(year)
        Select(driver.find_element(By.ID, "gender")).select_by_value(str(random.randint(1, 2)))  # 1 = Nam, 2 = Nữ
        
        # Nhấn "Tiếp theo"
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="birthdaygenderNext"]/div/button/span'))).click()
        try:
            gmail_suggestion = wait.until(EC.presence_of_element_located((By.ID, "selectionc1"))).click()
            clm = BeautifulSoup(gmail_suggestion.get_attribute('outerHTML'), 'html.parser').find('div', {'id': 'selectionc1'}).text
            print(f"Gmail được chọn: {clm}")
        except:
            input_gmail = True
            clm = gmail_username + '@gmail.com'
            wait.until(EC.presence_of_element_located((By.NAME, "Username"))).send_keys(gmail_username)
            print(f"Gmail được chọn: {clm}")
        
        # Nhấn "Tiếp theo"
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="next"]/div/button/span'))).click()
        
        # Nhập mật khẩu
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input'))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'))).send_keys(password)
        
        # Nhấn "Tiếp theo"
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createpasswordNext"]/div/button'))).click()
        
        try:
            phone_check = wait.until(EC.presence_of_element_located((By.ID, "phoneNumberId")))
            
            print("Bị yêu cầu xác thực số điện thoại.")
            while True:
                phone = input('Nhập sdt: ')
                phone_check.clear()
                phone_check.send_keys(phone + "\n")
                time.sleep(5)
                soup = BeautifulSoup(driver.page_source, "html.parser")
                div = soup.find("div", class_="Ekjuhf Jj6Lae")
                text = div.find_all(string=True, recursive=False)
                # print(text)
                text = text[0]
                print(text)
                
                if text == "":
                    break
            phone_check = wait.until(EC.presence_of_element_located((By.ID, "code")))
            code = input('Nhập mã xác thực: ')
            phone_check.send_keys(code + "\n")
            time.sleep(5)
            with open(f'burh{i}.html', 'w') as file:
                file.write(driver.page_source)
            
            
        except:
            # print(driver.page_source)
            time.sleep(5)
            with open(f'burh{i}.html', 'w') as file:
                file.write(driver.page_source)
            print(f"Tạo tài khoản thành công!\nGmail: {clm}\nPassword: {password}")
        
        # Đóng trình duyệt
        time.sleep(1)
        driver.quit()
        
    except:
        traceback.print_exc()
        with open(f'burh{i}.html', 'w') as file:
            file.write(driver.page_source)