from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
gecko_driver_path = 'c:\\Users\\DELL\\Desktop\\New folder\\geckodriver.exe'
#OR gecko_driver_path = r'c:\Users\DELL\Desktop\New folder\geckodriver.exe'

firefox_options = webdriver.FirefoxOptions()
# Thêm các tùy chọn nếu cần thiết
# firefox_options.add_argument('--headless')

# Sử dụng service để cấu hình đường dẫn đến geckodriver
service = webdriver.firefox.service.Service(gecko_driver_path)

# Khởi tạo trình duyệt Firefox
driver = webdriver.Firefox(service=service, options=firefox_options)
driver.set_window_size(700,800)
# Mở trang web
driver.get('https://www.facebook.com/')

# Tìm và click vào ô input có id là 'email'
input_element = driver.find_element('id', 'email')
input_element.click()
# Gửi dữ liệu vào ô input
input_element.send_keys('0838678950')

# Nhap Pass
# nk = driver.find_element('id','pass')
# nk.click()
# nk.send_keys("Handsome@98")
driver.find_element('id','pass').send_keys("Handsome@98")
 
element_name = driver.find_element(By.NAME, 'login')
element_name.click()
# Thực hiện thêm các thao tác khác nếu cần thiết

# Đóng trình duyệt



