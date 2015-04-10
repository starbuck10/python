import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.95.148",21))
banner = s.recv(1024)

if ("FreeFloat Ftp Server (version 1.00)" in banner):
  print "[+] FreeFloat FTP Server is vulnerable."

elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
  print "[+] 3CDaemon FTP Server is vulberable."

elif ("Ability Server 2.34" in banner):
  print "[+] Ability Server is vulnerable."

elif ("Sami FTP Server 2.0.2" in banner):
  print "[+] Sami FTP Server is vulberable."

else:
  print "[-] FTP Server is not vulnerable."
