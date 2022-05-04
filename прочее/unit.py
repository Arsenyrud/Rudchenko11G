import unittest
import sqlite3


class TestBD(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.database = sqlite3.connect('testdb.db')
        self.cur = self.database.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "Item" (
        "id"	INTEGER,
        "Name"	TEXT,
        "Amount"	INTEGER,
        "Price"	INTEGER
);''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "User" (
        "id"	INTEGER,
        "Name"	TEXT,
        "Surname"	TEXT,
        "Phone"	INTEGER,
        "Address"	TEXT,
        "Bdate"	TEXT,
        "Rdate"	TEXT
);''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "Order" (
        "id"	INTEGER,
        "Date"	TEXT,
        "Summ"	INTEGER,
        "Address"	TEXT
);''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS "Basket" (
        "id user"	INTEGER,
        "id item"	INTEGER
);''')


        self.cur.execute('''CREATE TABLE IF NOT EXISTS "Receipt" (
        "id order"	INTEGER,
        "id user"	INTEGER,
        "id item"	INTEGER
);''')

        self.cur.execute('''INSERT INTO "Item" VALUES (1,'Холодный',24,9990);''')
        self.cur.execute('''INSERT INTO "Item" VALUES (2,'Тёплый',50,15700);''')
        self.cur.execute('''INSERT INTO "Item" VALUES (3,'Финский',35,22870);''')
        self.cur.execute('''INSERT INTO "User" VALUES (1,'Арсений','Хлоп',555,'дом 5','1999-05-05','2013-10-10');''')
        self.cur.execute('''INSERT INTO "User" VALUES (2,'Андрей','Вокориш',223,'дом 3','2004-12-12','2015-11-11');''')
        self.cur.execute('''INSERT INTO "User" VALUES (3,'Наталья','Черепаха',889,'море','1979-09-09','2017-01-01');''')
        self.cur.execute('''INSERT INTO "User" VALUES (4,'Егор','Денис',209,'дом 9','2005-01-01','2021-11-20');''')
        self.cur.execute('''INSERT INTO "User" VALUES (5,'Виталий','Линда',990,'дом 11','2003-01-05','2021-11-19');''')
        self.cur.execute('''INSERT INTO "Order" VALUES (1,'12.07',15000,'дом 3');''')
        self.cur.execute('''INSERT INTO "Order" VALUES (2,'15.10',10000,'дом 5');''')
        self.cur.execute('''INSERT INTO "Basket" VALUES (2,3);''')
        self.cur.execute('''INSERT INTO "Basket" VALUES (2,1);''')
        self.cur.execute('''INSERT INTO "Basket" VALUES (1,2);''')
        self.cur.execute('''INSERT INTO "Receipt" VALUES (1,2,2);''')
        self.cur.execute('''INSERT INTO "Receipt" VALUES (1,1,1);''')

    @classmethod
    def tearDownClass(self):
        self.cur.execute("DROP TABLE User")
        self.cur.execute("DROP TABLE Basket")
        self.cur.execute("DROP TABLE Receipt")
        self.cur.execute("DROP TABLE Item")
        self.database.commit()

    def test_1(self):
        print('Первый тест:')
        self.cur.execute("select Name, Surname, Rdate from user order by Rdate desc LIMIT 1;")
        print(*self.cur.fetchall())

    def test_2(self):
        print('Второй тест:')
        self.cur.execute(
            "select DISTINCt SUBSTR(Bdate, 1, 4) from user;")
        for el in self.cur.fetchall():
            print(*el)

    def test_3(self):
        print('Третий тест:')
        self.cur.execute('select sum(amount) from item;')
        print(*self.cur.fetchall())


if __name__ == "__main__":
    unittest.main()
