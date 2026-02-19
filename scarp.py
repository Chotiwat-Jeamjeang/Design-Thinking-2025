from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import calendar
from datetime import datetime

# 1. ตั้งค่า Chrome Options (เช่น ปรับให้ทำงานแบบ Background หรือไม่)
chrome_options = Options()
# chrome_options.add_argument("--headless") # เปิดบรรทัดนี้หากไม่ต้องการให้หน้าต่าง Browser เด้งขึ้นมา

# 2. เริ่มต้น WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3. ไปยังหน้าเว็บเป้าหมาย
    url = "https://dsq.up.ac.th/TIMETABLE-2"
    driver.get(url)
    time.sleep(2) # รอให้หน้าเว็บโหลดครู่หนึ่ง
    # 4. ดึงข้อมูล (ตัวอย่าง: ชื่อหนังสือทั้งหมดในหน้าแรก)
    calender = driver.find_elements(By.CSS_SELECTOR, ".tab-content m-t10")

    print(f"พบตารางเวลาทั้งหมด {len(calender)} ตารางในหน้านี้\n")

    # เก็บข้อมูลที่ scrap ได้
    scraped_data = []
    for book in calender:
        # ดึงราคา (อยู่ในคลาส .price_color)
        price = book.find_element(By.CSS_SELECTOR, ".rounded-md shadow-md").text
        scraped_data.append(price)
        print(f"ชื่อเรื่อง: {price}")
    
    # แสดงปฏิทินของเดือนปัจจุบัน
    print("\n" + "="*50)
    print("ปฏิทินเดือนปัจจุบัน")
    print("="*50 + "\n")
    
    now = datetime.now()
    cal = calendar.monthcalendar(now.year, now.month)
    
    # แสดงชื่อเดือนและปี
    month_name = calendar.month_name[now.month]
    print(f"{month_name} {now.year}\n")
    
    # แสดงวันในสัปดาห์
    print("จันทร์  อังคาร พุธ  พฤหัสบดี  ศุกร์  เสาร์  อาทิตย์")
    print("-" * 50)
    
    # แสดงตารางปฏิทิน
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "       "  # ว่างสำหรับวันที่ไม่อยู่ในเดือนนี้
            else:
                week_str += f"{day:>2}     "
        print(week_str)

finally:
    # 5. ปิด Browser
    driver.quit()

    