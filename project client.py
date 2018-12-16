import re
import socket
import threading

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)

with open('wordslistUnique.txt', 'rt', encoding='utf-8') as f:
    s = f.read()

pat = re.compile('^[가-힣]+$')
wordDict = dict()
hanbangSet = set()
alreadySet = set()
lastWord = ''

# [출처] 파이썬 1인용 끝말잇기 | 작성자 njw1204
# 한글로 이루어져 있고, 길이가 2 이상인 단어 추출
for i in sorted([i for i in s.split() if pat.match(i) and len(i) >= 2], key=lambda x:-len(x)):
    if i[0] not in wordDict:
        wordDict[i[0]] = set()
    wordDict[i[0]].add(i)

# 한방단어 제거 & 추출
delList = list()
for i in wordDict:
    for j in wordDict[i]:
        if j[-1] not in wordDict:
            delList.append(j)
for j in delList:
    hanbangSet.add(j)
    wordDict[j[0]].remove(j)

def userKKUTU(word):
    global lastWord
    while True:
        yourWord = word
        firstLetter = yourWord[0]
        if firstLetter != lastWord[-1]:
            print(" [오류] '" + lastWord[-1] + "' (으)로 시작하는 단어를 입력하세요.")
            break
        elif yourWord in hanbangSet:
            print(' [오류] 한방단어는 사용할 수 없습니다.')
            break
        elif yourWord in alreadySet:
            print(' [오류] 이미 나온 단어입니다.')
            break
        elif yourWord not in wordDict.get(firstLetter, set()):
            print(' [오류] 사전에 없는 단어입니다.')
            break
        else:
            alreadySet.add(yourWord)
            lastWord = yourWord
            break


def receive():
    global mysock
    global lastWord
    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break
        except OSError:
            print("서버와의 접속을 끊었습니다.")
            break

        print(data.decode('UTF-8'))  # 서버로 부터 받은 값을 출력
        lastWord = data

def main_thread():
    global mysock
    global lastWord
    a = lastWord
    # 메시지 받는 스레스 시작
    thread_recv = threading.Thread(target=receive, args=())
    thread_recv.start()
    while True:
        while True:
            try:
                data = input('>')
            except KeyboardInterrupt:
                continue
            userKKUTU(data)
            if a != lastWord:
                break

        try:
            mysock.send(bytes(lastWord, 'UTF-8'))  # 서버에 메시지를 전송
        except ConnectionError:
            break

thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()

# 메시지를 받고, 보내는 스레드가 종료되길 기다림
thread_main.join()

# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()