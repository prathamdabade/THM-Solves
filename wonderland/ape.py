import requests
import string

allchars = string.ascii_lowercase

url = "http://10.10.19.244/"

while True:
	count = 0
	for char in allchars:
		fuzzurl = url + char + "/"
		print(fuzzurl)
		r = requests.get(fuzzurl)
		if "404" not in r.text :
			print("/"+char)
			url = fuzzurl
			break
		count += 1
	if count > 24:
		break		