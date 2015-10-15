# Syllabus259191
[ENG CMU 259191](https://elearning.cmu.ac.th/course/view.php?id=552)

## How to use
โหลดไฟล์ exe จากในแถบ release ได้เลยสำหรับ windows

หากใช้ linux, mac ให้โหลด Syllabus.py ไปเก็บไว้
ให้ลง module นี้ก่อน โดนใช้ python pip หรือื่น ๆ
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

![Example Poll](http://chawasit.github.io/259191.png)
Choice ปรกติเป็น 1 และ 2 เป็นไม่เข้าร่วมดังรูป ยกเว้นบางกิจกรรมที่มีหลายรอบ


