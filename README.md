# Syllabus259191
[ENG CMU 259191](https://elearning.cmu.ac.th/course/view.php?id=552)

## How to use
โหลดไฟล์ exe จากในแถบ release ได้เลยสำหรับ windows

หากใช้ linux, mac ให้ดาวน์โหลด Syllabus.py ไปเก็บไว้
ลง module ตามนี้ก่อน โดยใช้ python pip หรือื่น ๆ
```
requests
gevent
BeautifulSoup4
```
การใช้งาน เปิด terminal ขึ้นหาไปที่ path ที่เก็บ Syllabus.py ไว้
```
$ python Syllabus.py
```

Poll id หาได้จาก url ของกิจกรรมที่จะเข้า หน้าตาแบบนี้
```
    https://elearning.cmu.ac.th/mod/choice/view.php?id=[Poll id]
```

ตัวอย่าง
``` 
    https://elearning.cmu.ac.th/mod/choice/view.php?id=24482 
```
Poll id คือ 24482

Choice ปรกติเป็น 1 และ 2 เป็นไม่เข้าร่วมดังรูป ยกเว้นบางกิจกรรมที่มีหลายรอบ

![Example Poll](http://chawasit.github.io/259191.png)

(1 ในรูปตัวอย่างคือ "รอบที่ 1", 2 คือ "ไม่เข้าร่วม"")


