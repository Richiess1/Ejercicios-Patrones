import sqlite3

# === Abstract SQL Adapter ===
class SQLAdapter:
    def __init__(self, db_path, table):
        self.conn = sqlite3.connect(db_path)
        self.table = table
        self.select_fields = "*"
        self.where_clauses = []

    def select(self, fields):
        self.select_fields = ", ".join(fields)
        return self

    def where(self, condition):
        self.where_clauses.append(condition)
        return self

    def get_all(self):
        query = f"SELECT {self.select_fields} FROM {self.table}"
        if self.where_clauses:
            query += " WHERE " + " AND ".join(self.where_clauses)
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def count(self):
        query = f"SELECT COUNT(*) FROM {self.table}"
        if self.where_clauses:
            query += " WHERE " + " AND ".join(self.where_clauses)
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchone()[0]

    def reset(self):
        self.select_fields = "*"
        self.where_clauses = []

    def setup_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                is_active BOOLEAN,
                role TEXT
            )
        """)
        self.conn.commit()

    def insert_sample_data(self):
        sample_users = [
            ("alice", True, "admin"),
            ("bob", True, "admin"),
            ("carol", False, "admin"),
            ("dave", True, "admin"),
            ("eve", False, "user")
        ]
        cursor = self.conn.cursor()
        cursor.executemany("INSERT INTO users (username, is_active, role) VALUES (?, ?, ?)", sample_users)
        self.conn.commit()

# === Query Object ===
class UserQuery:
    def __init__(self, adapter: SQLAdapter):
        self.adapter = adapter
        self.adapter.reset()

    def active(self):
        self.adapter.where("is_active = 1")
        return self

    def with_role(self, role):
        self.adapter.where(f"role = '{role}'")
        return self

    def usernames(self):
        self.adapter.select(["username"])
        return self

    def result(self):
        return self.adapter.get_all()

    def count(self):
        return self.adapter.count()

# === Main Execution ===
if __name__ == "__main__":
    adapter = SQLAdapter("users.db", "users")
    adapter.setup_schema()
    adapter.insert_sample_data()

    query = UserQuery(adapter)
    total = query.active().with_role("admin").count()
    results = query.active().with_role("admin").usernames().result()

    print("Active admin users:", total)
    for user in results:
        print(f"- {user[0]}")