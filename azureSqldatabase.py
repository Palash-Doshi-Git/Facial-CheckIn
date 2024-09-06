import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

load_dotenv()

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'student-records.db')

config = {
    'host': os.getenv('host'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'database': os.getenv('database_name')
}

try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
    cursor = conn.cursor()

    def cleanup():
        cursor.close()
        conn.close()
        print("Connection Closed")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS StudentAttendance (
            Student_Name TEXT,
            Date_Time TEXT
        )
    ''')
    conn.commit()

def insert_data(name, dtstring):
    cursor.execute('''
        INSERT INTO StudentAttendance (Student_Name, Date_Time)
        VALUES (%s, %s)
    ''', (name, dtstring))
    conn.commit()


def get_all_attendance_records():
    cursor.execute("SELECT * FROM StudentAttendance")
    records = cursor.fetchall()
    return records


def exist_name(name):
    cursor.execute('SELECT Student_Name FROM StudentAttendance WHERE Student_Name = %s', (name,))
    row = cursor.fetchone()
    return row is not None


def delete_all_records():
    cursor.execute('DELETE FROM StudentAttendance')
    conn.commit()
    print("All records deleted.")


def update_data(name, dtstring):
    if exist_name(name):
        cursor.execute(
            "UPDATE StudentAttendance SET Date_Time = %s WHERE Student_Name = %s",
            (dtstring, name)
        )
        conn.commit()
    else:
        insert_data(name, dtstring)



