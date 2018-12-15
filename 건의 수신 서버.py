import socket

myip = '127.0.0.1' #임의
myport = 50000
address = (myip, myport)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

client_sock, client_addr = server_sock.accept()

newword = open("newword.txt", 'w')

# 클라이언트가 보내온 메시지를 받아 저장
def receive():
    global client_sock
    while True:
        try:
            data = client_sock.recv(1024)
            if data == '':
                break
            newword.write(data)
            newword.close()
        except OSError:
            print('연결이 종료되었습니다.')
            break
    client_sock.close()

while True:
    receive()

# 서버 종료
server_sock.close()