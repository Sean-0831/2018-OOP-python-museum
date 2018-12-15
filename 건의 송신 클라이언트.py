import socket

# 접속할 서버의 정보
server_ip = '127.0.0.1' # 변경 가능
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)

# 메시지 전송
while True:
    try:
        data = input('>')
    except KeyboardInterrupt:
        break
    if data == '!quit' or '':
        break

    mysock.send(bytes(data, 'UTF-8'))
# 종료
mysock.close()
print("연결 종료")