import psycopg2

class DBLogger:
    _instance = None

    def __new__(cls, db_config=None):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._setup(db_config)
        return cls._instance

    def _setup(self, db_config):
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def log(self, message):
        self.cursor.execute("INSERT INTO logs (message) VALUES (%s)", (message,))
        self.conn.commit()

    def show_logs(self):
        self.cursor.execute("SELECT id, message, created_at FROM logs ORDER BY id")
        for log in self.cursor.fetchall():
            print(f"[{log[0]}] {log[1]} - {log[2]}")

    def close(self):
        self.conn.close()


db_config = {
    'dbname': 'bookswap',
    'user': 'postgres',
    'password': 'suser',
    'host': 'localhost',
    'port': '5432'
}

logger = DBLogger(db_config)
logger.log("Mensaje guardado en PostgreSQL")
logger.log("Otro evento registrado")
logger.show_logs()
logger.close()