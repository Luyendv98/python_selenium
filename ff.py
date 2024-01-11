from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pyautogui as pag
gecko_driver_path = r'c:\Users\DELL\Desktop\New folder\geckodriver.exe'

firefox_options = webdriver.FirefoxOptions()
# Thêm các tùy chọn nếu cần thiết
# firefox_options.add_argument('--headless')

# Sử dụng service để cấu hình đường dẫn đến geckodriver
service = webdriver.firefox.service.Service(gecko_driver_path)

# Khởi tạo trình duyệt Firefox
driver = webdriver.Firefox(service=service, options=firefox_options)

# Mo trang web
driver.get('https://www.facebook.com/')
pag.hotkey('ctrl','t')
driver.get('https://www.youtube.com/')


# element_by_id = driver.element_by_id('email')
# element_by_id.click()
# # gui du lieu vao o input
# input_element.send_keys('0838678950')



# Tiếp tục với công việc của bạn

# print(webdriver.__version__)

# # # Khởi tạo trình duyệt Firefox

# print("Before driver initialization")
# driver = webdriver.Firefox(executable_path=r'c:\Users\DELL\Desktop\New folder\geckodriver.exe')
# print("After driver initialization")

# # # # Đường dẫn đến tập tin GeckoDriver
# # # gecko_driver_path = '/đường/dẫn/tới/geckodriver'

# # # # Khởi tạo trình duyệt Firefox
# # # driver = webdriver.Firefox(executable_path=gecko_driver_path)

# # # Các thao tác khác với trình duyệt...
# # time.sleep(5)
# # # Đóng trình duyệt
# # driver.quit()