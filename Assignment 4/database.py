from peewee import SqliteDatabase

db = SqliteDatabase("person.db", pragmas={'ignore_check_constraints': 0})
db.connect()
