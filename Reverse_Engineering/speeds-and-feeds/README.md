# speeds and feeds

---
AUTHOR: RYAN RAMSEYER

Description
There is something on my shop network running at nc mercury.picoctf.net 59953, but 
I can't tell what it is. Can you?

---
so when we connect to the challenge it will give g-codes. which is basicallya geo coordinates. 
save the g-codes in a file

```bash
nc mercury.picoctf.net 59953 > gcodes.txt
```


we can decode it online. upload the file  on this website https://ncviewer.com/

<img width="1396" alt="Screenshot 2024-06-24 at 10 07 05 PM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/7aa9985b-3e2e-4c52-bf6d-b20679518df3">

---

flag:```picoCtf{num3r1cal_c0ntr0l_f3fea95b}```

---
