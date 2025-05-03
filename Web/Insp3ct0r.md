# Insp3ct0r

### Description

Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/44924/ (link) or http://jupiter.challenges.picoctf.org:44924

## Hints 
How do you inspect web code on a browser?

There's 3 parts

## Solution
Right click and inspect the website

<img width="1440" alt="Screenshot 2023-05-12 at 3 15 14 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/f50bf7e8-cff1-45f8-be8a-919a3f102761">


go to sources tab
There we can find three files....
1. Index
2. mycss.css
3. myjs.js

All the above files contains 3 parts of the flags.....

### In index
<img width="1166" alt="Screenshot 2023-05-12 at 3 14 24 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/ffbbc659-d77b-4a57-86cc-6bfacdcb25e4">

### In mycss.css
<img width="1171" alt="Screenshot 2023-05-12 at 3 14 45 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/336d88fa-2219-401b-9398-ec959a20b8d0">

### In myjs.js


<img width="1176" alt="Screenshot 2023-05-12 at 3 14 56 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/ee760c67-2ecb-4ea1-a621-42a3a54b2682">

## FLAG picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}

