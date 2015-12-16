"""HTTP Requests with Python

=================   Using urllib:   ==================
import urllib
urlhandler = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in urlhandler:
    print line.strip()
======================================================
"""

import socket

def make_socket():
    """Create a socket to a host, port."""

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(('www.py4inf.com', 80))
    my_socket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
    return my_socket

def main():
    """Main function."""

    my_socket = make_socket()
    print "\n"
    while True:
        data = my_socket.recv(512)
        if len(data) < 1:
            break
        print data
    my_socket.close()

if __name__ == '__main__':
    main()
