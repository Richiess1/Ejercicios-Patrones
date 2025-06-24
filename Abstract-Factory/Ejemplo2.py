class Connection:
    def connect(self):
        pass

class Command:
    def execute(self):
        pass

class MySQLConnection(Connection):
    def connect(self):
        print("Conectando a MySQL...")

class MySQLCommand(Command):
    def execute(self):
        print("Ejecutando comando en MySQL")

class PostgresConnection(Connection):
    def connect(self):
        print("Conectando a PostgreSQL...")

class PostgresCommand(Command):
    def execute(self):
        print("Ejecutando comando en PostgreSQL")

class DBFactory:
    def create_connection(self): pass
    def create_command(self): pass

class MySQLFactory(DBFactory):
    def create_connection(self): return MySQLConnection()
    def create_command(self): return MySQLCommand()

class PostgresFactory(DBFactory):
    def create_connection(self): return PostgresConnection()
    def create_command(self): return PostgresCommand()

# Cliente
def ejecutar_operacion(factory: DBFactory):
    conn = factory.create_connection()
    cmd = factory.create_command()
    conn.connect()
    cmd.execute()

# Uso
ejecutar_operacion(MySQLFactory())
ejecutar_operacion(PostgresFactory())