# Syllabus259191
[ENG CMU 259191](https://elearning.cmu.ac.th/course/view.php?id=552)

## How to use
โหลดไฟล์ exe จากใน dist ได้เลยสำหรับ windows

หากใช้ linux, mac ให้โหลด Syllabus.py ไปเก็บไว้
ให้ลง module ก่อน 
```
requests, gevent, BeautifulSoup4 ก่อน
```
การใช้งาน เปิด terminal ขึ้นหาไปที่ path ที่เก็บ Syllabus.py ไว้
```
$ python Syllabus.py
```

Pole id หาได้จาก url ของกิจกรรมที่จะเข้า หน้าตาแบบนี้
```
    https://elearning.cmu.ac.th/mod/choice/view.php?id=[Pole id]
```

ตัวอย่าง
``` 
    https://elearning.cmu.ac.th/mod/choice/view.php?id=24482 
```
Pole id คือ 24482

Choice ปรกติเป็น 1 และ 2 เป็นไม่เข้าร่วม ยกเว้นบางกิจกรรมที่มีหลายรอบ


