# แบบฝึกหัด Socket API & Docker

**ข้อมูลผู้จัดทำ**
- ชื่อ-นามสกุล: สุวิจกขณ์ ไผ่แจ้ตามูล
- รหัสนักศึกษา: 6814952028
- กลุ่ม/เซกชัน: 2

---

## แบบฝึกหัดที่ 1: ระบบ Chat ด้วย Docker (2 Clients & 1 Server)

### คำอธิบายการทำงาน
ระบบแชตใช้ Socket API แบบ TCP โดยมี Server ตัวเดียวรับข้อความจาก Client แล้วกระจาย (broadcast) ไปยัง Client ตัวอื่น ทั้ง Server และ Client รันแยกกันใน Docker Container ผ่าน Docker Compose

### โครงสร้างไฟล์
![โครงสร้างไฟล์](images/ex1-files.png)

### วิธีรัน
1. เข้าโฟลเดอร์แบบฝึกหัดที่ 1
   ```bash
   cd exercise-1
   ```
2. สร้างและรันคอนเทนเนอร์
   ```bash
   docker compose up --build
   ```
   ![รันระบบ](images/ex1-up.png)

3. ตรวจสอบคอนเทนเนอร์
   ```bash
   docker ps
   ```
   ![docker ps](images/ex1-ps.png)

4. เปิด Terminal ใหม่ เพื่อเข้า Client 1
   ```bash
   docker exec -it chat_client1 bash
   python client.py
   ```
5. เปิด Terminal ใหม่ เพื่อเข้า Client 2
   ```bash
   docker exec -it chat_client2 bash
   python client.py
   ```
6. พิมพ์ข้อความใน Client หนึ่ง แล้วดูว่าไปแสดงที่อีก Client

   ![ผลการแชต](images/ex1-chat.png)

7. ปิดระบบ
   ```bash
   docker compose down
   ```
   ![ปิดระบบ](images/ex1-down.png)

---

## แบบฝึกหัดที่ 2: เว็บแอป Flask ส่งข้อความไป Socket Server

### คำอธิบายการทำงาน
ผู้ใช้กรอกข้อความในฟอร์มบนหน้าเว็บ (Flask) ด้วย POST method จากนั้น Flask ส่งข้อความไปยัง Socket Server ผ่าน Socket API แล้วรับคำตอบ (Echo) กลับมาแสดงบนหน้าเว็บ แยกเป็น 2 คอนเทนเนอร์: `web_app` และ `socket_server`

### โครงสร้างไฟล์
![โครงสร้างไฟล์](images/ex2-files.png)

### วิธีรัน
1. เข้าโฟลเดอร์แบบฝึกหัดที่ 2
   ```bash
   cd exercise-2
   ```
2. สร้างและรันคอนเทนเนอร์
   ```bash
   docker compose up --build
   ```
3. ตรวจสอบคอนเทนเนอร์
   ```bash
   docker ps
   ```
   ![docker ps](images/ex2-ps.png)

4. เปิดเบราว์เซอร์ไปที่ http://localhost:5000

   ![หน้าฟอร์ม](images/ex2-form.png)

5. กรอกข้อความแล้วกด Send หน้าเว็บจะแสดงข้อความที่ส่งและคำตอบ `Echo: ...` จาก Server

   ![ผลลัพธ์](images/ex2-result.png)

6. Log ฝั่ง Socket Server

   ![log ของ socket server](images/ex2-log.png)

7. ปิดระบบ
   ```bash
   docker compose down
   ```
   ![ปิดระบบ](images/ex2-down.png)

---

## ข้อกำหนดเบื้องต้น
- ติดตั้ง Docker Desktop
- ติดตั้ง WSL (สำหรับ Windows)
