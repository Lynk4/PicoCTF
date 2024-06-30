# Transformation 

Let’s examine the “enc” file to understand its content. 

---
<img width="713" alt="Screenshot 2024-04-01 at 7 55 30 PM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/dffdff0a-a874-4745-9f73-6d09e1a331e3">

---

Option 1: CyberChef (online decoder)

Extract the encoded text from the "enc" file.
Go to the CyberChef website (https://gchq.github.io/CyberChef/).
Copy the encoded text and paste it into the CyberChef input box.
Utilise the "From UTF-8" procedure.
CyberChef will decode the data and display the resultant flag.


---
<img width="1440" alt="solution" src="https://github.com/Lynk4/PicoCTF/assets/44930131/63a3c167-4692-47fa-8140-e26f47bb55c6">

---


Option 2: Python Script:

Python code that decodes the encoded flag:

---
<img width="1440" alt="Screenshot 2024-04-01 at 7 58 18 PM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/77393ab5-7420-4afa-8d44-ca40f083532c">

---

Flag: 
```
picoCTF{16_bits_inst34d_of_8_26684c20}
```

---
