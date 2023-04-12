from socket import socket, AF_INET, SOCK_STREAM
import json


class Client:
    def __init__(self, ip, port):
        self.cli = socket(AF_INET, SOCK_STREAM)
        self.cli.connect(
            (ip, port)
        )

    def connect(self):
        while True:
            try:
                msg = self.cli.recv(1024).decode('utf-8')
            except Exception as e:
                print(f'ERROR: {str(e)}')
                exit()

            if msg == 'YOU ARE CONNECTED!':
                self.listen()
            else:
                exit()

    def sender(self, text, params=None):
        if params is None:
            params = {}
        data = json.dumps(
            {'request': text, 'params': params},
            ensure_ascii=False,
            default=str
        )
        self.cli.send(data.encode('utf-8'))
        while self.cli.recv(1024).decode('utf-8') != 'getted':
            self.cli.send(text.encode('utf-8'))

    def listen(self):
        is_work = True
        while is_work:
            req = input('--> ')

            if req:
                if req == 'disconnect':
                    self.sender(req)
                    print(self.cli.recv(1024).decode('utf-8'))
                    break
                elif req == 'reg':
                    lastName = input('lastName - ')
                    firstName = input('firstName - ')
                    middleName = input('middleName - ')
                    login = input('login - ')
                    password = input('password - ')
                    phone = input('phone - ')

                    self.sender(req, {
                        'lastName': lastName,
                        'firstName': firstName,
                        'middleName': middleName,
                        'login': login,
                        'password': password,
                        'phone': phone
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Регистрация прошла успешно')
                    else:
                        print('Регистрация не удалась!')

                elif req == 'login':
                    user = input('user - ')
                    password = input('password - ')

                    self.sender(req, {
                        'user': user,
                        'password': password
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Вы вошли в систему!')
                    else:
                        print('Неверный логин, или пароль.')

                elif req == 'wprof':
                    user = input('user - ')

                    self.sender(req, {
                        'user': user
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Вот звёзды!')
                    else:
                        print('Ой, их нет.')

                elif req == 'review':
                    user = input('user - ')

                    self.sender(req, {
                        'user': user
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Все ваши отзывы')
                    else:
                        print('Ой, их нет.')

                elif req == 'add_review':
                    user = input('user - ')
                    travel = input('travel - ')
                    count_pas = input('count_pas - ')
                    text = input('text - ')
                    star = input('star - ')

                    self.sender(req, {
                        'user': user,
                        'travel': travel,
                        'count_pas': count_pas,
                        'text': text,
                        'star': float(star)
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Отзыв успешно добавлен')
                    else:
                        print('Произошло неизведанное')

                elif req == 'add_travel':
                    user = input('user - ')
                    From = input('From - ')
                    To = input('To - ')
                    date = input('date - ')
                    time = input('time - ')
                    prise = input('prise - ')
                    count_pas = input('count_pas - ')

                    self.sender(req, {
                        'user': user,
                        'From': From,
                        'To': To,
                        'date': date,
                        'time': time,
                        'prise': prise,
                        'count_pas': count_pas
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Поездка добавлена ', data['answer'])
                    else:
                        print('Произошло неизведанное')

                elif req == 'add_request':
                    login = input('login - ')
                    From = input('From - ')
                    To = input('To - ')
                    date = input('date - ')

                    self.sender(req, {
                        'login': login,
                        'From': From,
                        'To': To,
                        'date': date
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Запрос успешно добавлен')
                    else:
                        print('Произошло неизведанное')

                elif req == 'add_passager':
                    user = input('user - ')
                    travel = input('travel - ')

                    self.sender(req, {
                        'user': user,
                        'travel': travel
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Запрос успешно добавлен')
                    else:
                        print('Произошло неизведанное')

                elif req == 'load_fellow':
                    From = input('From - ')
                    To = input('To - ')
                    date = input('date - ')

                    self.sender(req, {
                        'From': From,
                        'To': To,
                        'date': date
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Попутчики загружены ', data['answer'])
                    else:
                        print('Произошло неизведанное')

                elif req == 'add_fellow':
                    user = input('user - ')
                    travel = input('travel - ')
                    From = input('From - ')
                    To = input('To - ')
                    date = input('date - ')

                    self.sender(req, {
                        'user': user,
                        'travel': travel,
                        'From': From,
                        'To': To,
                        'date': date,
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Запрос успешно добавлен')
                    else:
                        print('Произошло неизведанное')

                elif req == 'load_travels':
                    From = input('From - ')
                    To = input('To - ')
                    date = input('date - ')

                    self.sender(req, {
                        'From': From,
                        'To': To,
                        'date': date
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Возможные поездки ', data['answer'])
                    else:
                        print('Произошло неизведанное')

                elif req == 'load_story_travel':
                    user = input('user - ')

                    self.sender(req, {
                        'user': user
                    })

                    data = json.loads(self.cli.recv(1024).decode('utf-8'))
                    print(data)
                    if data['answer']:
                        print('Вся ваша история ', data['answer'])
                    else:
                        print('Произошло неизведанное')



Client('192.168.56.1', 8888).connect()
# login - 123
# From - [43.2345, 23.2345]
# To - [32.2345, 42.2345]
# date - 2023-04-16
# time - 18:30
# prise - 350
# count_pas - 3
