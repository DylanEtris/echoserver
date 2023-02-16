import unittest
import socket
import select
import subprocess
import os
import signal

class TestEchoServer(unittest.TestCase):
    HOST = 'localhost'
    PORT = 10823

    def setUp(self):
        self.p = subprocess.Popen(['./bin/echoserver'])
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tearDown(self) -> None:
        os.kill(self.p.pid, signal.SIGKILL)
        self.p.wait()
        self.s.close()
        
    def test_echoserver(self):
        self.s.connect((self.HOST, self.PORT))
        self.s.sendall(b'Hello, world')
        data = self.s.recv(1024)
        self.assertEqual(data, b'Hello, world')

if __name__ == '__main__':
    unittest.main()