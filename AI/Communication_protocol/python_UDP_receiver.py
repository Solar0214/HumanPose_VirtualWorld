import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 소켓을 생성한다
sock.bind(("127.0.0.1", 8080))
while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode().upper()
    sock.sendto(data.encode(), addr)
    print(data, addr)
sock.close()