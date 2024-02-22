# Milkslap


The milk character in the description refers to this website: http://mercury.picoctf.net:16940/ .

The webpage contains a gif of a man getting milk dumped on him. Because the hint refers to the problem category, which is forensics, we should locate the image. Going to the code and then the CSS, we notice that the image is at the URL http://mercury.picoctf.net:16940/concat_v.png.

The image is 1280x47520 png. This is probably where the flag is. After downloading the image, we can run a variety of forensics programmes on it. After a time, we came upon zsteg and used it on the image:

If zsteg in not working well

try this command to obatin the flag.

```
RUBY_THREAD_VM_STACK_SIZE=500000000 zsteg concat_v.png

```

After a while you willl get a flag.........

FLAG```picoCTF{imag3_m4n1pul4t10n_sl4p5}```

