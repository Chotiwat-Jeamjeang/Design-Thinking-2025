from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import calendar
from datetime import datetime
import requests
import os

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
    
    # 4. ดึงข้อมูล
    # สร้างโฟลเดอร์สำหรับเก็บรูปภาพ
    image_dir = "scraped_images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    
    # ดึงรูปภาพจากหน้าเว็บ
    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"พบรูปภาพทั้งหมด {len(images)} รูปในหน้านี้\n")
    
    for i, img in enumerate(images):
        src = img.get_attribute("src")
        if src:
            # ตรวจสอบว่าเป็น URL เต็มหรือไม่
            if not src.startswith("http"):
                src = url + "/" + src.lstrip("/")
            
            try:
                response = requests.get(src)
                if response.status_code == 200:
                    # สร้างชื่อไฟล์
                    filename = f"image_{i+1}.png"
                    filepath = os.path.join(image_dir, filename)
                    
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                    
                    print(f"ดาวน์โหลดรูปภาพ: {filename}")
            except Exception as e:
                print(f"ไม่สามารถดาวน์โหลดรูปภาพ {src}: {e}")
    
    # ดึงข้อมูล taskbar หรือ navigation bar
    print("\n" + "="*50)
    print("ดึงข้อมูล Taskbar/Navigation")
    print("="*50 + "\n")
    
    # ค้นหา navigation elements (อาจเป็น nav, ul, li หรือ a tags ใน navigation)
    nav_elements = driver.find_elements(By.CSS_SELECTOR, "nav a, .navbar a, .nav a, header a, .menu a")
    if not nav_elements:
        # ถ้าไม่พบ ให้ลองหา a tags ที่อาจเป็น navigation
        nav_elements = driver.find_elements(By.TAG_NAME, "a")
    
    print(f"พบลิงก์ navigation ทั้งหมด {len(nav_elements)} ลิงก์\n")
    
    navigation_data = []
    for i, link in enumerate(nav_elements[:10]):  # จำกัดแค่ 10 ลิงก์แรกเพื่อไม่ให้เยอะเกินไป
        href = link.get_attribute("href")
        text = link.text.strip()
        if text and href:  # ตรวจสอบว่ามีข้อความและลิงก์
            navigation_data.append({"text": text, "url": href})
            print(f"{i+1}. {text} -> {href}")
    
    # บันทึกข้อมูล navigation ลงไฟล์
    if navigation_data:
        nav_file = "scraped_navigation.txt"
        with open(nav_file, "w", encoding="utf-8") as f:
            f.write("Navigation Links from Scraping:\n")
            f.write("="*50 + "\n")
            for item in navigation_data:
                f.write(f"{item['text']} -> {item['url']}\n")
        print(f"\nบันทึกข้อมูล navigation ลงไฟล์: {nav_file}")
    
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