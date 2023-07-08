import oracledb
from config import CS, DB_USER, DB_PASS, DB_TABLE, pwd_context

    
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