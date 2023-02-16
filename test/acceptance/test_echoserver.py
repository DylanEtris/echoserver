import unittest
import socket
import select
import subprocess
import os
import signal
import time

class TestEchoServer(unittest.TestCase):
    HOST = 'localhost'
    PORT = 10823

    def setUp(self):
        self.p = subprocess.Popen(["/home/ubuntu/dev/echoserver/bin/echoserver"])
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tearDown(self) -> None:
        os.kill(self.p.pid, signal.SIGKILL)
        self.p.wait()
        self.s.close()
        
    def test_echoserver(self):
        time.sleep(1)
        self.s.connect((self.HOST, self.PORT))
        self.s.sendall(b'Hello, world')
        data = self.s.recv(1024)
        self.assertEqual(data, b'Hello, world')

    def test_multiple_client_calls(self):
        time.sleep(1)
        self.s.connect((self.HOST, self.PORT))
        self.s.sendall(b'Hello, world')
        data = self.s.recv(1024)
        self.assertEqual(data, b'Hello, world')
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2.connect((self.HOST, self.PORT))
        s2.sendall(b'Hello, world')
        data = s2.recv(1024)
        self.assertEqual(data, b'Hello, world')
        s2.close()

if __name__ == '__main__':
    unittest.main()