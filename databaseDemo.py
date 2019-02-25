import sqlite3


def main():
    print("sqlite")

    # create a database
    db = sqlite3.connect('bigBikes.db')

    db.execute('create table bike (b1 text, c1 int)')

    db.execute('insert into bike (b1, c1) values (?, ?)', ('street', 750))
    db.execute('insert into bike (b1, c1) values (?, ?)', ('fortyeight', 1200))
    db.execute('insert into bike (b1, c1) values (?, ?)', ('streetbob', 1600))

    db.commit()

    cursor = db.execute('select * from bike order by c1')

    for item in cursor:
        print(item)


if __name__ == "__main__":
    main()
