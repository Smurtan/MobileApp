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
                return self.cli
            else:
                print('НЕТ НО МЫ ДОБЬЁМСЯ')

    #def listen(self):

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

    def disconnect(self):
        self.sender('disconnect')

    def registration(self, lastName, firstName, middleName, password, phone):
        self.sender('reg', {
            'lastName': lastName,
            'firstName': firstName,
            'middleName': middleName,
            'phone': phone,
            'password': password
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            return True
        else:
            return False

    def login(self, phone, password):
        self.sender('login', {
            'phone': phone,
            'password': password
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Вы вошли в систему!')
            return data['answer']
        else:
            print('Неверный логин, или пароль.')
            return False

    def watchProfile(self, user):
        self.sender('wprof', {
            'user': user
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Вот звёзды!')
            return data['answer']
        else:
            print('Ой, их нет.')
            return False

    def watchReview(self, user):
        self.sender('review', {
            'user': user
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Все ваши отзывы')
            return data['answer']
        else:
            print('Ой, их нет.')
            return False

    def addReview(self, user, travel, count_pas, text, star):
        self.sender('add_review', {
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
            return True
        else:
            print('Произошло неизведанное')
            return False

    def addTravel(self, user, From, To, date, time, prise, count_pas):
        self.sender('add_travel', {
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
            return True
        else:
            print('Произошло неизведанное')
            return False

    def loadFellow(self, From, To, date):
        self.sender('load_fellow', {
            'From': From,
            'To': To,
            'date': date
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Попутчики загружены ', data['answer'])
            return data['answer']
        else:
            print('Произошло неизведанное')
            return False

    def addRequest(self, user, From, To, date):
        self.sender('add_request', {
            'user': user,
            'From': From,
            'To': To,
            'date': date
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Запрос успешно добавлен')
            return True
        else:
            print('Произошло неизведанное')
            return False

    def addPassager(self, user, travel):
        self.sender('add_passager', {
            'user': user,
            'travel': travel
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Запрос успешно добавлен')
            return True
        else:
            print('Произошло неизведанное')
            return False

    def addFellow(self, user, travel, From, To, date):
        self.sender('add_fellow', {
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
            return True
        else:
            print('Произошло неизведанное')
            return False

    def loadTravels(self, From, To, date):
        self.sender('load_travels', {
            'From': From,
            'To': To,
            'date': date
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Возможные поездки ', data['answer'])
            return data['answer']
        else:
            print('Произошло неизведанное')
            return False

    def loadStoryTravel(self, user):
        self.sender('load_story_travel', {
            'user': user
        })

        data = json.loads(self.cli.recv(1024).decode('utf-8'))
        print(data)
        if data['answer']:
            print('Вся ваша история ', data['answer'])
            return data['answer']
        else:
            print('Произошло неизведанное')
            return False

