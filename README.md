# Installation

Well ya know just $git clone *url*

    chmod +x copypasta.py
    chmod +x copypasta.sh


# Additional Notes

Right so and forgive me for saying this, I'm using Arch. Virsh commands need to be ran as root/super user. In the past I've had issues with scripts and sudo prompts. The attempt was to always force a pop up prompt the user for a password. However, then I realized that because you're running this in terminal and that's super not needed. However, in my journey across stackoverflow I found some helpful code. 

   ```bash
#!/bin/bash
echo -n Password: 
read -s password
echo
echo $password
```
The `read -s` will turn off echo for you. Just replace the `echo` on the last line with the command you want to run.
OR
```bash
read -s -p "Password: " password
```
OR straight up remove sudo from inside the bash script then when running the script from terminal toss a sudo in front of that bad boy. 
```bash 
sudo ./copypasta.sh
```

The only reason I mentioned by distro was because the first two options were being dumb and not working. 
 

## Useful Notes

[# KVM virsh send-key example (Control-Alt-Delete and more)](https://rentry.co/x563n)
Things like;
```bash
--holdtime 1000
``` 
holds the key down for a hot minute and
```bash
KEY_LEFTCRTL
```
are also valid.
This link also has more notes about what hexadecimal (is it hex for short?) press what keys. 

## Why you're here & running the whole command

I'm lazy as shit. I didn't want to do all the work to set up a spice server just to be able to copy and paste some stuff sometimes. That's also why I used python, no offense but its a pretty lazy programming language but also convenient when I don't wanna open an IDE to program things and stuff. 

```bash
./copypasta.py && ./copypasta.sh
```
There's probably a way to set that exact command in a env/bin option so you don't have to do
```bash
cd /path/to/file
./copypasta.py && ./copypasta.sh
```
However, I'm too lazy to figure it out. 
What something like
```bash
cd /usr/bin
nano lazy.sh
#!/bin/bash
cd copypastafiles/
./copypasta.py && ./copypasta.sh
#ctrl s && ctrl x
chmod +x lazy.sh
```
And now you can open it up from your default new terminal window/tab probably maybe. Probably need to adjust the env vars. 

# TL;DR
This is a lazy way to copy and paste text into a QEMU/Libvirt VM. 
