# unpackme.py

Description:

Can you get the flag?
Reverse engineer this Python program.

---
let's review the source code:

```python3
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABkzWGO_8MlYpNM0n0o718LL-w9m3rzXvCMRFghMRl6CSZwRD5DJOvN_jc8TFHmHmfiI8HWSu49MyoYKvb5mOGm_Jn4kkhC5fuRiGgmwEpxjh0z72dpi6TaPO2TorksAd2bNLemfTaYPf9qiTn_z9mvCQYV9cFKK9m1SqCSr4qDwHXgkQpm7IJAmtEJqyVUfteFLszyxv5-KXJin5BWf9aDPIskp4AztjsBH1_q9e5FIwIq48H7AaHmR8bdvjcW_ZrvhAIOInm1oM-8DjamKvhh7u3-lA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())


```

As we can see there's a execution in the last line. 

***Never execute payload directly you never know what's inside the payload.***

What we can do is comment out the exec :

---

```python3
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABkzWGO_8MlYpNM0n0o718LL-w9m3rzXvCMRFghMRl6CSZwRD5DJOvN_jc8TFHmHmfiI8HWSu49MyoYKvb5mOGm_Jn4kkhC5fuRiGgmwEpxjh0z72dpi6TaPO2TorksAd2bNLemfTaYPf9qiTn_z9mvCQYV9cFKK9m1SqCSr4qDwHXgkQpm7IJAmtEJqyVUfteFLszyxv5-KXJin5BWf9aDPIskp4AztjsBH1_q9e5FIwIq48H7AaHmR8bdvjcW_ZrvhAIOInm1oM-8DjamKvhh7u3-lA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
# exec(plain.decode())
print(plain.decode())

```

---

by running this we get our flag:

---

```bash
❯ python3 unpackme.flag.py

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_5274ff21}')
else:
  print('That password is incorrect.')


```

---

Make sure you have installed python cryptography package:
if not install. It is required by the program.

```bash
pip install cryptography
```

