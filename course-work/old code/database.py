import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                family_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
                family_id INTEGER NOT NULL,
                FOREIGN KEY (family_id) REFERENCES User(family_id)
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
                FOREIGN KEY (bank_acc_id) REFERENCES bank_accounts(bank_acc_id)
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
                FOREIGN KEY (bank_acc_id) REFERENCES bank_accounts(bank_acc_id)
            )
        ''')

        self.connection.commit()


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

    def get_security_question(self):
        try:
            self.cursor.execute('''
                SELECT code_question FROM User
                ORDER BY family_id ASC LIMIT 1
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
                SELECT code_answer FROM User
                ORDER BY family_id ASC LIMIT 1
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
                UPDATE User
                SET password = ?
                WHERE family_id = ?
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
                INSERT INTO bank_accounts (name, account_info, money, family_id)
                VALUES (?, ?, ?, ?)
            ''', (name, account_info, money, user_id))
            self.connection.commit()
            print("Счет успешно добавлен.")
            return True
        except sqlite3.Error as e:
            print("Ошибка при добавлении счета:", e)
            return False

    def get_accounts(self):
        try:
            self.cursor.execute('''
                SELECT id, name FROM bank_accounts
            ''')
            accounts = self.cursor.fetchall()
            return accounts
        except sqlite3.Error as e:
            print("Ошибка при получении списка счетов:", e)
            return None