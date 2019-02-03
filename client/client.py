import socket
import sys
import zipfile
import os

host = '127.0.0.1'
port = 1337
k = int(sys.argv[1])
zip_name = 'main.zip'

s = socket.socket()
print('[+] Client socket is created.')

s.connect((host, port))
print('[+] Socket is connected to {}'.format(host))

with zipfile.ZipFile(zip_name, 'w') as file:
	for j in range(1, (k+1)):
		file.write('{}.jpg'.format(j))
		print('[+] {}.jpg is sent'.format(j))

s.send(zip_name.encode())

f = open(zip_name, 'rb')
l = f.read()
s.sendall(l)

os.remove(zip_name)
f.close()
s.close()