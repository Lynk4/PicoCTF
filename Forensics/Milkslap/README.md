# Milkslap


The milk character in the description refers to this website: http://mercury.picoctf.net:16940/ .

The webpage contains a gif of a man getting milk dumped on him. Because the hint refers to the problem category, which is forensics, we should locate the image. Going to the code and then the CSS, we notice that the image is at the URL http://mercury.picoctf.net:16940/concat_v.png.

---

<img width="1152" alt="Screenshot 2024-02-22 at 9 15 15 PM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/0cbdf88f-786a-4f2d-ba05-d939648d526b">

---

<img width="1125" alt="Screenshot 2024-02-23 at 1 16 01 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/98d985ce-83be-4736-bb2d-544e7d9afda1">


---

The image is 1280x47520 png. This is probably where the flag is. After downloading the image, we can run a variety of forensics programmes on it. After a time, we came upon zsteg and used it on the image:

#### If zsteg in not working well...

try this command to obatin the flag.

```
RUBY_THREAD_VM_STACK_SIZE=500000000 zsteg concat_v.png
```
---

<img width="1440" alt="Screenshot 2024-02-23 at 1 16 27 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/7041b79e-7e34-4337-a753-8ab6e7e8c2ca">


---

After a while you willl get a flag.........

FLAG```picoCTF{imag3_m4n1pul4t10n_sl4p5}```

---

