from environment import Environment
from sqlalchemy import create_engine


def connect_to_postgres_db():
    username = Environment.database_key_name('postgres', 'username')
    password = Environment.database_key_name('postgres', 'password')
    db_name = Environment.database_key_name('postgres', 'db_name')
    port = Environment.database_key_name('postgres', 'port')
    dialect = Environment.database_key_name('postgres', 'dialect')
    host = Environment.database_key_name('postgres', 'host')
    connection_str = f'{dialect}://{username}:{password}@{host}:{port}/{db_name}'
    engine = create_engine(connection_str)
    
    with engine.connect() as connection:
        result = connection.execute("select * from roles")
        
        for row in result:
            print("role name is:", row['role_name'])

# connect_to_postgres_db()



def connect_to_mysql_db():
    username = Environment.database_key_name('mysql', 'username')
    password = Environment.database_key_name('mysql', 'password')
    db_name = Environment.database_key_name('mysql', 'db_name')
    port = Environment.database_key_name('mysql', 'port')
    dialect = Environment.database_key_name('mysql', 'dialect')
    host = Environment.database_key_name('mysql', 'host')
    connection_str = 'mysql+mysqlclient://jamie_vardy:Leicester@localhost/menagerie'
    # connection_str = f'{dialect}://{username}:{password}@{host}/{db_name}'
    # print(connection_str)
    engine = create_engine(connection_str)

    with engine.connect() as connection:
        result = connection.execute("select * from tutorials_tbl")
        
        for row in result:
            print("Tutorial title is:", row['tutorial_title'])


connect_to_mysql_db()

# 'mysql://scott:tiger@localhost/foo'

