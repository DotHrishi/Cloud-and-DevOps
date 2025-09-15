from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

DB_HOST = 'notes-db.c4j8kemku47n.us-east-1.rds.amazonaws.com'
DB_USER = 'admin'
DB_PASSWORD = 'hrishi123'
DB_NAME = 'notes_app'
DB_PORT = 3306

def connect_db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM notes")
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/view/<int:note_id>')
def view(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM notes WHERE id = %s", (note_id,))
    note = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('view.html', note=note) if note else "Note not found"

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (title, content, note_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT id, title, content FROM notes WHERE id = %s", (note_id,))
    note = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', note=note) if note else "Note not found"

@app.route('/delete/<int:note_id>')
def delete(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)