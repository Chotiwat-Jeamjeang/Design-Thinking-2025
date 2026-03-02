# Design-Thinking-2025
โปรเจครายวิชาการคิดเชิงออกแบบสำหรับวิทยาการข้อมูล เรื่อง ระบบบันทึกการใช้บริการสนามแบดมินตัน

<img width="1278" height="570" alt="image" src="https://github.com/user-attachments/assets/2892f735-ec56-4f6a-87a9-05ed6bd1b92d" />

## ระบบบันทึกการใช้บริการสนามแบดมินตัน(Badminton Court Usage Logging System)
เป็นระบบบันทึกการจองสนามแบดมินตันให้กับกองพัฒนาคุณภาพนิสิตและนิสิตพิการของมหาวิทยาลัยพะเยา เพื่อช่วยลดการใช้กระดาษ เพิ่มความสะดวกสบาย และยกระดับการจัดการได้อย่างมีประสิทธิภาพ

## ฟีเจอร์หลัก
- ฟีเจอร์ที่ 1 ระบบจองสนามแบดมินตัน
- ฟีเจอร์ที่ 2 ระบบ Log in
- ฟีเจอร์ที่ 3 ตารางแสดงการจองสนามแบดมินตัน
- ฟีเจอร์ที่ 4 ระบบเก็บข้อมูลใน Database

## สมาชิกและภาระงาน (Team Members & Responsibilities)

ตารางแสดงการแบ่งงานรายสัปดาห์ระหว่างสมาชิกทั้ง 2 คน:

| สัปดาห์ที่ (Week) | [นางสาวพัชราภรณ์ พวงสุวรรณ์] | [นายโชติวัฒน์ แจ่มแจ้ง] |
| :--- | :--- | :--- |
| **Week 1** | วางแผนโครงงาน ออกแบบ UI/UX | วางแผนโครงงาน และรวบรวมความต้องการ |
| **Week 2** | จัดเตรียมและทำความสะอาดข้อมูล (Data Preprocessing) | พัฒนาส่วนเชื่อมต่อกับผู้ใช้ (Frontend Layout) |
| **Week 3** | สกัดข้อมูลจากเว็บ (Web Scarping) | พัฒนาโมเดลหรือลอจิกเบื้องหลัง (Backend Logic) และ เชื่อมต่อโมเดลเข้ากับหน้าเว็บ Streamlit |
| **Week 4** | จัดทำเอกสารประกอบโครงงาน และ Deploy | ทดสอบระบบ (Testing) และแก้ไข Bug |

---

## เทคโนโลยีที่ใช้ (Tech Stack)
- **Language:** Python
- **Framework:** Streamlit
- **Libraries(Web Application):** streamlit, booking, datetime, database, auth, sqlite3,
- **Libraries(Web Scarping):** selenium, webdriver-manager, requests, time, calendar, datetime, os

## 📦 การติดตั้งและการใช้งาน (Setup & Installation)

**Clone repository นี้:**
   ```bash
   git clone [https://github.com/Chotiwat-Jeamjeang/Design-Thinking-2025.git](https://github.com/Chotiwat-Jeamjeang/Design-Thinking-2025.git)
   cd Design-Thinking-2025

# https://design-thinking-2025-main.streamlit.app/
