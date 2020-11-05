from environment import Environment
from sqlalchemy import create_engine
import pymysql
import mysql.connector


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
    # mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    connection_str = f'mysql+{dialect}://{username}:{password}@{host}:{port}/{db_name}'
    # connection_str = 'mysql+pymysql://sp:sp123@localhost/sp'
    engine = create_engine(connection_str)
    print(engine)

    with engine.connect() as connection:
    #     # result is a list of dicts 
    #     # result = [{}, {}, {}]
        result = connection.execute("select * from tblEmployee")
        print(result)
        
    #     # a row is a dict, {column: 'data value'}
        for row in result:
            print("The Employee's last name is :", row['Employee_last_name'])


# connect_to_mysql_db()

# 'mysql://scott:tiger@localhost/foo'

def connect_to_mongodb():
    # engine = create_engine("mongodb///?Server=MyServer&Port=27017&Database=test&User=test&Password=Password")
    username = Environment.database_key_name('mongo', 'username')
    password = Environment.database_key_name('mongo', 'password')
    db_name = Environment.database_key_name('mongo', 'db_name')
    port = Environment.database_key_name('mongo', 'port')
    dialect = Environment.database_key_name('mongo', 'dialect')
    host = Environment.database_key_name('mongo', 'host')
    # mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
    connection_str = f'{dialect}//{username}:{password}@{host}:{port}/{db_name}'
    # connection_str = 'mysql+pymysql://sp:sp123@localhost/sp'
    engine = create_engine(connection_str)
    print(engine)

    with engine.connect() as connection:
    #     # result is a list of dicts 
    #     # result = [{}, {}, {}]
        result = connection.execute('db.inventory.find( { item: "canvas" } )')
        print(result)
        
    #     # a row is a dict, {column: 'data value'}
        for row in result:
            print(row)


connect_to_mongodb()

