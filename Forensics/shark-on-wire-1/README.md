# shark on wire 1

I downloaded the file, and it had the pcap extension, indicating that it is a Wireshark file. Wireshark is a programme that sniffs and analyses packets.



Most of the time, the packets we're interested in are UDP and TCP protocols; when I scrolled down, I noticed a lot of UDP traffic. I randomly selected one of those packets (simply click on it) and opened the data tab.


Is the data dispersed across multiple packets? To check this, you can use something called udp streams. To check those streams, select a random udp packet, and then right-clicked on it, followed by udp stream:



This stream has all the text in the window, but it's just junk. Maybe this isn't the right stream, so I tried to check the others with the stream id changed.




I found the flag in the 6th stream!