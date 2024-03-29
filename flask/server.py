from flask import Flask, jsonify
import psycopg2

compose = Flask(__name__)

@compose.route('/<int:id>')
def get_id(id):
    conn = psycopg2.connect(compose.config['DATABASE_URL'])
    cur = conn.cursor()
    cur.execute('SELECT * FROM mytable WHERE id=%s', (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        return jsonify({'error': 'Not found'}), 404
    else:
        return jsonify(row)


@compose.route('/')
def index():
    conn = psycopg2.connect(compose.config['DATABASE_URL'])
    cur = conn.cursor()
    cur.execute('SELECT * FROM mytable')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    compose.config['DATABASE_URL'] = 'postgresql://myuser:mypassword@db:5432/mydb'
    compose.run(host='0.0.0.0', port=5000)
