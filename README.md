# Installation
Shouldn't need anything by the default python install. But in case it does this program uses os, sys, subprocess, and argparse.

Which would just be a simple `pip install <package-name>`


# Instructions Notes
-l or --list is to list all your vm's
other than that its just
`python copypasta.py *vm name* *'the string you want to send surrounded by single quotes'*


## Examples
`python copypasta.py uwu11 'https://www.google.com/'`
or
`python copypasta.py -l`
 

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
This link also has more notes about what hexadecimal value press what keys.

## Why you're here & running the whole command

I'm lazy as shit. I didn't want to do all the work to set up a spice server just to be able to copy and paste some stuff sometimes. That's also why I used python, no offense but its a pretty lazy programming language but also convenient when I don't wanna open an IDE to program things and stuff. 


# TL;DR
This is a lazy way to copy and paste text into a QEMU/Libvirt VM. 
