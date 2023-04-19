import sqlite3

from faker import Faker

fake = Faker()


def create_db():
    con = sqlite3.connect('mydatabase.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE customers(first_name TEXT, second_name TEXT)")
    for i in range(30):
        first_name = fake.first_name()
        second_name = fake.last_name()
        cur.execute("""
            INSERT INTO customers
                (first_name, second_name)
            VALUES (?, ?)""", (first_name, second_name))

    cur.execute("CREATE TABLE tracks(title TEXT, lenght INTEGER)")
    for i in range(20):
        title = fake.sentence(nb_words=3)
        lenght = fake.random_int(min=120, max=500)
        cur.execute("""
            INSERT INTO tracks
                (title, lenght)
            VALUES (?, ?)""", (title, lenght))
    con.commit()