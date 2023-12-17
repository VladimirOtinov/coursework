import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT,
                password TEXT,
                code_question TEXT,
                code_answer TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Bank_account (
                bank_acc_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                account_info TEXT,
                money REAL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES User(user_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Transaction_in (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cost REAL,
                date TEXT,
                info TEXT,
                category TEXT,
                bank_acc_id INTEGER,
                FOREIGN KEY (bank_acc_id) REFERENCES Bank_account(bank_acc_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Transaction_out (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cost REAL,
                date TEXT,
                info TEXT,
                category TEXT,
                bank_acc_id INTEGER,
                FOREIGN KEY (bank_acc_id) REFERENCES Bank_account(bank_acc_id)
            )
        ''')

        self.connection.commit()

    def close_connection(self):
        self.connection.close()


    def add_user(self, login, password, code_question, code_answer):
        try:
            self.cursor.execute('''
                INSERT INTO User (login, password, code_question, code_answer)
                VALUES (?, ?, ?, ?)
            ''', (login, password, code_question, code_answer))
            self.connection.commit()
            print("Пользователь успешно добавлен.")
            return True
        except sqlite3.Error as e:
            print("Ошибка при добавлении пользователя:", e)
            return False

    def check_credentials(self, login, password):
        try:
            self.cursor.execute('''
                SELECT * FROM User
                WHERE login = ? AND password = ?
            ''', (login, password))
            user_data = self.cursor.fetchone()

            if user_data:
                print("Вход выполнен успешно.")
                return True
            else:
                print("Неправильный логин или пароль.")
                return False
        except sqlite3.Error as e:
            print("Ошибка при проверке учетных данных:", e)
            return False

    def check_user_exists(self):
        try:
            self.cursor.execute('SELECT * FROM User LIMIT 1')
            user_data = self.cursor.fetchone()
            return user_data is not None
        except sqlite3.Error as e:
            print("Ошибка при проверке наличия пользователя:", e)
            return False

    def get_security_answer(self, id):
        try:
            self.cursor.execute('''
                SELECT code_answer FROM User
                WHERE login = ?
            ''', (id))

            answer = self.cursor.fetchone()
            return answer[0] if answer else None

        except sqlite3.Error as e:
            print("Ошибка при получении ответа на вопрос безопасности:", e)
            return None

    def get_security_question(self):
        try:
            self.cursor.execute('SELECT code_question FROM User LIMIT 1')

            question = self.cursor.fetchone()
            return question[0] if question else "нет вопроса на данный момент"

        except sqlite3.Error as e:
            print("Ошибка при получении первого вопроса безопасности:", e)
            return "не найден вопрос"