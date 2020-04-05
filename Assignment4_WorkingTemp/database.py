from peewee import SqliteDatabase

db = SqliteDatabase("person.db")
db.connect()
