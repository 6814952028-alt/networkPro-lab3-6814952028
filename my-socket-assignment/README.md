# แบบฝึกหัด Socket API & Docker

**ข้อมูลผู้จัดทำ**
- ชื่อ-นามสกุล: [สุวิจกขณ์ ไฝ่แจ้คำมูล]
- รหัสนักศึกษา: [6814952028]
- กลุ่ม/เซกชัน: [2]

---

## แบบฝึกหัดที่ 1: ระบบ Chat ด้วย Docker (2 Clients & 1 Server)

### คำอธิบายการทำงาน
ระบบแชตใช้ Socket API แบบ TCP โดยมี Server ตัวเดียวรับข้อความจาก Client แล้วกระจาย (broadcast) ไปยัง Client ตัวอื่น ทั้ง Server และ Client รันแยกกันใน Docker Container ผ่าน Docker Compose

### วิธีรัน
1. เข้าโฟลเดอร์แบบฝึกหัดที่ 1
   ```bash
   cd exercise-1
   ```
2. สร้างและรันคอนเทนเนอร์
   ```bash
   docker compose up --build
   ```
3. เปิด Terminal ใหม่ เพื่อเข้า Client 1
   ```bash
   docker exec -it chat_client1 bash
   python client.py
   ```
4. เปิด Terminal ใหม่ เพื่อเข้า Client 2
   ```bash
   docker exec -it chat_client2 bash
   python client.py
   ```
5. พิมพ์ข้อความใน Client หนึ่ง แล้วดูว่าไปแสดงที่อีก Client
6. ปิดระบบ
   ```bash
   docker compose down
   ```

---

## แบบฝึกหัดที่ 2: เว็บแอป Flask ส่งข้อความไป Socket Server

### คำอธิบายการทำงาน
ผู้ใช้กรอกข้อความในฟอร์มบนหน้าเว็บ (Flask) ด้วย POST method จากนั้น Flask ส่งข้อความไปยัง Socket Server ผ่าน Socket API แล้วรับคำตอบ (Echo) กลับมาแสดงบนหน้าเว็บ แยกเป็น 2 คอนเทนเนอร์: `web_app` และ `socket_server`

### วิธีรัน
1. เข้าโฟลเดอร์แบบฝึกหัดที่ 2
   ```bash
   cd exercise-2
   ```
2. สร้างและรันคอนเทนเนอร์
   ```bash
   docker compose up --build
   ```
3. เปิดเบราว์เซอร์ไปที่ http://localhost:5000 กรอกข้อความแล้วกด Send
4. หน้าเว็บจะแสดงข้อความที่ส่งและคำตอบ `Echo: ...` จาก Server
5. ปิดระบบ
   ```bash
   docker compose down
   ```

---

## ข้อกำหนดเบื้องต้น
- ติดตั้ง Docker Desktop
- ติดตั้ง WSL (สำหรับ Windows)