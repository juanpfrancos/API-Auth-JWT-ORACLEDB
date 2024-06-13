import oracledb
from datetime import datetime
from config import CS, DB_USER, DB_PASS, DB_TABLE, pwd_context
from models.user import UserSignUp


def signup_user(data):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO {DB_TABLE} (USERNAME, PASSWORD, EMAIL, FIRST_NAME, LAST_NAME, PHONE_NUMBER, ADDRESS, COUNTRY, STATE, CITY, ZIP_CODE, DATE_OF_BIRTH, GENDER, ACCOUNT_TYPE) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, TO_DATE(:12, 'YYYY-MM-DD'), :13, :14)"
            data = (data['username'], data['password'],  data['email'], data['first_name'], data['last_name'], data['phone_number'], data['address'], data['country'], data['state'], data['city'], data['zip_code'], data['date_of_birth'].strftime('%Y-%m-%d'), data['gender'], data['account_type'])
            cursor.execute(sql, data)
            connection.commit()
    
def auth_user(credentials):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {DB_TABLE} WHERE username = '{credentials.username}' AND ROWNUM = 1"
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()
            if data is not None:
                verify = pwd_context.verify(credentials.password, data["PASSWORD"])
                if verify:
                    return data
            return None
    
def get_auth_user(username: str):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = """
                SELECT 
                    username, 
                    password, 
                    email, 
                    first_name, 
                    last_name, 
                    phone_number, 
                    address, 
                    country, 
                    state, 
                    city, 
                    zip_code, 
                    date_of_birth, 
                    gender, 
                    profile_picture, 
                    account_type, 
                    language
                FROM users 
                WHERE username = :username AND ROWNUM = 1
            """
            cursor.execute(sql, username=username)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            user_data = cursor.fetchone()

    if user_data:
        user = UserSignUp(**user_data)
        return user
    else:
        return None


def verify_user_exist(username:str, email:str):
    with oracledb.connect(user=DB_USER, password=DB_PASS, dsn=CS) as connection:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {DB_TABLE} WHERE username = '{username}' OR email = '{email}'"
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()
    return data