import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS familly (
                familly_id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT,
                password TEXT,
                code_question TEXT,
                code_answer TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bank_accounts (
                bank_acc_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                account_info TEXT,
                money REAL NOT NULL,
                familly_id INTEGER NOT NULL,
                FOREIGN KEY (familly_id) REFERENCES familly(familly_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Transaction_ (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cost REAL,
                date TEXT,
                info TEXT,
                category TEXT,
                bank_acc_id INTEGER,
                type_transaction int,
                FOREIGN KEY (bank_acc_id) REFERENCES bank_accounts(bank_acc_id)
            )
        ''')

        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def add_user(self, login, password, code_question, code_answer):
        try:
            self.cursor.execute('''
                INSERT INTO familly (login, password, code_question, code_answer)
                VALUES (?, ?, ?, ?)
            ''', (login, password, code_question, code_answer))
            self.connection.commit()
            self.cursor.execute('''
                            SELECT * FROM familly
                            WHERE login = ? AND password = ?
                        ''', (login, password))
            user_data = self.cursor.fetchone()
            return user_data
        except sqlite3.Error as e:
            print("Ошибка при добавлении пользователя:", e)
            return False

    def add_tr(self, cost, date, info, category, bank_acc_id, type_tr):
        try:
            self.cursor.execute('''
                INSERT INTO Transaction_ (cost, date, info, category, bank_acc_id, type_transaction)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (cost, date, info, category, bank_acc_id, type_tr))
            self.connection.commit()
            print("добавлен0 000")
        except sqlite3.Error as e:
            print("Ошибка", e)
            return False

    def select_tr(self):
        try:
            self.cursor.execute('''
                SELECT id, cost, bank_accounts.name, date, info, category, type_transaction FROM Transaction_
                inner join bank_accounts using(bank_acc_id)
            ''')
            data = self.cursor.fetchall()
            return data
        except sqlite3.Error as e:
            print(e)

    def remove_tr(self, cost, date, info, category):
        try:
            self.cursor.execute('''
                DELETE from Transaction_ 
                where cost = ? and date=? and info =? and category = ? 
            ''', (cost, date, info, category))
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)

    def check_credentials(self, login, password):
        try:
            self.cursor.execute('''
                SELECT * FROM familly
                WHERE login = ? AND password = ?
            ''', (login, password))
            user_data = self.cursor.fetchone()
            if user_data:
                return user_data
            else:
                return False
        except sqlite3.Error as e:
            print("Ошибка при проверке учетных данных:", e)
            return False

    def get_bank_data(self, familly_id: int):
        try:
            self.cursor.execute('''
                SELECT * FROM bank_accounts
                WHERE familly_id = ?
            ''', (familly_id,))
            bank_data = self.cursor.fetchall()
            print(bank_data)

            if bank_data:
                return bank_data
            else:
                return False
        except sqlite3.Error as e:
            print("get_bank_data", e)
            return False

    def check_user_exists(self):
        try:
            self.cursor.execute('SELECT * FROM familly LIMIT 1')
            user_data = self.cursor.fetchone()
            return user_data is not None
        except sqlite3.Error as e:
            print("Ошибка при проверке наличия пользователя:", e)
            return False

    def get_security_question(self):
        try:
            self.cursor.execute('''
                SELECT code_question FROM familly
                ORDER BY familly_id ASC LIMIT 1
            ''')
            question = self.cursor.fetchone()

            if question:
                return question[0]
            else:
                print("Пользователь не найден.")
                return None
        except sqlite3.Error as e:
            print("Ошибка при получении кодового вопроса:", e)
            return None

    def get_security_answer(self):
        try:
            self.cursor.execute('''
                SELECT code_answer FROM familly
                ORDER BY familly_id ASC LIMIT 1
            ''')
            answer = self.cursor.fetchone()

            if answer:
                return answer[0]
            else:
                print("Пользователь не найден.")
                return None
        except sqlite3.Error as e:
            print("Ошибка при получении кодового ответа:", e)
            return None

    def change_password_by_id(self, user_id, new_password):
        try:
            self.cursor.execute('''
                UPDATE familly
                SET password = ?
                WHERE familly_id = ?
            ''', (new_password, user_id))
            self.connection.commit()
            print("Пароль успешно изменен.")
            return True
        except sqlite3.Error as e:
            print("Ошибка при изменении пароля:", e)
            return False

    def add_bank_account(self, name, account_info, money, user_id):
        try:
            self.cursor.execute('''
                INSERT INTO bank_accounts (name, account_info, money, familly_id)
                VALUES (?, ?, ?, ?)
            ''', (name, account_info, money, user_id))
            self.connection.commit()
            print("Счет успешно добавлен.")
            return True
        except sqlite3.Error as e:
            print("Ошибка при добавлении счета:", e)
            return False
