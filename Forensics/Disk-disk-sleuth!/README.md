# Disk, disk, sleuth!


Use srch_strings from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz


This was a pretty straitforward challenge, after extracting the zip file I ran the search string command and piped that into grep:

---

<img width="1071" alt="Screenshot 2024-02-22 at 9 09 09 PM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/e4721bc1-d35e-4a03-a4d3-a17adb083b0d">


---


srch_strings -a dds1-alpine.flag.img| grep picoCTF

  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_ad5c96c0}
