from socket import socket, AF_INET, SOCK_STREAM
import json

from storage import Storage


class Server:
    def __init__(self, ip, port, host_name, user_name, user_password, db_name):
        print(f'SERVER IP: {ip}\nSERVER PORT: {port}\n')
        self.storage = Storage(host_name, user_name, user_password, db_name)

        self.ser = socket(AF_INET, SOCK_STREAM)
        self.ser.bind(
            (ip, port)
        )
        self.ser.listen(3)

    @staticmethod
    def sender(user, text):
        user.send(text.encode('utf-8'))

    def start_server(self):
        while True:
            user, addr = self.ser.accept()
            print(f'CLIENT CONNECTED:\n\tIP: {addr[0]}\n\tPORT: {addr[1]}')
            self.listen(user)

    def listen(self, user):
        self.sender(user, 'YOU ARE CONNECTED!')
        is_work = True

        while is_work:
            try:
                data = user.recv(1024)
                self.sender(user, 'getted')
            except Exception as e:
                data = ''
                is_work = False

            if len(data) > 0:
                msg = json.loads(data.decode('utf-8'))
                req = msg['request']
                params = msg['params']

                if req == 'disconnect':
                    self.sender(user, 'YOU ARE DISCONNECTED!')
                    user.close()
                    is_work = False

                elif req == 'reg':
                    answer = self.storage.registration(params)
                    if answer:
                        self.sender(user, answer)
                    else:
                        self.sender(user, 'Not Found')

                elif req == 'login':
                    answer = self.storage.enter(params)
                    self.sender(user, answer)

                elif req == 'wprof':
                    answer = self.storage.loadStar(params)
                    self.sender(user, answer)

                elif req == 'review':
                    answer = self.storage.loadReview(params)
                    self.sender(user, answer)

                elif req == 'add_review':
                    answer = self.storage.appendReview(params)
                    self.sender(user, answer)

                elif req == 'add_travel':
                    answer = self.storage.appendTravel(params)
                    self.sender(user, answer)

                elif req == 'add_request':
                    answer = self.storage.appendRequest(params)
                    self.sender(user, answer)

                elif req == 'add_passager':
                    answer = self.storage.appendPassager(params)
                    self.sender(user, answer)

                elif req == 'load_fellow':
                    answer = self.storage.loadFellow(params)
                    self.sender(user, answer)

                elif req == 'add_fellow':
                    answer = self.storage.addFellow(params)
                    self.sender(user, answer)

                elif req == 'load_travels':
                    answer = self.storage.loadTravels(params)
                    self.sender(user, answer)

                elif req == 'load_story_travel':
                    answer = self.storage.loadStoryTravels(params)
                    self.sender(user, answer)



                self.storage.changeStatusTravels()

                data = b''
                msg = ''

            else:
                print('CLIENT DISCONNECTED!')
                is_work = False


IP = '192.168.0.84'
PORT = 9090

HOST = '127.0.0.1'
USER_NAME = 'mapp'
USER_PASSWORD = 'nbkmn'
DB_NAME = 'mobile-app'

Server(IP, PORT, HOST, USER_NAME, USER_PASSWORD, DB_NAME).start_server()

# p = str(Server.hash_password('123'))
# print(p)
# print(bytes(p[2:-1], encoding='utf-8'))
# b = p[16:]
# print(b)
#
# salt = p[:16]
# print(salt)
# c = Server.hash_password('123', salt)
# print(b)
# print(c[16:])
