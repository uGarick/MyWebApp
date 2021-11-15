import requests
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="123",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute('SELECT * FROM service.users WHERE login=%s AND password=%s', (str(username), str(password)))
    records = list(cursor.fetchall())

    return render_template('account.html', full_name=records[0][1])


if __name__ == '__main__':
    app.run()