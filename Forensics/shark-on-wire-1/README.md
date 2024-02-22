# shark on wire 1

I downloaded the file, and it had the pcap extension, indicating that it is a Wireshark file. Wireshark is a programme that sniffs and analyses packets.



Most of the time, the packets we're interested in are UDP and TCP protocols; when I scrolled down, I noticed a lot of UDP traffic. I randomly selected one of those packets (simply click on it) and opened the data tab.


Is the data dispersed across multiple packets? To check this, you can use something called udp streams. To check those streams, select a random udp packet, and then right-clicked on it, followed by udp stream:



This stream has all the text in the window, but it's just junk. Maybe this isn't the right stream, so I tried to check the others with the stream id changed.

---

<img width="1440" alt="Screenshot 2024-02-23 at 2 12 19 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/291bcb3f-4b2c-45a8-aa56-ba0ae817971d">

---

I found the flag in the 6th stream!

---

<img width="1440" alt="Screenshot 2024-02-23 at 2 08 20 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/fc9229a4-8bb6-4b59-b5e7-40b757a0cb17">

---
