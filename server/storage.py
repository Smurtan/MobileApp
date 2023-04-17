import mysql.connector
from mysql.connector import Error
import json

import hashlib
import os

from datetime import date, datetime


class Storage:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name

    @staticmethod
    def hash_password(password, salt=None):
        if not salt:
            salt = os.urandom(16)
        print('Salt --> ')
        print(salt)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)

        return (salt + key).hex()

    def create_db_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name
            )
            print("MySQL DB connection successful")
        except Error as e:
            print(f'Error: "{e}"')

        return connection

    @staticmethod
    def append_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            result = True
            print("Query successful")
        except Error as e:
            print(f"Error: '{e}'")
            result = False

        return result

    @staticmethod
    def read_query(connection, query):
        cursor = connection.cursor()
        result = None
        error = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result, error
        except Error as e:
            print(f"Error: '{e}'")
            return result, error

    # ===========================================================================================================

    def registration(self, params):
        connect = self.create_db_connection()
        password = self.hash_password(params['password'])
        sql_request = """
            INSERT INTO
                users
                (last_name, first_name, middle_name, phone, password)
            VALUES 
                ('%s', '%s', '%s', '%s', '%s');
    """ % (params['lastName'], params['firstName'], params['middleName'], params['phone'], password)
        print(sql_request)
        answer = self.append_query(connect, sql_request)
        if answer:
            sql_request = """
                    SELECT
                        id_user
                    FROM
                        users
                    WHERE
                        phone = '%s';""" % params['phone']
            answer = self.read_query(connect, sql_request)[0][0][0]  # ([(x,)], None) --> x
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def enter(self, params):
        connect = self.create_db_connection()

        sql_request = """
        SELECT
            password
        FROM
            users
        WHERE
            phone = '%s';""" % params['phone']
        answer = self.read_query(connect, sql_request)[0]
        if answer:
            answer = answer[0][0]
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
            connect = None
            return ans
        print(answer)

        salt = bytes.fromhex(answer)[:16]
        key = self.hash_password(params['password'], salt)

        if key == answer:
            sql_request = """
                        SELECT
                            id_user
                        FROM
                            users
                        WHERE
                            phone = '%s';""" % params['phone']
            answer = self.read_query(connect, sql_request)[0][0][0]  # ([(x,)], None) --> x
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def loadStar(self, params):
        connect = self.create_db_connection()
        sql_request = """
            SELECT
                avg_star,
                first_name
            FROM
                users
            WHERE
                id_user = '%s';""" % params['user']
        answer = self.read_query(connect, sql_request)[0][0]
        if answer:
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def loadReview(self, params):
        connect = self.create_db_connection()
        sql_request = """
                    SELECT
                        r.text,
                        r.star,
                        u.first_name
                    FROM
                        reviews AS r,
                        users As u
                    WHERE
                        u.id_user = r.id_from AND 
                        %s = r.id_to;""" % params['user']
        answer = self.read_query(connect, sql_request)[0]
        print(answer)

        if answer:
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def appendReview(self, params):
        connect = self.create_db_connection()
        sql_key_to = """
            SELECT
                id_driver,
                id_passager
            FROM
                travels As t
            WHERE
                t.id_travel = %s;""" % params['travel']
        key_to = self.read_query(connect, sql_key_to)[0][0]
        count_pas = int(params['count_pas'])
        people = []
        people.append(key_to[0])
        people.append(key_to[1].split(' ')[:])

        sql_request = """
            INSERT INTO
                reviews
                (id_from, id_to, text, star)
            VALUES
                (%s, %s, '%s', %s);""" % (params['user'], people[count_pas], params['text'], params['star'])
        answer = self.append_query(connect, sql_request)
        print(answer)

        if answer:
            ans = json.dumps(
                {'answer': True, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def appendTravel(self, params):
        connect = self.create_db_connection()
        sql_request = """
                    INSERT INTO
                        travels
                        (id_driver, tr_from, tr_to, stops, date, time, prise, count_passager, id_passager, id_condition)
                    VALUES 
                        (%s, '%s', '%s', NULL, '%s', '%s', %s, %s, NULL, 1);
            """ % (
            params['user'], params['From'], params['To'], params['date'], params['time'], int(params['prise']),
            params['count_pas'])
        answer = self.append_query(connect, sql_request)

        if answer:
            sql_request = """
                        SELECT
                            id_travel
                        FROM
                            travels
                        WHERE
                            id_driver = %s AND tr_from = '%s' AND tr_to = '%s' AND `date` = '%s' AND 
                            `time` = '%s';""" % (params['user'], params['From'], params['To'], params['date'], params['time'])
            answer = self.read_query(connect, sql_request)[0][0][0]  # ([(x,)], None) --> x
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def appendRequest(self, params):
        connect = self.create_db_connection()
        sql_request = """
                    INSERT INTO
                        requesrs
                        (id_user, re_from, re_to, date)
                    VALUES 
                        (%s, '%s', '%s', '%s');
            """ % (params['user'], params['From'], params['To'], params['date'])
        answer = self.append_query(connect, sql_request)

        if answer:
            ans = json.dumps(
                {'answer': True, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def appendPassager(self, params):
        connect = self.create_db_connection()
        sql_passager = """
            SELECT
                id_passager
            FROM
                travels
            WHERE
                id_travel = %s """ % params['travel']
        passager = self.read_query(connect, sql_passager)[0][0][0]
        print(passager)

        if not passager:
            passager = params['user']
        else:
            passager += " " + str(params['user'])

        sql_request = """
            UPDATE
                travels
            SET
                id_passager = '%s'
            WHERE 
                id_travel = %s ;""" % (passager, params['travel'])
        answer = self.append_query(connect, sql_request)

        if answer:
            ans = json.dumps(
                {'answer': True, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def loadFellow(self, params):
        connect = self.create_db_connection()
        sql_user = """
                    SELECT
                        u.first_name,
                        u.id_user
                    FROM
                        requesrs AS r,
                        users AS u
                    WHERE
                         r.re_from = '%s' AND r.re_to = '%s' AND r.date = '%s' AND r.id_user = u.id_user;""" % (
        params['From'], params['To'], params['date'])
        answer = self.read_query(connect, sql_user)[0]  # ([('efg', x)], None) --> [('efg', x)]

        if answer:
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def addFellow(self, params):
        self.appendPassager(params)

        connect = self.create_db_connection()
        sql_request = """
                    DELETE 
                    FROM 
                        requesrs
                    WHERE 
	                    `id_user` = %s AND `re_from` = '%s' AND `re_to` = '%s' AND `date` = '%s';
            """ % (params['user'], params['From'], params['To'], params['date'])
        answer = self.append_query(connect, sql_request)

        if answer:
            ans = json.dumps(
                {'answer': True, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def loadTravels(self, params):
        connect = self.create_db_connection()
        sql_request = """
                    SELECT
                        t.id_travel,
                        t.prise,
                        t.time,
                        u.first_name,
                        t.`count_passager`
                    FROM
                        travels AS t,
                        users AS u
                    WHERE
                        t.`tr_from` = '%s' AND t.`tr_to` = '%s' AND t.`date` = '%s' AND t.id_condition = 1 AND
                        t.id_driver = u.id_user""" % (
            params['From'], params['To'], params['date']
        )
        answer = self.read_query(connect, sql_request)[0]
        print(answer)

        if answer:
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def loadStoryTravels(self, params):
        connect = self.create_db_connection()

        sql_request = """
                    SELECT
                        t.tr_from,
                        t.tr_to,
                        t.date,
                        t.time
                    FROM
                        travels AS t
                    WHERE
                        (t.`id_driver` = %s OR t.`id_passager` LIKE '%s') AND t.id_condition = 2;""" % (params['user'], '%' + str(params['user']) + '%')
        answer = self.read_query(connect, sql_request)[0]

        if answer:
            ans = json.dumps(
                {'answer': answer, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def changeData(self, params):
        connect = self.create_db_connection()
        sql_user = """
                    SELECT
                        id_user
                    FROM
                        users AS u
                    WHERE
                        u.phone = %s ;""" % params['phone']
        user = self.read_query(connect, sql_user)[0][0][0]
        sql_request = """
                    INSERT INTO
                        travels
                        (id_driver, tr_from, tr_to, stops, date, time, prise, count_passager, id_passager, id_condition)
                    VALUES 
                        (%s, '%s', '%s', NULL, '%s', '%s', %s, %s, NULL, 1);
            """ % (
            user, params['From'], params['To'], params['date'], params['time'], int(params['prise']),
            params['count_pas'])
        answer = self.append_query(connect, sql_request)

        if answer:
            ans = json.dumps(
                {'answer': True, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans

    def changeStatusTravels(self):
        connect = self.create_db_connection()

        sql_request = """
                    UPDATE
                        travels
                    SET
                        id_condition = 2
                    WHERE
                        `date` = current_date() AND id_condition = 1 AND `time` < current_time() + hour('2:0:0') 
        """
        self.append_query(connect, sql_request)

    '''def appendTravel(self, params):
        connect = self.create_db_connection()
        sql_user = """
                    SELECT
                        id_user
                    FROM
                        users AS u
                    WHERE
                        u.login = %s ;""" % params['login']
        user = self.read_query(connect, sql_user)[0][0][0]
        sql_request = """
                    INSERT INTO
                        travels
                        (id_driver, tr_from, tr_to, stops, date, time, prise, count_passager, id_passager, id_condition)
                    VALUES 
                        (%s, '%s', '%s', NULL, '%s', '%s', %s, %s, NULL, 1);
            """ % (
            user, params['From'], params['To'], params['date'], params['time'], int(params['prise']),
            params['count_pas'])
        answer = self.append_query(connect, sql_request)

        if answer:
            ans = json.dumps(
                {'answer': True, 'error': False},
                ensure_ascii=False,
                default=str
            )
        else:
            ans = json.dumps(
                {'answer': '', 'error': True},
                ensure_ascii=False,
                default=str
            )
        connect = None
        return ans
'''
