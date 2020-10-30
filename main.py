from environment import Environment
from sqlalchemy import create_engine


def connect():
    username = Environment.database_key_name('username')
    password = Environment.database_key_name('password')
    db_name = Environment.database_key_name('db_name')
    port = Environment.database_key_name('port')
    connection_str = f'postgresql://{username}:{password}@localhost:{port}/{db_name}'
    engine = create_engine(connection_str)
    
    with engine.connect() as connection:
        result = connection.execute("select * from roles")
        
        for row in result:
            print("role name is:", row['role_name'])

connect()
