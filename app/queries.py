import oracledb
from datetime import datetime
from config import CS, DB_USER, DB_PASS, DB_TABLE, pwd_context


def signup_user(data):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO {DB_TABLE} (ID_USER, FULLNAME, USERNAME, EMAIL, PASS, CREATION_DATE, APP_NAME, ACTIVE) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"
            data = (data['id'],data['fullname'],data['username'],data['email'],data['password'], datetime.utcnow(), 'Auth_APP', 1)
            cursor.execute(sql, data)
            connection.commit()
    
def auth_user(username: str, password: str):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {DB_TABLE} WHERE username = '{username}' AND ROWNUM = 1"
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()
            verify = pwd_context.verify(password, data["PASS"])
    if verify:
        return data
    
def get_auth_user(username:str):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {DB_TABLE} WHERE username = '{username}' AND ROWNUM = 1"
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()
    return data


def verify_user_exist(username:str, email:str):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {DB_TABLE} WHERE username = '{username}' OR email = '{email}'"
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()
    return data