# Jack of all trades

found a name johny graves has a twitter and a tweet for his encryption

below is a base64 string
```
Remember to wish Johny Graves well with his crypto jobhunting! His encoding systems are amazing! Also gotta remember your password: u?WtKSraq

``` 

his encryption methods:

```
My Favourite Crypto Method:
First encode your message with a ROT13 cipher. Next Convert it to Hex. Finally convert the result into Base32.
It's uncrackable!
```

also found /recovery.php
```
UmVtZW1iZXIgdG8gd2lzaCBKb2hueSBHcmF2ZXMgd2VsbCB3aXRoIGhpcyBjcnlwdG8gam9iaHVudGluZyEgSGlzIGVuY29kaW5nIHN5c3RlbXMgYXJlIGFtYXppbmchIEFsc28gZ290dGEgcmVtZW1iZXIgeW91ciBwYXNzd29yZDogdT9XdEtTcmFxCg
```
decoding that
```
Remember that the credentials to the recovery login are hidden on the homepage! I know how forgetful you are, so here's a hint: bit.ly/2TvYQ2S
```

steg -> steghide

##found creds in header.jpg

```
?cmd=
```
gives RCE

we have a jacks password list in home
using hydra to bruteforce ssh

jacks password:
```
ITMJpGGIqg1jn?>@
```

get user.jpg for user flag

```
 /usr/bin/strings /root/root.txt
``` 
for root flag