import sqlite3

class SQLite:
	def __init__(self):
		self.connection = sqlite3.connect('./database.db')
		self.create_tables()

	def create_tables(self):
		cursor = self.connection.cursor()
		cursor.execute('''
			CREATE TABLE IF NOT EXISTS courses (
				id INTEGER NOT NULL,
				channel INTEGER NOT NULL,
				last_check TIMESTAMP NOT NULL
			)
		''')

		self.connection.commit()