Scan IP with .250 suffix

Generate IPs with .250 in China, then you can scan them with Zmap.

First need install `ipaddr` package of python.

	pip install ipaddr --user

Then, generate ip list:
	
	python genip.py

Zmap scan command is:

	zmap -p 80 -w ips.txt -o result.csv

Done !

IP range of China Come from [https://github.com/17mon/china_ip_list](https://github.com/17mon/china_ip_list)
